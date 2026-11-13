"""Zero to AI Engineer · Python · Part 22 of 25
Follow-along lab: A token bucket with a fake clock
Run: python 10_lab_a_token_bucket_with_a_fake_clock.py
"""
class Bucket:
    def __init__(self, rate, cap):
        self.rate, self.cap = rate, cap
        self.tok, self.t = cap, 0.0
    def take(self, now, cost=1):
        add = (now - self.t) * self.rate
        self.tok = min(self.cap, self.tok+add)
        self.t = now
        ok = self.tok >= cost
        if ok: self.tok -= cost
        return ok
b = Bucket(rate=1.0, cap=3)
for now in (0, 0, 0, 0, 1, 1):
    print(f"t={now} served={b.take(now)}")
