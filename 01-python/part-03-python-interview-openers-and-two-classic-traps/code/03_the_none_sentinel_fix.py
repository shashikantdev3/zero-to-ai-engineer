"""Zero to AI Engineer · Python · Part 3 of 25
Slide: The None sentinel fix
Run: python 03_the_none_sentinel_fix.py
"""
def add_msg(msg, history=None):
    if history is None:
        history = []
    history.append(msg)
    return history

assert add_msg("a") == ["a"]
# with history=[] this would be ["a", "b"]
assert add_msg("b") == ["b"]
