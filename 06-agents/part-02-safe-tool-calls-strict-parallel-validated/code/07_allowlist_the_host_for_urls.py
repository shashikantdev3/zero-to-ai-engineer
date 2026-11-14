"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Allowlist the host for URLs
Run: python 07_allowlist_the_host_for_urls.py
"""
from urllib.parse import urlparse

ALLOWED = {"status.internal.example.com"}

def check_url(url: str) -> str:
    p = urlparse(url)
    bad_host = p.hostname not in ALLOWED
    if p.scheme != "https" or bad_host:
        # blocks http://169.254.169.254/
        raise ValueError("URL not allowed")
    # fetch it with redirects disabled
    return url
