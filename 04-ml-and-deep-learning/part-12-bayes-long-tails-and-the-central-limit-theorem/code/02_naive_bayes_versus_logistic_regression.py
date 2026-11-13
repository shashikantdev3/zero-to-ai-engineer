"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Slide: Naive Bayes versus logistic regression
Run: python 02_naive_bayes_versus_logistic_regression.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets, linear_model
from sklearn import model_selection as ms
from sklearn.naive_bayes import GaussianNB
X, y = datasets.make_classification(
    n_samples=500, random_state=0)
logreg = linear_model.LogisticRegression
models = (GaussianNB(), logreg(max_iter=1000))
for m in models:
    s = ms.cross_val_score(m, X, y, cv=5,
        scoring="average_precision")
    print(type(m).__name__, s.mean())
