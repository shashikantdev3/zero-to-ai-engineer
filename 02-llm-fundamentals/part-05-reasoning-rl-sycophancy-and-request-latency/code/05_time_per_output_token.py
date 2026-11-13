"""Zero to AI Engineer · LLM Fundamentals · Part 5 of 18
Slide: Time per Output Token
Run: python 05_time_per_output_token.py
"""
# --- repeated from 04_measuring_time_to_first_token.py so this file runs on its own ---
from time import perf_counter as clock
import anthropic
client = anthropic.Anthropic()
p = "Summarise this incident in two lines."
msgs = [{"role": "user", "content": p}]
t0, first = clock(), None
with client.messages.stream(
        model="claude-haiku-5-5",
        max_tokens=300, messages=msgs,
        thinking={"type": "disabled"}) as s:
    for text in s.text_stream:
        first = first or clock() - t0
    final = s.get_final_message()

# --- this slide ---
total = clock() - t0
if first is None:
    # refusal, tool call only, empty reply
    print("no content tokens streamed")
else:
    out = final.usage.output_tokens
    per = (total - first) / max(out - 1, 1)
    print(f"TTFT {first:.2f}s")
    print(f"total {total:.2f}s")
    print(f"{out} tokens, {per:.3f}s each")
