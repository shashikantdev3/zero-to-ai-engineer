"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: Checking a Gradient by Hand
Run: python 02_checking_a_gradient_by_hand.py
"""
def loss(w, x, y):
    return 0.5 * (w * x - y) ** 2

def grad(w, x, y):
    # chain rule: error times x
    return (w * x - y) * x

w, x, y, eps = 1.5, 2.0, 1.0, 1e-6
up = loss(w + eps, x, y)
down = loss(w - eps, x, y)
numeric = (up - down) / (2 * eps)
assert abs(numeric - grad(w, x, y)) < 1e-6
