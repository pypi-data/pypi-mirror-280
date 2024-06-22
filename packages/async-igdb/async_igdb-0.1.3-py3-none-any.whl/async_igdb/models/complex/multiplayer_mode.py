from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from .platform import PlatformModel


class MultiplayerModeModel(BaseApiModel):
    type = "multiplayer_modes"
    searchable = False

    campaigncoop: bool = False
    dropin: bool = False
    game: ids(GameModel) = None
    lancoop: bool = False
    offlinecoop: bool = False
    offlinecoopmax: int | None = None
    offlinemax: int | None = None
    onlinecoop: bool = False
    onlinecoopmax: int | None = None
    onlinemax: int | None = None
    platform: ids(PlatformModel) = None
    splitscreen: bool = False
    splitscreenonline: bool = False
