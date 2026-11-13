"""Zero to AI Engineer · LLM Fundamentals · Part 7 of 18
Follow-along lab: A causal mask in plain Python
Run: python 02_lab_a_causal_mask_in_plain_python.py
"""
import math
n = 4
for i in range(n):
    row = [int(j > i) for j in range(n)]
    print(row)
scores = [2.0, 1.0, 0.5, 3.0]
# second token: sees indexes 0 and 1
masked = [s if j <= 1 else -math.inf
          for j, s in enumerate(scores)]
exps = [math.exp(s) for s in masked]
total = sum(exps)
print([round(e / total, 2) for e in exps])
