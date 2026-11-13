"""Zero to AI Engineer · Python · Part 6 of 25
Slide: Safe Order Versus Leaky Order
Run: python 04_safe_order_versus_leaky_order.py
"""
# --- repeated from 03_a_router_and_a_login_check.py so this file runs on its own ---
ROUTES = {}
def route(path):
    def deco(fn):
        ROUTES[path] = fn
        return fn
    return deco
def login_required(fn):
    def wrapper(user, *a, **kw):
        if user:
            return fn(user, *a, **kw)
        raise PermissionError
    return wrapper

# --- this slide ---
# route on top: registers the wrapper
@route("/safe")
@login_required
def safe(user): return "ok"

# route nearest: registers the bare function
@login_required
@route("/leaky")
def leaky(user): return "secret"

# prints 'secret': the check never ran
print(ROUTES["/leaky"](None))
