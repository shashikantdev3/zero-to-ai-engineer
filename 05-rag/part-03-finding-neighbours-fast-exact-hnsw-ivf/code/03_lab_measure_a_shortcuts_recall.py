"""Zero to AI Engineer · RAG and Vector Search · Part 3 of 26
Follow-along lab: Measure a shortcut's recall
Run: python 03_lab_measure_a_shortcuts_recall.py
"""
import random
random.seed(7)
r = random.random
pts = [complex(r(), r()) for _ in range(5000)]
q = complex(0.5, 0.5)
dist = lambda i: abs(pts[i] - q)
exact = sorted(range(5000), key=dist)[:10]
near = [i for i, p in enumerate(pts)
        if abs(p.real - 0.5) < 0.02]
ann = sorted(near, key=dist)[:10]
hits = len(set(ann) & set(exact))
print("vectors stored:", len(pts))
print("vectors visited:", len(near))
print("recall@10:", hits / 10)
