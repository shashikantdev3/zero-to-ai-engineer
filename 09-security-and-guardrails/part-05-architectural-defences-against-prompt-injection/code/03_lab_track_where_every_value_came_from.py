"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Follow-along lab: Track where every value came from
Run: python 03_lab_track_where_every_value_came_from.py
"""
store = {
    "$SUMMARY": ("Lunch Friday", "untrusted"),
    "$ADDR": ("x@evil.example", "untrusted"),
    "$ME": ("me@home.example", "user"),
    "$NOTE": ("Running late", "user")}
def send(to, body):
    origins = (store[to][1], store[body][1])
    if "untrusted" in origins:
        return "BLOCKED"
    return "sent to " + store[to][0]
print("show:", store["$SUMMARY"][0])
print("1:", send("$ADDR", "$NOTE"))
print("2:", send("$ME", "$SUMMARY"))
print("3:", send("$ME", "$NOTE"))
