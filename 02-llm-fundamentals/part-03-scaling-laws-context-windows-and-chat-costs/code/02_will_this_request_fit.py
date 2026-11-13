"""Zero to AI Engineer · LLM Fundamentals · Part 3 of 18
Slide: Will this request fit?
Run: python 02_will_this_request_fit.py
"""
# stand-in for a real tokenizer
class Enc:
    def encode(self, text):
        return text.split()

enc = Enc()

def fits(messages, max_context, reserve):
    used = sum(len(enc.encode(m["content"]))
               for m in messages)
    return used + reserve <= max_context
