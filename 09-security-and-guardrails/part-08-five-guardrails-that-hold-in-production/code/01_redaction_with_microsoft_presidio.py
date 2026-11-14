"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Slide: Redaction with Microsoft Presidio
Run: python 01_redaction_with_microsoft_presidio.py
"""
# Needs: pip install presidio_analyzer presidio_anonymizer
# (not run while building this repo, because the package was not installed there)
# Needs presidio and a spaCy model
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import (
    AnonymizerEngine)
text = "Call Asha on 212-555-0198"
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()
results = analyzer.analyze(
    text=text, language="en")
clean = anonymizer.anonymize(
    text=text, analyzer_results=results).text
print(clean)
