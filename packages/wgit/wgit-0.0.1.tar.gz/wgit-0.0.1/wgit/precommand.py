#!/usr/bin/env python

from platformdirs import user_data_dir
from os import makedirs, remove
from os.path import join, exists
import yaml
from wgit.utils import get_changed_subtree, get_current_branch, get_subtree_list
import subprocess
from typing import Callable

GIT_TO_PUSH_FOLDER = user_data_dir("wgit")


def pre_commit():
    """
    Function executed before committing changes.
    It stores the name of the changed subtrees for a later push.
    If a file containing the names of the changed subtrees already exists, it appends the new ones.
    """
    changed = get_changed_subtree()
    current_branch = get_current_branch()
    if changed:
        print("Found changes in subtrees. Let's store them for a later push. ")
        file_path = join(GIT_TO_PUSH_FOLDER, f"{current_branch}_to_push.txt")

        if not exists(GIT_TO_PUSH_FOLDER):
            makedirs(GIT_TO_PUSH_FOLDER)

        if exists(file_path):
            with open(file_path, "r") as f:
                to_push = yaml.load(f, Loader=yaml.FullLoader)
                changed = list(set(changed) | set(to_push))

        with open(file_path, "w") as f:
            yaml.dump(changed, f)
            print(f"Stored them in {file_path}.")


def pre_push():
    """
    Function executed before pushing the changes.
    It perform the git subtree push to all the changed subtrees.
    """
    current_branch = get_current_branch()

    file_path = join(GIT_TO_PUSH_FOLDER, f"{current_branch}_to_push.txt")

    if exists(file_path):
        with open(file_path, "r") as f:
            changed = yaml.load(f, Loader=yaml.FullLoader)

        print("Start pushing changes to subtrees...")
        for subtree in changed:
            r = subprocess.run(
                [
                    "git",
                    "subtree",
                    "push",
                    f"--prefix={subtree}",
                    f"{subtree}",
                    f"{current_branch}",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            print(f"Changes pushed to subtree '{subtree}'.")
        if r.returncode == 0:
            remove(file_path)


def pre_pull():
    current_branch = get_current_branch()
    subtrees = get_subtree_list()
    for subtree in subtrees:
        subprocess.run(
            [
                "git",
                "subtree",
                "pull",
                f"--prefix={subtree}",
                f"{subtree}",
                f"{current_branch}",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print(f"Changes pulled from subtree '{subtree}'.")


def get_precommand(cmd: str) -> Callable:
    """
    Function used to get the precommand based on the command.
    Args:
        cmd (str): The command from which there will be taken the precommand, if any.
    Returns:
        function: The precommand function corresponding to the command.
    """
    precmds = {"commit": pre_commit, "push": pre_push, "pull": pre_pull}
    return precmds.get(cmd, None)
