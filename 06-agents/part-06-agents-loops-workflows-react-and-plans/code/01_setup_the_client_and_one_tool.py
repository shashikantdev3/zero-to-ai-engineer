"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Slide: Setup: the client and one tool
Run: python 01_setup_the_client_and_one_tool.py
"""
# Needs: pip install anthropic
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
