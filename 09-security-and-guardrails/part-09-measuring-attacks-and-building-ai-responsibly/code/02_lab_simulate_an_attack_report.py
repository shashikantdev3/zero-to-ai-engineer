"""Zero to AI Engineer · Security and Guardrails · Part 9 of 11
Follow-along lab: Simulate an Attack Report
Run: python 02_lab_simulate_an_attack_report.py
"""
import random
rng = random.Random(7).random
cases = [0.0, 0.1, 0.0, 0.5, 0.0]
k = 5
runs = [[rng() < p for _ in range(k)]
        for p in cases]
total = len(cases) * k
hits = sum(map(sum, runs))
print(f"attempts: {total}")
print(f"per attempt: {hits / total:.2f}")
any_k = sum(any(r) for r in runs)
print(f"any of {k}: {any_k} of {len(cases)}")
print(f"0 of 20: up to {3 / 20:.0%}")
