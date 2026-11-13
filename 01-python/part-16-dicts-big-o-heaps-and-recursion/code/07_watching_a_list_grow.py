"""Zero to AI Engineer · Python · Part 16 of 25
Slide: Watching a list grow
Run: python 07_watching_a_list_grow.py
"""
import sys
a, last = [], sys.getsizeof([])
for i in range(20):
    a.append(i)
    size = sys.getsizeof(a)
    # print only when the array grew
    if size != last:
        print(len(a), size)
        last = size
