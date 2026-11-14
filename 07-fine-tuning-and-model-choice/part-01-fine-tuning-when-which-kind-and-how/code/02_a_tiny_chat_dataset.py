"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 1 of 10
Slide: A Tiny Chat Dataset
Run: python 02_a_tiny_chat_dataset.py
"""
# Needs: pip install datasets
# (not run while building this repo, because the package was not installed there)
from datasets import Dataset
chat = [{"role": "user", "content": "Hey"},
    {"role": "assistant", "content": "Hi."}]
rows = [{"messages": chat}]
train_ds = Dataset.from_list(rows)
