from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class KeywordModel(BaseApiModel):
    type = "keywords"
    searchable = False

    name: str | None = None
    slug: str | None = None
