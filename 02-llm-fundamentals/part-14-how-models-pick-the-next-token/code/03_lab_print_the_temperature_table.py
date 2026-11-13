"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Follow-along lab: Print the Temperature Table
Run: python 03_lab_print_the_temperature_table.py
"""
import math
def soft_t(logits, t):
    if t == 0:
        top = logits.index(max(logits))
        return [1.0 if i == top else 0.0
                for i in range(len(logits))]
    z = [x / t for x in logits]
    m = max(z)
    e = [math.exp(x - m) for x in z]
    return [round(x / sum(e), 3) for x in e]

for t in (0, 0.5, 1.0, 2.0):
    print(t, soft_t([2.0, 1.0, 0.1], t))
