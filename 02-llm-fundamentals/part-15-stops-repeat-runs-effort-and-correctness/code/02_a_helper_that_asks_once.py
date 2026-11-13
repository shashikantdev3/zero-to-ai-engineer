"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: A Helper That Asks Once
Run: python 02_a_helper_that_asks_once.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()

def ask(q):
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=50,
        thinking={"type": "disabled"},
        messages=[{"role": "user",
                   "content": q}])
    return resp.content[0].text
