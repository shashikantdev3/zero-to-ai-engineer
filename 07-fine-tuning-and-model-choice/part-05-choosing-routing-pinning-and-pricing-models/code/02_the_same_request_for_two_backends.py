"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: The same request for two backends
Run: python 02_the_same_request_for_two_backends.py
"""
BASES = {
    "vllm": "http://localhost:8000/v1",
    "hosted": "https://api.example.com/v1",
}
def build(base, model, text):
    msgs = [{"role": "user", "content": text}]
    body = {"model": model, "messages": msgs}
    return base + "/chat/completions", body

msg = "Classify: disk full on db-01"
for name, base in BASES.items():
    print(name, build(base, "my-model", msg))
