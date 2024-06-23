# Copyright (c) 2022,2023,2024 Kian-Meng Ang

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Generals Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Nox configuration."""
from io import StringIO

import nox

from heatmap_cli.cli import build_parser


@nox.session(reuse_venv=True)
def deps(session: nox.Session) -> None:
    """Update pre-commit hooks and deps."""
    session.install("pre-commit", "pipenv")
    session.run("pre-commit", "autoupdate", *session.posargs)
    session.run("pipenv", "update")


@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    """Runs pre-commit linter."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12"], reuse_venv=True)
def test(session: nox.Session) -> None:
    """Runs test."""
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run("pytest", "--numprocesses", "auto")


@nox.session(python="3.12", reuse_venv=True)
def cov(session: nox.Session) -> None:
    """Runs test coverage."""
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run(
        "pytest",
        "--numprocesses",
        "auto",
        "--cov",
        "--cov-report=term",
        "--cov-report=html",
    )


@nox.session(python="3.12", reuse_venv=True)
def doc(session: nox.Session) -> None:
    """Build doc with sphinx."""
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run("sphinx-build", "docs/source/", "docs/build/html")


@nox.session(python="3.12", reuse_venv=True)
def readme(_session: nox.Session) -> None:
    """Update console help menu to readme."""
    with open("README.md", "r+", encoding="utf8") as f:
        content = f.read()
        marker = content.split("<!--help !-->")[1]

        buffer = StringIO()
        parser = build_parser(["-vvv"])
        parser.print_help(file=buffer)

        help_message = f"\n\n```console\n{buffer.getvalue()}```\n\n"
        readme_md = content.replace(marker, help_message)

        f.seek(0)
        f.write(readme_md)
