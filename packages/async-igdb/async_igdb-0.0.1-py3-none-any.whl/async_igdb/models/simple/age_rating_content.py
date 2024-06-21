from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class AgeRatingContentDescriptionModel(BaseApiModel):
    type = "age_rating_content_descriptions"
    searchable = False

    category: AgeRatingContentDescriptionEnum | None = None
    description: str | None = None
