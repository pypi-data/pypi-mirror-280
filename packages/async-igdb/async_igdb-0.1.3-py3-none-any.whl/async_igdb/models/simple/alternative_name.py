from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class AlternativeNameModel(BaseApiModel):
    type = "alternative_names"
    searchable = False

    comment: str | None = None
    game: int | None = None
    name: str | None = None
