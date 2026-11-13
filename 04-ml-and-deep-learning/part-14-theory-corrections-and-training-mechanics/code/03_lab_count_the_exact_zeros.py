"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 14 of 28
Follow-along lab: Count the exact zeros
Run: python 03_lab_count_the_exact_zeros.py
"""
def sgn(x): return (x > 0) - (x < 0)
def soft(w, t):
    return sgn(w) * max(abs(w) - t, 0.0)
sub, prox, lr, t = [], [], 0.3, 0.03
for a in [0.05, -0.03, 2.0, 0.08]:
    w1 = w2 = 1.0
    for _ in range(200):
        w1 -= lr * (w1 - a) + t * sgn(w1)
        w2 = soft(w2 - lr * (w2 - a), t)
    sub.append(w1); prox.append(w2)
print("sub zeros:", sub.count(0.0))
print("prox zeros:", prox.count(0.0))
print("sub first w:", round(sub[0], 4))
print("prox big w:", round(prox[2], 4))
