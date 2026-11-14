"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: Ask, then keep the turn
Run: python 02_ask_then_keep_the_turn.py
"""
# Needs: pip install anthropic
# --- repeated from 01_describe_the_tool.py so this file runs on its own ---
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

# --- this slide ---
msgs = [{"role": "user",
         "content": "Where is ORD-123456?"}]
resp = client.messages.create(
    model=MODEL, max_tokens=300,
    thinking={"type": "disabled"},
    tools=tools, messages=msgs)
# keep the assistant turn that asked
msgs.append({"role": "assistant",
             "content": resp.content})
