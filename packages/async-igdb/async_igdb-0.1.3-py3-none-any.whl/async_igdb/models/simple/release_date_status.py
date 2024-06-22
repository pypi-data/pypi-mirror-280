from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class ReleaseDateStatusModel(BaseApiModel):
    type = "release_date_statuses"
    searchable = False

    description: str | None = None
    name: str | None = None
