from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ..simple import *
from ...util.enums import *


class CollectionRelationTypeModel(BaseApiModel):
    type = "collection_relation_types"
    searchable = False

    allowed_child_type: ids(CollectionTypeModel) = None
    allowed_parent_type: ids(CollectionTypeModel) = None
    description: str | None = None
    name: str | None = None
