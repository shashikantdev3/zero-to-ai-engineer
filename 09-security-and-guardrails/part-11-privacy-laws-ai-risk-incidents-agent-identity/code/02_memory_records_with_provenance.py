"""Zero to AI Engineer · Security and Guardrails · Part 11 of 11
Slide: Memory Records With Provenance
Run: python 02_memory_records_with_provenance.py
"""
# user_id, source, created_at, validated
memory = [
    ("u1", "user message", "2024-05-01", True),
    ("u1", "web_tool", "2024-05-02", False),
    ("u2", "user message", "2024-05-03", True),
]
def load(user_id):
    # filter server side, per user
    return [m for m in memory
            if m[0] == user_id and m[3]]
print(load("u1"))
