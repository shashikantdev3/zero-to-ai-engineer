"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: A schema for the search plan
Run: python 07_a_schema_for_the_search_plan.py
"""
# Needs: pip install pydantic
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
