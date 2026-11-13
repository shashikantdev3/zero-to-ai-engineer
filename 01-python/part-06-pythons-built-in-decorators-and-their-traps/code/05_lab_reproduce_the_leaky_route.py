"""Zero to AI Engineer · Python · Part 6 of 25
Follow-along lab: Reproduce the Leaky Route
Run: python 05_lab_reproduce_the_leaky_route.py
"""
ROUTES = {}
def route(path):
    def deco(fn):
        ROUTES[path] = fn
        return fn
    return deco
def guard(fn):
    return lambda u: fn(u) if u else "blocked"
def secret(u): return "secret"
route("/safe")(guard(secret))
leaky = guard(route("/leaky")(secret))
print("safe route:", ROUTES["/safe"](None))
print("leaky route:", ROUTES["/leaky"](None))
print("leaky name:", leaky(None))
