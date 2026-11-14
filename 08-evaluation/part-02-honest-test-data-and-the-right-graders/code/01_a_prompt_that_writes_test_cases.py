"""Zero to AI Engineer · Evaluation · Part 2 of 11
Slide: A prompt that writes test cases
Run: python 01_a_prompt_that_writes_test_cases.py
"""
PROMPT = (
    "Write one question a real employee\n"
    "might ask that is answered ONLY by\n"
    "the text below. Use different words.\n"
    'Return JSON: {{"question": "...", '
    '"answer": "..."}}\nTEXT:\n{chunk}'
)
chunk = "Refunds are paid within 14 days."
print(PROMPT.format(chunk=chunk))
q = "How soon do I get my money back?"
case = {"question": q, "origin": "synthetic",
        "expected_doc_ids": ["doc-7"]}
