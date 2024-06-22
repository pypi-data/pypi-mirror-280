from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from ..simple import *


class CompanyModel(BaseApiModel):
    type = "companies"
    searchable = False

    change_date: datetime | None = None
    change_date_category: DateCategoryEnum | None = None
    changed_company_id: ids("companies") | "CompanyModel" = None
    country: int | None = None
    description: str | None = None
    developed: ids(GameModel) = []
    logo: ids(CompanyLogoModel) = None
    name: str | None = None
    parent: ids("companies") | "CompanyModel" = None
    published: ids(GameModel) = []
    slug: str | None = None
    start_date: datetime | None = None
    start_date_category: DateCategoryEnum | None = None
    websites: ids(CompanyWebsiteModel) = []
