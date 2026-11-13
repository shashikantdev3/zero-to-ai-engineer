"""Zero to AI Engineer · Python · Part 21 of 25
Slide: Circuit breaker: its state
Run: python 07_circuit_breaker_its_state.py
"""
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
