"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: Splitting the Question
Run: python 07_splitting_the_question.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
q = "Compare 2025 and 2026 leave policies"
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    thinking={"type": "disabled"},
    messages=[{"role": "user", "content":
        "Split into independent search "
        "questions, one per line:\n" + q}],
)
subqs = resp.content[0].text.splitlines()
