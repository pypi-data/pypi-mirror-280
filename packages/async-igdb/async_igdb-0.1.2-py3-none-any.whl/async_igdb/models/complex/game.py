from datetime import datetime
from typing import Any, Union
from ..base import BaseApiModel, ids
from .age_rating import AgeRatingModel
from ..simple import *
from ...util.enums import *

class GameModel(BaseApiModel):
    type = "games"
    searchable = True

    age_ratings: ids("age_ratings") = []
    aggregated_rating: float = 0.0
    aggregated_rating_count: int = 0
    alternative_names: ids("alternative_names") = []
    artworks: ids("artworks") = []
    bundles: ids("games") | list["GameModel"] = []
    category: GameCategoryEnum = GameCategoryEnum.main_game
    collection: ids("collections") | Any = None
    collections: ids("collections") | list[Any] = []
    cover: ids("covers") | Any = None
    dlcs: ids("games") | list["GameModel"] = []
    expanded_games: ids("games") | list["GameModel"] = []
    expansions: ids("games") | list["GameModel"] = []
    external_games: ids("external_games") | list[Any] = []
    first_release_date: datetime | None = None
    forks: ids("games") | list["GameModel"] = []
    franchise: ids("franchises") | Any = None
    franchises: ids("franchises") | list[Any] = []
    game_engines: ids("game_engines") | list[Any] = []
    game_localizations: ids("game_localizations") | list[Any] = []
    game_modes: ids("game_modes") | list[Any] = []
    genres: ids("genres") | list[Any] = []
    involved_companies: ids("companies") | list[Any] = []
    keywords: ids("keywords") | list[Any] = []
    language_supports: ids("language_supports") | list[Any] = []
    multiplayer_modes: ids("multiplayer_modes") | list[Any] = []
    name: str | None = None
    parent_game: Union[ids("games"), "GameModel", None] = None
    platforms: ids("platforms") | list[Any] = []
    player_perspectives: ids("player_perspectives") | list[Any] = []
    ports: ids("games") | list["GameModel"] = []
    rating: float = 0.0
    rating_count: int = 0
    release_dates: ids("release_dates") | list[Any] = []
    remakes: ids("games") | list["GameModel"] = []
    remasters: ids("games") | list["GameModel"] = []
    screenshots: ids("screenshots") | list[Any] = []
    similar_games: ids("games") | list["GameModel"] = []
    slug: str | None = None
    standalone_expansions: ids("games") | list["GameModel"] = []
    status: GameStatusEnum | None = None
    storyline: str | None = None
    summary: str | None = None
    tags: list[int] = []
    themes: ids("themes") | list[Any] = []
    total_rating: float = 0.0
    total_rating_count: int = 0
    version_parent: Union[ids("games"), "GameModel", None] = None
    version_title: str | None = None
    videos: ids("game_videos") | list[Any] = []
    websites: ids("websites") | list[Any] = []
