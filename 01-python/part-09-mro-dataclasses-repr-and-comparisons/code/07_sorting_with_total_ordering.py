"""Zero to AI Engineer · Python · Part 9 of 25
Slide: Sorting with total_ordering
Run: python 07_sorting_with_total_ordering.py
"""
from functools import total_ordering
@total_ordering
class Ballot:
    def __init__(self, name, votes, ts):
        # most votes first, then earliest
        self.name, self.k = name, (-votes, ts)
    def __eq__(self, o): return self.k == o.k
    def __lt__(self, o): return self.k < o.k

bs = [Ballot("a", 3, 2), Ballot("b", 5, 9),
      Ballot("c", 3, 1)]
print([b.name for b in sorted(bs)])
