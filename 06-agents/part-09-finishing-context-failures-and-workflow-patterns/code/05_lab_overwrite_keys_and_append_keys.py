"""Zero to AI Engineer · Agents and Tools · Part 9 of 26
Follow-along lab: Overwrite keys and append keys
Run: python 05_lab_overwrite_keys_and_append_keys.py
"""
state = {"hyp": None, "evidence": []}
def update(hyp=None, ev=None, ok=False):
    if hyp:
        # overwrite key: replace, never append
        state["hyp"] = hyp
    if ev and ok:
        # append key: verified entries only
        state["evidence"].append(ev)
    print(state["hyp"], state["evidence"])

update(hyp="disk is full")
update(hyp="bad config")
update(ev="config diff", ok=True)
update(ev="a guess", ok=False)
