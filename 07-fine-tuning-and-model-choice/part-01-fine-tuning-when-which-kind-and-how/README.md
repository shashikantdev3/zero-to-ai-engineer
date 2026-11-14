# Fine-tuning and Model Choice · Part 1 of 10: Fine-Tuning: When, Which Kind, and How

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Fine-tune, prompt or RAG (behaviour, not facts)
2. Full fine-tuning vs PEFT
3. SFT (supervised fine-tuning)
4. RLHF and reward models

## Key takeaways

- Facts in retrieval, behaviour in weights.
- Full: ~16 bytes/param. PEFT: small add-ons.
- SFT: right template, prompt masked.
- RLHF shapes preferences; watch for reward hacking.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_lora_config_with_peft.py` | A LoRA Config with PEFT | after `pip install peft transformers` |
| `code/02_a_tiny_chat_dataset.py` | A Tiny Chat Dataset | after `pip install datasets` |
| `code/03_sft_with_assistant_only_loss.py` | SFT with Assistant-Only Loss | after `pip install trl` |
| `code/04_lab_see_which_tokens_get_graded.py` | See Which Tokens Get Graded | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_see_which_tokens_get_graded.py` prints:

```text
tokens: 9
graded: ['<assistant>', 'Paris.']
masked: 7
graded share: 22%
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A team says: fine-tune on our policy PDFs so the model knows them. What is the better design?**

- A. Fine-tune again on the PDFs weekly
- B. Fine-tune once on a bigger model
- C. Search index with access lists and citations

<details><summary>Answer</summary>

**C. Search index with access lists and citations**. Facts go in retrieval. Behaviour goes in weights.

</details>

**2. Is PEFT always as good as full fine-tuning?**

- A. Often close on narrow tasks, not guaranteed
- B. No, it is always clearly worse
- C. Yes, it always matches full fine-tuning

<details><summary>Answer</summary>

**A. Often close on narrow tasks, not guaranteed**. Prove it with the same eval set and a baseline.

</details>

**3. You ran SFT on raw text with no chat template. Outputs look odd. Most likely cause?**

- A. Training format differs from inference format
- B. Two epochs was far too few
- C. The base model was frozen

<details><summary>Answer</summary>

**A. Training format differs from inference format**. Train in the same chat template you serve.

</details>

**4. What does RLHF mainly change in a model?**

- A. The facts it knows
- B. Its preferences and style
- C. Its tokenizer and vocabulary

<details><summary>Answer</summary>

**B. Its preferences and style**. RLHF shapes preferences and style, not facts.

</details>

## Say it in the interview

**Behaviour in Weights, Facts in Retrieval**

- Fine-tuning changes behaviour. RAG changes knowledge.
- Changing facts and permissions mean retrieval.
- Fine-tune only after the prompted baseline plateaus.

**Full Fine-Tuning vs PEFT, Briefly**

- ~16 bytes per parameter: 8B model ≈ 128 GB.
- Frozen base, megabyte adapters, many tasks.
- Full fine-tuning needs data, change, and budget.

**SFT in Three Sentences**

- Prompts plus exact answers, next-token loss.
- Own template, masked prompt, check the version.
- SFT copies. DPO compares. Data is the ceiling.

**RLHF in Three Sentences**

- SFT, reward model, then PPO with a KL penalty.
- Complex, unstable, and open to reward hacking.
- DPO: same preference data, simpler training.

## Homework

- [ ] Write your facts vs behaviour rule
- [ ] Compute full fine-tuning memory for a 3B model
- [ ] Rerun the lab with two assistant turns
- [ ] Explain reward hacking and how to detect it
