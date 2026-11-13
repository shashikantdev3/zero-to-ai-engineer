"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: Counting Tokens With the API
Run: python 03_counting_tokens_with_the_api.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

text = "Reset the VPN token for user 4410-B"
msgs = [{"role": "user", "content": text}]
n = client.messages.count_tokens(
    model=MODEL, messages=msgs
).input_tokens
print(len(text.split()), "words")
print(n, "tokens")
