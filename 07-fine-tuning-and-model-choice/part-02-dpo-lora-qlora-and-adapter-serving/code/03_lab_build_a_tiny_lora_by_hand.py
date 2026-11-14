"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 2 of 10
Follow-along lab: Build a tiny LoRA by hand
Run: python 03_lab_build_a_tiny_lora_by_hand.py
"""
def mv(M, v):
    return [sum(m * e for m, e in zip(r, v))
            for r in M]
W, x = [[1, 2], [3, 4]], [1, 1]
A, B = [[1, 1]], [[0], [0]]
print("start update:", mv(B, mv(A, x)))
B = [[1], [2]]
up = mv(B, mv(A, x))
out = [p + q for p, q in zip(mv(W, x), up)]
print("W x plus B A x:", out)
Wm = [[W[i][j] + B[i][0] * A[0][j]
       for j in range(2)] for i in range(2)]
print("merged W x:", mv(Wm, x))
print("same:", out == mv(Wm, x))
