"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 6 of 28
Slide: Balanced weights, in code
Run: python 06_balanced_weights_in_code.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets as ds
from sklearn import linear_model as lm
X, y = ds.make_classification(n_samples=5000,
    weights=[0.97], random_state=42)
plain = lm.LogisticRegression(max_iter=1000)
wtd = lm.LogisticRegression(
    class_weight="balanced", max_iter=1000)
p1 = plain.fit(X, y).predict_proba(X)[:, 1]
p2 = wtd.fit(X, y).predict_proba(X)[:, 1]
print(p1.mean().round(3), p2.mean().round(3))
# PyTorch: weight=torch.tensor([1.0, 32.0])
