"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: Force that one tool
Run: python 11_force_that_one_tool.py
"""
# Needs: pip install anthropic
# --- repeated from 10_a_tool_to_classify_incidents.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()
tools = [{"name": "classify_incident",
  "description": "Classify one incident.",
  "input_schema": {"type": "object",
    "properties": {"severity": {
      "type": "string",
      "enum": ["low", "high"]}},
    "required": ["severity"],
    "additionalProperties": False}}]

# --- this slide ---
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"},
    tools=tools,
    tool_choice={"type": "tool",
                 "name": "classify_incident"},
    messages=[{"role": "user",
               "content": "DB is down"}])
print(resp.content[0].input)
# others: {"type": "auto"}, {"type": "any"},
# {"type": "none"}
