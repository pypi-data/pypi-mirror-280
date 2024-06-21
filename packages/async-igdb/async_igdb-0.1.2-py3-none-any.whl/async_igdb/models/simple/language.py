from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class LanguageModel(BaseApiModel):
    type = "languages"
    searchable = False

    locale: str | None = None
    name: str | None = None
    native_name: str | None = None
