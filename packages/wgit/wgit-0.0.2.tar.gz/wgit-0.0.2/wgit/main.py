import subprocess
import sys
from wgit.precommand import get_precommand
from wgit.extensions import get_extensions


def run_git(cmd: list[str]):
    if sys.platform == "win32":
        cmd.insert(0, "git.exe")

    elif sys.platform == "linux":
        cmd.insert(0, "/usr/bin/git")
    else:
        raise NotImplementedError("Unsupported platform")

    result = subprocess.run(cmd)
    if result:
        if result.returncode != 0:
            sys.exit(result.returncode)


def run():
    if len(sys.argv) < 2:
        print("Usage: wgit <git command>")
        sys.exit(1)
    cmd = sys.argv[1]
    pre_command = get_precommand(cmd)
    extension = get_extensions(cmd)

    if extension:
        extension()
        exit(0)

    if pre_command:
        pre_command()

    run_git(sys.argv[1:])
