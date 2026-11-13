"""Zero to AI Engineer · LLM Fundamentals · Part 17 of 18
Follow-along lab: Shape Passes, Code Still Blocks
Run: python 05_lab_shape_passes_code_still_blocks.py
"""
import json
raw = ('{"tool": "refund", '
       '"args": {"amount": 950}}')
call = json.loads(raw)
print("valid JSON:", isinstance(call, dict))
print("tool proposed:", call["tool"])
amount = call["args"]["amount"]
order_total = 95
ok = amount <= order_total
print("amount within order:", ok)
if ok:
    print("run refund")
else:
    print("blocked by code")
