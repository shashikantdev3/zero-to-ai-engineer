"""Zero to AI Engineer · RAG and Vector Search · Part 12 of 26
Slide: A refusal template and two rates
Run: python 04_a_refusal_template_and_two_rates.py
"""
REFUSAL = ("I could not find this in the "
    "policy documents. The closest related "
    "document is {nearest}. You can raise a "
    "request with {route}, and I will pass "
    "on this conversation.")
wrong_on_unanswerable, n_unanswerable = 6, 40
refusals_on_answerable, n_answerable = 9, 160
false_answer_rate = (
    wrong_on_unanswerable / n_unanswerable)
false_refusal_rate = (
    refusals_on_answerable / n_answerable)
print(false_answer_rate, false_refusal_rate)
