"""Zero to AI Engineer · Python · Part 25 of 25
Slide: A cache that forgets
Run: python 02_a_cache_that_forgets.py
"""
import weakref

class Big:
    pass

cache = weakref.WeakValueDictionary()
obj = Big()
cache["k"] = obj
print("k" in cache)
del obj
# False in CPython: last strong ref gone
print("k" in cache)
