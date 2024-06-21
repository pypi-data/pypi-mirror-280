from wgit.utils import get_subtree_list
from typing import Callable


def list_subtree():
    subtrees = get_subtree_list()
    if subtrees:
        print("Here the list of the available subtrees:")
        for subtree in subtrees:
            print(f"- {subtree}")
    else:
        print("No subtrees found in the current repository.")


def get_extensions(cmd: str) -> Callable:
    """
    Function used to get the extensions based on the input command.
    Args:
        cmd (str): The command correspondent to the extension, if any.
    Returns:
        function: The extension function requested.
    """
    extensions = {"subtrees": list_subtree}
    return extensions.get(cmd, None)
