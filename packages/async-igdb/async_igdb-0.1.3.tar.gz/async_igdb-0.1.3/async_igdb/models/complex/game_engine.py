from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from ..simple import *
from .company import CompanyModel
from .platform import PlatformModel


class GameEngineModel(BaseApiModel):
    type = "game_engines"
    searchable = False

    companies: ids(CompanyModel) = []
    description: str | None = None
    logo: ids(GameEngineLogoModel) = None
    name: str | None = None
    platforms: ids(PlatformModel) = []
    slug: str | None = None
