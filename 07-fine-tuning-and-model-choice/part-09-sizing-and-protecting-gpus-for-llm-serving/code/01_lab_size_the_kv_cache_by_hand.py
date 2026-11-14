"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 9 of 10
Follow-along lab: Size the KV Cache by Hand
Run: python 01_lab_size_the_kv_cache_by_hand.py
"""
rate = 5
secs = 8
seqs = rate * secs
kib = 128 * 1024
mean_gb = seqs * 3000 * kib / 1e9
p95_gb = seqs * 6000 * kib / 1e9
room_gb = 50
print(f"concurrent seqs: {seqs}")
print(f"floor (mean): {mean_gb:.1f} GB")
print(f"plan (p95): {p95_gb:.1f} GB")
print(f"fits in room: {p95_gb <= room_gb}")
print("next: load test at 40 seqs")
