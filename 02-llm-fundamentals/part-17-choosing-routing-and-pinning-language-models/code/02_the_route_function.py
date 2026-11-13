"""Zero to AI Engineer · LLM Fundamentals · Part 17 of 18
Slide: The Route Function
Run: python 02_the_route_function.py
"""
def route(kind, text):
    if text.startswith("RESET"):
        return "rules"
    n = client.messages.count_tokens(
        model=SMALL,
        messages=[{"role": "user",
                   "content": text}],
    ).input_tokens
    # limit in tokens, not characters
    if kind in EASY and n < 1_000:
        return SMALL
    return LARGE
