"""Zero to AI Engineer · Python · Interview Quiz
Slide: A decorator that takes arguments
Run: python 07_a_decorator_that_takes_arguments.py
"""
def repeat(times=2):
    def deco(fn):
        def wrapper(*args):
            for _ in range(times):
                fn(*args)
        return wrapper
    return deco
@repeat
def hello():
    print("hello")
print(hello.__name__)
