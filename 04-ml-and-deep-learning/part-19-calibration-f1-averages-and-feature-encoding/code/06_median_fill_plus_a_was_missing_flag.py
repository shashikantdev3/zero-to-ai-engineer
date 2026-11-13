"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: Median fill plus a was-missing flag
Run: python 06_median_fill_plus_a_was_missing_flag.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn import impute, pipeline
from sklearn import preprocessing as pp
from sklearn import linear_model as lm
X = np.array([[50], [np.nan], [70], [np.nan]])
y = [0, 1, 0, 1]
imp = impute.SimpleImputer(
    strategy="median", add_indicator=True)
pipe = pipeline.make_pipeline(imp,
    pp.StandardScaler(),
    lm.LogisticRegression(max_iter=1000))
pipe.fit(X, y)
