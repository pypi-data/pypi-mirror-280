from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .company import CompanyModel


class PlatformVersionCompanyModel(BaseApiModel):
    type = "platform_version_companies"
    searchable = False

    comment: str | None = None
    developer: bool = False
    manufacturer: bool = False
    company: ids(CompanyModel) = None
