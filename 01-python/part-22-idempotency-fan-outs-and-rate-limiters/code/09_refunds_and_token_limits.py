"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Refunds and token limits
Run: python 09_refunds_and_token_limits.py
"""
class TokenBucket:  # continued
    def refund(self, amount):
        with self.lock:
            self._refill()
            self.tokens += amount
            if self.tokens > self.capacity:
                self.tokens = self.capacity

# bucket = TokenBucket(rate=1.0, capacity=5)
# 60 per minute, burst of 5
# TPM: acquire(prompt_tokens + max_tokens)
# then refund(max_tokens - completion_tokens)
