"""Zero to AI Engineer · Evaluation · Part 11 of 11
Slide: Majority Vote and Agreement Score
Run: python 02_majority_vote_and_agreement_score.py
"""
# --- repeated from 01_normalise_then_sample.py so this file runs on its own ---
import random
from collections import Counter

def normalise(ans: str) -> str:
    text = " ".join(ans.lower().split())
    return text.rstrip(".")

def ask(q, temperature=0.7):
    # stand-in for a sampled model call
    picks = ["Paris.", "paris", "Lyon"]
    return random.choice(picks)

# --- this slide ---
def self_consistent(ask, q, n=5):
    # exact match: short answers only
    answers = []
    for _ in range(n):
        raw = ask(q, temperature=0.7)
        answers.append(normalise(raw))
    counts = Counter(answers)
    top, count = counts.most_common(1)[0]
    # low agreement: abstain or review
    return top, count / n
q = "Capital of France?"
print(self_consistent(ask, q))
