# Machine Learning and Deep Learning · Part 13 of 28: p-values, Power, and the Curse of Dimensionality

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. p-values and confidence intervals
2. Type I and Type II errors, and statistical power
3. Curse of dimensionality
4. Question drill: Probability and statistics

## Key takeaways

- p is P(data|null); CIs describe the procedure
- Plan power first; low power means unknown
- Many dimensions blur distance; reduce or embed
- Check the conditioning and the base rate

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_welchs_t_test_on_latency.py` | Welch's t-test on latency | yes |
| `code/02_lab_watch_intervals_catch_the_true_mean.py` | Watch intervals catch the true mean | yes |
| `code/03_sample_size_before_the_experiment.py` | Sample size before the experiment | yes |
| `code/04_watch_the_distance_ratio_climb.py` | Watch the distance ratio climb | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_watch_intervals_catch_the_true_mean.py` prints:

```text
true mean: 50
intervals built: 1000
contain the truth: 945
coverage: 0.945
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. p = 0.04. Does that mean we are 96% sure it works?**

- A. No, the conditioning is flipped
- B. Yes, one minus p is certainty
- C. Only if the sample is large

<details><summary>Answer</summary>

**A. No, the conditioning is flipped**. p is P(data given null), never P(it works)

</details>

**2. The A/B test was not significant. Is there no effect?**

- A. Yes, if p is above 0.5
- B. Not necessarily, check its power
- C. Yes, no significance means no effect

<details><summary>Answer</summary>

**B. Not necessarily, check its power**. Not significant with low power means unknown

</details>

**3. You add 500 columns and k-NN gets worse. Why?**

- A. A bug, since more features always help
- B. k-NN needs more training epochs
- C. Distances become nearly equal

<details><summary>Answer</summary>

**C. Distances become nearly equal**. Extra raw features blur every distance

</details>

**4. A 99% accurate test for a 1-in-10,000 disease is positive. Chance you have it?**

- A. About 1 in 102
- B. About 99 percent
- C. About 50 percent

<details><summary>Answer</summary>

**A. About 1 in 102**. Rare disease: false positives swamp true ones

</details>

## Say it in the interview

**p-values, said well**

- How surprising the data is, if no effect
- Confidence is about the procedure, not this interval
- Always report the effect size

**Errors and power, said well**

- Teams track Type I, ignore Type II
- Compute sample size first, power usually 80%
- Stopped early? We do not know yet.

**The curse, said well**

- Everything is about equally far apart
- Fewer features, PCA, or learned embeddings
- Training made the distances meaningful

## Homework

- [ ] Define a p-value in one correct sentence
- [ ] Rerun the coverage lab with another seed
- [ ] Power code: try a 10% to 12% lift
- [ ] Record the distance ratio per dimension
