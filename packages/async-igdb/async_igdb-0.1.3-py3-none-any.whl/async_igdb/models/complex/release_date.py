from datetime import datetime
from typing import Union

from pydantic import Field
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from .platform import PlatformModel
from ..simple import ReleaseDateStatusModel


class ReleaseDateModel(BaseApiModel):
    type = "release_dates"
    searchable = False

    category: DateCategoryEnum | None = None
    date: datetime | None = None
    game: ids(GameModel) = None
    human: str | None = None
    month: int | None = Field(default=None, alias="m")
    platform: ids(PlatformModel) = None
    region: RegionEnum | None = None
    status: ids(ReleaseDateStatusModel) = None
    year: int | None = Field(default=None, alias="y")
