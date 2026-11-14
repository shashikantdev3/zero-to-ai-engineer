"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Slide: A Token Bucket Class
Run: python 05_a_token_bucket_class.py
"""
from time import monotonic
class TokenBucket:
    def __init__(self, rate, cap):
        self.rate, self.cap = rate, cap
        self.tok, self.t = cap, monotonic()
    def try_take(self, n=1.0):
        old, self.t = self.t, monotonic()
        add = (self.t - old) * self.rate
        self.tok = min(self.cap, self.tok+add)
        if self.tok < n: return False
        self.tok -= n
        return True
