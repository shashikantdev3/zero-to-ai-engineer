# Evaluation · Part 7 of 11: Conversations, Safety Gates and Fresh Indexes

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Multi-turn and conversation evals
2. Safety and adversarial evals
3. Index freshness monitoring
4. Evaluation tooling and its currency

## Key takeaways

- Assert every turn and the final state.
- Safety cases are hard gates. One fail blocks.
- Monitor stale and orphaned docs continuously.
- Know what the metric computes. Pin versions.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_scripted_conversation_case.py` | A scripted conversation case | yes |
| `code/02_three_kinds_of_safety_case.py` | Three kinds of safety case | yes |
| `code/03_the_gate_that_blocks_release.py` | The gate that blocks release | yes |
| `code/04_finding_stale_and_orphaned_docs.py` | Finding stale and orphaned docs | yes |
| `code/05_lab_hash_compare_label.py` | Hash, compare, label | yes |
| `code/06_deepeval_style_the_setup.py` | DeepEval style: the setup | after `pip install deepeval` |
| `code/07_deepeval_style_the_test.py` | DeepEval style: the test | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_hash_compare_label.py` prints:

```text
leave -> stale, re-index
old-bonus -> orphaned, still indexed
travel -> fresh
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Our single-question golden set passes. Are conversations fine?**

- A. Yes, the golden set covers it
- B. Only if a case tests earlier turns
- C. Yes, if scores are above ninety

<details><summary>Answer</summary>

**B. Only if a case tests earlier turns**. Single-turn passes say nothing about memory.

</details>

**2. Our system prompt says to ignore injected instructions. Are we safe?**

- A. Yes, if it worked in a demo
- B. Yes, the prompt handles injection
- C. Only if injection cases gate releases

<details><summary>Answer</summary>

**C. Only if injection cases gate releases**. A prompt is a hope. A gate is evidence.

</details>

**3. A policy was deleted at the source last week. Can it still be retrieved?**

- A. Yes, unless you check for orphans
- B. No, if eval scores are high
- C. No, deleting the source removes it

<details><summary>Answer</summary>

**A. Yes, unless you check for orphans**. Check what is indexed, not just what exists.

</details>

**4. An interviewer asks how you evaluate your RAG system. What is the strongest answer?**

- A. Explain what each metric computes
- B. We use Ragas for everything
- C. List every tool you have tried

<details><summary>Answer</summary>

**A. Explain what each metric computes**. Explain the method, then name the tool.

</details>

## Say it in the interview

**Multi-turn evals in an interview**

- Single-turn evals miss how agents fail.
- Check every turn, then the final state.
- History is resent, so track tokens.

**Safety evals in an interview**

- Safety evals are hard gates, not averages.
- Injection cases, tenant canaries, P I I checks.
- One in five is still a working attack.

**Index freshness in an interview**

- Evals tested what was indexed, not current.
- Freshness is a monitor, not a test.
- The dangerous failures raise no errors.

**Eval tooling in an interview**

- Eval tools are convenience, not the method.
- Pin versions. Check docs, not memory.
- Did my system change, or the judge?

## Homework

- [ ] Write a three-turn case with an early constraint.
- [ ] Write one injection, canary, and PII case.
- [ ] Rerun the lab after deleting a source doc.
- [ ] Write what one tool's faithfulness computes.
