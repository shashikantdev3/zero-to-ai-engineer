"""Zero to AI Engineer · Evaluation · Part 11 of 11
Slide: Normalise, Then Sample
Run: python 01_normalise_then_sample.py
"""
import random
from collections import Counter

def normalise(ans: str) -> str:
    text = " ".join(ans.lower().split())
    return text.rstrip(".")

def ask(q, temperature=0.7):
    # stand-in for a sampled model call
    picks = ["Paris.", "paris", "Lyon"]
    return random.choice(picks)
