"""Zero to AI Engineer · Prompting · Part 4 of 10
Slide: Five Runs, Mean and Worst
Run: python 03_five_runs_mean_and_worst.py
"""
# Note: this is a fragment from the slide. It uses names that are set up elsewhere (for example a model client),
# so on its own it stops with NameError.
# golden_set: redacted real tickets
for case in golden_set:
    runs = [
        score(run_prompt(case.input))
        for _ in range(5)
    ]
    report(
        case.id,
        mean=sum(runs) / 5,
        worst=min(runs),
    )
