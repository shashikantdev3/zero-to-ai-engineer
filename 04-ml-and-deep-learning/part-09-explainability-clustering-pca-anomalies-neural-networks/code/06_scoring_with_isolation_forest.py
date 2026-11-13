"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: Scoring with Isolation Forest
Run: python 06_scoring_with_isolation_forest.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.ensemble import IsolationForest
rng = np.random.default_rng(42)
X_train = rng.normal(size=(500, 3))
X_val = rng.normal(size=(6, 3))
X_val[5] = 6.0
iso = IsolationForest(n_estimators=200,
    contamination="auto", random_state=42)
iso.fit(X_train)
# higher = more unusual; rank, take top k
anomaly_score = -iso.score_samples(X_val)
print(anomaly_score.round(2))
