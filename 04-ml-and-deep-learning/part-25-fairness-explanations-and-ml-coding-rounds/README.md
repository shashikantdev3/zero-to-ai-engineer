# Machine Learning and Deep Learning · Part 25 of 28: Fairness, Explanations and ML Coding Rounds

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Fairness impossibility results
2. Fairness through unawareness
3. LIME and the limits of SHAP
4. Question drill: Experiments and responsible ML
5. How to run an ML coding round

## Key takeaways

- Choose a fairness definition and document why
- Proxies survive; measure per group
- Ablate and re-evaluate, do not trust attributions
- No peeking; chi-square for sample ratios
- Shapes, simple version, then optimise

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_error_rates_per_group.py` | Error rates per group | yes |
| `code/02_lab_does_postcode_leak_the_group.py` | Does postcode leak the group? | yes |
| `code/03_set_up_a_suspect_feature.py` | Set up a suspect feature | yes |
| `code/04_ablate_and_re_evaluate.py` | Ablate and re-evaluate | yes |
| `code/05_shapes_stated_before_the_maths.py` | Shapes stated before the maths | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_does_postcode_leak_the_group.py` prints:

```text
majority guess: 0.56
postcode guess: 0.89
proxy present: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Base rates differ by group. Can a model be fair on every metric?**

- A. Yes, with enough tuning
- B. Yes, if the model is calibrated
- C. Only with perfect prediction

<details><summary>Answer</summary>

**C. Only with perfect prediction**. Different base rates force a trade-off

</details>

**2. "We don't use gender, so the model can't discriminate." What do you ask?**

- A. Is the model accurate overall?
- B. Can other features predict gender?
- C. Is gender stored securely?

<details><summary>Answer</summary>

**B. Can other features predict gender?**. Ask whether other features predict the attribute

</details>

**3. SHAP gives a sensitive feature no weight. Does that prove the model is fair?**

- A. No, SHAP can be fooled
- B. Yes, SHAP is mathematically exact
- C. Yes, if LIME agrees

<details><summary>Answer</summary>

**A. No, SHAP can be fooled**. Explanations are not proof; test directly

</details>

**4. A test planned 50/50 shows a 48/52 split. Is that a sample ratio mismatch?**

- A. No, 48/52 is close enough
- B. Depends on sample size; run chi-square
- C. Yes, any gap is a mismatch

<details><summary>Answer</summary>

**B. Depends on sample size; run chi-square**. Test it with chi-square, not by eye

</details>

**5. You coded silently and broadcasting fails at the end. What went wrong first?**

- A. You never stated the shapes
- B. You chose NumPy over loops
- C. You did not optimise early

<details><summary>Answer</summary>

**A. You never stated the shapes**. State shapes as you write

</details>

## Say it in the interview

**Fairness is a documented choice**

- Fairness is a choice to document
- Which error costs whom more?
- A biased label is a measurement problem

**Unawareness hides bias**

- Other features act as proxies
- Keep it to measure, measure per group
- Limit what the model can do

**Explain, then verify**

- LIME is fast; SHAP is principled
- Both can be fooled
- Change the feature, re-evaluate directly

**Open the round like this**

- Pin the shapes first
- Show you know what is inside

## Homework

- [ ] Compute TPR and FPR per group
- [ ] Rerun the proxy lab with new data
- [ ] Ablate one feature, compare scores
- [ ] Annotate shapes in a NumPy function
