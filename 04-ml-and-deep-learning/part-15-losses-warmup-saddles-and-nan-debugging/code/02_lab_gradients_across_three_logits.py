"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 15 of 28
Follow-along lab: Gradients across three logits
Run: python 02_lab_gradients_across_three_logits.py
"""
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

y = 1.0
for z in [-6.0, -2.0, 2.0]:
    p = sigmoid(z)
    ce = p - y
    m = 2 * (p - y) * p * (1 - p)
    msg = f"z {z:+.0f} ce {ce:+.3f}"
    print(msg, f"mse {m:+.3f}")
