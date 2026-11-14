# RAG and Vector Search · Part 12 of 26: Chat RAG: Access, Turns, Refusals, Limits

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. ACL freshness as a security signal
2. Per-turn retrieval in multi-turn RAG
3. Refusal design and refusal rate in both directions
4. When not to use RAG

## Key takeaways

- ACL age is a security alert
- Rewrite, retrieve fresh, drop old chunks
- Useful refusals, two-sided rates
- RAG finds written passages, nothing else

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_page_security_when_acls_go_stale.py` | Page security when ACLs go stale | yes |
| `code/02_tiny_stand_ins_for_a_chat_turn.py` | Tiny stand-ins for a chat turn | yes |
| `code/03_one_chat_turn_retrieved_fresh.py` | One chat turn, retrieved fresh | yes |
| `code/04_a_refusal_template_and_two_rates.py` | A refusal template and two rates | yes |
| `code/05_lab_find_the_guessing_behind_a_rate.py` | Find the guessing behind a rate | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_find_the_guessing_behind_a_rate.py` prints:

```text
refusal rate: 0.17
labelled: 9 vs 3
false refusal rate: 0.11
false answer rate: 0.67
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Permissions were captured at ingestion, and access was revoked an hour ago: is the user blocked?**

- A. Yes, the model will refuse it
- B. Yes, ingestion captured the permissions
- C. It depends on the ACL refresh window

<details><summary>Answer</summary>

**C. It depends on the ACL refresh window**. Captured once is not current: name the window

</details>

**2. Each turn's chunks are appended so the model has everything: why does turn five fail?**

- A. The model ran out of output tokens
- B. Stale chunks, or no standalone rewrite
- C. Turn five needed a bigger model

<details><summary>Answer</summary>

**B. Stale chunks, or no standalone rewrite**. Rewrite each turn, retrieve fresh, drop old chunks

</details>

**3. Our refusal rate is 2%, so is answer quality high?**

- A. Unknown until both directions are reported
- B. Yes, if users rarely complain
- C. Yes, it almost always answers

<details><summary>Answer</summary>

**A. Unknown until both directions are reported**. Low refusals can mean guessing: report both

</details>

**4. Can RAG over the tickets find this quarter's main complaint themes?**

- A. No, no single passage holds the themes
- B. Yes, retrieve the top-ranked tickets
- C. Yes, with a larger top k

<details><summary>Answer</summary>

**A. No, no single passage holds the themes**. No passage holds the themes, so retrieval can't

</details>

## Say it in the interview

**Say it in the interview**

- Index freshness is a security control
- Two ages, two alerts
- State the exposure window as a number

**Say it in the interview**

- Retrieval per turn, context not cumulative
- Summary plus recent turns verbatim
- Turn one working says nothing about five

**Say it in the interview**

- Design the refusal as carefully as the answer
- A low rate is also what guessing looks like
- Report both labelled directions

**Say it in the interview**

- Not written down: a content project
- Queries, behaviour, and themes are not RAG
- RAG: what does the document say

## Homework

- [ ] Write your ACL exposure window as a number
- [ ] Write three multi-turn test cases
- [ ] Rewrite one refusal with all three parts
- [ ] Triage five questions: RAG or another tool
