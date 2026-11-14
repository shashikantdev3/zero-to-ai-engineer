"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 4 of 10
Follow-along lab: When does self-hosting pay off?
Run: python 01_lab_when_does_self_hosting_pay_off.py
"""
# Example inputs only. Measure your own.
gpu_hour = 2.0
gpus = 2
tok_hour_p95 = 9_000_000
util = 0.5
cost_hour = gpu_hour * gpus
useful = tok_hour_p95 * util / 1_000_000
per_m = cost_hour / useful
print(f"GPU cost per hour: {cost_hour}")
print(f"Million tokens per hour: {useful}")
print(f"Self-host per million: {per_m:.3f}")
full = cost_hour / (tok_hour_p95 / 1e6)
print(f"Ignoring utilisation: {full:.3f}")
