"""Zero to AI Engineer · Python · Part 12 of 25
Follow-along lab: Watch cause and context get set
Run: python 03_lab_watch_cause_and_context_get_set.py
"""
def boom(use_from):
    try:
        {}["k"]
    except KeyError as e:
        if use_from:
            raise ValueError("x") from e
        raise ValueError("x")

for flag in (True, False):
    try:
        boom(flag)
    except ValueError as err:
        print("cause:", repr(err.__cause__))
        print("ctx:", repr(err.__context__))
