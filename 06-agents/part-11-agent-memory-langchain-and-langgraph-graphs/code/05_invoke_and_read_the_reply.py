"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: Invoke and read the reply
Run: python 05_invoke_and_read_the_reply.py
"""
# Needs: pip install langchain
# (not run while building this repo, because the package was not installed there)
# --- repeated from 04_building_an_agent.py so this file runs on its own ---
from langchain.agents import create_agent

def get_order(order_id: str) -> str:
    """Look up an order's status."""
    return f"{order_id}: shipped"

agent = create_agent(
    model="anthropic:claude-haiku-5-5",
    tools=[get_order],
    system_prompt="You help users track "
                  "orders. Read-only.")

# --- this slide ---
q = "Where is ORD-123456?"
out = agent.invoke(
    {"messages": [{"role": "user",
                   "content": q}]})
print(out["messages"][-1].text)
