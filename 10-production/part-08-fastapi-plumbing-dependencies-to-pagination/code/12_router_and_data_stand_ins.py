"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Router and data stand-ins
Run: python 12_router_and_data_stand_ins.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import APIRouter, FastAPI

app = FastAPI()
v1 = APIRouter(prefix="/v1")

# stand-ins for your data layer
class FakeDB:
    async def page(self, after, limit):
        return []
db = FakeDB()
encode = str
decode = lambda c: c
