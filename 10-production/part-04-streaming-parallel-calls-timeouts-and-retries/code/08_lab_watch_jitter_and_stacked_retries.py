"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Follow-along lab: Watch jitter and stacked retries
Run: python 08_lab_watch_jitter_and_stacked_retries.py
"""
import random
random.seed(7)
BASE, CAP = 0.5, 3.0
for i in range(4):
    top = min(CAP, BASE * 2 ** i)
    d = random.uniform(0, top)
    t = f"max {top:.1f}"
    print(f"try {i}: {t}, wait {d:.2f}")
# 3 layers, each 1 try + 3 retries
calls = (1 + 3) ** 3
print(f"3 layers x 3 retries: {calls} calls")
