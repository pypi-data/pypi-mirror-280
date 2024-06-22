from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class CompanyWebsiteModel(BaseApiModel):
    type = "company_websites"
    searchable = False

    category: CompanySiteCategoryEnum | None = None
    trusted: bool = False
