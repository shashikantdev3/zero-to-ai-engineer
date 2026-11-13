"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: Five stratified folds, in code
Run: python 01_five_stratified_folds_in_code.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn import model_selection as ms
from sklearn import preprocessing as pp
from sklearn.pipeline import make_pipeline
X, y = ds.make_classification(n_samples=5000,
    weights=[0.97], random_state=42)
pipe = make_pipeline(pp.StandardScaler(),
    lm.LogisticRegression(max_iter=1000))
# non-temporal data only
cv = ms.StratifiedKFold(n_splits=5,
    shuffle=True, random_state=42)
