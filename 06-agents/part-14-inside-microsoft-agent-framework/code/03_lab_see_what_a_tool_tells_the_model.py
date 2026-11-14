"""Zero to AI Engineer · Agents and Tools · Part 14 of 26
Follow-along lab: See what a tool tells the model
Run: python 03_lab_see_what_a_tool_tells_the_model.py
"""
from typing import Annotated
DESC = "One of: api, worker, scheduler"
OK = {"api", "worker", "scheduler"}
def service_status(
    service: Annotated[str, DESC]) -> dict:
    """Read-only. Health of ONE service."""
    if service not in OK:
        return {"ok": False, "err": "UNKNOWN"}
    return {"ok": True, "service": service}
a = service_status.__annotations__
print(service_status.__name__)
print(service_status.__doc__)
print(a["service"].__metadata__[0])
print(service_status("db"))
