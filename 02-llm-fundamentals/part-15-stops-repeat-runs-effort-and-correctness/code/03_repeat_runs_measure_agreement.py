"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: Repeat Runs, Measure Agreement
Run: python 03_repeat_runs_measure_agreement.py
"""
# --- repeated from 02_a_helper_that_asks_once.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()

def ask(q):
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=50,
        thinking={"type": "disabled"},
        messages=[{"role": "user",
                   "content": q}])
    return resp.content[0].text

# --- this slide ---
q = "Is 91 a prime? Answer yes or no."
runs = [ask(q) for _ in range(5)]
top = max(runs.count(r) for r in set(runs))
agreement = top / len(runs)
# flag anything below 100% for review
print(f"agreement {agreement:.0%}")
