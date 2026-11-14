"""Zero to AI Engineer · Production and LLMOps · Part 5 of 38
Follow-along lab: Watch a Bucket Cap a Burst
Run: python 06_lab_watch_a_bucket_cap_a_burst.py
"""
rate, cap = 1.0, 3.0
tok, last = cap, 0.0
def take(now):
    global tok, last
    tok = min(cap, tok + (now - last) * rate)
    last = now
    if tok < 1: return False
    tok -= 1
    return True
burst = sum(take(0) for _ in range(5))
print("burst of 5 at t=0:", burst)
print("t=1, two tries:", take(1), take(1))
idle = sum(take(100) for _ in range(5))
print("after long idle:", idle)
