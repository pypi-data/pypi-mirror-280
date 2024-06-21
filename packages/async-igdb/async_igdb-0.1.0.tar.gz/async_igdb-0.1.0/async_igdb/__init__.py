from typing import TypeVar

from async_igdb.models.base import IDWrapper
from .client import BaseClient
from .models import *
from . import models
from .manager import ApiObjectManager

TRoot = TypeVar("TRoot", bound=BaseApiModel)


class IGDBClient(BaseClient):
    REGISTRY: dict[str, BaseApiModel] = {
        getattr(models, model).type: getattr(models, model)
        for model in [
            i for i in dir(models) if i.endswith("Model") and i != "BaseApiModel"
        ]
    }

    def _generate_managers(self):
        template = """
@property
def {endpoint}(self) -> ApiObjectManager[{model}]:
    return ApiObjectManager[{model}](self, {model})
"""

        return "".join(
            [
                template.format(endpoint=endpoint, model=model.__name__)
                for endpoint, model in self.REGISTRY.items()
                if endpoint != "search"
            ]
        )

    @property
    def age_rating_content_descriptions(
        self,
    ) -> ApiObjectManager[AgeRatingContentDescriptionModel]:
        return ApiObjectManager[AgeRatingContentDescriptionModel](
            self, AgeRatingContentDescriptionModel
        )

    @property
    def age_ratings(self) -> ApiObjectManager[AgeRatingModel]:
        return ApiObjectManager[AgeRatingModel](self, AgeRatingModel)

    @property
    def alternative_names(self) -> ApiObjectManager[AlternativeNameModel]:
        return ApiObjectManager[AlternativeNameModel](self, AlternativeNameModel)

    @property
    def artworks(self) -> ApiObjectManager[ArtworkModel]:
        return ApiObjectManager[ArtworkModel](self, ArtworkModel)

    @property
    def characters(self) -> ApiObjectManager[CharacterModel]:
        return ApiObjectManager[CharacterModel](self, CharacterModel)

    @property
    def character_mug_shots(self) -> ApiObjectManager[CharacterMugShotModel]:
        return ApiObjectManager[CharacterMugShotModel](self, CharacterMugShotModel)

    @property
    def collection_memberships(self) -> ApiObjectManager[CollectionMembershipModel]:
        return ApiObjectManager[CollectionMembershipModel](
            self, CollectionMembershipModel
        )

    @property
    def collection_membership_types(
        self,
    ) -> ApiObjectManager[CollectionMembershipTypeModel]:
        return ApiObjectManager[CollectionMembershipTypeModel](
            self, CollectionMembershipTypeModel
        )

    @property
    def collections(self) -> ApiObjectManager[CollectionModel]:
        return ApiObjectManager[CollectionModel](self, CollectionModel)

    @property
    def collection_relations(self) -> ApiObjectManager[CollectionRelationModel]:
        return ApiObjectManager[CollectionRelationModel](self, CollectionRelationModel)

    @property
    def collection_relation_types(
        self,
    ) -> ApiObjectManager[CollectionRelationTypeModel]:
        return ApiObjectManager[CollectionRelationTypeModel](
            self, CollectionRelationTypeModel
        )

    @property
    def collection_types(self) -> ApiObjectManager[CollectionTypeModel]:
        return ApiObjectManager[CollectionTypeModel](self, CollectionTypeModel)

    @property
    def company_logos(self) -> ApiObjectManager[CompanyLogoModel]:
        return ApiObjectManager[CompanyLogoModel](self, CompanyLogoModel)

    @property
    def companies(self) -> ApiObjectManager[CompanyModel]:
        return ApiObjectManager[CompanyModel](self, CompanyModel)

    @property
    def company_websites(self) -> ApiObjectManager[CompanyWebsiteModel]:
        return ApiObjectManager[CompanyWebsiteModel](self, CompanyWebsiteModel)

    @property
    def covers(self) -> ApiObjectManager[CoverModel]:
        return ApiObjectManager[CoverModel](self, CoverModel)

    @property
    def event_logos(self) -> ApiObjectManager[EventLogoModel]:
        return ApiObjectManager[EventLogoModel](self, EventLogoModel)

    @property
    def events(self) -> ApiObjectManager[EventModel]:
        return ApiObjectManager[EventModel](self, EventModel)

    @property
    def event_networks(self) -> ApiObjectManager[EventNetworkModel]:
        return ApiObjectManager[EventNetworkModel](self, EventNetworkModel)

    @property
    def external_games(self) -> ApiObjectManager[ExternalGameModel]:
        return ApiObjectManager[ExternalGameModel](self, ExternalGameModel)

    @property
    def franchises(self) -> ApiObjectManager[FranchiseModel]:
        return ApiObjectManager[FranchiseModel](self, FranchiseModel)

    @property
    def game_engine_logos(self) -> ApiObjectManager[GameEngineLogoModel]:
        return ApiObjectManager[GameEngineLogoModel](self, GameEngineLogoModel)

    @property
    def game_engines(self) -> ApiObjectManager[GameEngineModel]:
        return ApiObjectManager[GameEngineModel](self, GameEngineModel)

    @property
    def game_localizations(self) -> ApiObjectManager[GameLocalizationModel]:
        return ApiObjectManager[GameLocalizationModel](self, GameLocalizationModel)

    @property
    def game_modes(self) -> ApiObjectManager[GameModeModel]:
        return ApiObjectManager[GameModeModel](self, GameModeModel)

    @property
    def games(self) -> ApiObjectManager[GameModel]:
        return ApiObjectManager[GameModel](self, GameModel)

    @property
    def game_version_features(self) -> ApiObjectManager[GameVersionFeatureModel]:
        return ApiObjectManager[GameVersionFeatureModel](self, GameVersionFeatureModel)

    @property
    def game_version_feature_values(
        self,
    ) -> ApiObjectManager[GameVersionFeatureValueModel]:
        return ApiObjectManager[GameVersionFeatureValueModel](
            self, GameVersionFeatureValueModel
        )

    @property
    def game_versions(self) -> ApiObjectManager[GameVersionModel]:
        return ApiObjectManager[GameVersionModel](self, GameVersionModel)

    @property
    def game_videos(self) -> ApiObjectManager[GameVideoModel]:
        return ApiObjectManager[GameVideoModel](self, GameVideoModel)

    @property
    def genres(self) -> ApiObjectManager[GenreModel]:
        return ApiObjectManager[GenreModel](self, GenreModel)

    @property
    def involved_companies(self) -> ApiObjectManager[InvolvedCompanyModel]:
        return ApiObjectManager[InvolvedCompanyModel](self, InvolvedCompanyModel)

    @property
    def keywords(self) -> ApiObjectManager[KeywordModel]:
        return ApiObjectManager[KeywordModel](self, KeywordModel)

    @property
    def languages(self) -> ApiObjectManager[LanguageModel]:
        return ApiObjectManager[LanguageModel](self, LanguageModel)

    @property
    def language_supports(self) -> ApiObjectManager[LanguageSupportModel]:
        return ApiObjectManager[LanguageSupportModel](self, LanguageSupportModel)

    @property
    def language_support_types(self) -> ApiObjectManager[LanguageSupportTypeModel]:
        return ApiObjectManager[LanguageSupportTypeModel](
            self, LanguageSupportTypeModel
        )

    @property
    def multiplayer_modes(self) -> ApiObjectManager[MultiplayerModeModel]:
        return ApiObjectManager[MultiplayerModeModel](self, MultiplayerModeModel)

    @property
    def network_types(self) -> ApiObjectManager[NetworkTypeModel]:
        return ApiObjectManager[NetworkTypeModel](self, NetworkTypeModel)

    @property
    def platform_families(self) -> ApiObjectManager[PlatformFamilyModel]:
        return ApiObjectManager[PlatformFamilyModel](self, PlatformFamilyModel)

    @property
    def platform_logos(self) -> ApiObjectManager[PlatformLogoModel]:
        return ApiObjectManager[PlatformLogoModel](self, PlatformLogoModel)

    @property
    def platforms(self) -> ApiObjectManager[PlatformModel]:
        return ApiObjectManager[PlatformModel](self, PlatformModel)

    @property
    def platform_version_companies(
        self,
    ) -> ApiObjectManager[PlatformVersionCompanyModel]:
        return ApiObjectManager[PlatformVersionCompanyModel](
            self, PlatformVersionCompanyModel
        )

    @property
    def platform_versions(self) -> ApiObjectManager[PlatformVersionModel]:
        return ApiObjectManager[PlatformVersionModel](self, PlatformVersionModel)

    @property
    def platform_version_release_dates(
        self,
    ) -> ApiObjectManager[PlatformVersionReleaseDateModel]:
        return ApiObjectManager[PlatformVersionReleaseDateModel](
            self, PlatformVersionReleaseDateModel
        )

    @property
    def platform_websites(self) -> ApiObjectManager[PlatformWebsiteModel]:
        return ApiObjectManager[PlatformWebsiteModel](self, PlatformWebsiteModel)

    @property
    def player_perspectives(self) -> ApiObjectManager[PlayerPerspectiveModel]:
        return ApiObjectManager[PlayerPerspectiveModel](self, PlayerPerspectiveModel)

    @property
    def regions(self) -> ApiObjectManager[RegionModel]:
        return ApiObjectManager[RegionModel](self, RegionModel)

    @property
    def release_dates(self) -> ApiObjectManager[ReleaseDateModel]:
        return ApiObjectManager[ReleaseDateModel](self, ReleaseDateModel)

    @property
    def release_date_statuses(self) -> ApiObjectManager[ReleaseDateStatusModel]:
        return ApiObjectManager[ReleaseDateStatusModel](self, ReleaseDateStatusModel)

    @property
    def screenshots(self) -> ApiObjectManager[ScreenshotModel]:
        return ApiObjectManager[ScreenshotModel](self, ScreenshotModel)

    @property
    def themes(self) -> ApiObjectManager[ThemeModel]:
        return ApiObjectManager[ThemeModel](self, ThemeModel)

    async def search(
        self, query: str, limit: int = 50, offset: int = 0
    ) -> list[SearchResultModel]:
        return await SearchResultModel.from_request(
            self, search=query, limit=limit, offset=offset
        )

    async def resolve_links(
        self, roots: list[TRoot] | TRoot, max_depth: int = 1
    ) -> list[TRoot] | TRoot:
        if type(roots) == list:
            to_resolve: list[TRoot] = roots[:]
            return_list = True
        else:
            to_resolve: list[TRoot] = [roots]
            return_list = False

        result = await self._resolve_array(to_resolve, max_depth, [])
        if return_list:
            return result
        return result[0]

    async def _resolve_array(
        self, roots: list[TRoot], depth: int, visited: list[str]
    ) -> list[TRoot]:
        if depth == 0:
            return roots

        if len(roots) == 0:
            return roots

        if not all([i.type == roots[0].type for i in roots]):
            raise ValueError("Array of models is non-homogenous")

        fields = roots[0].id_fields
        field_map: dict[str, tuple[IDWrapper, list[int]]] = {}
        new_visited = []
        for field in fields.keys():
            field_map[field] = (fields[field], [])
            for root in roots:
                field_val = getattr(root, field)
                index = None
                if type(field_val) == list:
                    index = []
                    for item in field_val:
                        if type(item) == int:
                            index.append(item)
                        elif isinstance(item, BaseApiModel):
                            index.append(item.id)
                elif type(field_val) == int:
                    index = field_val
                elif isinstance(field_val, BaseApiModel):
                    index = field_val.id

                if type(index) == list:
                    for _index in index:
                        if not _index in field_map[field][1]:
                            field_map[field][1].append(_index)
                            if (
                                not f"{fields[field].type}:{_index}" in visited
                                and not f"{fields[field].type}:{_index}" in new_visited
                            ):
                                new_visited.append(f"{fields[field].type}:{_index}")
                else:
                    if index != None and not index in field_map[field][1]:
                        field_map[field][1].append(index)
                        if (
                            not f"{fields[field].type}:{index}" in visited
                            and not f"{fields[field].type}:{index}" in new_visited
                        ):
                            new_visited.append(f"{fields[field].type}:{index}")

        resolved_fields: dict[str, dict[int, BaseApiModel]] = {}
        for field_key, field_params in field_map.items():
            resolved: list[BaseApiModel] = await field_params[0].resolve(
                self, field_params[1]
            )
            to_traverse = []
            for i in resolved:
                if not f"{field_params[0].type}:{i.id}" in visited:
                    if f"{field_params[0].type}:{i.id}" in new_visited:
                        new_visited.remove(f"{field_params[0].type}:{i.id}")
                    visited.append(f"{field_params[0].type}:{i.id}")
                    to_traverse.append(i)
            traversed = {
                i.id: i
                for i in await self._resolve_array(to_traverse, depth - 1, visited)
            }
            resolved_fields[field_key] = {
                obj.id: traversed[obj.id] if obj.id in traversed.keys() else obj
                for obj in resolved
            }

        result = []
        for root in roots:
            for field, field_ids in resolved_fields.items():
                if type(getattr(root, field)) == list:
                    setattr(
                        root,
                        field,
                        [
                            field_ids[i] if i in field_ids.keys() else i
                            for i in getattr(root, field)
                        ],
                    )
                elif type(getattr(root, field)) == int:
                    index = getattr(root, field)
                    setattr(
                        root,
                        field,
                        field_ids[index] if index in field_ids.keys() else index,
                    )

            result.append(root)

        return result
