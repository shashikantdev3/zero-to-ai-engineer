"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: The answer function
Run: python 03_the_answer_function.py
"""
# Needs: pip install anthropic
# --- repeated from 01_retrieval_with_a_permission_filter.py, 02_calling_the_model.py so this file runs on its own ---
THRESHOLD = 0.5
REFUSAL = "I do not know. Open a ticket?"
DOCS = [("leave-policy-2026#s3-c2",
         "Staff get 25 days of leave.", "hr")]

def retrieve(q, groups):
    # permission filter first
    hits = [(c, t, 0.9) for c, t, g in DOCS
            if g in groups]
    # rerank stand-in: best score first
    hits.sort(key=lambda h: -h[2])
    return hits[:5]

import anthropic
client = anthropic.Anthropic()
SYSTEM = "Use only the documents. Cite ids."
def ask_model(msg):
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=200, system=SYSTEM,
        thinking={"type": "disabled"},
        messages=[{"role": "user",
                   "content": msg}])
    return resp.content[0].text

# --- this slide ---
def answer(q, groups):
    top = retrieve(q, groups)
    if not top or top[0][2] < THRESHOLD:
        return REFUSAL
    context = "\n\n".join(
        f"[{c}] {t}" for c, t, _ in top)
    msg = (f"<documents>\n{context}\n"
           f"</documents>\nQuestion: {q}")
    return ask_model(msg)

print(answer("How much leave?", {"hr"}))
print(answer("How much leave?", {"it"}))
