import subprocess
from os.path import exists


def get_changed_subtree() -> list[str]:
    """
    Get the list of subtrees folders in which there are some changes, according to git.

    Returns:
        A list of strings representing the names of the changed subtrees.
    """
    print("Checking for changes in subtrees...")
    try:
        # Get the list of changed files
        result = subprocess.run(
            ["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True
        )
        changed_files = result.stdout.strip().split("\n")
        if changed_files:
            subtree_folders = get_subtree_list()
            changed_files = [file.split("/")[0][2:].strip() for file in changed_files]
            changed_files = [f for f in changed_files if f in subtree_folders]
        return changed_files

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git command: {e}")
        return []


def get_current_branch() -> str:
    """
    Get the name of the current branch in the git repository.

    Returns:
        A string representing the name of the current branch.
    """
    return subprocess.run(
        ["git", "branch", "--show-current"],
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()


def get_subtree_list() -> list[str]:
    """
    Get the list of subtrees in the git repository.
    Only the subtrees that are currently present in the local filesystem are returned.

    Returns:
        A set of strings representing the names of the subtrees.
    """
    res = (
        subprocess.run(
            ["git", "log"],
            stdout=subprocess.PIPE,
            text=True,
        )
        .stdout.strip()
        .split("\n")
    )
    subtrees = [s for s in res if "git-subtree-dir" in s]
    subtrees = set([s.replace("git-subtree-dir: ", "").strip() for s in subtrees])
    subtrees = sorted([s for s in subtrees if exists(s)])
    return subtrees
