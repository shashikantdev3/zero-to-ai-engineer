"""Zero to AI Engineer · LLM Fundamentals · Part 5 of 18
Slide: Measuring Time to First Token
Run: python 04_measuring_time_to_first_token.py
"""
# Needs: pip install anthropic
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
