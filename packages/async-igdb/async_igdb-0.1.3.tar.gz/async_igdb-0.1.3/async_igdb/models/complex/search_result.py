from datetime import datetime
from typing import Any, Literal, Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .character import CharacterModel
from .collection import CollectionModel
from .company import CompanyModel
from .game import GameModel
from .platform import PlatformModel
from ..simple import ThemeModel


class SearchResultModel(BaseApiModel):
    type = "search"
    searchable = False

    alternative_name: str | None = None
    character: ids(CharacterModel) = None
    collection: ids(CollectionModel) = None
    company: ids(CompanyModel) = None
    description: str | None = None
    game: ids(GameModel) = None
    name: str | None = None
    platform: ids(PlatformModel) = None
    published_at: datetime | None = None
    theme: ids(ThemeModel) = None

    @property
    def result_type(
        self,
    ) -> (
        Literal["character", "collection", "company", "game", "platform", "theme"]
        | None
    ):
        for key in ["character", "collection", "company", "game", "platform", "theme"]:
            if getattr(self, key) != None:
                return key

        return None

    async def get_result(self) -> Any | None:
        match self.result_type:
            case "character":
                ref = "characters"
            case "collection":
                ref = "collections"
            case "company":
                ref = "companies"
            case "game":
                ref = "games"
            case "platform":
                ref = "platforms"
            case "theme":
                ref = "themes"
            case _:
                return None

        constructor: BaseApiModel = self.client.REGISTRY[ref]
        return await constructor.from_request(
            self.client, ids=[getattr(self, self.result_type)]
        )
