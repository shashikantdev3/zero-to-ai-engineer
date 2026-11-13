"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 17 of 28
Slide: Regression Metrics in scikit-learn
Run: python 03_regression_metrics_in_scikit_learn.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error, r2_score)
y_val = np.array([3.0, 5.0, 7.0, 9.0])
pred = np.array([2.5, 5.5, 7.0, 11.0])
mae = mean_absolute_error(y_val, pred)
mse = mean_squared_error(y_val, pred)
rmse = np.sqrt(mse)
# negative r2: worse than predicting the mean
r2 = r2_score(y_val, pred)
print(mae, rmse, r2)
