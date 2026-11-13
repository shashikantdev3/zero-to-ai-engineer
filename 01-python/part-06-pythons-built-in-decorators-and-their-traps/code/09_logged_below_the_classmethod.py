"""Zero to AI Engineer · Python · Part 6 of 25
Slide: Logged Below the Classmethod
Run: python 09_logged_below_the_classmethod.py
"""
import functools
def logged(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("calling", fn.__qualname__)
        return fn(*args, **kwargs)
    return wrapper
class Client:
    # classmethod outermost, logged inside
    @classmethod
    @logged
    def from_env(cls, env): return cls()
