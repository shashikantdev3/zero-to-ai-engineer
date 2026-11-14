"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: A simple breaker, part one
Run: python 01_a_simple_breaker_part_one.py
"""
import time

class Breaker:
    def __init__(self, th=5, cd=30):
        self.th, self.cd = th, cd
        self.fails, self.opened = 0, None
    def allow(self):
        if self.opened is None:
            return True
        # half-open: let a probe through
        t = time.monotonic() - self.opened
        return t >= self.cd
