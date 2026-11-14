# Security and Guardrails · Part 7 of 11: Secrets, Data Policies and Guardrails

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Secrets: management, scanning and rotation
2. Power Platform and Copilot Studio DLP
3. Guardrails on both sides (input and output)
4. Content safety and toxicity classifiers
5. Prompt injection classifiers (Prompt Shields)

## Key takeaways

- Vault, scan, and rotate leaked keys
- DLP: connector combinations; Purview: content
- Input guards early; output guards judge results
- Separate classifier, per-category thresholds
- Classifiers detect; downstream gates still decide

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_scanning_a_repo_with_gitleaks.py` | Scanning a repo with gitleaks | yes |
| `code/02_guard_stand_ins.py` | Guard stand-ins | yes |
| `code/03_the_handle_function.py` | The handle function | yes |
| `code/04_setting_up_content_safety.py` | Setting up Content Safety | after `pip install azure-identity` |
| `code/05_reading_the_severity_scores.py` | Reading the severity scores | after `pip install azure-identity` |
| `code/06_lab_a_blocklist_meets_a_paraphrase.py` | A blocklist meets a paraphrase | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_a_blocklist_meets_a_paraphrase.py` prints:

```text
True | Ignore previous instruct
False | Disregard what you were 
False | What is our refund polic
Paraphrase slipped through.
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A key was committed, then deleted in the next commit. Are we fine?**

- A. Yes, if the repo is private
- B. Yes, the deletion removed it
- C. No, revoke and rotate it now

<details><summary>Answer</summary>

**C. No, revoke and rotate it now**. Rotation is the fix; history rewriting is housekeeping

</details>

**2. SharePoint and Outlook are both Business. Can a flow email a confidential file outside?**

- A. No, DLP stops data leaving
- B. Yes, unless other controls stop it
- C. Only if Outlook is Non-business

<details><summary>Answer</summary>

**B. Yes, unless other controls stop it**. DLP controls connector combinations, not content

</details>

**3. We filter every input. Is every output clean then?**

- A. Yes, if the system prompt is strict
- B. No, retrieved text skips the input filter
- C. Yes, clean input gives clean output

<details><summary>Answer</summary>

**B. No, retrieved text skips the input filter**. Output guards catch what input filters never saw

</details>

**4. Azure OpenAI has a built-in filter. Are we done with content safety?**

- A. No, check thresholds fit your domain
- B. Yes, the model judges its replies
- C. Yes, the built-in filter covers it

<details><summary>Answer</summary>

**A. No, check thresholds fit your domain**. Tune thresholds to your domain; measure wrong blocks

</details>

**5. Does an injection classifier make our app injection-proof?**

- A. No, it still misses some attacks
- B. Yes, if it checks documents too
- C. Yes, it is trained on attacks

<details><summary>Answer</summary>

**A. No, it still misses some attacks**. It reduces how often gates are tested, never replaces them

</details>

## Say it in the interview

**Secrets: the**

- No secret in code, prompts or config
- Deleting a committed key does nothing
- Rotate first, check logs, then clean history

**Data policies: the**

- DLP sits under every agent a maker builds
- New connectors default to Non-business until reviewed
- Combinations, not content: content is Purview's job

**Both sides: the**

- Both sides: each catches different failures
- Output checks judge what was actually produced
- Guardrails add to authorization, never replace it

**Content safety: the**

- A separate classifier scores every reply
- The classifier only sees the final text
- Thresholds per category, tuned on labelled traffic

**Prompt Shields: the**

- A better blocklist, on prompts and documents
- Flagged document: drop it or lower trust
- Reduces tests of the gates, never replaces them

## Homework

- [ ] Run gitleaks on one of your repos
- [ ] List input and output guards for one app
- [ ] Add two paraphrases to the blocklist lab
- [ ] Write the content safety answer in three sentences
