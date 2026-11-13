"""Zero to AI Engineer · Python · Part 21 of 25
Follow-along lab: Classify codes, count attempts
Run: python 04_lab_classify_codes_count_attempts.py
"""
NOT_PROCESSED = {429, 503}
UNKNOWN = {408, 500, 502, 504}

def retry(status, safe):
    if status in NOT_PROCESSED:
        return True
    return status in UNKNOWN and safe

print("429 write:", retry(429, False))
print("502 refund:", retry(502, False))
print("502 with key:", retry(502, True))
print("404 any:", retry(404, True))
print("attempts:", 3 * 3 * 3)
