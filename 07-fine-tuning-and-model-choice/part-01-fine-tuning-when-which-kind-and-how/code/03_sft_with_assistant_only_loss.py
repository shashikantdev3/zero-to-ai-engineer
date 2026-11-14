"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 1 of 10
Slide: SFT with Assistant-Only Loss
Run: python 03_sft_with_assistant_only_loss.py
"""
# Needs: pip install trl
# (not run while building this repo, because the package was not installed there)
from trl import SFTTrainer, SFTConfig
MODEL_ID = "Qwen/Qwen3-0.6B"
# Arg names change between TRL versions.
# Check your installed version.
args = SFTConfig(output_dir="out",
    num_train_epochs=2,
    assistant_only_loss=True)
trainer = SFTTrainer(model=MODEL_ID,
    train_dataset=train_ds, args=args)
trainer.train()
