# Prompting · Part 7 of 10: Treating Prompts Like Production Code

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Prompt templates
2. Version prompts
3. Prompt regression testing
4. Prompt portability
5. Behaviour, not facts (prompt vs RAG vs fine-tune)

## Key takeaways

- Templates: values in, literal braces doubled.
- A prompt change is a deploy.
- Case by case. Critical breaks block.
- A model upgrade is a prompt change.
- Facts in retrieval, behaviour in weights.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_template_text.py` | The Template Text | after `pip install langchain_core` |
| `code/02_filling_the_template_safely.py` | Filling the Template Safely | no: ModuleNotFoundError, see the note in the file |
| `code/03_a_versioned_prompt_record.py` | A Versioned Prompt Record | yes |
| `code/04_blocking_a_critical_regression.py` | Blocking a Critical Regression | no: a message, see the note in the file |
| `code/05_lab_average_up_release_blocked.py` | Average Up, Release Blocked | yes |
| `code/06_prompt_and_model_one_release.py` | Prompt and Model, One Release | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_average_up_release_blocked.py` prints:

```text
old passes: 2
new passes: 3
regressions: ['outage']
blocked: ['outage']
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. You add a JSON example to your template and it throws KeyError. Why?**

- A. The model rejected the JSON
- B. The documents were too long
- C. The JSON braces were not doubled

<details><summary>Answer</summary>

**C. The JSON braces were not doubled**. Double literal braces in templates.

</details>

**2. Your team edits the live prompt in a web portal when needed. What's the risk?**

- A. Portal edits are slower than Git
- B. Production changes with no review or eval
- C. None, small edits are always safe

<details><summary>Answer</summary>

**B. Production changes with no review or eval**. A prompt change is a deploy.

</details>

**3. The average score went up, but one critical case now fails. Ship it?**

- A. Yes, and fix it next sprint
- B. No, block until that case passes
- C. Yes, the average improved

<details><summary>Answer</summary>

**B. No, block until that case passes**. Always ask: did anything get worse?

</details>

**4. A newer version of the same model family ships. Will your prompt still work?**

- A. Not reliably, rerun the golden set
- B. Only if the price stays the same
- C. Yes, same family means same behaviour

<details><summary>Answer</summary>

**A. Not reliably, rerun the golden set**. Same family is not same behaviour.

</details>

**5. Should you fine-tune on your policy PDFs so the model knows your policies?**

- A. No, put the policies in retrieval
- B. Yes, then it will know them
- C. Yes, but with a bigger model

<details><summary>Answer</summary>

**A. No, put the policies in retrieval**. Facts in retrieval, behaviour in weights.

</details>

## Say it in the interview

**Say It: Prompt Templates**

- Templates in files, filled from validated inputs.
- Double literal braces. Pass content as values.
- Reviewable in pull requests, loggable by version.

**Say It: Versioned Prompts**

- A prompt change is a deploy.
- Log versions per request. Roll back by pointer.

**Say It: Regression Testing**

- Compare case by case, not by average.
- Past failures join the set. Critical breaks block.

**Say It: Prompt Portability**

- A model upgrade is a prompt change.
- Pin both. Rerun the golden set per case.

**Say It: Prompt, RAG, Fine-Tune**

- Facts in retrieval, behaviour in weights.
- Fine-tune only after evals show a ceiling.
- Fine-tuning has real costs.

## Homework

- [ ] Move one prompt into a template file.
- [ ] Trigger the KeyError, then double the braces.
- [ ] Write five golden cases, mark critical ones.
- [ ] Pin model and prompt version together.
