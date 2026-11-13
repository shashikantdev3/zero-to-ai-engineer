"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Follow-along lab: Forward Versus Central Differences
Run: python 03_lab_forward_versus_central_differences.py
"""
def f(w):
    return w ** 3

w, eps = 1.5, 1e-3
exact = 3 * w ** 2
fwd = (f(w + eps) - f(w)) / eps
cen = (f(w + eps) - f(w - eps)) / (2 * eps)
fwd_err = abs(fwd - exact)
cen_err = abs(cen - exact)
print("exact slope:", exact)
print("forward error:", round(fwd_err, 7))
print("central error:", round(cen_err, 7))
print("central closer:", cen_err < fwd_err)
