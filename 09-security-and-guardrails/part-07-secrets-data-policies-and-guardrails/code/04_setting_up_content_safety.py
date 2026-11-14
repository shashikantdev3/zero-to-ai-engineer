"""Zero to AI Engineer · Security and Guardrails · Part 7 of 11
Slide: Setting up Content Safety
Run: python 04_setting_up_content_safety.py
"""
# Needs: pip install azure-identity
# (not run while building this repo, because the package was not installed there)
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
