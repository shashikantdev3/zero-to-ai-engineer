"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 7 of 10
Slide: Sizing the cache in Python
Run: python 01_sizing_the_cache_in_python.py
"""
# FP16 = 2 bytes per value
def kv_per_token(layers, kv_heads, dim, b=2):
    return 2 * layers * kv_heads * dim * b

# Llama-3-8B shape
per_tok = kv_per_token(32, 8, 128)
print(per_tok)
email = per_tok * 3000 / 1e6
users = per_tok * 3000 * 100 / 1e9
print(round(email), 'MB')
print(round(users, 1), 'GB')
