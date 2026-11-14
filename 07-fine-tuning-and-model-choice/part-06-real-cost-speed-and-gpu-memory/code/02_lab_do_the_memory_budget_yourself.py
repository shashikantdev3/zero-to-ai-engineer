"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 6 of 10
Follow-along lab: Do the memory budget yourself
Run: python 02_lab_do_the_memory_budget_yourself.py
"""
gpu_gb = 80
util = 0.9
usable = gpu_gb * util
weights = 8e9 * 2 / 1e9
overhead = 6
kv_gb = usable - weights - overhead
per_tok = 128 * 1024
tokens = kv_gb * 1e9 / per_tok
seqs = tokens // 3000
print(f"usable GB: {usable:.0f}")
print(f"weights GB: {weights:.0f}")
print(f"KV cache GB: {kv_gb:.0f}")
print(f"KV tokens: {tokens:,.0f}")
print(f"seqs of 3000: {seqs:.0f}")
