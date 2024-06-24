# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_wtf.api import exp03_wotlk

dir_root = Path.dir_here(__file__)
if __name__ == "__main__":
    content = exp03_wotlk.to_module(
        dir_root=dir_root,
        import_dir_root_line="from .wtf_dataset import dir_root",
    )
    dir_root.joinpath("wtf_enum.py").write_text(content, encoding="utf-8")
