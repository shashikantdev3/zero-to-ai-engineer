"""Zero to AI Engineer · Python · Part 20 of 25
Follow-along lab: Lab: plain backoff versus jitter
Run: python 06_lab_lab_plain_backoff_versus_jitter.py
"""
import random
random.seed(7)
base, cap = 0.5, 20.0
def top(i):
    return min(cap, base * 2 ** i)
print("attempt 0 waits", top(0))
print("attempt 3 waits", top(3))
print("attempt 9 waits", top(9))
same = [top(2)] * 4
print("no jitter:", same)
mixed = [round(random.uniform(0, top(2)), 1)
         for _ in range(4)]
print("full jitter:", mixed)
