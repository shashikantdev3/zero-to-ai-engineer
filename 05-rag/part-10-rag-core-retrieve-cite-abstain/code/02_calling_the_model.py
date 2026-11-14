"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Calling the model
Run: python 02_calling_the_model.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
SYSTEM = "Use only the documents. Cite ids."
def ask_model(msg):
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=200, system=SYSTEM,
        thinking={"type": "disabled"},
        messages=[{"role": "user",
                   "content": msg}])
    return resp.content[0].text
