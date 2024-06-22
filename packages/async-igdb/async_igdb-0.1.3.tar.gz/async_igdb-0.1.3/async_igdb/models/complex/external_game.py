from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from .platform import PlatformModel


class ExternalGameModel(BaseApiModel):
    type = "external_games"
    searchable = False

    category: ExternalGameCategoryEnum | None = None
    countries: list[int] = []
    game: ids(GameModel) = None
    media: ExternalGameMediaEnum | None = None
    name: str | None = None
    platform: ids(PlatformModel) = None
    uid: str | None = None
    year: int | None = None
