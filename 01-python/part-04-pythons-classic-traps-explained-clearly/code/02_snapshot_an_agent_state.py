"""Zero to AI Engineer · Python · Part 4 of 25
Slide: Snapshot an Agent State
Run: python 02_snapshot_an_agent_state.py
"""
import copy
msg = {"role": "user", "content": "hi"}
state = {"messages": [msg]}
shallow = state.copy()
deep = copy.deepcopy(state)
reply = {"role": "assistant",
         "content": "hello"}
state["messages"].append(reply)
# shallow prints 2, deep prints 1
print(len(shallow["messages"]))
print(len(deep["messages"]))
