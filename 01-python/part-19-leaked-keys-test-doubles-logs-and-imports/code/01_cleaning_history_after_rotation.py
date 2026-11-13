"""Zero to AI Engineer · Python · Part 19 of 25
Slide: Cleaning history after rotation
Run: python 01_cleaning_history_after_rotation.py
"""
# Only after the key is revoked and rotated.
# Fresh mirror clone: filter-repo needs one.
clone = "git clone --mirror URL repo.git"

# case 1: the secret is a whole file
whole = ("git filter-repo --path .env"
         " --invert-paths")

# case 2: the key sits in a file you keep
rule = "sk-OLD-KEY-VALUE==>REMOVED"
text = ("git filter-repo --replace-text"
        " ../expressions.txt")
