"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 1 of 10
Slide: A LoRA Config with PEFT
Run: python 01_a_lora_config_with_peft.py
"""
# Needs: pip install peft transformers
# (not run while building this repo, because the package was not installed there)
from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
repo = "hf-internal-testing/"
name = repo + "tiny-random-LlamaForCausalLM"
load = AutoModelForCausalLM.from_pretrained
base = load(name)
cfg = LoraConfig(r=8, lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM")
model = get_peft_model(base, cfg)
# shows trainable vs total parameters
model.print_trainable_parameters()
