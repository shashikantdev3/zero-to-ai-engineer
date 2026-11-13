"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Follow-along lab: Watch oversampling leak into test
Run: python 05_lab_watch_oversampling_leak_into_test.py
"""
import random
rows = [(i, int(i < 30)) for i in range(1000)]
fr = [r for r in rows if r[1]]
# Wrong: copy frauds to 50/50, then split
bad = rows + fr * 31
random.Random(0).shuffle(bad)
test, train = bad[:400], bad[400:]
ids = {r[0] for r in train}
t_fr = [r[0] for r in test if r[1]]
print("test rate:", round(len(t_fr) / 400, 2))
seen = sum(i in ids for i in t_fr)
print(seen, "of", len(t_fr), "seen in train")
fair = [r[1] for r in rows[::5]]
print("fair rate:", sum(fair) / len(fair))
