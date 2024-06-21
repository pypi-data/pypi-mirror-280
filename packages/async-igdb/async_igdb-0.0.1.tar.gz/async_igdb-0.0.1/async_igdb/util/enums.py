from enum import IntEnum as BaseIntEnum
from typing import Any


class IntEnum(BaseIntEnum):

    @classmethod
    def _missing_(cls, value: object) -> Any:
        return getattr(cls, cls._member_names_[0])


class AgeRatingCategoryEnum(IntEnum):
    ESRB = 1
    PEGI = 2
    CERO = 3
    USK = 4
    GRAC = 5
    CLASS_IND = 6
    ACB = 7


class AgeRatingEnum(IntEnum):
    Three = 1
    Seven = 2
    Twelve = 3
    Sixteen = 4
    Eighteen = 5
    RP = 6
    EC = 7
    E = 8
    E10 = 9
    T = 10
    M = 11
    AO = 12
    CERO_A = 13
    CERO_B = 14
    CERO_C = 15
    CERO_D = 16
    CERO_Z = 17
    USK_0 = 18
    USK_6 = 19
    USK_12 = 20
    USK_16 = 21
    USK_18 = 22
    GRAC_ALL = 23
    GRAC_Twelve = 24
    GRAC_Fifteen = 25
    GRAC_Eighteen = 26
    GRAC_TESTING = 27
    CLASS_IND_L = 28
    CLASS_IND_Ten = 29
    CLASS_IND_Twelve = 30
    CLASS_IND_Fourteen = 31
    CLASS_IND_Sixteen = 32
    CLASS_IND_Eighteen = 33
    ACB_G = 34
    ACB_PG = 35
    ACB_M = 36
    ACB_MA15 = 37
    ACB_R18 = 38
    ACB_RC = 39


class AgeRatingContentDescriptionEnum(IntEnum):
    ESRB_alcohol_reference = 1
    ESRB_animated_blood = 2
    ESRB_blood = 3
    ESRB_blood_and_gore = 4
    ESRB_cartoon_violence = 5
    ESRB_comic_mischief = 6
    ESRB_crude_humor = 7
    ESRB_drug_reference = 8
    ESRB_fantasy_violence = 9
    ESRB_intense_violence = 10
    ESRB_language = 11
    ESRB_lyrics = 12
    ESRB_mature_humor = 13
    ESRB_nudity = 14
    ESRB_partial_nudity = 15
    ESRB_real_gambling = 16
    ESRB_sexual_content = 17
    ESRB_sexual_themes = 18
    ESRB_sexual_violence = 19
    ESRB_simulated_gambling = 20
    ESRB_strong_language = 21
    ESRB_strong_lyrics = 22
    ESRB_strong_sexual_content = 23
    ESRB_suggestive_themes = 24
    ESRB_tobacco_reference = 25
    ESRB_use_of_alcohol = 26
    ESRB_use_of_drugs = 27
    ESRB_use_of_tobacco = 28
    ESRB_violence = 29
    ESRB_violent_references = 30
    ESRB_animated_violence = 31
    ESRB_mild_language = 32
    ESRB_mild_violence = 33
    ESRB_use_of_drugs_and_alcohol = 34
    ESRB_drug_and_alcohol_reference = 35
    ESRB_mild_suggestive_themes = 36
    ESRB_mild_cartoon_violence = 37
    ESRB_mild_blood = 38
    ESRB_realistic_blood_and_gore = 39
    ESRB_realistic_violence = 40
    ESRB_alcohol_and_tobacco_reference = 41
    ESRB_mature_sexual_themes = 42
    ESRB_mild_animated_violence = 43
    ESRB_mild_sexual_themes = 44
    ESRB_use_of_alcohol_and_tobacco = 45
    ESRB_animated_blood_and_gore = 46
    ESRB_mild_fantasy_violence = 47
    ESRB_mild_lyrics = 48
    ESRB_realistic_blood = 49
    PEGI_violence = 50
    PEGI_sex = 51
    PEGI_drugs = 52
    PEGI_fear = 53
    PEGI_discrimination = 54
    PEGI_bad_language = 55
    PEGI_gambling = 56
    PEGI_online_gameplay = 57
    PEGI_in_game_purchases = 58
    CERO_love = 59
    CERO_sexual_content = 60
    CERO_violence = 61
    CERO_horror = 62
    CERO_drinking_smoking = 63
    CERO_gambling = 64
    CERO_crime = 65
    CERO_controlled_substances = 66
    CERO_languages_and_others = 67
    GRAC_sexuality = 68
    GRAC_violence = 69
    GRAC_fear_horror_threatening = 70
    GRAC_language = 71
    GRAC_alcohol_tobacco_drug = 72
    GRAC_crime_anti_social = 73
    GRAC_gambling = 74
    CLASS_IND_violencia = 75
    CLASS_IND_violencia_extrema = 76
    CLASS_IND_conteudo_sexual = 77
    CLASS_IND_nudez = 78
    CLASS_IND_sexo = 79
    CLASS_IND_sexo_explicito = 80
    CLASS_IND_drogas = 81
    CLASS_IND_drogas_licitas = 82
    CLASS_IND_drogas_ilicitas = 83
    CLASS_IND_linguagem_impropria = 84
    CLASS_IND_atos_criminosos = 85


class CharacterGenderEnum(IntEnum):
    Male = 0
    Female = 1
    Other = 2


class CharacterSpeciesEnum(IntEnum):
    Human = 1
    Alien = 2
    Animal = 3
    Android = 4
    Unknown = 5


class DateCategoryEnum(IntEnum):
    YYYYMMMMDD = 0
    YYYYMMMM = 1
    YYYY = 2
    YYYYQ1 = 3
    YYYYQ2 = 4
    YYYYQ3 = 5
    YYYYQ4 = 6
    TBD = 7


class CompanySiteCategoryEnum(IntEnum):
    official = 1
    wikia = 2
    wikipedia = 3
    facebook = 4
    twitter = 5
    twitch = 6
    instagram = 8
    youtube = 9
    iphone = 10
    ipad = 11
    android = 12
    steam = 13
    reddit = 14
    itch = 15
    epicgames = 16
    gog = 17
    discord = 18


class ExternalGameCategoryEnum(IntEnum):
    steam = 1
    gog = 5
    youtube = 10
    microsoft = 11
    apple = 13
    twitch = 14
    android = 15
    amazon_asin = 20
    amazon_luna = 22
    amazon_adg = 23
    epic_game_store = 26
    oculus = 28
    utomik = 29
    itch_io = 30
    xbox_marketplace = 31
    kartridge = 32
    playstation_store_us = 36
    focus_entertainment = 37
    xbox_game_pass_ultimate_cloud = 54
    gamejolt = 55


class ExternalGameMediaEnum(IntEnum):
    digital = 1
    physical = 2


class GameCategoryEnum(IntEnum):
    main_game = 0
    dlc_addon = 1
    expansion = 2
    bundle = 3
    standalone_expansion = 4
    mod = 5
    episode = 6
    season = 7
    remake = 8
    remaster = 9
    expanded_game = 10
    port = 11
    fork = 12
    pack = 13
    update = 14


class GameStatusEnum(IntEnum):
    released = 0
    alpha = 2
    beta = 3
    early_access = 4
    offline = 5
    cancelled = 6
    rumored = 7
    delisted = 8


class GameVersionFeatureCategoryEnum(IntEnum):
    boolean = 0
    description = 1


class GameVersionFeatureValueIncludedFeatureEnum(IntEnum):
    NOT_INCLUDED = 0
    INCLUDED = 1
    PRE_ORDER_ONLY = 2


class PlatformCategoryEnum(IntEnum):
    console = 1
    arcade = 2
    platform = 3
    operating_system = 4
    portable_console = 5
    computer = 6


class RegionEnum(IntEnum):
    europe = 1
    north_america = 2
    australia = 3
    new_zealand = 4
    japan = 5
    china = 6
    asia = 7
    worldwide = 8
    korea = 9
    brazil = 10


class PlatformWebsiteCategoryEnum(IntEnum):
    official = 1
    wikia = 2
    wikipedia = 3
    facebook = 4
    twitter = 5
    twitch = 6
    instagram = 8
    youtube = 9
    iphone = 10
    ipad = 11
    android = 12
    steam = 13
    reddit = 14
    discord = 15
    google_plus = 16
    tumblr = 17
    linkedin = 18
    pinterest = 19
    soundcloud = 20


class WebsiteCategoryEnum(IntEnum):
    official = 1
    wikia = 2
    wikipedia = 3
    facebook = 4
    twitter = 5
    twitch = 6
    instagram = 8
    youtube = 9
    iphone = 10
    ipad = 11
    android = 12
    steam = 13
    reddit = 14
    itch = 15
    epicgames = 16
    gog = 17
    discord = 18
