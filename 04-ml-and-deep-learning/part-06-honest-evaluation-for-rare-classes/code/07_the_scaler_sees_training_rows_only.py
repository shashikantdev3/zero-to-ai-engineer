"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: The scaler sees training rows only
Run: python 07_the_scaler_sees_training_rows_only.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn import model_selection as ms
from sklearn import preprocessing as pp
from sklearn.pipeline import make_pipeline
X, y = ds.make_classification(n_samples=5000,
    weights=[0.97], random_state=42)
X_tr, X_te, y_tr, y_te = ms.train_test_split(
    X, y, test_size=0.2, shuffle=False)
pipe = make_pipeline(pp.StandardScaler(),
    lm.LogisticRegression(max_iter=1000))
pipe.fit(X_tr, y_tr)
