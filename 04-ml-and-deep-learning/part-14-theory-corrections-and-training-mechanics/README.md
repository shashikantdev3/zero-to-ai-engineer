# Machine Learning and Deep Learning · Part 14 of 28: Theory Corrections and Training Mechanics

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Problem framing: what decision does the output support
2. Bias-variance decomposition: squared loss only
3. Training error above validation error
4. L1 sparsity needs the right optimiser
5. Label smoothing and data augmentation

## Key takeaways

- Name the decision before picking a model
- Bias plus variance plus noise: squared loss only
- Check what each pass computes
- Zeros need proximal steps or coordinate descent
- Smooth targets, augment without changing labels

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_score_train_data_in_eval_mode.py` | Score train data in eval mode | yes |
| `code/02_soft_thresholding_in_numpy.py` | Soft-thresholding in NumPy | yes |
| `code/03_lab_count_the_exact_zeros.py` | Count the exact zeros | yes |
| `code/04_label_smoothing_in_pytorch.py` | Label smoothing in PyTorch | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_count_the_exact_zeros.py` prints:

```text
sub zeros: 0
prox zeros: 3
sub first w: 0.0139
prox big w: 1.9
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A team picked a model before naming the decision. Which follow-up exposes it?**

- A. Who acts on this number, and how?
- B. How many layers does it have?
- C. Which cloud will host it?

<details><summary>Answer</summary>

**A. Who acts on this number, and how?**. Name the decision before the model

</details>

**2. Does bias² + variance + noise hold exactly for accuracy?**

- A. Only when the dataset is large
- B. No, exact for squared error only
- C. Yes, it holds for any loss

<details><summary>Answer</summary>

**B. No, exact for squared error only**. The formula is algebra only for squared error

</details>

**3. Train loss is above validation loss. What do you check first?**

- A. Is dropout or augmentation training-only?
- B. Whether you need ten times more rows
- C. Nothing, it clearly generalises well

<details><summary>Answer</summary>

**A. Is dropout or augmentation training-only?**. Ask what changes between train and eval passes

</details>

**4. You add lam * np.sign(w) to your gradient update. How many weights end up exactly zero?**

- A. Every small weight hits exactly zero
- B. Usually none, they hover near zero
- C. Exactly half of them

<details><summary>Answer</summary>

**B. Usually none, they hover near zero**. Exact zeros need proximal steps or coordinate descent

</details>

**5. You augment digit images by rotating them 180 degrees. What goes wrong?**

- A. Training simply runs slower
- B. Nothing, rotations always keep labels
- C. Sixes become nines, labels go wrong

<details><summary>Answer</summary>

**C. Sixes become nines, labels go wrong**. Augment only with label-preserving transforms

</details>

## Say it in the interview

**Say it in the interview**

- What decision does the output support?
- Nobody acts on it? A science project.
- Baseline: today's process and a simple rule

**Say it in the interview**

- Exact for squared error, not zero-one
- For classifiers: intuition, not algebra
- Train versus validation, plus a learning curve

**Say it in the interview**

- The two numbers measure different things
- Dropout, epoch average, penalty, then leakage
- Minutes to check. Do it before celebrating.

**Say it in the interview**

- L1's push stays constant. L2's push fades.
- Plain gradient descent leaves tiny weights
- Coordinate descent or proximal steps give zeros

**Say it in the interview**

- Smoothing stops rewarding bigger logits
- Augmentation: the closest thing to more data
- Dropout is rarely the first lever

## Homework

- [ ] Write down who acts on one output
- [ ] Run the lab, change the threshold
- [ ] Score a training sample in eval mode
- [ ] List three label-preserving transforms
