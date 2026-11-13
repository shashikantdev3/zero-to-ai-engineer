# Machine Learning and Deep Learning · Part 1 of 28: Learning Types, Data Splits, Baselines, Bias

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Supervised, unsupervised and reinforcement learning
2. Train, validation and test split
3. Baseline model
4. Bias and variance

## Key takeaways

- Labels, structure, rewards. Pretraining: self-supervised.
- Split by time, gap, matured labels only
- Beat the baseline. Accuracy lies on rare classes.
- Both high: bias. Big gap: variance.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_drop_unripe_rows_set_the_cut_offs.py` | Drop unripe rows, set the cut-offs | yes |
| `code/02_slice_the_three_sets.py` | Slice the three sets | yes |
| `code/03_only_for_data_with_no_time_order.py` | Only for data with no time order | yes |
| `code/04_a_dummy_classifier_as_baseline.py` | A dummy classifier as baseline | yes |
| `code/05_lab_the_97_percent_trap.py` | The 97 percent trap | yes |
| `code/06_a_learning_curve_in_time_order.py` | A learning curve, in time order | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_the_97_percent_trap.py` prints:

```text
rows: 100
accuracy: 0.97
caught: 0 of 3
recall: 0.0
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. LLM pretraining has no human labels. So where do its labels come from?**

- A. It needs no labels at all
- B. Humans tag every sentence
- C. The next token is the label

<details><summary>Answer</summary>

**C. The next token is the label**. Pretraining is self-supervised: the next token is the label

</details>

**2. Your newest month of data looks almost fraud-free. Why?**

- A. Fraud really dropped that month
- B. Its chargebacks have not arrived yet
- C. The model blocked all the fraud

<details><summary>Answer</summary>

**B. Its chargebacks have not arrived yet**. Immature labels look legit until the chargeback arrives

</details>

**3. Your model scores 0.85 AUC. Is that good?**

- A. Cannot say without baseline and cost
- B. No, it needs at least 0.95
- C. Yes, anything above 0.8 is good

<details><summary>Answer</summary>

**A. Cannot say without baseline and cost**. No baseline, no verdict

</details>

**4. Train and validation both score 0.6. Will doubling the data help?**

- A. Probably not much, it is bias
- B. Yes, this is a variance problem
- C. Yes, more data fixes any error

<details><summary>Answer</summary>

**A. Probably not much, it is bias**. More data helps variance, not bias

</details>

## Say it in the interview

**Three ways to learn, in an interview**

- Supervised has labels. Unsupervised finds structure.
- LLMs: self-supervised, supervised, then RLHF
- The hard part is trustworthy labels

**Data splits, in an interview**

- Train fits, validation tunes, test reports once
- Split by date, with a maturity gap
- Only use rows with matured labels

**Baselines, in an interview**

- Dumbest predictor, simple rule, logistic regression
- Cannot clearly beat it? Keep it simple.
- First question: compared to what?

**Bias and variance, in an interview**

- Bias: too simple. Variance: memorises noise.
- Diagnose from train versus validation error
- Trust the validation curve over theory

## Homework

- [ ] Label three problems by learning type
- [ ] Run the lab with a new fraud rate
- [ ] Write a time split with a gap
- [ ] Explain bias and variance in two sentences
