# Python · Part 18 of 25: Testing, Quality and Tooling for Python AI

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. pytest: fixtures, parametrize and monkeypatch
2. Mocking an LLM client
3. Code quality: ruff, mypy, coverage and Hypothesis
4. Packaging and environments: imports, venv, uv, pyproject.toml, lockfiles, semver
5. Debugging, profiling and logging

## Key takeaways

- Fixtures, parametrize, monkeypatch: clean and isolated
- Inject fakes; patch where the name is used
- Coverage counts lines run, not checks
- Commit the lockfile; upgrades are deploys
- Profile first; log with correlation IDs

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_parametrize_a_retry_rule.py` | parametrize a retry rule | yes |
| `code/02_a_fixture_with_monkeypatch.py` | A fixture with monkeypatch | yes |
| `code/03_a_classifier_that_retries.py` | A classifier that retries | yes |
| `code/04_testing_the_retry_path.py` | Testing the retry path | yes |
| `code/05_lab_script_a_failure_then_a_success.py` | Script a failure, then a success | yes |
| `code/06_a_property_chunking_loses_nothing.py` | A property: chunking loses nothing | yes |
| `code/07_script_entry_versus_import.py` | Script entry versus import | yes |
| `code/08_a_formatter_that_shows_the_id.py` | A formatter that shows the ID | yes |
| `code/09_extra_fields_and_memory_snapshots.py` | Extra fields and memory snapshots | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_script_a_failure_then_a_success.py` prints:

```text
reply: ok
calls: 2
args: {'prompt': 'hi'}
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A team's unit tests call the real model to be realistic, so why does their CI fail randomly and cost money?**

- A. Live model calls are random and billed
- B. pytest runs tests in random order
- C. Fixtures always leak between tests

<details><summary>Answer</summary>

**A. Live model calls are random and billed**. Mock in unit tests. Evaluate the model separately.

</details>

**2. Your module imports Client from openai, you patch openai dot Client, so why is the real client still called?**

- A. side effect must be a list
- B. Patch the name where it is used
- C. Use async mock instead of Mock

<details><summary>Answer</summary>

**B. Patch the name where it is used**. Patch where it is looked up, not defined.

</details>

**3. A team has ninety five percent coverage, so are they well tested?**

- A. Only if my pie also passes
- B. Not necessarily, lines ran but may be unchecked
- C. Yes, ninety five percent is excellent

<details><summary>Answer</summary>

**B. Not necessarily, lines ran but may be unchecked**. Coverage counts executed lines, not checks.

</details>

**4. Production broke although nobody changed code, and requirements listed unpinned names, so what happened?**

- A. The virtual environment was deleted
- B. Semver forbids minor version bumps
- C. A transitive dependency moved

<details><summary>Answer</summary>

**C. A transitive dependency moved**. Commit the lockfile.

</details>

**5. Someone added print statements and optimised a loop, so what should have come first?**

- A. Profile to find the real bottleneck
- B. Add more print statements
- C. Rewrite the loop with NumPy

<details><summary>Answer</summary>

**A. Profile to find the real bottleneck**. Profile first. Then optimise.

</details>

## Say it in the interview

**pytest in the interview**

- Fixtures give clean fakes, then clean up.
- parametrize turns a table into tests.
- Unit tests never hit a real model.

**Mocking in the interview**

- Inject the client; pass in a fake.
- Script failures, then assert the calls.
- Patch the name where it is used.

**Code quality in the interview**

- CI: ruff, mypy, pytest with coverage.
- Coverage is a floor, not a goal.
- State a property; let Hypothesis hunt.

**Packaging in the interview**

- Own venv, ranges, committed lockfile.
- Pin the model SDK on purpose.
- A dependency upgrade is a deploy.

**Debugging in the interview**

- Read tracebacks bottom up.
- Profile before you optimise.
- Correlation IDs. Never raw prompts.

## Homework

- [ ] Write a parametrize test for retry codes
- [ ] Script error then success with side_effect
- [ ] Run ruff, mypy and coverage once
- [ ] Profile one script with cProfile
