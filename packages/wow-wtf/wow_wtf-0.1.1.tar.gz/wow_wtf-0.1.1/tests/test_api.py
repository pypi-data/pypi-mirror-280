# -*- coding: utf-8 -*-

from wow_wtf import api


def test():
    _ = api
    _ = api.get_values
    _ = api.group_by
    _ = api.logger
    _ = api.exp03_wotlk

    exp03_wotlk = api.exp03_wotlk
    _ = exp03_wotlk.Client
    _ = exp03_wotlk.AccLvlMapping
    _ = exp03_wotlk.CharLvlMapping
    _ = exp03_wotlk.WtfMapping
    _ = exp03_wotlk.to_module
    _ = exp03_wotlk.Client.get_account_config_cache_wtf
    _ = exp03_wotlk.Client.get_account_bindings_cache_wtf
    _ = exp03_wotlk.Client.get_account_macros_cache_txt
    _ = exp03_wotlk.Client.get_account_saved_variables
    _ = exp03_wotlk.Client.get_character_config_cache_wtf
    _ = exp03_wotlk.Client.get_character_chat_cache_txt
    _ = exp03_wotlk.Client.get_character_bindings_cache_wtf
    _ = exp03_wotlk.Client.get_character_layout_local_txt
    _ = exp03_wotlk.Client.get_character_addons_txt
    _ = exp03_wotlk.Client.get_character_macros_cache_txt
    _ = exp03_wotlk.Client.get_character_saved_variables
    _ = exp03_wotlk.AccLvlMapping.make_many
    _ = exp03_wotlk.CharLvlMapping.make_many
    _ = exp03_wotlk.WtfMapping.apply_client_config
    _ = exp03_wotlk.WtfMapping.apply_account_user_interface
    _ = exp03_wotlk.WtfMapping.apply_account_macros
    _ = exp03_wotlk.WtfMapping.apply_account_saved_variables
    _ = exp03_wotlk.WtfMapping.apply_character_user_interface
    _ = exp03_wotlk.WtfMapping.apply_character_chat
    _ = exp03_wotlk.WtfMapping.apply_character_keybinding
    _ = exp03_wotlk.WtfMapping.apply_character_layout
    _ = exp03_wotlk.WtfMapping.apply_character_addons
    _ = exp03_wotlk.WtfMapping.apply_character_macros
    _ = exp03_wotlk.WtfMapping.apply_character_saved_variables


if __name__ == "__main__":
    from wow_wtf.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf.api", preview=False)
