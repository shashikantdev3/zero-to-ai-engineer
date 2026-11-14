# Security and Guardrails · Part 10 of 11: Erasure, Audit Logs, Residency, EU AI Act

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Retention and the right to erasure
2. Audit logs and tamper evidence
3. Data residency
4. EU AI Act

## Key takeaways

- Tag derived data, delete it as a pipeline
- Hash chain detects, anchor and storage protect
- Confirm the source, then pin everything in region
- Classify the use case before anything else

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_erase_pipeline_in_miniature.py` | An Erase Pipeline in Miniature | yes |
| `code/02_hashing_one_log_entry.py` | Hashing One Log Entry | yes |
| `code/03_appending_to_the_chain.py` | Appending to the Chain | yes |
| `code/04_verifying_the_chain.py` | Verifying the Chain | yes |
| `code/05_lab_catch_a_rewrite_with_an_anchor.py` | Catch a Rewrite With an Anchor | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_catch_a_rewrite_with_an_anchor.py` prints:

```text
anchor: 4a3ceb4fbd3d
before edit: True
rewritten: 4ef4d9841037
after edit: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A user asks to be erased. You deleted their source file. Are you done?**

- A. Only after the next backup cycle
- B. No, derived copies still exist
- C. Yes, the source file is gone

<details><summary>Answer</summary>

**B. No, derived copies still exist**. Erasure must reach every derived record

</details>

**2. An insider rewrites the chain from the edited entry onward. Does verify catch it?**

- A. Never, so hash chains are useless
- B. Yes, hashes cannot be recomputed
- C. Only if the latest hash is anchored

<details><summary>Answer</summary>

**C. Only if the latest hash is anchored**. Verify alone passes a full rewrite, anchor it

</details>

**3. Your VNet is in West Europe. Are you compliant with EU residency?**

- A. Not yet, check inference and traces
- B. Yes, the network is in the EU
- C. Only if users log in from EU

<details><summary>Answer</summary>

**A. Not yet, check inference and traces**. Residency covers inference and traces too

</details>

**4. Does GDPR require EU personal data to be stored in the EU?**

- A. No, it controls transfers outside
- B. Only for health and payment data
- C. Yes, storage must stay in the EU

<details><summary>Answer</summary>

**A. No, it controls transfers outside**. GDPR restricts transfers, it does not mandate storage

</details>

**5. An Indian team builds a claims assistant for an EU insurer. Can the EU AI Act apply?**

- A. Only if the team moves to the EU
- B. Yes, if the system is used in the EU
- C. No, it only covers EU companies

<details><summary>Answer</summary>

**B. Yes, if the system is used in the EU**. Use in the EU matters, not where you are based

</details>

## Say it in the interview

**Say It in the Interview**

- Data spreads, so retention is easy to forget
- Every derived record carries its source ID
- Short defaults, plus check the provider

**Say It in the Interview**

- Who asked, what it saw, decided, approved
- Hash chain plus an external anchor
- Detection needs append-only storage beside it

**Say It in the Interview**

- Residency follows the data subject
- Confirm where the requirement comes from
- Pin everything, including backups and telemetry

**Say It in the Interview**

- Banned, high-risk, and transparency tiers
- Classify first, then disclose
- Check current dates with legal

## Homework

- [ ] Map where one document's data lands
- [ ] Build and break the hash chain lab
- [ ] List where traces and backups live
- [ ] Classify one use case under the AI Act
