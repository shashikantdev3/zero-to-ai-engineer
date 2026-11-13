"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Slide: An RBF kernel SVM in scikit-learn
Run: python 01_an_rbf_kernel_svm_in_scikit_learn.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import make_moons
from sklearn.pipeline import make_pipeline
import sklearn.preprocessing as pp
from sklearn.svm import SVC
X, y = make_moons(200, noise=0.2)
X_train, y_train = X[:150], y[:150]
X_val = X[150:]
svm = make_pipeline(pp.StandardScaler(),
                    SVC(kernel="rbf", C=1.0))
svm.fit(X_train, y_train)
# margins: rank with them, calibrate first
scores = svm.decision_function(X_val)
