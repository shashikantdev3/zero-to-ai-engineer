"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: Confusion Matrix in scikit-learn
Run: python 07_confusion_matrix_in_scikit_learn.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import confusion_matrix
y_val = np.array([0, 0, 0, 0, 1, 1])
proba = np.array([.1, .6, .2, .3, .9, .4])
y_pred = (proba >= 0.5).astype(int)
cm = confusion_matrix(y_val, y_pred)
tn, fp, fn, tp = cm.ravel()
fpr = fp / (fp + tn)
print(tn, fp, fn, tp, fpr)
