from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from ..simple import RegionModel


class CoverModel(BaseApiModel):
    type = "covers"
    searchable = False

    alpha_channel: bool = False
    animated: bool = False
    game: int | None = None
    height: int = 0
    image_id: str | None = None
    width: int = 0
    game: ids(GameModel) = None
    game_localization: ids("game_localizations") | "GameLocalizationModel" = None


class GameLocalizationModel(BaseApiModel):
    type = "game_localizations"
    searchable = False

    cover: ids(CoverModel) = None
    game: ids(GameModel) = None
    name: str | None = None
    region: ids(RegionModel) = None
