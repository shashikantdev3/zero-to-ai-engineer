"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: A rubric judge prompt
Run: python 06_a_rubric_judge_prompt.py
"""
RUBRIC = """Question: {q}
Answer: {a}
Does the answer directly address every
part of the question?
Reply PASS or FAIL, then one sentence
of reason."""

q = "Can I carry forward unused leave?"
a = "Leave is paid time off from work."
