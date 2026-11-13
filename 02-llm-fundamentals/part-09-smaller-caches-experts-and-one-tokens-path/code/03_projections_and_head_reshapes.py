"""Zero to AI Engineer · LLM Fundamentals · Part 9 of 18
Slide: Projections and head reshapes
Run: python 03_projections_and_head_reshapes.py
"""
def mha(X, Wq, Wk, Wv, Wo, h, causal=True):
    B, n, d = X.shape
    dk = d // h
    # (B, n, d) -> (B, h, n, dk)
    def heads(W):
        Y = (X @ W).reshape(B, n, h, dk)
        return Y.transpose(0, 2, 1, 3)
    Q, K, V = heads(Wq), heads(Wk), heads(Wv)
    out = attend(Q, K, V, causal)
    # back to (B, n, d)
    out = out.transpose(0, 2, 1, 3)
    return out.reshape(B, n, d) @ Wo
