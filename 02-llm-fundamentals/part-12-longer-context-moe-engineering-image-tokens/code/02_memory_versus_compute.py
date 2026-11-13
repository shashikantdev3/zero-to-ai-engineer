"""Zero to AI Engineer · LLM Fundamentals · Part 12 of 18
Slide: Memory Versus Compute
Run: python 02_memory_versus_compute.py
"""
total = 671e9
active = 37e9
# FP8 weights, illustrative
bytes_per = 1
gb = total * bytes_per / 1e9
print(gb, "GB of weights resident")
# like a ~37B dense model
gflops = 2 * active / 1e9
print(gflops, "GFLOPs per token")
