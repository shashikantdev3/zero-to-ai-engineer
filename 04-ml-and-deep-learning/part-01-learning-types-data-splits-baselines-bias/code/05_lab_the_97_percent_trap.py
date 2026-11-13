"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 1 of 28
Follow-along lab: The 97 percent trap
Run: python 05_lab_the_97_percent_trap.py
"""
# 3 fraud cases in 100 transactions
labels = [1] * 3 + [0] * 97
# baseline: always predict legit
preds = [0] * len(labels)
pairs = list(zip(preds, labels))
right = sum(p == t for p, t in pairs)
caught = sum(p == 1 and t == 1
             for p, t in pairs)
total = sum(labels)
print("rows:", len(labels))
print("accuracy:", right / len(labels))
print("caught:", caught, "of", total)
print("recall:", caught / total)
