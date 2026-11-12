"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Two-Pass Stable Sort
Run: python 08_two_pass_stable_sort.py
"""
from operator import itemgetter

rows = [{"id": "b", "score": 0.8},
        {"id": "a", "score": 0.8},
        {"id": "c", "score": 0.9}]
# pass 1: secondary key
out = sorted(rows, key=itemgetter("id"))
# pass 2: primary key
out.sort(key=itemgetter("score"),
         reverse=True)
# ['c', 'a', 'b']
print([r["id"] for r in out])
