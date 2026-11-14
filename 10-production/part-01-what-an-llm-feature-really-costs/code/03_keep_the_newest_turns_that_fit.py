"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: Keep the newest turns that fit
Run: python 03_keep_the_newest_turns_that_fit.py
"""
# Needs: pip install anthropic
# Note: this calls a model, so it needs your key in ANTHROPIC_API_KEY (see SETUP.md).
# (not run while building this repo)
# --- repeated from 02_count_tokens_before_sending.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

def count(text):
    msg = [{"role": "user", "content": text}]
    return client.messages.count_tokens(
        model=MODEL, messages=msg).input_tokens

# --- this slide ---
def fit_history(system, turns, max_tok=6_000):
    kept, used = [], count(system)
    # walk newest turn first
    for t in reversed(turns):
        n = count(t["content"])
        if used + n > max_tok:
            break
        kept.append(t)
        used += n
    return list(reversed(kept))
turns = [{"role": "user", "content": "Hi"}]
print(fit_history("Be brief.", turns))
