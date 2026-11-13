"""Zero to AI Engineer · Python · Part 22 of 25
Slide: The token bucket's state
Run: python 06_the_token_buckets_state.py
"""
import threading, time

class TokenBucket:
    def __init__(self, rate, capacity):
        if rate <= 0 or capacity <= 0:
            raise ValueError("must be > 0")
        self.rate = rate  # tokens per sec
        self.capacity = capacity  # max burst
        self.tokens = capacity
        self.updated = time.monotonic()
        # short sections, never across await
        self.lock = threading.Lock()
