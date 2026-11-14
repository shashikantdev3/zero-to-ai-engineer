"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: Building an agent
Run: python 04_building_an_agent.py
"""
# Needs: pip install langchain
# (not run while building this repo, because the package was not installed there)
from langchain.agents import create_agent

def get_order(order_id: str) -> str:
    """Look up an order's status."""
    return f"{order_id}: shipped"

agent = create_agent(
    model="anthropic:claude-haiku-5-5",
    tools=[get_order],
    system_prompt="You help users track "
                  "orders. Read-only.")
