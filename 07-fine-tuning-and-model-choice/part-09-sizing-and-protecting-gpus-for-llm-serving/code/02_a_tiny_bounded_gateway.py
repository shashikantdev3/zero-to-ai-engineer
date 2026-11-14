"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 9 of 10
Slide: A Tiny Bounded Gateway
Run: python 02_a_tiny_bounded_gateway.py
"""
MAX_SEQS, MAX_QUEUE = 2, 2
running, queue = [], []
def admit(req):
    if len(running) < MAX_SEQS:
        running.append(req)
        return "running"
    if len(queue) < MAX_QUEUE:
        queue.append(req)
        return "queued"
    return "429, Retry-After 2"
for req in range(5):
    print(req, admit(req))
