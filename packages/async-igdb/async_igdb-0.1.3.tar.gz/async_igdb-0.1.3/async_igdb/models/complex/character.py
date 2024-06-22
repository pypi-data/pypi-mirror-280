from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ..simple import *
from ...util.enums import *
from .game import GameModel


class CharacterModel(BaseApiModel):
    type = "characters"
    searchable = True

    akas: list[str] = []
    country_name: str | None = None
    description: str | None = None
    games: ids(GameModel) = []
    gender: CharacterGenderEnum = CharacterGenderEnum.Other
    mug_shot: ids(base=CharacterMugShotModel) = None
    name: str | None = None
    slug: str | None = None
    species: CharacterSpeciesEnum = CharacterSpeciesEnum.Unknown
