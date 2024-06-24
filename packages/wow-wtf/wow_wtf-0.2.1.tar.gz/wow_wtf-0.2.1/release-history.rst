.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.1 (2024-06-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following public API:
    - :func:`concat_lists <wow_wtf.utils.concat_lists>`

**Minor Improvements**

- Add ``acc_group.py`` and ``wtf_group.py`` to the example ``wow_wtf/tests/exp03_wotlk/`` directory.


0.1.1 (2024-06-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add the following public API:
    - :func:`get_values <wow_wtf.utils.get_values>`
    - :func:`group_by <wow_wtf.utils.group_by>`
    - :attr:`logger <wow_wtf.logger.logger>`
    - :mod:`exp03_wotlk <wow_wtf.exp03_wotlk.api>`
    - :class:`exp03_wotlk.Client <wow_wtf.exp03_wotlk.mapping.Client>`
    - :class:`exp03_wotlk.AccLvlMapping <wow_wtf.exp03_wotlk.mapping.AccLvlMapping>`
    - :class:`exp03_wotlk.CharLvlMapping <wow_wtf.exp03_wotlk.mapping.CharLvlMapping>`
    - :class:`exp03_wotlk.WtfMapping <wow_wtf.exp03_wotlk.mapping.WtfMapping>`
    - :class:`exp03_wotlk.to_module <wow_wtf.exp03_wotlk.dataset.to_module>`
    - :meth:`exp03_wotlk.Client.get_account_config_cache_wtf <wow_wtf.exp03_wotlk.mapping.Client.get_account_config_cache_wtf>`
    - :meth:`exp03_wotlk.Client.get_account_bindings_cache_wtf <wow_wtf.exp03_wotlk.mapping.Client.get_account_bindings_cache_wtf>`
    - :meth:`exp03_wotlk.Client.get_account_macros_cache_txt <wow_wtf.exp03_wotlk.mapping.Client.get_account_macros_cache_txt>`
    - :meth:`exp03_wotlk.Client.get_account_saved_variables <wow_wtf.exp03_wotlk.mapping.Client.get_account_saved_variables>`
    - :meth:`exp03_wotlk.Client.get_character_config_cache_wtf <wow_wtf.exp03_wotlk.mapping.Client.get_character_config_cache_wtf>`
    - :meth:`exp03_wotlk.Client.get_character_chat_cache_txt <wow_wtf.exp03_wotlk.mapping.Client.get_character_chat_cache_txt>`
    - :meth:`exp03_wotlk.Client.get_character_bindings_cache_wtf <wow_wtf.exp03_wotlk.mapping.Client.get_character_bindings_cache_wtf>`
    - :meth:`exp03_wotlk.Client.get_character_layout_local_txt <wow_wtf.exp03_wotlk.mapping.Client.get_character_layout_local_txt>`
    - :meth:`exp03_wotlk.Client.get_character_addons_txt <wow_wtf.exp03_wotlk.mapping.Client.get_character_addons_txt>`
    - :meth:`exp03_wotlk.Client.get_character_macros_cache_txt <wow_wtf.exp03_wotlk.mapping.Client.get_character_macros_cache_txt>`
    - :meth:`exp03_wotlk.Client.get_character_saved_variables <wow_wtf.exp03_wotlk.mapping.Client.get_character_saved_variables>`
    - :meth:`exp03_wotlk.AccLvlMapping.make_many <wow_wtf.exp03_wotlk.mapping.AccLvlMapping.make_many>`
    - :meth:`exp03_wotlk.CharLvlMapping.make_many <wow_wtf.exp03_wotlk.mapping.CharLvlMapping.make_many>`
    - :meth:`exp03_wotlk.WtfMapping.apply_client_config <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_client_config>`
    - :meth:`exp03_wotlk.WtfMapping.apply_account_user_interface <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_user_interface>`
    - :meth:`exp03_wotlk.WtfMapping.apply_account_macros <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_macros>`
    - :meth:`exp03_wotlk.WtfMapping.apply_account_saved_variables <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_account_saved_variables>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_user_interface <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_user_interface>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_chat <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_chat>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_keybinding <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_keybinding>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_layout <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_layout>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_addons <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_addons>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_macros <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_macros>`
    - :meth:`exp03_wotlk.WtfMapping.apply_character_saved_variables <wow_wtf.exp03_wotlk.mapping.WtfMapping.apply_character_saved_variables>`
