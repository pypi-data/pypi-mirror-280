from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel


class GameVideoModel(BaseApiModel):
    type = "game_videos"
    searchable = False

    game: ids(GameModel) = None
    name: str | None = None
    video_id: str | None = None
