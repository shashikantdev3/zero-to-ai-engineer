"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: TargetEncoder in scikit-learn
Run: python 07_targetencoder_in_scikit_learn.py
"""
# Needs: pip install pandas scikit-learn
import pandas as pd
from sklearn import preprocessing as pp
col = "merchant_id"
X_train = pd.DataFrame(
    {col: list("aabbccddee") * 5})
y_train = [0, 1] * 25
X_val = pd.DataFrame({col: ["a", "z"]})
# fit_transform cross-fits inside folds
enc = pp.TargetEncoder(
    target_type="binary", smooth="auto")
X_tr_enc = enc.fit_transform(X_train, y_train)
X_val_enc = enc.transform(X_val)
