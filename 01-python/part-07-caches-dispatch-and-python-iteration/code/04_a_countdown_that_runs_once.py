"""Zero to AI Engineer · Python · Part 7 of 25
Slide: A countdown that runs once
Run: python 04_a_countdown_that_runs_once.py
"""
class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

it = Countdown(3)
print(list(it), list(it))
# [3, 2, 1] []
