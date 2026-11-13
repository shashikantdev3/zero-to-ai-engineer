"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Acquire, and why it is unfair
Run: python 08_acquire_and_why_it_is_unfair.py
"""
class TokenBucket:  # continued
    async def acquire(self, cost=1.0):
        self._check(cost)
        while True:
            with self.lock:
                self._refill()
                if self.tokens >= cost:
                    self.tokens -= cost
                    return
                need = cost - self.tokens
                wait = need / self.rate
            await asyncio.sleep(wait)
