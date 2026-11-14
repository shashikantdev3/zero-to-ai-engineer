"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: Building the rewrite prompt
Run: python 01_building_the_rewrite_prompt.py
"""
history = (
    "User: What's the parental leave rule?\n"
    "Assistant: Here is the staff policy.")
message = "and what about for contractors?"
rewrite_prompt = (
    "Rewrite the last user message as a "
    "standalone search query. Use the "
    "conversation only to resolve "
    "references. Return only the query.\n\n"
    f"{history}\nUser: {message}"
)
