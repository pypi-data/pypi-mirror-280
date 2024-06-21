from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class ThemeModel(BaseApiModel):
    type = "themes"
    searchable = True

    name: str | None = None
    slug: str | None = None
