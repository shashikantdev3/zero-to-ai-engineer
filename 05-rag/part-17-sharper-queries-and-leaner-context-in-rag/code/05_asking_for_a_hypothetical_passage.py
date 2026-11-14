"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: Asking for a hypothetical passage
Run: python 05_asking_for_a_hypothetical_passage.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
question = (
    "Can contractors take parental leave?")
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"},
    messages=[{"role": "user", "content":
        "Write a short passage that would "
        f"answer: {question}"}])
draft = resp.content[0].text
