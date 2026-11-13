"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Follow-along lab: Precision, Recall, F1 by Hand
Run: python 03_lab_precision_recall_f1_by_hand.py
"""
y = [1, 1, 1, 0, 1, 0, 0, 0]
s = [.9, .8, .7, .6, .5, .4, .3, .2]
for thr in (0.85, 0.65, 0.45, 0.0):
    p = [int(x >= thr) for x in s]
    pairs = list(zip(y, p))
    tp = sum(a and b for a, b in pairs)
    fp = sum(b and not a for a, b in pairs)
    fn = sum(a and not b for a, b in pairs)
    pr = tp / (tp + fp)
    rc = tp / (tp + fn)
    f1 = 2 * pr * rc / (pr + rc)
    print(f"thr {thr}: P {pr:.2f}",
          f"R {rc:.2f} F1 {f1:.2f}")
