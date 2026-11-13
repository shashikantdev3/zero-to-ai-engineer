"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Truth check three: grounding
Run: python 10_truth_check_three_grounding.py
"""
def grounding_problems(inv, source):
    ok = id_found(inv.invoice_no, source)
    probs = [] if ok else ["invoice_no missing"]
    nums = numbers_in(source)
    amounts = [("total", inv.total),
               ("tax", inv.tax)]
    for i, l in enumerate(inv.lines):
        amounts += [(f"line {i}", l.amount)]
    for name, value in amounts:
        if value not in nums:
            probs.append(f"{name} not found")
    return probs
