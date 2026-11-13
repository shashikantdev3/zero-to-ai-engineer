"""Zero to AI Engineer · Python · Part 9 of 25
Slide: Equality that steps aside
Run: python 06_equality_that_steps_aside.py
"""
class Ballot:
    def __init__(self, name, votes, ts):
        self.name, self.k = name, (-votes, ts)
    def __eq__(self, o):
        if not isinstance(o, Ballot):
            return NotImplemented
        return self.k == o.k
    def __hash__(self):
        # same fields as __eq__
        return hash(self.k)

print(Ballot("a", 1, 1) == "x")
