# Fine-tuning and Model Choice · Part 3 of 10: Fine-Tuning Done Right: Data to Evaluation

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Clean data for fine-tuning
2. Training hyperparameters and overfitting
3. Catastrophic forgetting
4. Distillation
5. Evaluating a fine-tuned model

## Key takeaways

- Clean, consistent data with a frozen test set.
- Stop when validation turns up. Pick by eval.
- Always measure general skills beside the task.
- Students copy teachers, mistakes included.
- Beat the prompted baseline on a frozen set.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_training_settings_for_a_lora_run.py` | Training Settings for a LoRA Run | yes |
| `code/02_lab_find_the_best_checkpoint.py` | Find the Best Checkpoint | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_find_the_best_checkpoint.py` prints:

```text
last ckpt: 300 1.9
best ckpt: 200 1.4
overfit from step 250
final gap: 1.5
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your training data has 5% wrong labels. What happens?**

- A. The model learns the wrong labels too
- B. Training averages the errors away
- C. Only the loss gets slightly higher

<details><summary>Answer</summary>

**A. The model learns the wrong labels too**. The model learns the mistakes, and evals may reward them.

</details>

**2. How should you choose the checkpoint to ship?**

- A. Take the final checkpoint
- B. Validation metric on a held-out set
- C. Pick the lowest training loss

<details><summary>Answer</summary>

**B. Validation metric on a held-out set**. Name the validation metric and the held-out set.

</details>

**3. Your fine-tune got better at triage. Is it still good at summaries?**

- A. Yes, because the task score went up
- B. Unknown unless you measured it
- C. Yes, LoRA prevents forgetting

<details><summary>Answer</summary>

**B. Unknown unless you measured it**. Measure general skills, not only the target task.

</details>

**4. Can you do logit distillation from a closed API model?**

- A. Usually not, no full distribution
- B. Yes, the API returns all logits
- C. Yes, by raising the temperature

<details><summary>Answer</summary>

**A. Usually not, no full distribution**. Closed APIs mean output-based distillation, not logits.

</details>

**5. Your fine-tune beats the base model with no prompt. Fair test?**

- A. Yes, if the test set is big
- B. Yes, it is the same model underneath
- C. No, it inflates the gain

<details><summary>Answer</summary>

**C. No, it inflates the gain**. Beat the best prompted baseline on a frozen set.

</details>

## Say it in the interview

**Clean Data: The**

- The model learns the data, mistakes included.
- Dedupe, fix labels, strip secrets, match real traffic.
- Freeze the test set first. Check for leaks.

**Hyperparameters: The**

- Small learning rate, warmup, few epochs.
- Validation turns up: stop at the best checkpoint.
- Pick checkpoints by task and regression evals.

**Forgetting: The**

- Narrow training pulls shared weights away.
- Mix data, train gently, use LoRA, eval both.
- Route only the narrow task to the fine-tune.

**Distillation: The**

- Full distribution needs an open-weights teacher.
- Filtered teacher outputs train the student.
- Check the licence. Evaluate the student held-out.

**Evaluation: The**

- Beat the best prompt on a frozen set.
- Case by case, plus safety, cost and latency.
- A tie means no ship.

## Homework

- [ ] List the clean-data steps from memory
- [ ] Rerun the lab with your own losses
- [ ] Sketch a two-column eval report
- [ ] Rehearse: which baseline, which set, frozen when
