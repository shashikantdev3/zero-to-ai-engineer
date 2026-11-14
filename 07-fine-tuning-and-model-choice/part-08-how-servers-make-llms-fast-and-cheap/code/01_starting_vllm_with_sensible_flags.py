"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 8 of 10
Slide: Starting vLLM with sensible flags
Run: python 01_starting_vllm_with_sensible_flags.py
"""
# the vllm serve command, as a list
cmd = [
    "vllm", "serve", "MODEL",
    "--max-model-len", "8192",
    "--max-num-seqs", "64",
    "--gpu-memory-utilization", "0.90",
    "--enable-prefix-caching",
]
print(" ".join(cmd))
