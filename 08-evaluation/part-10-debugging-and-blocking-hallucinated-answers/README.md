# Evaluation · Part 10 of 11: Debugging and Blocking Hallucinated Answers

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Retrieval failure or generation failure
2. Temperature zero does not fix hallucination
3. Citation per claim
4. Verification pass

## Key takeaways

- Read the context before blaming the model
- Stable is not the same as accurate
- Every claim cites a real, checked chunk
- Draft, then verify in a separate step

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_triage_function.py` | A triage function | yes |
| `code/02_lab_stable_but_wrong_in_code.py` | Stable but wrong, in code | yes |
| `code/03_normalize_then_check.py` | Normalize, then check | yes |
| `code/04_the_citation_checker.py` | The citation checker | yes |
| `code/05_a_narrow_judge_prompt.py` | A narrow judge prompt | yes |
| `code/06_parse_the_judges_reply.py` | Parse the judge's reply | yes |
| `code/07_the_verify_loop.py` | The verify loop | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_stable_but_wrong_in_code.py` prints:

```text
temp 1.0: wrong p=0.55
temp 0.2: wrong p=0.92
stable: True
accurate: False
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your RAG bot answers with an old price. What is your first move?**

- A. Switch to a stronger model
- B. Rewrite the system prompt
- C. Read the chunks the model actually saw

<details><summary>Answer</summary>

**C. Read the chunks the model actually saw**. Check the context before blaming the model

</details>

**2. Your team set temperature to 0. Does that prevent hallucinations?**

- A. No, it can be wrong every run
- B. Yes, but only on reasoning models
- C. Yes, the output is deterministic now

<details><summary>Answer</summary>

**A. No, it can be wrong every run**. Identical every run can mean wrong every run

</details>

**3. Does an empty quote pass a plain substring check?**

- A. Yes, it is inside every chunk
- B. No, empty strings never match
- C. Only if the chunk is short

<details><summary>Answer</summary>

**A. Yes, it is inside every chunk**. Require a minimum quote length

</details>

**4. Why not let the same model double-check itself in the same prompt?**

- A. It uses too many tokens
- B. The call that invented it won't catch it
- C. Models cannot read their own output

<details><summary>Answer</summary>

**B. The call that invented it won't catch it**. Separate calls, narrow questions, code where possible

</details>

## Say it in the interview

**Say it in the interview**

- My first move is reading what was retrieved
- Missing means retrieval. Present but wrong means generation.
- The split decides which team fixes it

**Say it in the interview**

- It reduces variation, not ignorance
- Fix hallucination upstream, not with temperature
- Not guaranteed deterministic either

**Say it in the interview**

- Cite per claim, not one link at the bottom
- Real ID, verbatim quote, meaningful length
- Verbatim proves it exists, not that it supports

**Say it in the interview**

- Drafting and checking are different steps
- Code first, then one narrow call per claim
- Adds latency: use it on high-risk answers

## Homework

- [ ] Write triage and test two sample traces
- [ ] Rerun the lab with the right answer on top
- [ ] Prove an empty quote gets flagged
- [ ] Write a judge prompt for a two-chunk claim
