"""Zero to AI Engineer · LLM Fundamentals · Part 18 of 18
Follow-along lab: Perplexity by Hand
Run: python 03_lab_perplexity_by_hand.py
"""
import math
lp = [-0.2, -1.5, -0.7, -3.0]
nll = -sum(lp) / len(lp)
print(f"mean NLL: {nll:.2f}")
print(f"perplexity: {math.exp(nll):.2f}")
uni = [math.log(1 / 10)] * 4
u = -sum(uni) / len(uni)
print(f"uniform over 10: {math.exp(u):.2f}")
sure = [-0.01] * 4
s = -sum(sure) / len(sure)
print(f"confident model: {math.exp(s):.2f}")
