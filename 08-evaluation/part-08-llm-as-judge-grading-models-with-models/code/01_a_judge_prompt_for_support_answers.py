"""Zero to AI Engineer · Evaluation · Part 8 of 11
Slide: A judge prompt for support answers
Run: python 01_a_judge_prompt_for_support_answers.py
"""
JUDGE_PROMPT = """\
You are grading a support answer.
Question: {q}
Retrieved context: {ctx}
Answer: {a}
Rule: PASS only if every factual claim
is supported by the context AND the
question is answered.
First give a one-sentence reason, then
on the last line write PASS or FAIL."""
filled = JUDGE_PROMPT.format(q="Refund?",
    ctx="Refunds: 30 days.", a="30 days.")
