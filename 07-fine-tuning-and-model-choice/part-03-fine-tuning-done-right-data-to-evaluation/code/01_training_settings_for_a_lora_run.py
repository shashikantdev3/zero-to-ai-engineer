"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 3 of 10
Slide: Training Settings for a LoRA Run
Run: python 01_training_settings_for_a_lora_run.py
"""
# Values for TRL's SFTConfig (illustrative)
cfg = dict(
    output_dir="out",
    learning_rate=2e-4,
    num_train_epochs=2,
    warmup_ratio=0.03,
    eval_strategy="steps", eval_steps=50,
    save_strategy="steps", save_steps=100,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
)
