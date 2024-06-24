# -*- coding: utf-8 -*-

from wow_wtf.api import exp03_wotlk
from wow_wtf.logger import logger


def test():
    from wow_wtf.tests.exp03_wotlk.acc_dataset import dir_here, ds

    path = dir_here.joinpath("acc_enum.py")
    content = ds.to_module(
        import_line="from wow_wtf.tests.exp03_wotlk.acc_dataset import ds",
    )
    path.write_text(content)

    content = exp03_wotlk.to_module(
        dir_here,
        import_dir_root_line="from wow_wtf.tests.exp03_wotlk.wtf_dataset import dir_root",
    )
    dir_here.joinpath("wtf_enum.py").write_text(content, encoding="utf-8")

    from wow_wtf.tests.exp03_wotlk.wtf_mapping import wtf_mapping

    wtf_mapping.client.dir_wtf.remove_if_exists()
    real_run = True

    with logger.disabled(
        disable=True,  # DON't show log
        # disable=False, # show log
    ):
        wtf_mapping.apply_client_config(real_run)

        wtf_mapping.apply_account_user_interface(real_run)
        wtf_mapping.apply_account_saved_variables(real_run)

        wtf_mapping.apply_character_user_interface(real_run)
        wtf_mapping.apply_character_chat(real_run)
        wtf_mapping.apply_character_keybinding(real_run)
        wtf_mapping.apply_character_layout(real_run)
        wtf_mapping.apply_character_addons(real_run)
        wtf_mapping.apply_character_saved_variables(real_run)


if __name__ == "__main__":
    from wow_wtf.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf.exp03_wotlk", preview=False)
