"""Zero to AI Engineer · Security and Guardrails · Part 2 of 11
Follow-along lab: Naive check versus real hostname
Run: python 04_lab_naive_check_versus_real_hostname.py
"""
from urllib.parse import urlsplit

OK = "learn.microsoft.com"
def allowed(url):
    host = urlsplit(url).hostname or ""
    host = host.lower()
    good = host.endswith("." + OK)
    return host == OK or good
tests = ["https://evil.com/?x=" + OK,
         "https://notlearn.microsoft.com/",
         "https://" + OK + "@evil.com/",
         "https://LEARN.microsoft.com/a"]
for u in tests:
    print(OK in u, allowed(u))
