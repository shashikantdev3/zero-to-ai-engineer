"""Zero to AI Engineer · LLM Fundamentals · Part 5 of 18
Follow-along lab: A Latency Budget in Python
Run: python 06_lab_a_latency_budget_in_python.py
"""
network, queue = 0.05, 0.40
in_tok, prefill_per_tok = 4000, 0.0001
out_tok, decode_per_tok = 300, 0.02
prefill = in_tok * prefill_per_tok
ttft = network + queue + prefill
total = ttft + out_tok * decode_per_tok
print(f"prefill: {prefill:.2f}s")
print(f"TTFT: {ttft:.2f}s")
print(f"total: {total:.2f}s")
capped = ttft + 100 * decode_per_tok
print(f"capped at 100: {capped:.2f}s")
peak = network + 2 * queue + prefill
print(f"TTFT at peak: {peak:.2f}s")
