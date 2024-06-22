from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class GameEngineLogoModel(BaseApiModel):
    type = "game_engine_logos"
    searchable = False

    alpha_channel: bool = False
    animated: bool = False
    height: int = 0
    image_id: str | None = None
    width: int = 0
