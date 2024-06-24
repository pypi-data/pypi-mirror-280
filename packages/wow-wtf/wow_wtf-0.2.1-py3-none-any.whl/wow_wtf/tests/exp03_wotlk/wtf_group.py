# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from wow_wtf.api import get_values
from wow_wtf.tests.exp03_wotlk.wtf_enum import (
    ClientConfigEnum,
    AccountUserInterfaceEnum as AuiEnum,
    AccountMacrosEnum as AmEnum,
    AccountSavedVariablesEnum as AsvEnum,
    CharacterUserInterfaceEnum as CuiEnum,
    CharacterChatEnum as CcEnum,
    CharacterKeybindingsEnum as CkEnum,
    CharacterLayoutEnum as ClEnum,
    CharacterAddonsEnum as CaEnum,
    CharacterMacrosEnum as CmEnum,
    CharacterSavedVariablesEnum as CsvEnum,
)


# ==============================================================================
# START of manual editing
# ==============================================================================
class AsvGroupEnum:
    common = get_values(AsvEnum)


class CsvGroupEnum:
    common = [
        CsvEnum.Atlas,
        CsvEnum.AtlasLoot,
        CsvEnum.Vendomatic,
    ]


# ==============================================================================
# End of manual editing
# ==============================================================================
