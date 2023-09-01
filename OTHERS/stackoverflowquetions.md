## Git is not working in the subdirectory
---
i have files in `/TIL/2. Big data`. TIL is the root directory that is tracked by git so that git stages all the things below the `TIL` including `2. Big data`

All the files in `2. Big data` were generated in 'conda env'. When i modify them and try `git add .`, the following messaage comes out
```
$ git commit -m 'asdf'
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean 
```

Moreover, When attempted git commit and push, the changes only in the `2. Big data` does not appear in my remote repository

After a lot of trial I found that it happens because conda env is too big to be committed, but still don't know how to solve the problem.

How do I add, commit, or push all the files generated in the conda env without moving or duplicating them?<br>
i want to push only the files i've made not the whole conda env