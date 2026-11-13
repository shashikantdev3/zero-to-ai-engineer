"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: Set Effort, Read the Usage
Run: python 05_set_effort_read_the_usage.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
msg = "Plan a 3 step data migration."
resp = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1500,
    output_config={"effort": "low"},
    messages=[{"role": "user",
               "content": msg}])
# a thinking block may come first
text = "".join(b.text for b in resp.content
               if b.type == "text")
print(text)
print(resp.usage.output_tokens)
