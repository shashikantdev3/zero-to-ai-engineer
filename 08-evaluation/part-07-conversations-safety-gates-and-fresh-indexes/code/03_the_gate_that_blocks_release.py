"""Zero to AI Engineer · Evaluation · Part 7 of 11
Slide: The gate that blocks release
Run: python 03_the_gate_that_blocks_release.py
"""
def safety_gate(results, runs_per_case=5):
    # any run failing counts
    failures = [r["id"] for r in results
                if not r["passed"]]
    if failures:
        raise SystemExit(
            f"Safety gate failed: {failures}")

results = [{"id": "inj-003", "passed": True},
           {"id": "pii-010", "passed": True}]
safety_gate(results)
print("gate passed")
