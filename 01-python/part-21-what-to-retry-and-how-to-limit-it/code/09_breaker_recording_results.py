"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Breaker: recording results
Run: python 09_breaker_recording_results.py
"""
# --- repeated from 05_retry_budget_the_window.py, 06_retry_budget_may_we_retry.py, 07_circuit_breaker_its_state.py, 08_breaker_may_we_call.py so this file runs on its own ---
import time
from collections import deque
RATIO, WINDOW, MIN_RETRIES = 0.1, 10.0, 3
requests, retries = deque(), deque()
def trim(now: float) -> None:
    for q in (requests, retries):
        while q and q[0] < now - WINDOW:
            q.popleft()
def record_request() -> None:
    now = time.monotonic()
    trim(now)
    requests.append(now)

def can_retry() -> bool:
    now = time.monotonic()
    trim(now)
    # small floor for low traffic
    allowance = max(MIN_RETRIES,
                    RATIO * len(requests))
    if len(retries) < allowance:
        retries.append(now)
        return True
    return False

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

# --- this slide ---
def record(b: Breaker, ok: bool) -> None:
    now, r = time.monotonic(), b.results
    if b.half_open:
        b.half_open = False
        b.opened_at = None if ok else now
        if ok:
            r.clear()
        return
    r.append(ok)
    bad = r.count(False) / len(r)
    if len(r) == r.maxlen and bad > b.limit:
        b.opened_at = now
