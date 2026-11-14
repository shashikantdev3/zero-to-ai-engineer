"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: Parse the judge's reply
Run: python 06_parse_the_judges_reply.py
"""
def parse_ids(reply):
    if not reply.startswith("SUPPORTED"):
        return set()
    rest = reply[len("SUPPORTED"):].split(",")
    # strip brackets if the judge copies them
    ids = {i.strip(" []") for i in rest}
    ids.discard("")
    return ids

print(sorted(parse_ids("SUPPORTED [c1], c3")))
