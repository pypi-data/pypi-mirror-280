from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class PlatformWebsiteModel(BaseApiModel):
    type = "platform_websites"
    searchable = False

    category: PlatformWebsiteCategoryEnum | None = None
    trusted: bool = False
