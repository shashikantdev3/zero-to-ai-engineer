"""Zero to AI Engineer · Prompting · Part 5 of 10
Slide: Counting Tokens
Run: python 02_counting_tokens.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

class BudgetExceeded(Exception): ...

def n_tokens(s: str) -> int:
    msgs = [{"role": "user", "content": s}]
    r = client.messages.count_tokens(
        model=MODEL, messages=msgs)
    return r.input_tokens
