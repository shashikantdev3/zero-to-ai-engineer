# Agents and Tools · Part 7 of 26: Reflection, Search, Memory and Stop Rules

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Reflection and self-critique
2. Tree of thoughts
3. Agent memory: short and long, episodic and semantic
4. Stop rules: step limit, budget, loop guard

## Key takeaways

- Reflect on real signals, cap the rounds.
- Branching search: powerful, costly, rare in production.
- Keep short-term small, validate long-term writes.
- Limits in code, per run, then escalate.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_run_state.py` | The run state | yes |
| `code/02_steps_budget_poll_cap.py` | Steps, budget, poll cap | yes |
| `code/03_loop_guard_and_counting.py` | Loop guard and counting | yes |
| `code/04_wiring_before_call.py` | Wiring before_call | yes |
| `code/05_lab_watch_the_rules_fire.py` | Watch the rules fire | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_watch_the_rules_fire.py` prints:

```text
stop: repeat at step 1
done after 3 steps
stop: step limit at 4
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your agent critiques its own answer with no tests or validator. What usually happens?**

- A. It reliably fixes its own mistakes
- B. It only gets slower, never worse
- C. It often agrees with itself, or worsens

<details><summary>Answer</summary>

**C. It often agrees with itself, or worsens**. Same-model critique shares the model's errors.

</details>

**2. Do more branches in tree of thoughts always mean better answers?**

- A. No, cost and latency multiply
- B. Yes, if the search is depth first
- C. Yes, more branches always help

<details><summary>Answer</summary>

**A. No, cost and latency multiply**. Branches multiply calls and latency.

</details>

**3. Context windows are big. Why not resend the whole history every turn?**

- A. The API remembers it for you
- B. Cost grows, since history is rebilled
- C. Fine, big windows make it free

<details><summary>Answer</summary>

**B. Cost grows, since history is rebilled**. Stateless APIs rebill the history every turn.

</details>

**4. Your system prompt says: stop when you are done. Is that a stop rule?**

- A. No, limits must live in code
- B. Yes, if the prompt is firm enough
- C. Yes, the model will obey it

<details><summary>Answer</summary>

**A. No, limits must live in code**. Stop rules live in code, not the prompt.

</details>

## Say it in the interview

**Reflection in the interview**

- Feedback must be real, not imagined.
- Critique from tests, schemas, evidence checks.
- Cap the rounds, then escalate.

**Tree of thoughts in the interview**

- Reasoning as a search with backtracking.
- Good for puzzles, costly in production.
- Prefer self-consistency: sample, then vote.

**Agent memory in the interview**

- Split memory by lifetime.
- Long-term memory is data with rules.
- One bad write poisons every session.

**Stop rules in the interview**

- No stop rules means an open tab.
- Steps, budget, timeout, loop guard, poll caps.
- Per-run counters. Stop, summarise, escalate.

## Homework

- [ ] Sketch a validate and revise loop, two rounds
- [ ] Price branching three at depth four
- [ ] Sort sample memories: episodic or semantic
- [ ] Add a poll cap to the lab
