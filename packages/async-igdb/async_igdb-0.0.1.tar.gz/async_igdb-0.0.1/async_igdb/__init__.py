from .client import BaseClient
from .models import *
from . import models
from .manager import ApiObjectManager


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
