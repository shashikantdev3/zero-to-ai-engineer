"""Zero to AI Engineer · LLM Fundamentals · Part 17 of 18
Slide: Router Setup: Two Models
Run: python 01_router_setup_two_models.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
SMALL = "claude-haiku-5-5"
LARGE = "claude-sonnet-5-5"
EASY = {"classify", "extract"}

def ask(model, text):
    resp = client.messages.create(
        model=model, max_tokens=1000,
        messages=[{"role": "user",
                   "content": text}])
    # skip any thinking block
    return "".join(b.text for b in resp.content
                   if b.type == "text")
