"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Refill and the capacity check
Run: python 07_refill_and_the_capacity_check.py
"""
class TokenBucket:  # continued
    def _refill(self):
        now = time.monotonic()
        dt = now - self.updated
        full = self.tokens + dt * self.rate
        self.tokens = min(self.capacity, full)
        self.updated = now

    def _check(self, cost):
        if cost > self.capacity:
            raise ValueError("never fits")
