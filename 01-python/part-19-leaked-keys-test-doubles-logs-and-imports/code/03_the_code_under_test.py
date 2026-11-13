"""Zero to AI Engineer · Python · Part 19 of 25
Slide: The code under test
Run: python 03_the_code_under_test.py
"""
def answer(q: str, llm, ret) -> str:
    ctx = "\n".join(ret.search(q, k=3))
    prompt = f"Use only this context:\n{ctx}"
    prompt += f"\n\nQ: {q}"
    return llm.complete(prompt=prompt,
                        temperature=0)

class FakeRetriever:
    def __init__(self, docs): self.docs = docs
    def search(self, q, k):
        return [d for d in self.docs
                if q.split()[0] in d][:k]
