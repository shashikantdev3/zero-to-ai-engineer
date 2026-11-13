"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Follow-along lab: Prove every row is validated
Run: python 06_lab_prove_every_row_is_validated.py
"""
import random
def kfold(n, k, seed=0):
    idx = list(range(n))
    random.Random(seed).shuffle(idx)
    for i in range(k):
        va = idx[i::k]
        tr = [j for j in idx if j not in va]
        yield tr, va
folds = list(kfold(11, 3))
for tr, va in folds:
    print(len(tr), len(va), set(tr) & set(va))
vals = [j for _, va in folds for j in va]
print(sorted(vals) == list(range(11)))
print('n // k slicing keeps', 11 // 3 * 3)
