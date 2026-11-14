"""Zero to AI Engineer · Evaluation · Part 2 of 11
Slide: The grader has its own tests
Run: python 05_the_grader_has_its_own_tests.py
"""
# --- repeated from 04_a_code_grader_for_a_total.py so this file runs on its own ---
import json
def grade(output: str, total: float) -> bool:
    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        return False
    got = float(data.get("total", -1))
    return abs(got - total) < 0.01

# --- this slide ---
def test_grade():
    assert grade('{"total": 118.0}', 118.0)
    assert not grade("not json", 118.0)
    assert not grade('{"amount": 118}', 118.0)
test_grade()
print("grader tests pass")
