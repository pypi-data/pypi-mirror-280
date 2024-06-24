# -*- coding: utf-8 -*-

from pathlib_mate import Path
from wow_acc.api import Dataset

dir_here = Path(__file__).absolute().parent
ds = Dataset.from_yaml(dir_here.joinpath("acc_dataset.yml").read_text())

if __name__ == "__main__":
    path = dir_here.joinpath("acc_enum.py")
    content = ds.to_module(
        import_line="from wow_wtf.tests.exp03_wotlk.acc_dataset import ds",
    )
    path.write_text(content)
