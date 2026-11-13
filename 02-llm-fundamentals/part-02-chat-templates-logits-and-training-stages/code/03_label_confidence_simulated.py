"""Zero to AI Engineer · LLM Fundamentals · Part 2 of 18
Slide: Label Confidence, Simulated
Run: python 03_label_confidence_simulated.py
"""
import math
# made-up logits for two labels
logits = {"refund": 4.1, "complaint": 3.8}
m = max(logits.values())
ex = {t: math.exp(v - m)
      for t, v in logits.items()}
total = sum(ex.values())
probs = {t: e / total for t, e in ex.items()}
for t, p in probs.items():
    print(t, round(math.log(p), 3))
a, b = probs.values()
print("gap", round(abs(a - b), 3))
