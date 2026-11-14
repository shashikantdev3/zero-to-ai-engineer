"""Zero to AI Engineer · Evaluation · Part 2 of 11
Slide: A code grader for a total
Run: python 04_a_code_grader_for_a_total.py
"""
import json
def grade(output: str, total: float) -> bool:
    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        return False
    got = float(data.get("total", -1))
    return abs(got - total) < 0.01
