"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Follow-along lab: Feel the loss in plain Python
Run: python 06_lab_feel_the_loss_in_plain_python.py
"""
import math

def ce(p_true):
    return -math.log(p_true)

print(f"p true 0.9: {ce(0.9):.3f}")
print(f"p true 0.5: {ce(0.5):.3f}")
print(f"p true 0.01: {ce(0.01):.3f}")
errs = [1, 1, 1, 10]
mse = sum(e * e for e in errs) / len(errs)
mae = sum(abs(e) for e in errs) / len(errs)
print(f"MSE with one outlier: {mse}")
print(f"MAE with one outlier: {mae}")
