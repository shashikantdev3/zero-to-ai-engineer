"""Zero to AI Engineer · Python · Part 10 of 25
Slide: A cooperative diamond
Run: python 01_a_cooperative_diamond.py
"""
class A:
    def __init__(self, **kw):
        print("A"); super().__init__(**kw)
class B(A):
    def __init__(self, b=None, **kw):
        print("B"); super().__init__(**kw)
class C(A):
    def __init__(self, c=None, **kw):
        print("C"); super().__init__(**kw)
class D(B, C): pass

D(b=1, c=2)  # B C A: A runs once
