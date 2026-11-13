# Prompting · Part 6 of 10: Chains, Reasoning, Memory and Caching

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Prompt chaining
2. Reasoning models and reasoning effort
3. Conversation memory and compaction
4. Prompt caching

## Key takeaways

- Chain small steps, gate them in code
- Goals not steps, effort per task
- Compact safely; summary is untrusted data
- Stable first; cached tokens still fill window

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_one_helper_for_every_call.py` | One helper for every call | yes |
| `code/02_extract_check_then_draft.py` | Extract, check, then draft | yes |
| `code/03_setting_effort_on_a_routine_task.py` | Setting effort on a routine task | yes |
| `code/04_cut_only_on_a_clean_turn.py` | Cut only on a clean turn | yes |
| `code/05_compact_at_a_threshold.py` | Compact at a threshold | yes |
| `code/06_lab_watch_a_naive_cut_go_wrong.py` | Watch a naive cut go wrong | yes |
| `code/07_marking_a_cache_breakpoint.py` | Marking a cache breakpoint | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_watch_a_naive_cut_go_wrong.py` prints:

```text
naive cut starts at: result
naive keeps: result a u a
safe cut starts at: u
kept: u call result a u a
summarised: 2 turns
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does a prompt chain always beat a single prompt?**

- A. Yes, smaller prompts are always better
- B. Yes, as long as one model runs it
- C. No, it adds calls and latency

<details><summary>Answer</summary>

**C. No, it adds calls and latency**. Chain only where evals show one prompt failing

</details>

**2. Should you always use the highest reasoning effort?**

- A. Yes, hidden reasoning tokens are free
- B. No, match effort to the task
- C. Yes, it always gives better answers

<details><summary>Answer</summary>

**B. No, match effort to the task**. Match effort to the task, check cost per ticket

</details>

**3. Where should a conversation summary go?**

- A. In a fenced untrusted block in history
- B. In the system prompt, so it's respected
- C. Nowhere, keep the full history instead

<details><summary>Answer</summary>

**A. In a fenced untrusted block in history**. The summary is data, never system instructions

</details>

**4. With prompt caching, are long chats basically free?**

- A. No, cached tokens still fill the window
- B. Yes, cached tokens cost nothing
- C. Yes, if the system prompt never changes

<details><summary>Answer</summary>

**A. No, cached tokens still fill the window**. Caching discounts tokens; you still compact

</details>

## Say it in the interview

**Say it in the interview**

- One prompt, three jobs? Split it.
- Validate between steps, cheap models for easy ones
- Fixed steps: a workflow, not an agent

**Say it in the interview**

- Goal, constraints, format. Not step by step.
- Cost per resolved task, not just accuracy
- On Azure, check deployment and API version

**Say it in the interview**

- History grows every turn, so I compact
- Cut on turn boundaries, keep tool pairs
- Summary untrusted, decisions stored as facts

**Say it in the interview**

- Stable content first, variable content last
- Writes cost extra; edits invalidate what follows
- Cached tokens still fill the window

## Homework

- [ ] Split one multi-job prompt into a chain
- [ ] Rerun the lab with keep equal to two
- [ ] Reorder a prompt: stable content first
- [ ] List three facts to store by code
