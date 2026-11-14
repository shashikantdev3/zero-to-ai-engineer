"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: Running one case k times
Run: python 02_running_one_case_k_times.py
"""
import random

def flaky(q):
    return random.choice(["4", "4", "5"])

def run_case(system, case, k=5):
    res = [system(case["q"]) == case["a"]
           for _ in range(k)]
    return {"pass_rate": sum(res) / k,
            "pass_all": all(res),
            "pass_any": any(res)}
print(run_case(flaky, {"q": "2+2", "a": "4"}))
