"""Zero to AI Engineer · Python · Part 3 of 25
Slide: Beat four in code: the fix
Run: python 02_beat_four_in_code_the_fix.py
"""
def add_turn(turn, history=None):
    # beat 4: the fix
    if history is None:
        # new list per call
        history = []
    history.append(turn)
    return history
