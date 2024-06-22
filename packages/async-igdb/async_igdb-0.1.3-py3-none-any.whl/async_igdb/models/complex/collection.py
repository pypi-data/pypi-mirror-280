from datetime import datetime
from typing import Union

from pydantic import Field
from ..base import BaseApiModel, ids
from .collection_relation import CollectionRelationModel
from ..simple import CollectionTypeModel
from .game import GameModel
from ...util.enums import *


class CollectionModel(BaseApiModel):
    type = "collections"
    searchable = True

    as_child_relations: ids(CollectionRelationModel) = []
    as_parent_relations: ids(CollectionRelationModel) = []
    games: ids(GameModel) = []
    name: str | None = None
    slug: str | None = None
    collection_type: ids(CollectionTypeModel) = Field(default=None, alias="type")
