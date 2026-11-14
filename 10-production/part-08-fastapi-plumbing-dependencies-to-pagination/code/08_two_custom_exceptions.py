"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: Two custom exceptions
Run: python 08_two_custom_exceptions.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
BASE = "https://errors.example.com/"

class UpstreamModelError(Exception): ...
# invalid or unparseable model output
class ModelOutputError(Exception): ...
