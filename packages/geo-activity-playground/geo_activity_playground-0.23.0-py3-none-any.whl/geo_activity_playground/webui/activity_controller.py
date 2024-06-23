import datetime
import functools
import io
import logging
import pickle

import altair as alt
import geojson
import matplotlib
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
from PIL import Image
from PIL import ImageDraw

from geo_activity_playground.core.activities import ActivityRepository
from geo_activity_playground.core.activities import extract_heart_rate_zones
from geo_activity_playground.core.activities import make_geojson_color_line
from geo_activity_playground.core.activities import make_geojson_from_time_series
from geo_activity_playground.core.activities import make_speed_color_bar
from geo_activity_playground.core.heatmap import add_margin_to_geo_bounds
from geo_activity_playground.core.heatmap import build_map_from_tiles
from geo_activity_playground.core.heatmap import crop_image_to_bounds
from geo_activity_playground.core.heatmap import get_bounds
from geo_activity_playground.core.heatmap import get_sensible_zoom_level
from geo_activity_playground.core.heatmap import OSM_TILE_SIZE
from geo_activity_playground.core.tiles import compute_tile_float

logger = logging.getLogger(__name__)


class ActivityController:
    def __init__(self, repository: ActivityRepository) -> None:
        self._repository = repository

    @functools.lru_cache()
    def render_activity(self, id: int) -> dict:
        activity = self._repository.get_activity_by_id(id)

        time_series = self._repository.get_time_series(id)
        line_json = make_geojson_from_time_series(time_series)

        meta = self._repository.meta
        similar_activities = meta.loc[
            (meta.name == activity["name"]) & (meta.id != activity["id"])
        ]
        similar_activities = [row for _, row in similar_activities.iterrows()]
        similar_activities.reverse()

        result = {
            "activity": activity,
            "line_json": line_json,
            "distance_time_plot": distance_time_plot(time_series),
            "color_line_geojson": make_geojson_color_line(time_series),
            "speed_time_plot": speed_time_plot(time_series),
            "speed_distribution_plot": speed_distribution_plot(time_series),
            "similar_activites": similar_activities,
            "speed_color_bar": make_speed_color_bar(time_series),
            "date": activity.start.date(),
            "time": activity.start.time(),
        }
        if (heart_zones := extract_heart_rate_zones(time_series)) is not None:
            result["heart_zones_plot"] = heartrate_zone_plot(heart_zones)
        if "altitude" in time_series.columns:
            result["altitude_time_plot"] = altitude_time_plot(time_series)
        if "heartrate" in time_series.columns:
            result["heartrate_time_plot"] = heartrate_time_plot(time_series)
        return result

    def render_sharepic(self, id: int) -> bytes:
        time_series = self._repository.get_time_series(id)
        return make_sharepic(time_series)

    def render_day(self, year: int, month: int, day: int) -> dict:
        meta = self._repository.meta
        selection = meta["start"].dt.date == datetime.date(year, month, day)
        activities_that_day = meta.loc[selection]

        time_series = [
            self._repository.get_time_series(activity_id)
            for activity_id in activities_that_day["id"]
        ]

        cmap = matplotlib.colormaps["Dark2"]
        fc = geojson.FeatureCollection(
            features=[
                geojson.Feature(
                    geometry=geojson.MultiLineString(
                        coordinates=[
                            [
                                [lon, lat]
                                for lat, lon in zip(
                                    group["latitude"], group["longitude"]
                                )
                            ]
                            for _, group in ts.groupby("segment_id")
                        ]
                    ),
                    properties={"color": matplotlib.colors.to_hex(cmap(i % 8))},
                )
                for i, ts in enumerate(time_series)
            ]
        )

        activities_list = activities_that_day.to_dict(orient="records")
        for i, activity_record in enumerate(activities_list):
            activity_record["color"] = matplotlib.colors.to_hex(cmap(i % 8))

        return {
            "activities": activities_list,
            "geojson": geojson.dumps(fc),
            "date": datetime.date(year, month, day).isoformat(),
        }

    def render_all(self) -> dict:
        cmap = matplotlib.colormaps["Dark2"]
        fc = geojson.FeatureCollection(
            features=[
                geojson.Feature(
                    geometry=geojson.MultiLineString(
                        coordinates=[
                            [
                                [lon, lat]
                                for lat, lon in zip(
                                    group["latitude"], group["longitude"]
                                )
                            ]
                            for _, group in self._repository.get_time_series(
                                activity["id"]
                            ).groupby("segment_id")
                        ]
                    ),
                    properties={
                        "color": matplotlib.colors.to_hex(cmap(i % 8)),
                        "activity_name": activity["name"],
                        "activity_id": str(activity["id"]),
                    },
                )
                for i, activity in enumerate(self._repository.iter_activities())
            ]
        )

        return {
            "geojson": geojson.dumps(fc),
        }

    def render_name(self, name: str) -> dict:
        meta = self._repository.meta
        selection = meta["name"] == name
        activities_with_name = meta.loc[selection]

        time_series = [
            self._repository.get_time_series(activity_id)
            for activity_id in activities_with_name["id"]
        ]

        cmap = matplotlib.colormaps["Dark2"]
        fc = geojson.FeatureCollection(
            features=[
                geojson.Feature(
                    geometry=geojson.MultiLineString(
                        coordinates=[
                            [
                                [lon, lat]
                                for lat, lon in zip(
                                    group["latitude"], group["longitude"]
                                )
                            ]
                            for _, group in ts.groupby("segment_id")
                        ]
                    ),
                    properties={"color": matplotlib.colors.to_hex(cmap(i % 8))},
                )
                for i, ts in enumerate(time_series)
            ]
        )

        activities_list = activities_with_name.to_dict(orient="records")
        for i, activity_record in enumerate(activities_list):
            activity_record["color"] = matplotlib.colors.to_hex(cmap(i % 8))

        return {
            "activities": activities_list,
            "geojson": geojson.dumps(fc),
            "name": name,
            "tick_plot": name_tick_plot(activities_with_name),
            "equipment_plot": name_equipment_plot(activities_with_name),
            "distance_plot": name_distance_plot(activities_with_name),
            "minutes_plot": name_minutes_plot(activities_with_name),
        }


def speed_time_plot(time_series: pd.DataFrame) -> str:
    return (
        alt.Chart(time_series, title="Speed")
        .mark_line()
        .encode(
            alt.X("time", title="Time"),
            alt.Y("speed", title="Speed / km/h"),
            alt.Color("segment_id:N", title="Segment"),
        )
        .interactive(bind_y=False)
        .to_json(format="vega")
    )


def speed_distribution_plot(time_series: pd.DataFrame) -> str:
    df = pd.DataFrame(
        {
            "speed": time_series["speed"],
            "step": time_series["time"].diff().dt.total_seconds() / 60,
        }
    ).dropna()
    return (
        alt.Chart(df.loc[df["speed"] > 0], title="Speed distribution")
        .mark_bar()
        .encode(
            alt.X("speed", bin=alt.Bin(step=5), title="Speed / km/h"),
            alt.Y("sum(step)", title="Duration / min"),
        )
        .to_json(format="vega")
    )


def distance_time_plot(time_series: pd.DataFrame) -> str:
    return (
        alt.Chart(time_series, title="Distance")
        .mark_line()
        .encode(
            alt.X("time", title="Time"),
            alt.Y("distance_km", title="Distance / km"),
            alt.Color("segment_id:N", title="Segment"),
        )
        .interactive()
        .to_json(format="vega")
    )


def altitude_time_plot(time_series: pd.DataFrame) -> str:
    return (
        alt.Chart(time_series, title="Altitude")
        .mark_line()
        .encode(
            alt.X("time", title="Time"),
            alt.Y("altitude", scale=alt.Scale(zero=False), title="Altitude / m"),
            alt.Color("segment_id:N", title="Segment"),
        )
        .interactive(bind_y=False)
        .to_json(format="vega")
    )


def heartrate_time_plot(time_series: pd.DataFrame) -> str:
    return (
        alt.Chart(time_series, title="Heart Rate")
        .mark_line()
        .encode(
            alt.X("time", title="Time"),
            alt.Y("heartrate", scale=alt.Scale(zero=False), title="Heart rate"),
            alt.Color("segment_id:N", title="Segment"),
        )
        .interactive(bind_y=False)
        .to_json(format="vega")
    )


def heartrate_zone_plot(heart_zones: pd.DataFrame) -> str:
    return (
        alt.Chart(heart_zones, title="Heart Rate Zones")
        .mark_bar()
        .encode(
            alt.X("minutes", title="Duration / min"),
            alt.Y("heartzone:O", title="Zone"),
            alt.Color("heartzone:O", scale=alt.Scale(scheme="turbo"), title="Zone"),
        )
        .to_json(format="vega")
    )


def name_tick_plot(meta: pd.DataFrame) -> str:
    return (
        alt.Chart(meta, title="Repetitions")
        .mark_tick()
        .encode(
            alt.X("start", title="Date"),
        )
        .to_json(format="vega")
    )


def name_equipment_plot(meta: pd.DataFrame) -> str:
    return (
        alt.Chart(meta, title="Equipment")
        .mark_bar()
        .encode(alt.X("count()", title="Count"), alt.Y("equipment", title="Equipment"))
        .to_json(format="vega")
    )


def name_distance_plot(meta: pd.DataFrame) -> str:
    return (
        alt.Chart(meta, title="Distance")
        .mark_bar()
        .encode(
            alt.X("distance_km", bin=True, title="Distance / km"),
            alt.Y("count()", title="Count"),
        )
        .to_json(format="vega")
    )


def name_minutes_plot(meta: pd.DataFrame) -> str:
    minutes = meta["elapsed_time"].dt.total_seconds() / 60
    return (
        alt.Chart(pd.DataFrame({"minutes": minutes}), title="Elapsed time")
        .mark_bar()
        .encode(
            alt.X("minutes", bin=True, title="Time / min"),
            alt.Y("count()", title="Count"),
        )
        .to_json(format="vega")
    )


def make_sharepic(time_series: pd.DataFrame) -> bytes:
    lat_lon_data = np.array([time_series["latitude"], time_series["longitude"]]).T

    geo_bounds = get_bounds(lat_lon_data)
    geo_bounds = add_margin_to_geo_bounds(geo_bounds)
    tile_bounds = get_sensible_zoom_level(geo_bounds, (1500, 1500))
    background = build_map_from_tiles(tile_bounds)
    # background = convert_to_grayscale(background)

    img = Image.new("RGB", tile_bounds.shape[::-1])
    draw = ImageDraw.Draw(img)

    for _, group in time_series.groupby("segment_id"):
        xs, ys = compute_tile_float(
            group["latitude"], group["longitude"], tile_bounds.zoom
        )
        yx = list(
            (
                int((x - tile_bounds.x_tile_min) * OSM_TILE_SIZE),
                int((y - tile_bounds.y_tile_min) * OSM_TILE_SIZE),
            )
            for x, y in zip(xs, ys)
        )

        draw.line(yx, fill="red", width=4)

    aimg = np.array(img) / 255

    weight = np.dstack([aimg[:, :, 0]] * 3)

    background = (1 - weight) * background + aimg
    background[background > 1.0] = 1.0
    background[background < 0.0] = 0.0

    background = crop_image_to_bounds(background, geo_bounds, tile_bounds)

    f = io.BytesIO()
    pl.imsave(f, background, format="png")
    return bytes(f.getbuffer())
