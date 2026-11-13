"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 25 of 28
Slide: Error rates per group
Run: python 01_error_rates_per_group.py
"""
# Needs: pip install pandas scikit-learn
import pandas as pd
from sklearn.metrics import confusion_matrix
df = pd.DataFrame({
    "group": ["a", "a", "a", "b", "b", "b"],
    "y": [1, 0, 1, 1, 0, 0],
    "pred": [1, 0, 0, 1, 1, 0]})
for g, d in df.groupby("group"):
    tn, fp, fn, tp = confusion_matrix(
        d.y, d.pred, labels=[0, 1]).ravel()
    print(g, "TPR", tp / max(tp + fn, 1),
          "FPR", fp / max(fp + tn, 1),
          "PPV", tp / max(tp + fp, 1))
