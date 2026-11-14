# Security and Guardrails · Part 11 of 11: Privacy Laws, AI Risk, Incidents, Agent Identity

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. GDPR and India's DPDP Act
2. NIST AI RMF and ISO/IEC 42001
3. AI incident response
4. Memory poisoning
5. Agent identity

## Key takeaways

- Pseudonymised data is still personal data
- NIST structures risk; ISO 42001 certifies
- Contain, trace, fix, add an eval
- Memory informs, never authorises
- Every agent gets its own identity and owner

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_feature_flag_as_kill_switch.py` | A Feature Flag as Kill Switch | yes |
| `code/02_memory_records_with_provenance.py` | Memory Records With Provenance | yes |
| `code/03_lab_audit_an_agent_inventory.py` | Audit an Agent Inventory | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_audit_an_agent_inventory.py` prints:

```text
support-bot: ok, owner ops-team
refund-bot: orphan, disable
search-bot: expired, review
agents checked: 3
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You replaced names with IDs and kept the lookup table. Does GDPR still apply?**

- A. Only if a customer complains
- B. No, the data is anonymised
- C. Yes, it is only pseudonymised

<details><summary>Answer</summary>

**C. Yes, it is only pseudonymised**. Can you re-identify it? Then it is personal data.

</details>

**2. A vendor says: "We are NIST AI RMF certified." What is wrong?**

- A. The AI RMF is voluntary, not a certification
- B. Only government vendors can be certified
- C. Nothing, NIST audits AI vendors yearly

<details><summary>Answer</summary>

**A. The AI RMF is voluntary, not a certification**. NIST AI RMF is voluntary. ISO 42001 is certifiable.

</details>

**3. A RAG bot starts giving wrong answers. What do you check first?**

- A. Plan to retrain the model
- B. The retrieval logs and traces
- C. Switch to a bigger model

<details><summary>Answer</summary>

**B. The retrieval logs and traces**. Evidence first. Retraining is rarely the fix.

</details>

**4. "Memory only stores what the user said, so it is safe." Is that true?**

- A. Yes, if memory is encrypted
- B. No, ask who decides what gets written
- C. Yes, users cannot inject themselves

<details><summary>Answer</summary>

**B. No, ask who decides what gets written**. Ask who writes to memory, and from where

</details>

**5. Twenty agents share one app registration. One misbehaves. What is the problem?**

- A. You cannot revoke or attribute just one
- B. None, it is simpler to manage
- C. Only the token cost goes up

<details><summary>Answer</summary>

**A. You cannot revoke or attribute just one**. Shared identity: no attribution, no single revoke

</details>

## Say it in the interview

**Say It in the Interview**

- Purpose, minimise, secure, show, delete
- Processor contracts, including the model provider
- The model drafts, a human decides

**Say It in the Interview**

- Four functions map to engineering work
- Govern, Map, Measure, Manage
- They ensure someone decided and wrote it down

**Say It in the Interview**

- Protect users first: flag off, human queue
- Investigate from evidence, not memory
- Fix root cause, add it to evals

**Say It in the Interview**

- Memory is untrusted text with a long life
- Per-user scope, provenance, purge
- Inform, never authorise

**Say It in the Interview**

- The question is who owns each agent
- Own identity, owner, least privilege, expiry
- Attribution, single revoke, no orphans

## Homework

- [ ] List personal data and its purpose
- [ ] Map five controls to the four functions
- [ ] Write a one-page incident plan
- [ ] Add grants and review date to the lab
