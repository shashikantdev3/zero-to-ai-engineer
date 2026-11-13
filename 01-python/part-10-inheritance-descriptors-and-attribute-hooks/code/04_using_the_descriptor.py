"""Zero to AI Engineer · Python · Part 10 of 25
Slide: Using the descriptor
Run: python 04_using_the_descriptor.py
"""
# --- repeated from 03_a_validating_descriptor.py so this file runs on its own ---
class Positive:
    def __set_name__(self, owner, name):
        self.private = f"_{name}"
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)
    # __set__ makes it a data descriptor
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("not positive")
        setattr(obj, self.private, value)

# --- this slide ---
class Config:
    top_k = Positive()
    def __init__(self, top_k: int):
        # goes through __set__
        self.top_k = top_k

c = Config(5)
# Config(0) -> ValueError
