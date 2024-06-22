from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *


class AgeRatingModel(BaseApiModel):
    type = "age_ratings"
    searchable = False

    category: AgeRatingCategoryEnum | None = None
    content_descriptions: ids(AgeRatingContentDescriptionModel) = []
    rating: AgeRatingEnum | None = None
    rating_cover_url: str | None = None
    synopsis: str | None = None
