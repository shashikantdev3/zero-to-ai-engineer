"""Zero to AI Engineer · Evaluation · Part 8 of 11
Slide: Kappa and failure catch rate
Run: python 05_kappa_and_failure_catch_rate.py
"""
# Needs: pip install scikit-learn
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
e1 = [1, 1, 0, 1, 0, 1, 1, 0]  # 1 = pass
e2 = [1, 1, 0, 1, 1, 1, 1, 0]
judge = [1, 1, 1, 1, 0, 1, 1, 0]
ceiling = cohen_kappa_score(e1, e2)
print("human ceiling:", ceiling)
print("judge vs human:",
      cohen_kappa_score(e1, judge))
tn, fp, fn, tp = confusion_matrix(
    e1, judge, labels=[0, 1]).ravel()
print("catches failures:", tn / (tn + fp))
