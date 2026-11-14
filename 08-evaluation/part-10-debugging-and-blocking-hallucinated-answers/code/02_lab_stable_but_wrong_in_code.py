"""Zero to AI Engineer · Evaluation · Part 10 of 11
Follow-along lab: Stable but wrong, in code
Run: python 02_lab_stable_but_wrong_in_code.py
"""
import math
def softmax(scores, temp):
    ex = [math.exp(s / temp) for s in scores]
    return [e / sum(ex) for e in ex]
answers = ["wrong", "right", "unsure"]
scores = [2.0, 1.5, 0.5]
for t in (1.0, 0.2):
    p = softmax(scores, t)
    print(f"temp {t}: wrong p={p[0]:.2f}")
# temp 0 is greedy: always take the max
best = scores.index(max(scores))
runs = [answers[best] for _ in range(5)]
print("stable:", len(set(runs)) == 1)
print("accurate:", runs[0] == "right")
