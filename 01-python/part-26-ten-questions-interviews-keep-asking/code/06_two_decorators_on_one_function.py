"""Zero to AI Engineer · Python · Interview Quiz
Slide: Two decorators on one function
Run: python 06_two_decorators_on_one_function.py
"""
def tag(name):
    def deco(fn):
        def wrapper():
            print(name, "before")
            fn()
            print(name, "after")
        return wrapper
    return deco
@tag("A")
@tag("B")
def run(): print("run")
run()
