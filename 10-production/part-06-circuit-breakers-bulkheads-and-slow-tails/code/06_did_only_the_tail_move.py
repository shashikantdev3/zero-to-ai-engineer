"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: Did only the tail move?
Run: python 06_did_only_the_tail_move.py
"""
from statistics import quantiles

# durations in ms, grouped in 10-minute bins
bins = {
    "09:00": [50] * 100,
    "09:10": [50] * 96 + [2000] * 4,
}

for t, ms in bins.items():
    q = quantiles(ms, n=100)
    print(t, "p50", q[49], "p99", q[98])
