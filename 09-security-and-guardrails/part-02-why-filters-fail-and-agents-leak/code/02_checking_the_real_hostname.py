"""Zero to AI Engineer · Security and Guardrails · Part 2 of 11
Slide: Checking the real hostname
Run: python 02_checking_the_real_hostname.py
"""
from urllib.parse import urlsplit
ALLOWED = ("learn.microsoft.com",
           "intranet.example.com")
def allowed(url: str) -> bool:
    try:
        u = urlsplit(url.strip())
        host = (u.hostname or "").lower()
    except ValueError:
        return False
    return any(host == d or
               host.endswith("." + d)
               for d in ALLOWED)
