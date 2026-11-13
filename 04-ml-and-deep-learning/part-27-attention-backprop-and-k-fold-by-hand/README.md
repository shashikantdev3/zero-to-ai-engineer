# Machine Learning and Deep Learning · Part 27 of 28: Attention, Backprop and k-fold by Hand

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Masked attention from scratch
2. Two-layer network backprop by hand
3. k-fold indices from scratch
4. Overfit one batch
5. Question drill: ML coding

## Key takeaways

- Mask before softmax. First row equals V[0].
- Gate the ReLU gradient on saved z1.
- Shuffle once, array_split, validate every row once.
- Can it memorise ten? Only then tune.
- Answer, then the reason. Every time.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_attention_function.py` | The attention function | yes |
| `code/02_check_the_first_row.py` | Check the first row | yes |
| `code/03_one_training_step_by_hand.py` | One training step by hand | yes |
| `code/04_run_it_then_go_leaky.py` | Run it, then go leaky | yes |
| `code/05_k_fold_index_generator.py` | k-fold index generator | yes |
| `code/06_lab_prove_every_row_is_validated.py` | Prove every row is validated | yes |
| `code/07_a_tiny_model_to_debug.py` | A tiny model to debug | yes |
| `code/08_overfit_ten_examples.py` | Overfit ten examples | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_prove_every_row_is_validated.py` prints:

```text
7 4 set()
7 4 set()
8 3 set()
True
n // k slicing keeps 9
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You zero masked weights after the softmax. What breaks?**

- A. The rows no longer sum to one
- B. The scores overflow to infinity
- C. Nothing, the result is identical

<details><summary>Answer</summary>

**A. The rows no longer sum to one**. Mask before the softmax, never after.

</details>

**2. Why does gating the ReLU gradient on a1 usually go unnoticed?**

- A. The bias gradient cancels it
- B. Plain ReLU gives the same mask
- C. Autograd fixes it automatically

<details><summary>Answer</summary>

**B. Plain ReLU gives the same mask**. Gate on z1. Leaky ReLU and GELU need it.

</details>

**3. With n = 11 and k = 3, what does n // k slicing do?**

- A. Two rows are never validated
- B. It raises an error
- C. The last fold gets the extra rows

<details><summary>Answer</summary>

**A. Two rows are never validated**. Use array_split. Every row must be validated.

</details>

**4. Your model runs but does not learn. What do you try first?**

- A. Sweep the learning rate
- B. Add more regularisation
- C. Overfit about ten examples

<details><summary>Answer</summary>

**C. Overfit about ten examples**. Prove the code can learn before you tune.

</details>

**5. Should you apply L2 regularisation to the bias term?**

- A. Yes, like every other weight
- B. No, it carries the base rate
- C. Only when classes are balanced

<details><summary>Answer</summary>

**B. No, it carries the base rate**. Regularise the weights, not the bias.

</details>

## Say it in the interview

**Masked attention, in one breath**

- Scores, mask, stable softmax, then times V.
- Mask before softmax. Big negative, not minus infinity.
- First output row equals the first row of V.

**Backprop by hand, in one breath**

- Gate the ReLU derivative on z1.
- Leaky ReLU and GELU need z1's value.
- State the convention. Check with finite differences.

**k-fold, in one breath**

- Shuffle once, seeded. array_split handles remainders.
- Each row validated once, never trains itself.
- Stratify, forward-chain, fit transforms inside the fold.

**Debugging, in one breath**

- First, overfit one batch of ten.
- Cannot overfit means bug. Stop tuning.
- Shapes, softmax, zero_grad, labels. Rate last.

## Homework

- [ ] Write masked attention and assert the first row.
- [ ] Gradient-check the two-layer step with finite differences.
- [ ] Run k-fold with 11 rows and 4 folds.
- [ ] Overfit ten examples in one of your scripts.
