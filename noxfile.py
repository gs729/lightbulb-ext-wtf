# -*- coding: utf-8 -*-
# Copyright © tandemdude 2020-present
#
# This file is part of Filament.
#
# Filament is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Filament is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Filament. If not, see <https://www.gnu.org/licenses/>.
import os

import nox
from nox import options

PATH_TO_PROJECT = os.path.join(".", "wtf")
SCRIPT_PATHS = [
    PATH_TO_PROJECT,
    "noxfile.py",
    "docs/source/conf.py",
]

options.sessions = ["format_fix", "sphinx"]


@nox.session()
def format_fix(session):
    session.install("black")
    session.install("isort")
    session.run("python", "-m", "black", *SCRIPT_PATHS)
    session.run("python", "-m", "isort", *SCRIPT_PATHS)


# noinspection PyShadowingBuiltins
@nox.session()
def format(session):
    session.run("pip", "install", "-U", "black")
    session.run("python", "-m", "black", *SCRIPT_PATHS, "--check")


@nox.session(reuse_venv=True)
def sphinx(session):
    session.install("-Ur", "docs_requirements.txt")
    session.install("-Ur", "requirements.txt")
    session.run("python", "-m", "sphinx.cmd.build", "docs/source", "docs/build", "-b", "html")
