"""Zero to AI Engineer · Python · Part 4 of 25
Slide: is Versus == in Code
Run: python 01_is_versus_in_code.py
"""
a = int("1000")
b = int("1000")
print(a == b, a is b)
# True False on CPython
x = None
if x is None:
    print("x is None")
