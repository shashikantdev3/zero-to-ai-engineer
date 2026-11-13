"""Zero to AI Engineer · Python · Part 19 of 25
Slide: Re-add origin, then force push
Run: python 02_re_add_origin_then_force_push.py
"""
# filter-repo removed the origin remote.
readd = "git remote add origin URL"

# Push every branch, then every tag.
push = ["git push --force --all",
        "git push --force --tags"]

# Then everyone re-clones.
for cmd in [readd, *push]:
    print(cmd)
