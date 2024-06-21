from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel


class GameVersionModel(BaseApiModel):
    type = "game_versions"
    searchable = False
    features: ids("game_version_features") | list["GameVersionFeatureModel"] = []
    game: ids(GameModel) = None
    games: ids(GameModel) = []


class GameVersionFeatureModel(BaseApiModel):
    type = "game_version_features"
    searchable = False

    category: GameVersionFeatureCategoryEnum | None = None
    description: str | None = None
    position: int | None = None
    title: str | None = None
    values: (
        ids("game_version_feature_values") | list["GameVersionFeatureValueModel"]
    ) = []


class GameVersionFeatureValueModel(BaseApiModel):
    type = "game_version_feature_values"
    searchable = False

    game: ids(GameModel) = None
    game_feature: ids(GameVersionFeatureModel) = None
    included_feature: GameVersionFeatureValueIncludedFeatureEnum | None = None
    note: str | None = None
