"""Zero to AI Engineer · Security and Guardrails · Part 7 of 11
Slide: Reading the severity scores
Run: python 05_reading_the_severity_scores.py
"""
# Needs: pip install azure-identity
# (not run while building this repo, because the package was not installed there)
# --- repeated from 04_setting_up_content_safety.py so this file runs on its own ---
import os
from azure.ai.contentsafety import (
    ContentSafetyClient)
from azure.ai.contentsafety.models import (
    AnalyzeTextOptions)
from azure.identity import (
    DefaultAzureCredential)

ENDPOINT = os.environ["CS_ENDPOINT"]
cred = DefaultAzureCredential()
client = ContentSafetyClient(ENDPOINT, cred)
reply = "Sample reply to check."

# --- this slide ---
opts = AnalyzeTextOptions(text=reply)
res = client.analyze_text(opts)
# e.g. {"Hate": 0, "SelfHarm": 2, ...}
scores = {c.category: c.severity
          for c in res.categories_analysis}
print(scores)
