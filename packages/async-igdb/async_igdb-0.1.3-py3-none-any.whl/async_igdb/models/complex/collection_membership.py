from datetime import datetime
from typing import Union

from pydantic import Field
from ..base import BaseApiModel, ids
from ...util.enums import *
from .collection import CollectionModel
from .game import GameModel
from .collection_membership_type import CollectionMembershipTypeModel
from ..simple import *


class CollectionMembershipModel(BaseApiModel):
    type = "collection_memberships"
    searchable = False

    collection: ids(CollectionModel) = None
    game: ids(GameModel) = None
    membership_type: ids(CollectionMembershipTypeModel) = Field(
        default=None, alias="type"
    )
