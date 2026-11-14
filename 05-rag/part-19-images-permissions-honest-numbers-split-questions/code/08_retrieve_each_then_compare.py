"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: Retrieve Each, Then Compare
Run: python 08_retrieve_each_then_compare.py
"""
# Needs: pip install anthropic
# --- repeated from 07_splitting_the_question.py so this file runs on its own ---
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

# --- this slide ---
def retrieve(sq, user, k):
    # stand-in for permission-trimmed search
    return [f"chunk about {sq}"][:k]
def generate_compare(q, evidence):
    # stand-in for the final compare call
    return f"{q}: {len(evidence)} sources"
user = "u1"
# hard cap of 4 sub-questions
evidence = {sq: retrieve(sq, user=user, k=5)
            for sq in subqs[:4] if sq.strip()}
print(generate_compare(q, evidence))
