"""Zero to AI Engineer · Python · Part 6 of 25
Slide: A Router and a Login Check
Run: python 03_a_router_and_a_login_check.py
"""
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
