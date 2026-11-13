"""Zero to AI Engineer · LLM Fundamentals · Part 17 of 18
Slide: Fallback on Failed Validation
Run: python 03_fallback_on_failed_validation.py
"""
# --- repeated from 01_router_setup_two_models.py, 02_the_route_function.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()
SMALL = "claude-haiku-5-5"
LARGE = "claude-sonnet-5-5"
EASY = {"classify", "extract"}

def ask(model, text):
    resp = client.messages.create(
        model=model, max_tokens=1000,
        messages=[{"role": "user",
                   "content": text}])
    # skip any thinking block
    return "".join(b.text for b in resp.content
                   if b.type == "text")

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

# --- this slide ---
def handle(kind, text):
    model = route(kind, text)
    if model == "rules":
        return "Handled by a rule."
    answer = ask(model, text)
    # fallback on failed validation
    if not answer.strip():
        answer = ask(LARGE, text)
    return answer

print(handle("classify", "Printer offline"))
