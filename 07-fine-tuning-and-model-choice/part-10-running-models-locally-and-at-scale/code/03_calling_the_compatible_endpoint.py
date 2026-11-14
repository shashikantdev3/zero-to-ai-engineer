"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 10 of 10
Slide: Calling the compatible endpoint
Run: python 03_calling_the_compatible_endpoint.py
"""
# --- repeated from 02_the_serve_command_part_by_part.py so this file runs on its own ---
import json

model = "Qwen/Qwen2.5-1.5B-Instruct"
# The shell command, as a list of parts
serve = ["vllm", "serve", model,
    "--max-model-len", "8192",
    "--gpu-memory-utilization", "0.90",
    "--max-num-seqs", "64"]
print(" ".join(serve))

# --- this slide ---
base = "http://localhost:8000/v1"
url = base + "/chat/completions"
msg = {"role": "user",
       "content": "Summarise this alert."}
body = {"model": model, "messages": [msg]}
print(url)
print(json.dumps(body))
