"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: Scores, spread and the time gap
Run: python 02_scores_spread_and_the_time_gap.py
"""
# Needs: pip install scikit-learn
# --- repeated from 01_five_stratified_folds_in_code.py so this file runs on its own ---
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

# --- this slide ---
s = ms.cross_val_score(pipe, X, y, cv=cv,
    scoring="average_precision")
print(s.mean().round(3), s.std().round(3))
# Time data: rows sorted oldest first.
# gap counts rows, not days.
rows_per_day = 5
cv_t = ms.TimeSeriesSplit(n_splits=5,
    gap=rows_per_day * 60)
s_t = ms.cross_val_score(pipe, X, y,
    cv=cv_t, scoring="average_precision")
print(s_t.mean().round(3))
