# Evaluation · Part 4 of 11: Evaluation as a Release Gate

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. CI gate (evaluation as a release gate)
2. Versioning prompts, datasets and graders together
3. Online signals
4. Offline, shadow mode and A/B testing

## Key takeaways

- Every change runs the gate; regressions block merges
- Every score carries all its versions
- Behaviour beats thumbs; slice by workflow
- Offline, shadow, canary, then everyone

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_gate_decision_in_python.py` | The gate decision in Python | yes |
| `code/02_a_run_record.py` | A run record | yes |
| `code/03_lab_spot_what_changed_between_runs.py` | Spot what changed between runs | yes |
| `code/04_one_traces_signals.py` | One trace's signals | yes |
| `code/05_shadow_mode_the_setup.py` | Shadow mode: the setup | yes |
| `code/06_shadow_mode_the_handler.py` | Shadow mode: the handler | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_spot_what_changed_between_runs.py` prints:

```text
prompt same
model same
judge CHANGED
Judge changed: rescore baseline
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your gate failed three PRs this week that changed only a README. Most likely cause?**

- A. The README edit changed the prompt
- B. The golden set is too large
- C. Threshold set at the baseline score

<details><summary>Answer</summary>

**C. Threshold set at the baseline score**. Set bars below the lower confidence bound

</details>

**2. Your workflow has a path filter. Someone edits only the judge prompt. Does the gate run?**

- A. Only if the filter covers evals and graders
- B. Yes, every edit always triggers it
- C. No, a judge prompt is not code

<details><summary>Answer</summary>

**A. Only if the filter covers evals and graders**. Path filters must cover eval data and graders

</details>

**3. This week's score from a new judge is lower than last month's from the old judge. What do you conclude?**

- A. Quality dropped, roll back the release
- B. Nothing yet, rescore the baseline first
- C. The new judge is broken

<details><summary>Answer</summary>

**B. Nothing yet, rescore the baseline first**. New judge? Rescore the baseline before comparing

</details>

**4. Users give thumbs up 90 percent of the time. What should you ask first?**

- A. Which model earned the thumbs?
- B. What fraction of users vote at all?
- C. Can we push it to 95 percent?

<details><summary>Answer</summary>

**B. What fraction of users vote at all?**. Ask who votes before trusting thumbs

</details>

**5. Your shadow agent just closed real tickets. What went wrong?**

- A. Its write tools were live, not recorders
- B. The A/B slice was too large
- C. The timeout was too short

<details><summary>Answer</summary>

**A. Its write tools were live, not recorders**. In shadow, stub every write tool

</details>

## Say it in the interview

**Say it in the interview**

- A prompt change is a deploy
- Required check: fails on drops or critical breaks
- Pinned model in reviewed config, no console swaps

**Say it in the interview**

- A score without versions is meaningless
- Pin the model, store every ID
- Changed judge? Rescore the baseline first

**Say it in the interview**

- Offline is the past, online is today
- Escalation rate first, then behaviour signals
- Slice by workflow; low signals feed golden set

**Say it in the interview**

- Offline pass does not earn full rollout
- Shadow on sampled traffic, compare everything
- Small slice, rollback triggers, stubbed write tools

## Homework

- [ ] Write a gate returning 0, 1 or 2
- [ ] Draft a run record with every version ID
- [ ] List three behavioural signals for your app
- [ ] Draw the rollout stages and stub points
