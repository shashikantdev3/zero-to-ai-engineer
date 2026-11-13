"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: PCA keeping 95 percent of variance
Run: python 05_pca_keeping_95_percent_of_variance.py
"""
# Needs: pip install scikit-learn
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn import datasets, preprocessing
X_train, _ = datasets.load_digits(
    return_X_y=True)
# keep 95% of the variance
pca = make_pipeline(
    preprocessing.StandardScaler(),
    PCA(n_components=0.95)).fit(X_train)
p = pca[-1]
print(p.n_components_)
print(p.explained_variance_ratio_[:3])
