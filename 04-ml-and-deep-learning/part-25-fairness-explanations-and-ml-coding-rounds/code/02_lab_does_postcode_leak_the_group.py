"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 25 of 28
Follow-along lab: Does postcode leak the group?
Run: python 02_lab_does_postcode_leak_the_group.py
"""
from collections import Counter, defaultdict
rows = [("N1", "x"), ("N1", "x"), ("N1", "y"),
        ("S2", "y"), ("S2", "y"), ("S2", "y"),
        ("E3", "x"), ("E3", "x"), ("E3", "x")]
seen = defaultdict(Counter)
for c, g in rows: seen[c][g] += 1
top = {c: n.most_common(1)[0][0]
       for c, n in seen.items()}
hits = sum(top[c] == g for c, g in rows)
groups = Counter(g for _, g in rows)
base = round(max(groups.values()) / 9, 2)
print("majority guess:", base)
print("postcode guess:", round(hits / 9, 2))
print("proxy present:", hits / 9 > base)
