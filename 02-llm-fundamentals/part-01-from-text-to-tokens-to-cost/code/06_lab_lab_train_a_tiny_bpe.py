"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Follow-along lab: Lab: Train a Tiny BPE
Run: python 06_lab_lab_train_a_tiny_bpe.py
"""
from collections import Counter
ws = ["l o w", "l o w e r",
      "l o w e s t", "s l o w"]
for _ in range(3):
    pairs = Counter()
    for w in ws:
        s = w.split()
        pairs.update(zip(s, s[1:]))
    (a, b), n = pairs.most_common(1)[0]
    print(f"merge {a}+{b} seen {n} times")
    old, new = f" {a} {b} ", f" {a}{b} "
    ws = [f" {w} ".replace(old, new).strip()
          for w in ws]
print(" | ".join(ws))
