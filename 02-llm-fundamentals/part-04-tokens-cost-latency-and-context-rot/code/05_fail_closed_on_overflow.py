"""Zero to AI Engineer · LLM Fundamentals · Part 4 of 18
Slide: Fail closed on overflow
Run: python 05_fail_closed_on_overflow.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
# set this to your model's context window
MAX_CONTEXT = 200_000
RESERVE = 300
doc = "quarterly report text " * 50
msgs = [{"role": "user", "content": doc}]
n = client.messages.count_tokens(
    model=MODEL, messages=msgs).input_tokens
if n + RESERVE > MAX_CONTEXT:
    raise ValueError("Prompt too long, trim it")
