"""Zero to AI Engineer · LLM Fundamentals · Part 9 of 18
Follow-along lab: Watch the shapes move
Run: python 05_lab_watch_the_shapes_move.py
"""
B, n, d, h = 2, 5, 128, 8
dk = d // h
Q = (B, h, n, dk)
print("Q shape:", Q)
full_T = Q[::-1]
print(".T shape:", full_T)
swapped = Q[:2] + (Q[3], Q[2])
print("swapaxes shape:", swapped)
scores = (B, h, n, n)
print("scores shape:", scores)
print("scale:", dk ** 0.5, "not", d ** 0.5)
