# Agents and Tools · Part 9 of 26: Finishing, Context, Failures and Workflow Patterns

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Explicit completion check: escalate, do not truncate
2. Context management on long runs: compaction, tool-result clearing, memory tool
3. Long-context failure modes: poisoning, distraction, confusion, clash
4. Five workflow patterns

## Key takeaways

- Code checks done; limits escalate, never truncate
- Clear, then compact; write memory first
- Poisoning, distraction, confusion, clash: four fixes
- Simplest workflow pattern that works

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_completion_rule_and_a_stopped_run.py` | A completion rule and a stopped run | yes |
| `code/02_the_finish_function.py` | The finish function | yes |
| `code/03_clearing_old_tool_results.py` | Clearing old tool results | yes |
| `code/04_write_to_memory_then_compact.py` | Write to memory, then compact | yes |
| `code/05_lab_overwrite_keys_and_append_keys.py` | Overwrite keys and append keys | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_overwrite_keys_and_append_keys.py` prints:

```text
disk is full []
bad config []
bad config ['config diff']
bad config ['config diff']
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The step limit fires at step 8 and the model says DONE. What does the user get?**

- A. An incomplete status, escalated with context
- B. The partial answer, marked complete
- C. A silent retry from step one

<details><summary>Answer</summary>

**A. An incomplete status, escalated with context**. A partial answer dressed as finished is worse than an error

</details>

**2. After compaction, where is the exact error code from step 3?**

- A. Possibly lost, unless saved to memory first
- B. Safe, summaries keep every detail
- C. Safe, compaction is free headroom

<details><summary>Answer</summary>

**A. Possibly lost, unless saved to memory first**. Compaction is lossy. Write to memory before compacting.

</details>

**3. Does a bigger context window fix a poisoned fact?**

- A. Yes, more room dilutes the bad fact
- B. No, it just keeps it longer
- C. Yes, if the window doubles

<details><summary>Answer</summary>

**B. No, it just keeps it longer**. A bigger window keeps poison longer

</details>

**4. In a design round, what should you say after naming the pattern?**

- A. Which agent framework you prefer
- B. That everything is a ReAct agent
- C. Why the simpler pattern was not enough

<details><summary>Answer</summary>

**C. Why the simpler pattern was not enough**. Name the pattern, justify it over the simpler one

</details>

## Say it in the interview

**Completion, in your own words**

- The model alone does not decide it finished
- Code checks schema and verified evidence
- Limit fires: mark incomplete, escalate with trace

**Context management, in your words**

- Clear old tool results first: cheap, re-fetchable
- Write to memory before you compact
- Store facts, not inferences, keyed by tenant

**Failure modes, in your words**

- Name the failure; each has its own fix
- Verify, summarise, narrow, replace
- Naming the mode turns complaint into diagnosis

**Workflow patterns, in your words**

- Workflows versus agents: five named patterns
- First three: path in code, testable
- Name it, justify it, stop

## Homework

- [ ] Write a finish check that escalates on limit
- [ ] Type clear_old and test which message clears
- [ ] Run the state lab; add a third hypothesis
- [ ] Label one agent bug by failure mode
