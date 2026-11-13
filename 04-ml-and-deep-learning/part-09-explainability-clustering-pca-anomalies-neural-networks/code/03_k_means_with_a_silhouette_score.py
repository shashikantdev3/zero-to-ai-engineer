"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: k-means with a silhouette score
Run: python 03_k_means_with_a_silhouette_score.py
"""
# Needs: pip install scikit-learn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn import datasets, preprocessing
X, _ = datasets.make_blobs(
    n_samples=300, centers=8,
    random_state=42)
scaler = preprocessing.StandardScaler()
X_s = scaler.fit_transform(X)
km = KMeans(n_clusters=8, init="k-means++",
            n_init=10, random_state=42)
km.fit(X_s)
print(silhouette_score(X_s, km.labels_))
