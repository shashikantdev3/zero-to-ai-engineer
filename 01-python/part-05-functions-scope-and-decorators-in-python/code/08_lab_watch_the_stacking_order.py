"""Zero to AI Engineer · Python · Part 5 of 25
Follow-along lab: Watch the stacking order
Run: python 08_lab_watch_the_stacking_order.py
"""
import functools
def tag(name):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print("enter", name)
            return fn(*args, **kwargs)
        return wrapper
    return deco

@tag("outer")
@tag("inner")
def greet(who): return f"hi {who}"
print(greet("dev"), greet.__name__)
