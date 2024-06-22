from datetime import datetime
from typing import Union

from async_igdb.models.complex.game import GameModel
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game_video import GameVideoModel


class EventModel(BaseApiModel):
    type = "events"
    searchable = False

    description: str | None = None
    end_time: datetime | None = None
    event_logo: ids("event_logos") | "EventLogoModel" = None
    event_networks: ids("event_networks") | list["EventNetworkModel"] = []
    games: ids(GameModel) = []
    live_stream_url: str | None = None
    name: str | None = None
    slug: str | None = None
    start_time: datetime | None = None
    time_zone: str | None = None
    videos: ids(GameVideoModel) = []


class NetworkTypeModel(BaseApiModel):
    type = "network_types"
    searchable = False

    event_networks: ids("event_networks") | list["EventNetworkModel"] = []
    name: str | None = None


class EventNetworkModel(BaseApiModel):
    type = "event_networks"
    searchable = False

    event: ids(EventModel) = None
    network_type: ids(NetworkTypeModel) = None


class EventLogoModel(BaseApiModel):
    type = "event_logos"
    searchable = False

    alpha_channel: bool = False
    animated: bool = False
    game: int | None = None
    height: int = 0
    image_id: str | None = None
    width: int = 0
    event: ids(EventModel) = None
