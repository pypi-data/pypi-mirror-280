# -*- coding: utf-8 -*-

from wow_wtf.tests.exp03_wotlk.wtf_mapping import wtf_mapping

real_run = True

wtf_mapping.apply_client_config(real_run)

wtf_mapping.apply_account_user_interface(real_run)
wtf_mapping.apply_account_saved_variables(real_run)

wtf_mapping.apply_character_user_interface(real_run)
wtf_mapping.apply_character_chat(real_run)
wtf_mapping.apply_character_keybinding(real_run)
wtf_mapping.apply_character_layout(real_run)
wtf_mapping.apply_character_addons(real_run)
wtf_mapping.apply_character_saved_variables(real_run)

# wtf_mapping.apply_account_macros(real_run)  ## MOST LIKELY NOT NEEDED, we use SDM AddOns to manage macro
# wtf_mapping.apply_character_macros(real_run) ## MOST LIKELY NOT NEEDED, we use SDM AddOns to manage macro
