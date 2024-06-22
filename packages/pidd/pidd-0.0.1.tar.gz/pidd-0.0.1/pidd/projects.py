"""CI projects."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import urljoin

GROUP_AND_NAME = [
    "GITHUB_REPOSITORY",
    "CI_PROJECT_PATH",
]
SERVER_URL = [
    "GITHUB_SERVER_URL",
    "CI_SERVER_URL",
]


class Projects:
    def __init__(self: Projects) -> None:
        self.environment = os.environ
        # group, name
        for variable in GROUP_AND_NAME:
            if value := self.environment.get(variable, None):
                path = Path(value)
                self.group = str(path.parent)
                self.name = path.name
        # url
        for variable in SERVER_URL:
            if value := self.environment.get(variable, None):
                self.url = urljoin(value, self.group)

    def __str__(self: Projects) -> str:
        return f"""\
group = {self.group}
 name = {self.name}
  url = {self.url}
"""
