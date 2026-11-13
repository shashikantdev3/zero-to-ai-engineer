"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: Read the Label, Hide the Rest
Run: python 06_read_the_label_hide_the_rest.py
"""
# --- repeated from 05_reasoning_field_comes_first.py so this file runs on its own ---
import json, anthropic
client = anthropic.Anthropic()
LABELS = ["access", "hardware", "software",
          "network", "other"]
# reasoning first: generated first
schema = {"type": "object",
    "properties": {
        "reasoning": {"type": "string"},
        "category": {"type": "string",
                     "enum": LABELS}},
    "required": ["reasoning", "category"],
    "additionalProperties": False}

# --- this slide ---
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=300,
    thinking={"type": "disabled"},
    output_config={"format": {
        "type": "json_schema",
        "schema": schema}},
    messages=[{"role": "user",
               "content": "VPN drops often"}])
out = json.loads(resp.content[0].text)
# redact reasoning before logging
# never show it to users
print(out["category"])
