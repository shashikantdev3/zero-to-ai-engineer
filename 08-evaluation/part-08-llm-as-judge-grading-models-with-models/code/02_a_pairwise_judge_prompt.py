"""Zero to AI Engineer · Evaluation · Part 8 of 11
Slide: A pairwise judge prompt
Run: python 02_a_pairwise_judge_prompt.py
"""
PAIRWISE = """Question: {q}
Answer A: {a}
Answer B: {b}
Which answer is more correct and complete
given the context? Ignore length.
Reply with A, B or TIE on the last line."""
reply = "B is grounded in the context.\nB"
verdict = reply.strip().splitlines()[-1]
print(verdict)
