"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: A tool to classify incidents
Run: python 10_a_tool_to_classify_incidents.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
tools = [{"name": "classify_incident",
  "description": "Classify one incident.",
  "input_schema": {"type": "object",
    "properties": {"severity": {
      "type": "string",
      "enum": ["low", "high"]}},
    "required": ["severity"],
    "additionalProperties": False}}]
