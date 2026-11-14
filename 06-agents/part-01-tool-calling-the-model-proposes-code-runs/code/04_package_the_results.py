"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: Package the results
Run: python 04_package_the_results.py
"""
# Needs: pip install anthropic
# --- repeated from 01_describe_the_tool.py, 02_ask_then_keep_the_turn.py, 03_treat_arguments_as_untrusted.py so this file runs on its own ---
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

msgs = [{"role": "user",
         "content": "Where is ORD-123456?"}]
resp = client.messages.create(
    model=MODEL, max_tokens=300,
    thinking={"type": "disabled"},
    tools=tools, messages=msgs)
# keep the assistant turn that asked
msgs.append({"role": "assistant",
             "content": resp.content})

import json, re
# in production: from the verified token
user_id = "u-42"
def get_order(order_id, user_id):
    return {"ok": True, "status": "shipped"}
def run_call(b):
    # arguments are untrusted input
    oid = str(b.input.get("order_id", ""))
    if not re.fullmatch(r"ORD-\d{6}", oid):
        return {"ok": False,
                "error": "INVALID_ARGS"}
    return get_order(oid, user_id=user_id)

# --- this slide ---
results = []
for b in resp.content:
    if b.type == "tool_use":
        res = json.dumps(run_call(b))
        results.append({
            "type": "tool_result",
            "tool_use_id": b.id,
            "content": res})
