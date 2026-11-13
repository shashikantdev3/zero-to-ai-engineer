"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: Split first, then resample
Run: python 03_split_first_then_resample.py
"""
# Needs: pip install imbalanced-learn scikit-learn
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn import model_selection as ms
from sklearn import preprocessing as pp
X, y = ds.make_classification(n_samples=5000,
    weights=[0.97], random_state=42)
# Split first, keep time order
X_tr, X_te, y_tr, y_te = ms.train_test_split(
    X, y, test_size=0.2, shuffle=False)
