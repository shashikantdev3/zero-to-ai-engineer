"""Zero to AI Engineer · LLM Fundamentals · Part 2 of 18
Slide: See the Real Role Markers
Run: python 01_see_the_real_role_markers.py
"""
# Needs: pip install transformers
from transformers import AutoTokenizer
MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
tok = AutoTokenizer.from_pretrained(MODEL_ID)
sys_msg = "Answer only from the context."
question = "Why did the job fail?"
messages = [
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": question}]
prompt = tok.apply_chat_template(
    messages, tokenize=False,
    add_generation_prompt=True)
print(prompt)
