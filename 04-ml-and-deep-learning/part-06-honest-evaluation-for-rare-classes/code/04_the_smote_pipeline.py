"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: The SMOTE pipeline
Run: python 04_the_smote_pipeline.py
"""
# Needs: pip install imbalanced-learn scikit-learn
# --- repeated from 03_split_first_then_resample.py so this file runs on its own ---
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

# --- this slide ---
clf = lm.LogisticRegression(max_iter=1000)
# imblearn Pipeline: SMOTE on train only
pipe = Pipeline([
    ("scale", pp.StandardScaler()),
    ("smote", SMOTE(random_state=42)),
    ("clf", clf)])
# fraud is temporal: forward folds
cv = ms.TimeSeriesSplit(n_splits=5)
s = ms.cross_val_score(pipe, X_tr, y_tr,
    cv=cv, scoring="average_precision")
print(s.mean().round(3))
# Categorical columns: SMOTENC or weights.
