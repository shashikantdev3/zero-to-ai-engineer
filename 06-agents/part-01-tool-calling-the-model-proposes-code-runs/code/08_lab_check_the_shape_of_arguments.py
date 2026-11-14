"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Follow-along lab: Check the shape of arguments
Run: python 08_lab_check_the_shape_of_arguments.py
"""
REQ = ["service", "reason"]
OK = ["api", "worker", "scheduler"]
def check(a):
    if any(k not in a for k in REQ):
        return "missing a required field"
    if set(a) - set(REQ):
        return "invented field rejected"
    if a["service"] not in OK:
        return "service not in enum"
    return "shape ok"
good = {"service": "api", "reason": "slow"}
for a in [{"service": "api"}, good | {"x": 1},
          good | {"service": "db"}, good]:
    print(check(a))
