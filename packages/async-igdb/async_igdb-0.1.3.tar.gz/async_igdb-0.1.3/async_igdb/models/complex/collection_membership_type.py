from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *


class CollectionMembershipTypeModel(BaseApiModel):
    type = "collection_membership_types"
    searchable = False

    allowed_collection_type: ids(CollectionTypeModel) = None
    description: str | None = None
    name: str | None = None
