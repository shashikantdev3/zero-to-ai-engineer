"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: The groundedness judge prompt
Run: python 03_the_groundedness_judge_prompt.py
"""
JUDGE = """Context:
{context}

Claim: {claim}

Is the claim fully supported by the context?
Answer only SUPPORTED or NOT_SUPPORTED."""
