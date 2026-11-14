"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: The triad as three scores
Run: python 08_the_triad_as_three_scores.py
"""
q = "can unused leave carry forward"
chunks = "unused leave can carry forward"
answer = "yes unused leave can carry forward"
def overlap(a, b):
    wa, wb = set(a.split()), set(b.split())
    return round(len(wa & wb) / len(wa), 2)
triad = {
    "context_relevance": overlap(q, chunks),
    "groundedness": overlap(answer, chunks),
    "answer_relevance": overlap(q, answer),
}
print(triad)
