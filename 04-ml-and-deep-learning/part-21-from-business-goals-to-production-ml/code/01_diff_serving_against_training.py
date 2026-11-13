"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 21 of 28
Slide: Diff serving against training
Run: python 01_diff_serving_against_training.py
"""
# Serving log: raw request + value used
rows = [{"raw": {"age": None}, "age": 0.0},
        {"raw": {"age": 40}, "age": 40.0}]
# Training path fills missing age with 35
def train_age(raw):
    a = raw["age"]
    return 35.0 if a is None else float(a)
bad = 0
for r in rows:
    gap = r["age"] - train_age(r["raw"])
    bad += abs(gap) > 1e-6
print("share disagreeing:", bad / len(rows))
