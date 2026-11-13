"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: Three averages from one metric
Run: python 03_three_averages_from_one_metric.py
"""
# Needs: pip install scikit-learn
from sklearn.metrics import f1_score
yt = [0, 0, 0, 0, 0, 0, 1, 1, 2, 2]
yp = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
macro = f1_score(yt, yp, average="macro",
                 zero_division=0)
micro = f1_score(yt, yp, average="micro")
w = f1_score(yt, yp, average="weighted",
             zero_division=0)
print(macro, micro, w)
