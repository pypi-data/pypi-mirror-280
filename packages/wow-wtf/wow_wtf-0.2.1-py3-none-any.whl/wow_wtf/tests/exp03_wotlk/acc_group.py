# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from wow_wtf.api import get_values
from wow_wtf.tests.exp03_wotlk.acc_enum import AccountEnum, CharacterEnum


# ==============================================================================
# START of manual editing
# ==============================================================================
class AccountGroupEnum:
    all_accounts = get_values(AccountEnum)


class CharacterGroupEnum:
    all_characters = get_values(CharacterEnum)

    multiboxer_master_paladin = [
        CharacterEnum.acc02_realm1_mypaladin,
    ]
    multiboxer_master_non_paladin = [
        CharacterEnum.acc03_realm1_mydk,
    ]
    multiboxer_slave_paladin = []
    multiboxer_slave_non_paladin = (
        all_characters.difference(multiboxer_master_paladin)
        .difference(multiboxer_master_non_paladin)
        .difference(multiboxer_slave_paladin)
    )

    warrior_and_dk = [
        CharacterEnum.acc01_realm1_mywarrior,
        CharacterEnum.acc03_realm1_mydk,
    ]
    non_warrior_and_dk = all_characters.difference(warrior_and_dk)


# ==============================================================================
# END of manual editing
# ==============================================================================
