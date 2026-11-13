"""Zero to AI Engineer · Python · Part 20 of 25
Slide: Full jitter in one line
Run: python 05_full_jitter_in_one_line.py
"""
import random
def full_jitter(attempt: int, base=0.5,
                cap=20.0) -> float:
    top = min(cap, base * 2 ** attempt)
    return random.uniform(0, top)
print([round(full_jitter(i), 2)
       for i in range(5)])
