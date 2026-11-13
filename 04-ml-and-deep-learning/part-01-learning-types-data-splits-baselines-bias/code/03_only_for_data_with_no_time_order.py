"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 1 of 28
Slide: Only for data with no time order
Run: python 03_only_for_data_with_no_time_order.py
"""
# Needs: pip install scikit-learn
from sklearn.model_selection import (
    train_test_split,
)
# only for data with no time order
X = [[i] for i in range(100)]
y = [int(i % 10 == 0) for i in range(100)]
X_tmp, X_test, y_tmp, y_test = (
    train_test_split(
        X, y, test_size=0.2,
        stratify=y, random_state=42))
print(sum(y_test), "positive rows in test")
