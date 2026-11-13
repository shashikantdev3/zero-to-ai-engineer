"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 16 of 28
Follow-along lab: Size training memory by hand
Run: python 04_lab_size_training_memory_by_hand.py
"""
params = 1_000_000_000
GB = 1e9
w = params * 4 / GB
grads = w
adam = 2 * w
print(f"fp32 weights: {w:.0f} GB")
print(f"+ grads: {w + grads:.0f} GB")
print(f"+ Adam: {w + grads + adam:.0f} GB")
mixed = params * (4 + 2) / GB
print(f"fp32+fp16 weights: {mixed:.0f} GB")
print("activations: not counted yet")
