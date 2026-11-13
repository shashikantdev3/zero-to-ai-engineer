"""Zero to AI Engineer · Python · Part 12 of 25
Slide: finally overrides the return
Run: python 01_finally_overrides_the_return.py
"""
def f():
    try:
        raise ValueError("lost")
    finally:
        # exception discarded; 3.14 warns
        return "finally wins"

# prints: finally wins
print(f())
