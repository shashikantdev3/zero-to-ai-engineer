"""Zero to AI Engineer · Python · Part 10 of 25
Slide: When C3 cannot find an order
Run: python 02_when_c3_cannot_find_an_order.py
"""
class X: pass
class Y: pass
class P(X, Y): pass
class Q(Y, X): pass
# class R(P, Q): pass
# TypeError: Cannot create a consistent
# method resolution order (MRO)
