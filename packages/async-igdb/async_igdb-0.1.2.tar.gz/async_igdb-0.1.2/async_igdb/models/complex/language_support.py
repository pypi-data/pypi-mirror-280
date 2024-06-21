from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *
from .game import GameModel


class LanguageSupportModel(BaseApiModel):
    type = "language_supports"
    searchable = False

    game: ids(GameModel) = None
    language: ids(LanguageModel) = None
    language_support_type: ids(LanguageSupportTypeModel) = None
