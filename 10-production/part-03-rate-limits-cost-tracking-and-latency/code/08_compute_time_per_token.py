"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Compute time per token
Run: python 08_compute_time_per_token.py
"""
# Needs: pip install anthropic
# Note: this calls a model, so it needs your key in ANTHROPIC_API_KEY (see SETUP.md).
# (not run while building this repo)
# --- repeated from 06_set_up_the_timer.py, 07_time_the_stream.py so this file runs on its own ---
import time
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
msgs = [{"role": "user",
         "content": "Explain DNS briefly."}]
t0 = time.perf_counter()
first, n = None, 0

with client.messages.stream(
    model=MODEL, max_tokens=300,
    thinking={"type": "disabled"},
    messages=msgs,
) as stream:
    for text in stream.text_stream:
        if first is None:
            first = time.perf_counter() - t0
        n += 1
total = time.perf_counter() - t0
if first is None:
    first = total

# --- this slide ---
# chunks approximate tokens;
# use usage for exact counts
tpot = (total - first) / max(n - 1, 1)
print(f"TTFT {first:.2f} s")
print(f"TPOT {tpot:.3f} s, chunks {n}")
