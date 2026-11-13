"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Retry budget: the window
Run: python 05_retry_budget_the_window.py
"""
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
