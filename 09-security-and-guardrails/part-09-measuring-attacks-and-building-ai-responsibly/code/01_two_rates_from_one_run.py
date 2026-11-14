"""Zero to AI Engineer · Security and Guardrails · Part 9 of 11
Slide: Two Rates From One Run
Run: python 01_two_rates_from_one_run.py
"""
def asr(cases, run, k=5):
    results = []
    for c in cases:
        tries = [c.succeeded(run(c.prompt))
                 for _ in range(k)]
        results.append(tries)
    n = len(cases)
    hits = sum(map(sum, results))
    per_attempt = hits / (n * k)
    any_hit = sum(any(r) for r in results)
    return per_attempt, any_hit / n
