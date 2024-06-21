from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class PlatformFamilyModel(BaseApiModel):
    type = "platform_families"
    searchable = False

    name: str | None = None
    slug: str | None = None
