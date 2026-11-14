"""Zero to AI Engineer · RAG and Vector Search · Part 24 of 26
Slide: Spotting Broken Text
Run: python 02_spotting_broken_text.py
"""
def looks_broken(text):
    bad = sum(
        ch == "\ufffd"
        or 0xE000 <= ord(ch) <= 0xF8FF
        for ch in text)
    # replacement or private-use chars
    return bad / max(len(text), 1) > 0.02

print(looks_broken("Quarterly revenue rose"))
print(looks_broken("Q\ufffd\ufffdrterly"))
