"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Deadline: use what is left
Run: python 10_deadline_use_what_is_left.py
"""
import time
def call_timeout(deadline: float,
                 normal: float) -> float:
    # pass deadline down; use what is left
    left = deadline - time.monotonic()
    return max(0.0, min(normal, left))
