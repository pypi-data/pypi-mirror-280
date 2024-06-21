# ViCodePy - A video coder for psychological experiments
#
# Copyright (C) 2024 Esteban Milleret
# Copyright (C) 2024 Rafael Laboissière
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import appdirs
from yaml import load, Loader
from pathlib import Path

CONFIG_FILENAME = "config.yml"
APP_NAME = "vicodepy"


class Config(dict):
    def __init__(self):
        config = self._load_file(CONFIG_FILENAME)
        if not config:
            path = Path(appdirs.user_config_dir(APP_NAME)).joinpath(
                CONFIG_FILENAME
            )
            config = self._load_file(path)
            if not config:
                path = Path(appdirs.site_config_dir(APP_NAME)).joinpath(
                    CONFIG_FILENAME
                )
                config = self._load_file(path)
                if not config:
                    path = (
                        Path(__file__)
                        .parent.joinpath("config")
                        .joinpath(CONFIG_FILENAME)
                    )
                    config = self._load_file(path)
        for k, v in config.items():
            super().__setitem__(k, v)

    def _load_file(self, path):
        if os.path.isfile(path):
            with open(path, "r") as fid:
                return load(fid, Loader=Loader)
        else:
            return None
