"""Zero to AI Engineer · Python · Part 25 of 25
Slide: Counting references in code
Run: python 01_counting_references_in_code.py
"""
import gc, sys
x = []
# typically 2: x plus the argument
print(sys.getrefcount(x))
class Node:
    def __init__(self): self.other = None
a, b = Node(), Node()
# a cycle: counts never reach zero
a.other, b.other = b, a
del a, b
print(gc.collect())
print(gc.get_threshold())
