"""Zero to AI Engineer · Python · Interview Quiz
Slide: A logging decorator from scratch
Run: python 05_a_logging_decorator_from_scratch.py
"""
def logged(fn):
    def wrapper(*args, **kwargs):
        print("calling", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper
@logged
def add(a, b):
    """Add two numbers."""
    return a + b
print(add(2, 3))
print(add.__name__, add.__doc__)
