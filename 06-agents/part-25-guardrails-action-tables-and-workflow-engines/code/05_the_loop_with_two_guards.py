"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: The loop with two guards
Run: python 05_the_loop_with_two_guards.py
"""
def run(nodes, edges, start, state, cap=50):
    cur, seen = start, set()
    while cur != END:
        if len(seen) >= cap:
            raise StepLimit(f"at {cur}")
        fp = fingerprint(cur, state)
        if fp in seen:
            raise CycleDetected(cur)
        seen.add(fp)
        cur, state = step(nodes, edges,
                          cur, state)
    return state
