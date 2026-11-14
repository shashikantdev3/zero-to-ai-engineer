"""Zero to AI Engineer · RAG and Vector Search · Part 12 of 26
Slide: Page security when ACLs go stale
Run: python 01_page_security_when_acls_go_stale.py
"""
from datetime import datetime, timedelta
# agreed window, set with the security owner
ACL_SLA_MIN = 60
now = datetime.now()
last_acl_sync = now - timedelta(minutes=95)
def page_security_oncall(msg, age):
    print("PAGE:", msg, round(age), "min")
age = now - last_acl_sync
acl_age_min = age.total_seconds() / 60
if acl_age_min > ACL_SLA_MIN:
    page_security_oncall(
        "ACL sync stale", acl_age_min)
