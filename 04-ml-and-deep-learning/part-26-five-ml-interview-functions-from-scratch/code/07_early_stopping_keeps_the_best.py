"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: Early stopping keeps the best
Run: python 07_early_stopping_keeps_the_best.py
"""
def fit(X, y, Xv, yv, lr=0.1, lam=0.01):
    w, b = np.zeros(X.shape[1]), 0.0
    best, bw, bb, bad = np.inf, w, b, 0
    for _ in range(EPOCHS):
        idx = rng.permutation(len(y))
        w, b = epoch(X, y, w, b, idx, lr, lam)
        v = logloss(Xv, yv, w, b)
        if v < best - 1e-6:
            best, bw, bb, bad = v, w, b, 0
        elif (bad := bad + 1) >= PATIENCE:
            break
    return bw, bb
