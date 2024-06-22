from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class GenreModel(BaseApiModel):
    type = "genres"
    searchable = False

    name: str | None = None
    slug: str | None = None
