from datetime import datetime
from typing import Union

from pydantic import Field
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *
from .platform_version_company import PlatformVersionCompanyModel


class PlatformVersionModel(BaseApiModel):
    type = "platform_versions"
    searchable = False

    companies: ids(PlatformVersionCompanyModel) = []
    connectivity: str | None = None
    cpu: str | None = None
    graphics: str | None = None
    main_manufacturer: ids(PlatformVersionCompanyModel) = None
    media: str | None = None
    memory: str | None = None
    name: str | None = None
    os: str | None = None
    output: str | None = None
    platform_logo: ids(PlatformLogoModel) = None
    platform_version_release_dates: (
        ids("platform_version_release_dates") | list["PlatformVersionReleaseDateModel"]
    ) = []
    resolutions: str | None = None
    slug: str | None = None
    sound: str | None = None
    storage: str | None = None
    summary: str | None = None


class PlatformVersionReleaseDateModel(BaseApiModel):
    type = "platform_version_release_dates"
    searchable = False

    category: DateCategoryEnum | None = None
    date: datetime | None = None
    human: str | None = None
    month: int | None = Field(default=None, alias="m")
    platform_version: ids(PlatformVersionModel) = None
    region: RegionEnum | None = None
    year: int | None = Field(default=None, alias="y")
