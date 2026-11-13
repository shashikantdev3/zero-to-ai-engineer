"""Zero to AI Engineer · Prompting · Part 1 of 10
Follow-along lab: Test Your Done Check
Run: python 04_lab_test_your_done_check.py
"""
IDS = {"d1", "d2"}
def done(s, text, c):
    if len(text.split()) > 120:
        return False
    if s == "not_found":
        return not c
    return bool(c) and set(c) <= IDS
long = "word " * 130
print("valid cite:", done("ok", "Hi", ["d1"]))
print("fake cite:", done("ok", "Hi", ["d9"]))
print("no cite:", done("ok", "Hi", []))
print("too long:", done("ok", long, ["d1"]))
print("miss ok:", done("not_found", "", []))
