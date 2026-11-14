"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Reading every Retry-After form
Run: python 02_reading_every_retry_after_form.py
"""
def retry_after_seconds(h, default=1.0):
    # provider-specific header, check first
    if "retry-after-ms" in h:
        ms = float(h["retry-after-ms"])
        return ms / 1000
    value = h.get("retry-after")
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return seconds_until(value, default)
