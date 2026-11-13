"""Zero to AI Engineer · Python · Part 10 of 25
Slide: A forwarding proxy
Run: python 08_a_forwarding_proxy.py
"""
class Proxy:
    def __init__(self, inner):
        self._inner = inner
    # only for names not found normally
    def __getattr__(self, name):
        return getattr(self._inner, name)

p = Proxy("hello")
# HELLO, forwarded to the str
print(p.upper())
