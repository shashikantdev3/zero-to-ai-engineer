"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 2 of 10
Slide: The QLoRA settings
Run: python 04_the_qlora_settings.py
"""
# settings for BitsAndBytesConfig
bnb = dict(load_in_4bit=True,
           bnb_4bit_quant_type="nf4",
           bnb_4bit_use_double_quant=True,
           bnb_4bit_compute_dtype="bfloat16")
# settings for PEFT's LoraConfig
lora = dict(r=8, lora_alpha=16,
            target_modules="all-linear",
            task_type="CAUSAL_LM")
for key, value in {**bnb, **lora}.items():
    print(key, "=", value)
