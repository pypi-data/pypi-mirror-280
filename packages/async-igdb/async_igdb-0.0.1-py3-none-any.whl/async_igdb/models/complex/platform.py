from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *
from .platform_version import PlatformVersionModel


class PlatformModel(BaseApiModel):
    type = "platforms"
    searchable = True

    abbreviation: str | None = None
    alternative_name: str | None = None
    category: PlatformCategoryEnum | None = None
    generation: int | None = None
    name: str | None = None
    platform_family: ids(PlatformFamilyModel) = None
    platform_logo: ids(PlatformLogoModel) = None
    slug: str | None = None
    summary: str | None = None
    versions: ids(PlatformVersionModel) = []
    websites: ids(PlatformWebsiteModel) = []
