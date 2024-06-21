from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel


class FranchiseModel(BaseApiModel):
    type = "franchises"
    searchable = False

    games: ids(GameModel) = []
    name: str | None = None
    slug: str | None = None
