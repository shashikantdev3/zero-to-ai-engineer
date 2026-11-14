"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: Describe the tool
Run: python 01_describe_the_tool.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
tools = [{"name": "get_order",
  "description": "Read-only. Look up one "
  "order by ID. Use for order status.",
  "input_schema": {"type": "object",
    "properties": {"order_id": {
      "type": "string",
      "pattern": "^ORD-[0-9]{6}$"}},
    "required": ["order_id"],
    "additionalProperties": False}}]
