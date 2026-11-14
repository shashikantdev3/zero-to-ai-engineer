# Security and Guardrails · Part 5 of 11: Architectural Defences Against Prompt Injection

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Instruction hierarchy
2. Dual-LLM and quarantined-LLM patterns
3. Human approval gates and signed approvals
4. Permission-trimmed retrieval

## Key takeaways

- Hierarchy lowers risk; code gates catch the rest.
- The tool-holding model never sees untrusted text.
- Signed, plan-bound, one-time, expiring human approval.
- Filter inside search; default deny; watch ACL lag.

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_quarantined_call.py` | The quarantined call | with your API key |
| `code/02_fill_the_value_at_execution.py` | Fill the value at execution | with your API key |
| `code/03_lab_track_where_every_value_came_from.py` | Track where every value came from | yes |
| `code/04_canonical_bytes_and_known_keys.py` | Canonical bytes and known keys | yes |
| `code/05_the_checks_before_the_signature.py` | The checks before the signature | yes |
| `code/06_verify_then_mark_as_used.py` | Verify, then mark as used | yes |
| `code/07_sign_once_try_three_times.py` | Sign once, try three times | yes |
| `code/08_a_server_built_security_filter.py` | A server-built security filter | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_track_where_every_value_came_from.py` prints:

```text
show: Lunch Friday
1: BLOCKED
2: BLOCKED
3: sent to me@home.example
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A new model follows the instruction hierarchy well. Can you drop the code gates?**

- A. No, it lowers risk, not to zero
- B. Yes, if the system prompt says so
- C. Yes, the model now ignores tool text

<details><summary>Answer</summary>

**A. No, it lowers risk, not to zero**. The hierarchy helps; the code gate still decides.

</details>

**2. Your system has a generator model and a reviewer model. Is that the dual-LLM pattern?**

- A. Yes, any two models count
- B. Yes, if the reviewer is stronger
- C. Only if the tool model never sees untrusted text

<details><summary>Answer</summary>

**C. Only if the tool model never sees untrusted text**. Ask: does the model with tools see untrusted text?

</details>

**3. Who should approve an irreversible step that an agent planned?**

- A. A reviewer agent with a strict prompt
- B. A named human, signature bound to the plan
- C. The person who requested the change

<details><summary>Answer</summary>

**B. A named human, signature bound to the plan**. Reviewers read the same injection. Humans sign, once.

</details>

**4. You search everything, then drop chunks the user cannot see. What can go wrong?**

- A. All top ten hidden, user gets nothing
- B. Search becomes much slower
- C. The model sees too many tokens

<details><summary>Answer</summary>

**A. All top ten hidden, user gets nothing**. Filter inside the search, not after ranking.

</details>

## Say it in the interview

**Instruction hierarchy in an interview**

- System outranks user; tool output ranks lowest.
- Untrusted text never goes in the system message.
- Learned behaviour, not a guarantee.

**Dual LLM in an interview**

- Planner has tools, never sees raw content.
- Quarantined model reads, has no tools.
- Use it where the risk justifies the loss.

**Approval gates in an interview**

- A reviewer model is not a gate.
- Signed, bound to the plan, used once.
- Fewer, deduplicated incidents fight rubber-stamping.

**Trimmed retrieval in an interview**

- You cannot ask a model to keep a secret.
- Server-built filter, default deny, pre-filter.
- Monitor ACL lag like index freshness.

## Homework

- [ ] Check tool results never enter the system message
- [ ] Mark which model sees untrusted text
- [ ] Edit one plan field; watch approval fail
- [ ] Write one default-deny search filter
