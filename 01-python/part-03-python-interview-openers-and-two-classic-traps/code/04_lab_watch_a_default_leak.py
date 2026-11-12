"""Zero to AI Engineer · Python · Part 3 of 25
Follow-along lab: Watch a default leak
Run: python 04_lab_watch_a_default_leak.py
"""
def bad(msg, history=[]):
    history.append(msg)
    return history

def good(msg, history=None):
    if history is None:
        history = []
    history.append(msg)
    return history
print("bad a:", bad("a"))
print("bad b:", bad("b"))
print("defaults:", bad.__defaults__)
print("good a:", good("a"))
print("good b:", good("b"))
