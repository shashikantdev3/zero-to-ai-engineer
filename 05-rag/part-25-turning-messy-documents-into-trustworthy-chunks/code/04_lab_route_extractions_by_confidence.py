"""Zero to AI Engineer · RAG and Vector Search · Part 25 of 26
Follow-along lab: Route extractions by confidence
Run: python 04_lab_route_extractions_by_confidence.py
"""
MASTER = {"V-101", "V-202"}
LIMIT = {"vendor": 0.9, "amount": 0.8}
def route(doc):
    for name, (val, conf) in doc.items():
        if conf < LIMIT[name]:
            return "review: low " + name
    if doc["vendor"][0] not in MASTER:
        return "review: not in master"
    return "accept"
def make(v, vc, a, ac):
    return {"vendor": (v, vc), "amount": (a, ac)}
print(route(make("V-101", .97, "120", .95)))
print(route(make("V-101", .97, "120", .55)))
print(route(make("V-999", .99, "80", .96)))
