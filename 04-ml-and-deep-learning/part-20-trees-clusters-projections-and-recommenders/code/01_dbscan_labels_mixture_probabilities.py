"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 20 of 28
Slide: DBSCAN labels, mixture probabilities
Run: python 01_dbscan_labels_mixture_probabilities.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import make_blobs
import sklearn.preprocessing as pp
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
X, _ = make_blobs(500, random_state=42)
X_s = pp.StandardScaler().fit_transform(X)
db = DBSCAN(eps=0.5, min_samples=10)
# label -1 means noise
labels = db.fit_predict(X_s)
gmm = GaussianMixture(n_components=5,
    random_state=42).fit(X_s)
probs = gmm.predict_proba(X_s)
