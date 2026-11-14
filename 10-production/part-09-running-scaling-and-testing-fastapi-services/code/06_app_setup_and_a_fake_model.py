"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: App setup and a fake model
Run: python 06_app_setup_and_a_fake_model.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
import json
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
app = FastAPI()
PROBLEM = "application/problem+json"
def current_user(): return None
def llm_client(): return None
class FakeLLM:
    def __init__(self, reply):
        self.reply = reply
    async def complete(self, prompt):
        return self.reply
