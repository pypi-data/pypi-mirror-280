"""Python Integration, Delivery & Deployment."""

__version__ = "0.0.1"

import os
import sys
from pathlib import Path

import env
from rwx import fs, ps
from rwx.log import stream as log

import pidd
from pidd.project import Project
from pidd.projects import Projects

COMMANDS_PREFIX = "pidd-"

projects = Projects()
project = Project(projects)


def pidd_browse_workspace() -> None:
    browse(project.root)


def pidd_build_project() -> None:
    for extension in ["py", "sh"]:
        path = Path(project.root) / f"build.{extension}"
        if path.exists():
            ps.run(path)
            break
    else:
        pass


def pidd_clone_branch() -> None:
    log.info(projects)
    split()
    log.info(project)
    split()
    log.info(
        f"""\
{project.url}
↓
""",
        end="",
        flush=True,
    )
    ps.run(
        "git",
        "clone",
        "--branch",
        project.branch,
        "--",
        project.url,
        project.root,
    )


def pidd_list_environment() -> None:
    for variable, value in sorted(projects.environment.items()):
        log.info(f"{variable} = {value}")


def pidd_synchronize() -> None:
    host = "rwx.work"
    source = "out"
    user = "cd"
    #
    root = Path(os.sep) / user / project.branch / projects.group / project.name
    #
    target = f"{user}@{host}:{root}"
    ps.run(
        "rsync",
        "--archive",
        "--delete-before",
        "--verbose",
        f"{source}/",
        f"{target}/",
        "--dry-run",
    )


def browse(root: str) -> None:
    paths = []
    for directory, _, files in os.walk(root):
        for file in files:
            absolute_path = Path(directory) / file
            relative_path = os.path.relpath(absolute_path, start=root)
            paths.append(relative_path)
    frame(root)
    for path in sorted(paths):
        log.info(path)
    shut(root)


def cat(file: str) -> None:
    frame(file)
    log.info(fs.read_file_text(file).rstrip())
    shut(file)


def install_commands(path: str) -> None:
    step("Install commands")
    user = Path("/usr/local/bin")
    for command in [
        "browse-workspace",
        "build-project",
        "clone-branch",
        "list-environment",
        "synchronize",
    ]:
        log.info(command)
        (user / f"{COMMANDS_PREFIX}{command}").symlink_to(path)


def main() -> None:
    path, *arguments = sys.argv
    name = Path(path).name
    if name == "__main__.py":
        pidd.set_ssh(*arguments)
        pidd.install_commands(__file__)
    else:
        function = getattr(pidd, name.replace("-", "_"))
        function(*arguments)


def set_ssh(*arguments: str) -> None:
    step("Set SSH")
    #
    ssh_key, ssh_hosts = arguments
    #
    ssh_type = "ed25519"
    #
    home = Path("~").expanduser()
    #
    ssh = home / ".ssh"
    ssh.mkdir(exist_ok=True, parents=True)
    ssh.chmod(0o700)
    #
    key = ssh / f"id_{ssh_type}"
    if ssh_key:
        fs.write(key, ssh_key)
        key.chmod(0o400)
    #
    known = ssh / "known_hosts"
    if ssh_hosts:
        fs.write(known, ssh_hosts)
        known.chmod(0o400)
    #
    browse(ssh)
    cat(known)


def frame(text: str) -> None:
    log.info(f"{env.PIDD_OPEN}{text}")


def shut(text: str) -> None:
    log.info(f"{env.PIDD_SHUT}{text}")


def split() -> None:
    log.info(env.PIDD_SPLT)


def step(text: str) -> None:
    env.PIDD_STEP += 1
    log.info(env.PIDD_DOWN)
    log.info(f"{env.PIDD_VERT} {env.PIDD_STEP} {text}")
    log.info(env.PIDD___UP)
