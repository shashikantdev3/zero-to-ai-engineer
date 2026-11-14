"""Zero to AI Engineer · RAG and Vector Search · Part 18 of 26
Slide: The agent loop with a hard cap
Run: python 03_the_agent_loop_with_a_hard_cap.py
"""
MAX_STEPS = 4
def decide(q, evidence):
    if len(evidence) >= 2:
        return "answer", q
    return "search", q
def search_tool(query, user_id):
    return [f"hit: {query}"]  # filtered here
evidence = []
for step in range(MAX_STEPS):  # hard cap
    kind, query = decide("compare", evidence)
    if kind == "answer": break
    evidence += search_tool(query, "u42")
