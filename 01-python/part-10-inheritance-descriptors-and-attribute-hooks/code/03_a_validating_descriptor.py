"""Zero to AI Engineer · Python · Part 10 of 25
Slide: A validating descriptor
Run: python 03_a_validating_descriptor.py
"""
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
