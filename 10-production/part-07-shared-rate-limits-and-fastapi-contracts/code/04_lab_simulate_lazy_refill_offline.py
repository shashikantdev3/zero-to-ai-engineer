"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Follow-along lab: Simulate lazy refill offline
Run: python 04_lab_simulate_lazy_refill_offline.py
"""
cap, rate = 10, 2
tokens, ts = cap, 0
def take(now, cost):
    global tokens, ts
    gained = (now - ts) * rate
    tokens = min(cap, tokens + gained)
    ts = now
    ok = tokens >= cost
    if ok: tokens -= cost
    return ok
reqs = [(0, 8), (0, 5), (2, 5), (3, 9)]
for now, cost in reqs:
    ok = take(now, cost)
    print(f"t={now} ok={ok} left={tokens}")
