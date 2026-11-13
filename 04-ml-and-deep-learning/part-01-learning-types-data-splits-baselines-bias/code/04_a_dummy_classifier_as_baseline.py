"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 1 of 28
Slide: A dummy classifier as baseline
Run: python 04_a_dummy_classifier_as_baseline.py
"""
# Needs: pip install scikit-learn
from sklearn.dummy import DummyClassifier
from sklearn.metrics import recall_score
# 100 rows, 3 percent fraud
y_train = [int(i < 3) for i in range(100)]
X_train = [[i] for i in range(100)]
X_val, y_val = X_train, y_train
base = DummyClassifier(
    strategy="most_frequent")
base.fit(X_train, y_train)
print(base.score(X_val, y_val))
pred = base.predict(X_val)
print(recall_score(y_val, pred))
