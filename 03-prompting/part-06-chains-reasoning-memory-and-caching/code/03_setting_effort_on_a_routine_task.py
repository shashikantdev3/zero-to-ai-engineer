"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: Setting effort on a routine task
Run: python 03_setting_effort_on_a_routine_task.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
q = "Ticket: card charged twice. Category?"
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    # no temperature or top_p: effort instead
    output_config={"effort": "low"},
    messages=[{"role": "user", "content": q}],
)
# a thinking block may come first
print("".join(b.text for b in resp.content
              if b.type == "text"))
print(resp.usage.output_tokens)
