"""Zero to AI Engineer · Agents and Tools · Part 15 of 26
Follow-along lab: Simulate the 403 rule
Run: python 04_lab_simulate_the_403_rule.py
"""
NEEDS = "Search Index Data Reader"
grants = {"Owner"}

def call(roles, rbac_on):
    if not rbac_on:
        return "denied, keys only"
    if NEEDS not in roles:
        return "403, no data role"
    return "200 OK"

print("Owner:", call(grants, True))
grants.add(NEEDS)
print("Keys only:", call(grants, False))
print("RBAC on:", call(grants, True))
