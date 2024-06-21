from datetime import datetime
from typing import Literal, Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class RegionModel(BaseApiModel):
    type = "regions"
    searchable = False

    category: Literal["locale", "continent"] | None = None
    identifier: str | None = None
    name: str | None = None
