from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class GameModeModel(BaseApiModel):
    type = "game_modes"
    searchable = False

    name: str | None = None
    slug: str | None = None
