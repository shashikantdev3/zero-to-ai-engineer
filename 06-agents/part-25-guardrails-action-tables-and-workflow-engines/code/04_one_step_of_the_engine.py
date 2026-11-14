"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: One step of the engine
Run: python 04_one_step_of_the_engine.py
"""
def step(nodes, edges, cur, state):
    if cur not in nodes:
        raise UnknownNode(cur)
    # node gets a copy, returns an update
    update = nodes[cur](dict(state)) or {}
    state = {**state, **update}
    nxt = edges[cur](state)
    if nxt is None:
        raise UnknownNode(f"None from {cur}")
    return nxt, state
