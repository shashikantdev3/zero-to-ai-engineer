"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: A simple breaker, part two
Run: python 02_a_simple_breaker_part_two.py
"""
# --- repeated from 01_a_simple_breaker_part_one.py so this file runs on its own ---
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

# --- this slide ---
def record(self, ok: bool):
    if ok:
        self.fails, self.opened = 0, None
    else:
        self.fails += 1
        if self.fails >= self.th:
            self.opened = time.monotonic()

Breaker.record = record
