"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Follow-along lab: Count the winning pairs by hand
Run: python 03_lab_count_the_winning_pairs_by_hand.py
"""
pos = [0.9, 0.8, 0.35]
neg = [0.4, 0.2, 0.1, 0.35]

def auc(pos, neg):
    s = sum((a > b) + 0.5 * (a == b)
            for a in pos for b in neg)
    return s / (len(pos) * len(neg))

print("pairs:", len(pos) * len(neg))
print("AUC:", round(auc(pos, neg), 3))
print("more negs:", round(auc(pos, neg * 3), 3))
fpos = [-x for x in pos]
fneg = [-x for x in neg]
print("flipped:", round(auc(fpos, fneg), 3))
