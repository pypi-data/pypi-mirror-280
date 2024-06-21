from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class ArtworkModel(BaseApiModel):
    type = "artworks"
    searchable = False

    alpha_channel: bool = False
    animated: bool = False
    game: int | None = None
    height: int = 0
    image_id: str | None = None
    width: int = 0
