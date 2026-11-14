"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: Pause, then resume the thread
Run: python 05_pause_then_resume_the_thread.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
from langgraph.graph import StateGraph
g = StateGraph(S)
g.add_node("approval", approval)
g.set_entry_point("approval")
g.set_finish_point("approval")
app = g.compile(checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "inc-1"}}
# first call pauses at the interrupt
out = app.invoke({"plan": "restart db",
                 "approved": False}, cfg)
out = app.invoke(Command(resume="yes"), cfg)
print(out["approved"])
