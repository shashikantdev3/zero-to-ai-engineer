"""Zero to AI Engineer · Python · Part 9 of 25
Slide: A diamond you can print
Run: python 01_a_diamond_you_can_print.py
"""
class A:
    def hi(self): return ["A"]
class B(A):
    def hi(self): return ["B"] + super().hi()
class C(A):
    def hi(self): return ["C"] + super().hi()
class D(B, C):
    def hi(self): return ["D"] + super().hi()

print([k.__name__ for k in D.__mro__])
print(D().hi())
