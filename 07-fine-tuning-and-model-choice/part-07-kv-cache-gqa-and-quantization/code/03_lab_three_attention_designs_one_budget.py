"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 7 of 10
Follow-along lab: Three attention designs, one budget
Run: python 03_lab_three_attention_designs_one_budget.py
"""
def kv_bytes(layers, kv_heads, dim, b=2):
    return 2 * layers * kv_heads * dim * b

heads = [('MHA', 32), ('GQA', 8), ('MQA', 1)]
for name, kv in heads:
    per = kv_bytes(32, kv, 128)
    gb = per * 3000 * 100 / 1e9
    kib = per // 1024
    print(f'{name}: {kib} KiB, {gb:.1f} GB')
print('MHA / GQA:', 32 // 8, 'times')
