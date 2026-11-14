"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: A Wilson interval in code
Run: python 04_a_wilson_interval_in_code.py
"""
import math

def wilson(passes, n, z=1.96):
    # report ONE version's score
    p = passes / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * math.sqrt(
        p * (1 - p) / n + z**2 / (4 * n**2)
    ) / denom
    return centre - half, centre + half
print(wilson(45, 50))
