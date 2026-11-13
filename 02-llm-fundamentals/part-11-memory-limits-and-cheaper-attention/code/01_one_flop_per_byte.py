"""Zero to AI Engineer · LLM Fundamentals · Part 11 of 18
Slide: One flop per byte
Run: python 01_one_flop_per_byte.py
"""
params = 8e9
bytes_per = 2
flops_per_token = 2 * params
# weights only, batch size 1
bytes_read = params * bytes_per
# about 1 FLOP per byte: memory-bound
print(flops_per_token / bytes_read)
