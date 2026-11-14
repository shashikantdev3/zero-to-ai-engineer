"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: Permissions added by code
Run: python 09_permissions_added_by_code.py
"""
# Needs: pip install pydantic
# --- repeated from 07_a_schema_for_the_search_plan.py, 08_code_builds_the_user_filter.py so this file runs on its own ---
from typing import Literal, Optional
from pydantic import BaseModel
Country = Literal["IN", "US", "UK"]
class SearchPlan(BaseModel):
    query: str
    country: Optional[Country] = None
    year_min: Optional[int] = None

llm_output = ('{"query": "leave rules", '
    '"country": "IN", "year_min": 2025}')
plan = SearchPlan.model_validate_json(
    llm_output)

def build_filter(plan):
    p = []
    if plan.country:
        p.append(f"country={plan.country}")
    if plan.year_min:
        p.append(f"year>={plan.year_min}")
    return " and ".join(p)

# may be empty
user_part = build_filter(plan)
print(user_part)

# --- this slide ---
def permission_filter(user):
    if not user["groups"]:
        raise PermissionError("default deny")
    return f"group in {user['groups']}"

user = {"id": "u1", "groups": ["hr"]}
perm = permission_filter(user)
if user_part:
    filters = f"({user_part}) and ({perm})"
else:
    filters = perm
print(filters)
