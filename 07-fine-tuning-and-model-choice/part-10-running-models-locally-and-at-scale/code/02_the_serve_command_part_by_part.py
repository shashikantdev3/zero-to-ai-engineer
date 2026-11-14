"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 10 of 10
Slide: The serve command, part by part
Run: python 02_the_serve_command_part_by_part.py
"""
import json

model = "Qwen/Qwen2.5-1.5B-Instruct"
# The shell command, as a list of parts
serve = ["vllm", "serve", model,
    "--max-model-len", "8192",
    "--gpu-memory-utilization", "0.90",
    "--max-num-seqs", "64"]
print(" ".join(serve))
