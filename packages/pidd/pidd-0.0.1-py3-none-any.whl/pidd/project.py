"""CI project."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urljoin

if TYPE_CHECKING:
    from pidd.projects import Projects

BRANCH = [
    "GITHUB_REF_NAME",
    "CI_COMMIT_BRANCH",
]
NAME = [
    "GITHUB_REPOSITORY",
    "CI_PROJECT_PATH",
]
ROOT = [
    "GITHUB_WORKSPACE",
    "CI_PROJECT_DIR",
]


class Project:
    def __init__(self: Project, projects: Projects) -> None:
        self.projects = projects
        # branch
        for variable in BRANCH:
            if value := projects.environment.get(variable, None):
                self.branch = value
        # name
        for variable in NAME:
            if value := projects.environment.get(variable, None):
                self.name = Path(value).name
        # root
        for variable in ROOT:
            if value := projects.environment.get(variable, None):
                self.root = value
        # url
        self.url = urljoin(projects.url, self.name)

    def __str__(self: Project) -> str:
        return f"""\
branch = {self.branch}
  name = {self.name}
  root = {self.root}
   url = {self.url}
"""
