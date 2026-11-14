"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 10 of 10
Slide: Pull, run, point at localhost
Run: python 01_pull_run_point_at_localhost.py
"""
# In a terminal:
#   ollama pull <model>
#   ollama run <model> "Summarise: ..."
# Ollama also serves an OpenAI-compatible
# endpoint (check your version's docs):
LOCAL = "http://localhost:11434/v1"
prompt = "Summarise: disk 95% full on db-01"
print("Base URL:", LOCAL)
print("Prompt:", prompt)
