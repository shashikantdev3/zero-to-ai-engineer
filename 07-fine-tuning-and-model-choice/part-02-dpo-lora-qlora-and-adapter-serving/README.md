# Fine-tuning and Model Choice · Part 2 of 10: DPO, LoRA, QLoRA and Adapter Serving

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. DPO
2. LoRA and the low-rank maths
3. QLoRA
4. Merging adapters and multi-LoRA serving

## Key takeaways

- DPO: pairs, no reward model, watch the margin
- LoRA: tiny B times A, mergeable, zero start
- QLoRA: adapters on a 4-bit base
- Merge or multi-LoRA; log the release ID

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_one_pair_one_margin.py` | One pair, one margin | yes |
| `code/02_counting_trainable_numbers.py` | Counting trainable numbers | yes |
| `code/03_lab_build_a_tiny_lora_by_hand.py` | Build a tiny LoRA by hand | yes |
| `code/04_the_qlora_settings.py` | The QLoRA settings | yes |
| `code/05_a_tiny_multi_lora_router.py` | A tiny multi-LoRA router | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_build_a_tiny_lora_by_hand.py` prints:

```text
start update: [0, 0]
W x plus B A x: [5, 11]
merged W x: [5, 11]
same: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. After DPO training, what is guaranteed to go up?**

- A. The reward model's score
- B. The margin between chosen and rejected
- C. The chosen answer's probability

<details><summary>Answer</summary>

**B. The margin between chosen and rejected**. DPO raises the margin, not the chosen probability

</details>

**2. Is a higher LoRA rank always better?**

- A. No, more capacity and more overfitting risk
- B. Yes, rank only changes the speed
- C. Yes, more rank means more accuracy

<details><summary>Answer</summary>

**A. No, more capacity and more overfitting risk**. Higher rank: more capacity, more overfit risk

</details>

**3. What does QLoRA training hand you at the end?**

- A. LoRA adapters trained on a 4-bit base
- B. A fully retrained full-precision model
- C. A 4-bit model ready to serve

<details><summary>Answer</summary>

**A. LoRA adapters trained on a 4-bit base**. QLoRA trains adapters; serving is a separate choice

</details>

**4. An adapter is a small file. How should you treat it?**

- A. As a config file you can edit
- B. As part of the base model
- C. As a versioned, evaluated model release

<details><summary>Answer</summary>

**C. As a versioned, evaluated model release**. An adapter is a model release, not a config

</details>

## Say it in the interview

**Say it in the interview**

- Chosen beats rejected, against a frozen reference
- No reward model, no PPO, use after SFT
- Labels from reviewers, not a model's opinion

**Say it in the interview**

- Learn a low-rank update, B times A
- 65 thousand numbers instead of 17 million
- Start all-linear, test against attention-only

**Say it in the interview**

- LoRA on a frozen 4-bit base
- One GPU instead of several; compare on evals

**Say it in the interview**

- Merge for one task, or serve many
- One base in memory, adapters per request

## Homework

- [ ] Recount LoRA parameters at rank 16
- [ ] Write three DPO preference pairs
- [ ] Explain QLoRA in two sentences
- [ ] Sketch a log line with a release ID
