"""Zero to AI Engineer · LLM Fundamentals · Part 11 of 18
Slide: Cache size per token, compared
Run: python 03_cache_size_per_token_compared.py
"""
# cache per token per layer, in values
# MHA: 32 KV heads, head dim 128
mha = 2 * 32 * 128
# GQA: 8 KV heads
gqa8 = 2 * 8 * 128
# DeepSeek-V2 latent plus rotary key
mla = 512 + 64
# MQA: a single KV head
mqa = 2 * 1 * 128
print(mha, gqa8, mla, mqa)
