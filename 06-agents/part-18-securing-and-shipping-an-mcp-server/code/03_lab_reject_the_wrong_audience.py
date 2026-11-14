"""Zero to AI Engineer · Agents and Tools · Part 18 of 26
Follow-along lab: Reject the wrong audience
Run: python 03_lab_reject_the_wrong_audience.py
"""
AUD = "api://tickets-mcp"
NOW = 1000
tokens = {
    "mcp": {"aud": AUD, "exp": 1060},
    "hr": {"aud": "api://hr", "exp": 1060},
    "old": {"aud": AUD, "exp": 940},
}
for name, c in tokens.items():
    if c["aud"] != AUD:
        print(name, "rejected: audience")
    elif c["exp"] < NOW:
        print(name, "rejected: expired")
    else:
        print(name, "accepted")
