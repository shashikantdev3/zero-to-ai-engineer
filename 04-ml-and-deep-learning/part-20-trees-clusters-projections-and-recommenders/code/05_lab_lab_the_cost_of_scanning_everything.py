"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 20 of 28
Follow-along lab: Lab: the cost of scanning everything
Run: python 05_lab_lab_the_cost_of_scanning_everything.py
"""
import random
random.seed(0)
n_items, ms = 10_000_000, 1
hours = n_items * ms / 1000 / 3600
print(f"score all: {hours:.1f} hours")
print(f"rank 500: {500 * ms} ms")
user = [0.9, 0.1]
items = [[random.random(), random.random()]
         for _ in range(1000)]
def score(v):
    return sum(x * y for x, y in zip(user, v))
top = sorted(items, key=score, reverse=True)
print(f"kept {len(top[:5])} of {len(items)}")
print(f"best score: {score(top[0]):.2f}")
