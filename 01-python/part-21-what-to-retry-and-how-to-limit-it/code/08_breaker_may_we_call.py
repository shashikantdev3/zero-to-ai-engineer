"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Breaker: may we call?
Run: python 08_breaker_may_we_call.py
"""
# --- repeated from 07_circuit_breaker_its_state.py so this file runs on its own ---
import time
from collections import deque
class Breaker:
    def __init__(self, window=20,
                 limit=0.5, cooldown=30.0):
        self.results = deque(maxlen=window)
        self.limit = limit
        self.cooldown = cooldown
        self.opened_at = None
        self.half_open = False

# --- this slide ---
def allow(b: Breaker) -> bool:
    if b.opened_at is None:
        return True   # closed
    if b.half_open:
        # one probe already in flight
        return False
    waited = time.monotonic() - b.opened_at
    if waited >= b.cooldown:
        b.half_open = True  # single probe
        return True
    return False      # open: fail fast
