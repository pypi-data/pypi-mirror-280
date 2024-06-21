from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel


class WebsiteModel(BaseApiModel):
    type = "websites"
    searchable = False

    category: WebsiteCategoryEnum | None = None
    game: ids(GameModel) = None
    trusted: bool = False
