"""Zero to AI Engineer · Python · Part 3 of 25
Slide: The bug and two fixes
Run: python 05_the_bug_and_two_fixes.py
"""
fns = [lambda: i for i in range(3)]
# prints [2, 2, 2]
print([f() for f in fns])

fns = [lambda i=i: i for i in range(3)]
# prints [0, 1, 2]
print([f() for f in fns])

from functools import partial
fns = [partial(lambda i: i, i)
       for i in range(3)]
print([f() for f in fns])
