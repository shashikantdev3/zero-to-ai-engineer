"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 7 of 10
Slide: Half the bytes, twice the tokens
Run: python 05_half_the_bytes_twice_the_tokens.py
"""
def kv_per_token(layers, kv_heads, dim, b=2):
    return 2 * layers * kv_heads * dim * b

fp16 = kv_per_token(32, 8, 128, b=2)
fp8 = kv_per_token(32, 8, 128, b=1)
budget = 39 * 10**9
print(budget // fp16, 'tokens in FP16')
print(budget // fp8, 'tokens in FP8')
# vllm serve MODEL --kv-cache-dtype fp8
# check support for your GPU and version
