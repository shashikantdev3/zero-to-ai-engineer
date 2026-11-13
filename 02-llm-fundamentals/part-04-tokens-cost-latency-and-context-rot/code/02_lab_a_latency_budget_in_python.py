"""Zero to AI Engineer · LLM Fundamentals · Part 4 of 18
Follow-along lab: A latency budget in Python
Run: python 02_lab_a_latency_budget_in_python.py
"""
ttft = 0.5
tps = 50
def latency(out_tokens):
    return ttft + out_tokens / tps
long = latency(600)
short = latency(150)
print("600 tokens:", long, "s")
print("150 tokens:", short, "s")
print("saved:", long - short, "s")
share = 600 / tps / long
print("decode share:", round(share, 2))
