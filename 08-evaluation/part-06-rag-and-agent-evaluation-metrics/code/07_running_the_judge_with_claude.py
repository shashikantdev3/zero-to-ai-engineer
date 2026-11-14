"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: Running the judge with Claude
Run: python 07_running_the_judge_with_claude.py
"""
# Needs: pip install anthropic
# Note: this calls a model, so it needs your key in ANTHROPIC_API_KEY (see SETUP.md).
# (not run while building this repo)
# --- repeated from 06_a_rubric_judge_prompt.py so this file runs on its own ---
RUBRIC = """Question: {q}
Answer: {a}
Does the answer directly address every
part of the question?
Reply PASS or FAIL, then one sentence
of reason."""

q = "Can I carry forward unused leave?"
a = "Leave is paid time off from work."

# --- this slide ---
import anthropic
client = anthropic.Anthropic()

prompt = RUBRIC.format(q=q, a=a)
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    thinking={"type": "disabled"},
    messages=[{"role": "user",
               "content": prompt}],
)
print(resp.content[0].text)
