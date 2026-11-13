"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: A Role Line in Practice
Run: python 04_a_role_line_in_practice.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
ROLE = ("You are an IT operations assistant. "
        "Write for an on-call engineer at "
        "3 a.m.: short, specific, no filler.")
msg = "Disk on db1 is 95 percent full."
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"},
    system=ROLE,
    messages=[{"role": "user",
               "content": msg}])
print(resp.content[0].text)
