from talon.voice import Context, Key

context = Context("git")

context.keymap(
    {
        "run get": "git ",
        "get (R M | remove)": "git rm ",
        "[run] get add": "git add ",
        "git add dot": "git add .",
        "get bisect": "git bisect ",
        "get branch": "git branch ",
        "get branch all": "git branch -a ",
        "run get branch": "git branch\n",
        "get checkout": "git checkout ",
        "get checkout master": "git checkout master",
        "run get checkout master": "git checkout master\n",
        "[run] get checkout new": "git checkout -b ",
        "[run] get clone": "git clone ",
        "get commit": "git commit ",
        "run get commit": "git commit\n",
        "git commit message": ['git commit -m ""', Key("left")],
        "get diff": "git diff ",
        "run get diff": "git diff\n",
        "run get diff master": "git diff master\n",
        "get fetch": "git fetch",
        "run get fetch": "git fetch\n",
        "get grep": "git grep ",
        "get in it": "git init",
        "run get in it": "git init\n",
        "get log": "git log ",
        "run get log": "git log\n",
        "get brief log": "git log --oneline --max-count=5 ",
        "get next release": "git log --oneline --no-decorate --grep 'Merge pull' ",
        "get (author | co-author)": "git log --format='%an <%ae>' -n1 --author=",
        "[run] get merge": "git merge ",
        "get move": "git mv ",
        "get pull": "git pull ",
        "run get pull": "git pull\n",
        "get push": "git push ",
        "run get push": "git push\n",
        "get push up stream": "git push -u origin HEAD",
        "run get push up stream": "git push -u origin HEAD\n",
        "[run] get push origin": "git push origin ",
        "[run] get push master": "git push origin master",
        "get rebase": "git rebase ",
        "get rebase master": "git rebase master -i",
        "run get rebase master": "git rebase master -i\n",
        "get reset": "git reset ",
        "get reset (had | head)": "git reset HEAD^",
        "get show": "git show ",
        "get status": "git status",
        "run get status": "git status\n",
        "run get status short": "git status -s\n",
        "get stash": "git stash ",
        "run get stash": "git stash\n",
        "get stash pop": "git stash pop",
        "run get stash pop": "git stash pop\n",
        "get tag": "git tag ",
        "get tag list": "git tag --list",
        "get describe": "git describe",
        "run get describe": "git describe\n",
        "run get rev parse (had | head)": "git rev-parse HEAD",
        "run get last commit": "git rev-parse HEAD\n",
        "copy last commit": ["git rev-parse HEAD | pbcopy", Key("enter")],
        "get [remote] add origin": "git remote add origin ",
        "get remote": "git remote ",
    }
)
