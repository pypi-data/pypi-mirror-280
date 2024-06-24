# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf.api import get_values, exp03_wotlk
from wow_wtf.tests.exp03_wotlk.acc_enum import (
    AccountEnum as AccEnum,
    CharacterEnum as CharEnum,
)
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

Client = exp03_wotlk.Client
AccMap = exp03_wotlk.AccLvlMapping
CharMap = exp03_wotlk.CharLvlMapping
WtfMapping = exp03_wotlk.WtfMapping

dir_here = Path.dir_here(__file__)
dir_game_client = dir_here.joinpath("world_of_warcraft_enUS")

client = exp03_wotlk.Client(
    locale="enUS",
    dir=dir_game_client,
)
all_accounts = get_values(AccEnum)
all_characters = get_values(CharEnum)

client_config = ClientConfigEnum.f_1920_1080_max_graphic_sound

# ------------------------------------------------------------------------------
# acc_user_interface
# ------------------------------------------------------------------------------
# The AccLvlMapping.make_many and CharLvlMapping.make_many are very helpful
acc_user_interface = AccMap.make_many(all_accounts, AuiEnum.default)

# ------------------------------------------------------------------------------
# acc_saved_variables
# ------------------------------------------------------------------------------
acc_saved_variables = AccMap.make_many(all_accounts, get_values(AsvEnum))

# ------------------------------------------------------------------------------
# char_user_interface
# ------------------------------------------------------------------------------
char_user_interface = CharMap.make_many(all_characters, CuiEnum.default)

# ------------------------------------------------------------------------------
# char_chat
# ------------------------------------------------------------------------------
char_chat = CharMap.make_many(all_characters, CcEnum.default)

# ------------------------------------------------------------------------------
# char_keybinding
# ------------------------------------------------------------------------------
war_and_dk_chars = [
    CharEnum.acc01_realm1_mywarrior,
    CharEnum.acc03_realm1_mydk,
]
char_keybinding = CharMap.make_many(
    all_characters.difference(war_and_dk_chars), CkEnum.default
) + CharMap.make_many(war_and_dk_chars, CkEnum.warrior_and_dk)

# ------------------------------------------------------------------------------
# char_layout
# ------------------------------------------------------------------------------
char_layout = CharMap.make_many(all_characters, ClEnum.default)

# ------------------------------------------------------------------------------
# char_addons
# ------------------------------------------------------------------------------
mb_master_pala_chars = [
    CharEnum.acc02_realm1_mypaladin,
]
mb_master_non_pala_chars = [
    CharEnum.acc03_realm1_mydk,
]
mb_slave_pala_chars = []
# 这个是最多的, 除了司机和圣骑士, 剩下的角色肯定是最多的
mb_slave_non_pala_chars = all_characters.difference(
    mb_master_pala_chars + mb_master_non_pala_chars + mb_slave_pala_chars
)
char_addons = (
    CharMap.make_many(
        mb_master_pala_chars,
        CaEnum.f_01_multiboxer_master_paladin,
    )
    + CharMap.make_many(
        mb_master_non_pala_chars,
        CaEnum.f_02_multiboxer_master_non_paladin,
    )
    + CharMap.make_many(
        mb_slave_pala_chars,
        CaEnum.f_03_multiboxer_slave_paladin,
    )
    + CharMap.make_many(
        mb_slave_non_pala_chars,
        CaEnum.f_04_multiboxer_slave_non_paladin,
    )
)

# ------------------------------------------------------------------------------
# char_saved_variables
# ------------------------------------------------------------------------------
char_saved_variables = CharMap.make_many(
    all_characters,
    [
        CsvEnum.AtlasLoot,
        CsvEnum.Atlas,
        CsvEnum.Vendomatic,
    ],
) + [
    CharMap(char=CharEnum.acc02_realm1_mypaladin, file=CsvEnum.paladin__Healbot),
    CharMap(char=CharEnum.acc10_realm1_mypriest, file=CsvEnum.priest__Healbot),
]

# ------------------------------------------------------------------------------
# wtf_mapping
# ------------------------------------------------------------------------------
wtf_mapping = exp03_wotlk.WtfMapping(
    client=client,
    all_accounts=all_accounts,
    all_characters=all_characters,
    client_config=client_config,
    acc_user_interface=acc_user_interface,
    # acc_macros=acc_macros,
    acc_saved_variables=acc_saved_variables,
    char_user_interface=char_user_interface,
    char_chat=char_chat,
    char_keybinding=char_keybinding,
    char_layout=char_layout,
    char_addons=char_addons,
    # char_macros=char_macros,
    char_saved_variables=char_saved_variables,
)
