"""Zero to AI Engineer · Python · Part 25 of 25
Follow-along lab: Watch objects disappear
Run: python 03_lab_watch_objects_disappear.py
"""
import gc, weakref
class Node: pass
a = Node()
r = weakref.ref(a)
print("alive:", r() is a)
del a
print("after del:", r())
b, c = Node(), Node()
b.o, c.o = c, b
w = weakref.ref(b)
del b, c
print("in cycle:", w() is not None)
gc.collect()
print("after collect:", w())
