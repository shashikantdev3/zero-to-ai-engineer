"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: One helper for every call
Run: python 01_one_helper_for_every_call.py
"""
# Needs: pip install anthropic
import json
import anthropic
client = anthropic.Anthropic()
SMALL = "claude-haiku-5-5"
BIG = "claude-sonnet-5-5"
def llm(model, system, text):
    r = client.messages.create(
        model=model, max_tokens=1000,
        system=system,
        messages=[{"role": "user",
                   "content": text}])
    # skip any thinking block
    return "".join(b.text for b in r.content
                   if b.type == "text")
