"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Slide: The loop itself
Run: python 03_the_loop_itself.py
"""
# Needs: pip install anthropic
# --- repeated from 01_setup_the_client_and_one_tool.py, 02_the_gate_code_decides.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()
TOOLS = [{"name": "lookup",
  "description": "Get an order status",
  "input_schema": {"type": "object",
  "properties": {"id": {"type": "string"}}}}]
def ask(msgs, m="claude-haiku-5-5"):
    return client.messages.create(
        model=m, max_tokens=300,
        thinking={"type": "disabled"},
        tools=TOOLS, messages=msgs)
turn = lambda r, c: {"role": r, "content": c}

ALLOWED = {"lookup"}
def gate(c):
    return c.name in ALLOWED and "id" in c.input
def handle(calls):
    res = []
    for c in calls:
        out = "error: BLOCKED"
        if gate(c):
            out = f"{c.input['id']}: shipped"
        res.append({"type": "tool_result",
        "tool_use_id": c.id, "content": out})
    return res

# --- this slide ---
def run_agent(goal, max_steps=8):
    msgs = [turn("user", goal)]
    for _ in range(max_steps):
        r = ask(msgs)
        msgs += [turn("assistant", r.content)]
        if r.stop_reason != "tool_use":
            return r.content[0].text
        calls = [b for b in r.content
                 if b.type == "tool_use"]
        msgs += [turn("user", handle(calls))]
    return "Stopped: step limit. Escalate."
print(run_agent("Where is order 42?", 4))
