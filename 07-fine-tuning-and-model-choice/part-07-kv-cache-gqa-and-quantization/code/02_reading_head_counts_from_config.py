"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 7 of 10
Slide: Reading head counts from config
Run: python 02_reading_head_counts_from_config.py
"""
import json

raw = ('{"num_attention_heads": 32,'
       ' "num_key_value_heads": 8}')
cfg = json.loads(raw)
q = cfg['num_attention_heads']
kv = cfg['num_key_value_heads']
# size the cache with kv, not q
print('group size:', q // kv)
