"""Zero to AI Engineer · LLM Fundamentals · Part 3 of 18
Slide: Watch prompt tokens grow
Run: python 04_watch_prompt_tokens_grow.py
"""
def chat(msgs):
    # stand-in for the real API call
    words = [m["content"].split() for m in msgs]
    return "ok", sum(map(len, words))
msgs = [{"role": "system", "content": "Hi"}]
for t in ["first question", "second one"]:
    msgs.append({"role": "user", "content": t})
    reply, prompt_tokens = chat(msgs)
    msgs.append({"role": "assistant",
                 "content": reply})
    # grows on every turn
    print(prompt_tokens)
