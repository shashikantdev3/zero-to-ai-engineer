"""Zero to AI Engineer · Evaluation · Part 4 of 11
Slide: The gate decision in Python
Run: python 01_the_gate_decision_in_python.py
"""
MIN_HIT = 0.90
MIN_GROUND = 0.85

def gate(hit, ground, critical_broke, infra):
    # provider error, timeout, rate limit
    if infra:
        return 2
    if critical_broke:
        return 1
    if hit < MIN_HIT or ground < MIN_GROUND:
        return 1
    return 0
