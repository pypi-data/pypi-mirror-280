from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *


class CollectionTypeModel(BaseApiModel):
    type = "collection_types"
    searchable = False

    description: str | None = None
    name: str | None = None
