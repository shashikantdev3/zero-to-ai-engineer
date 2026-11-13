"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: Check the Stop Reason
Run: python 01_check_the_stop_reason.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    thinking={"type": "disabled"},
    stop_sequences=["\n### END"],
    messages=[{"role": "user",
               "content": "List 3 risks."}])
if resp.stop_reason == "max_tokens":
    raise ValueError("Truncated, do not parse")
print(resp.stop_reason)
print(resp.content[0].text)
