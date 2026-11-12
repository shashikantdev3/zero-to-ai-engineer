"""Zero to AI Engineer · Python · Part 2 of 25
Slide: The None Trap
Run: python 09_the_none_trap.py
"""
from operator import itemgetter

rows = [{"id": "b"}, {"id": "a"}]
# sort works in place, returns None
x = rows.sort(key=itemgetter("id"))
print(x)
print(rows)
