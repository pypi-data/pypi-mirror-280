from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class LanguageSupportTypeModel(BaseApiModel):
    type = "language_support_types"
    searchable = False

    name: str | None = None
