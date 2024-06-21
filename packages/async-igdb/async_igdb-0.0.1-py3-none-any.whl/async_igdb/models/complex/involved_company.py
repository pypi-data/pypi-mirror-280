from datetime import datetime
from typing import Union
from ..base import BaseApiModel, ids
from ...util.enums import *
from .game import GameModel
from .company import CompanyModel


class InvolvedCompanyModel(BaseApiModel):
    type = "involved_companies"
    searchable = False

    company: ids(CompanyModel) = None
    developer: bool = False
    game: ids(GameModel) = None
    porting: bool = False
    publisher: bool = False
    supporting: bool = False
