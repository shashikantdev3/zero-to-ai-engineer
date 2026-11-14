"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Parsing the date form
Run: python 01_parsing_the_date_form.py
"""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

def seconds_until(value, default=1.0):
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return default
    now = datetime.now(timezone.utc)
    wait = (when - now).total_seconds()
    return max(0.0, wait)
