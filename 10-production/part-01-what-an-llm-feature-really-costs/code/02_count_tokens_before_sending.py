"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: Count tokens before sending
Run: python 02_count_tokens_before_sending.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

def count(text):
    msg = [{"role": "user", "content": text}]
    return client.messages.count_tokens(
        model=MODEL, messages=msg).input_tokens
