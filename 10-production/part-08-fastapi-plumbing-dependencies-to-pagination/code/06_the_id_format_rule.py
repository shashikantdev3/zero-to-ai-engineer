"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: The ID format rule
Run: python 06_the_id_format_rule.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
import re
import uuid
from fastapi import FastAPI, Request

app = FastAPI()
HDR = "x-correlation-id"
CID_OK = re.compile(r"[A-Za-z0-9-]{8,64}")
