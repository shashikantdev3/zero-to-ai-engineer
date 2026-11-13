"""Zero to AI Engineer · Python · Part 10 of 25
Follow-along lab: Watch the lookup order happen
Run: python 05_lab_watch_the_lookup_order_happen.py
"""
class Data:
    def __get__(self, o, t): return "data"
    def __set__(self, o, v): pass
class NonData:
    def __get__(self, o, t): return "nondata"
class K:
    d = Data()
    n = NonData()
    def m(self): pass
k = K()
k.__dict__.update(d="inst", n="inst")
print("d ->", k.d)
print("n ->", k.n)
print("m is m:", k.m is k.m)
