"""Zero to AI Engineer · LLM Fundamentals · Part 8 of 18
Follow-along lab: Lab: move the dials
Run: python 04_lab_lab_move_the_dials.py
"""
def kv(tokens, heads=8, nbytes=2, seqs=1):
    per = 2 * 32 * heads * 128 * nbytes
    return per * tokens * seqs

print(f"per token: {kv(1)/1e3:.0f} KB")
print(f"one user: {kv(3000)/1e6:.0f} MB")
big = kv(3000, seqs=100) / 1e9
print(f"100 users: {big:.1f} GB")
mha = kv(3000, heads=32, seqs=100) / 1e9
print(f"no GQA: {mha:.1f} GB")
q8 = kv(3000, nbytes=1, seqs=100) / 1e9
print(f"8-bit cache: {q8:.1f} GB")
