"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Truth check two: numbers and IDs
Run: python 09_truth_check_two_numbers_and_ids.py
"""
def numbers_in(source):
    found = set()
    for m in NUMBER.findall(source):
        clean = m.replace(",", "")
        try:
            found.add(Decimal(clean))
        except InvalidOperation:
            pass
    return found
def id_found(no, text):
    pat = PRE + re.escape(no) + POST
    return bool(re.search(pat, text, re.I))
