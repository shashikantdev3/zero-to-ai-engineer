# Evaluation · Part 2 of 11: Honest Test Data and the Right Graders

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Synthetic evaluation data
2. Held-out set and overfitting to the eval
3. Benchmark contamination and public leaderboards
4. Three kinds of grader: code, model, human

## Key takeaways

- Synthetic data is cold-start scaffolding
- Tune on dev, decide on grouped held-out
- Leaderboards shortlist; your golden set decides
- Code first, judges for fuzz, humans calibrate

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_prompt_that_writes_test_cases.py` | A prompt that writes test cases | yes |
| `code/02_grouped_split_with_scikit_learn.py` | Grouped split with scikit-learn | yes |
| `code/03_lab_see_a_leaky_split.py` | See a leaky split | yes |
| `code/04_a_code_grader_for_a_total.py` | A code grader for a total | yes |
| `code/05_the_grader_has_its_own_tests.py` | The grader has its own tests | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_see_a_leaky_split.py` prints:

```text
case split leaks: 6
group split leaks: 0
held-out sizes: 6 6
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your synthetic set scores 95% but users complain. Why?**

- A. The eval set has too many cases
- B. The model needs more training data
- C. Generated questions reuse the documents' wording

<details><summary>Answer</summary>

**C. Generated questions reuse the documents' wording**. Synthetic questions echo the source; real users do not

</details>

**2. Your prompt scores 100% on the set you tuned it on. Ready?**

- A. No, that set became training data
- B. Yes, if the set is large enough
- C. Yes, a perfect score proves it

<details><summary>Answer</summary>

**A. No, that set became training data**. A set you tuned on is training data

</details>

**3. The top leaderboard model costs 10x more. What do you do?**

- A. Pick the cheapest model on the list
- B. Test shortlisted models on your golden set
- C. Pick it, the ranking proves quality

<details><summary>Answer</summary>

**B. Test shortlisted models on your golden set**. Prove extra quality matters on your traffic

</details>

**4. Should an LLM judge check whether output is valid JSON?**

- A. No, a code check does it reliably
- B. Yes, because code graders can be wrong
- C. Yes, a judge catches more errors

<details><summary>Answer</summary>

**A. No, a code check does it reliably**. Exact rules go to code, and code gets tests

</details>

## Say it in the interview

**Synthetic data in the interview**

- Synthetic data fixes cold start.
- Add paraphrases, unanswerable cases, human review.
- Never let synthetic alone gate a release.

**Held-out sets in the interview**

- A tuned-on set is training data.
- Split by conversation and time, not randomly.
- Trust held-out, then confirm with a rollout.

**Leaderboards in the interview**

- Leaderboards are a shortlist, not a decision.
- Cheapest model whose worst run clears the bar.
- Lowest cost per resolved task wins.

**Graders in the interview**

- Cheapest reliable grader for each check.
- Trust a judge only after human checks.
- Humans label samples and disagreements.

## Homework

- [ ] Write a generation prompt for one chunk
- [ ] Add a paraphrase and an unanswerable question
- [ ] Rerun the lab with other held-out threads
- [ ] Write a code grader with three tests
