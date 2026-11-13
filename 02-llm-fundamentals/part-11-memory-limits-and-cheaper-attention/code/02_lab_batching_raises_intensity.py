"""Zero to AI Engineer · LLM Fundamentals · Part 11 of 18
Follow-along lab: Batching raises intensity
Run: python 02_lab_batching_raises_intensity.py
"""
params = 8e9
bytes_per = 2
flops = 2 * params
weight_bytes = params * bytes_per
gb = weight_bytes / 1e9
print(f"weights read: {gb:.0f} GB")
# one weight read now serves b sequences
for b in (1, 8, 64):
    ratio = flops * b / weight_bytes
    print(f"batch {b}: {ratio:.0f} flop/byte")
