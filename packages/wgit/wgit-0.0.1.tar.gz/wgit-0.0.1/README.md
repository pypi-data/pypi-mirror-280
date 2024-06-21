# Git-wrapper
A git wrapper to execute pre-commands and extensions without using git-hooks

## Available extensions

- **subtrees**: list the subtrees currently present in the repository. Any previously created subtree that is no longer present in the repository won't be listed.

```bash
> wgit subtrees
Here the list of the available subtrees:
- A
- B
```
## Available pre-commands
Each *precommand* is executed before the actual git command. Any other git command that does not have a pre-command will be executed as usual.

- **commit**: store a list of subtree involved in the commit. The list is stored in a file having as name the branch name. Multiple commits will extend the list, if needed.
```bash
> wgit commit -m "chore: added v"
Checking for changes in subtrees...
Found changes in subtrees. Let's store them for a later push.
Stored them in /home/deg/.local/share/wgit/banana_to_push.txt.
[banana d0e49f5] chore: added v
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 B/v
```

- **push**: push the changes to the subtree retrieved from the file generated in the `pre-commit` function.
```bash 
wgit push
Start pushing changes to subtrees...
Changes pushed to subtree 'B'.
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 329 bytes | 329.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Analyzing objects... (3/3) (80 ms)
remote: Validating commits... (1/1) done (0 ms)
remote: Storing packfile... done (40 ms)
remote: Storing index... done (26 ms)
To ...
   810f375..d0e49f5  banana -> banana
```

- **pull**: pull the changes from all the available subtrees.
```bash
> wgit pull
Changes pulled from subtree 'A'.
Changes pulled from subtree 'B'.
Already up to date.
```