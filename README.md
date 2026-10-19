# Week 1 Summary: Python Programming and Git Foundations

**Name:** Shaqayeq Salimy | **Cohort:** TRNG-2493 | **Tag:** `week1-complete`

## What this repo contains

| Day | Program / folder | What it does | Python topics used | Git skill practised |
|---|---|---|---|---|
| Mon | `week1/monday/` | Formats test identifiers and calculates test summaries | Variables, types, input/output, f-strings | init, add, commit, log |
| Tue | `week1/tuesday/` | Contains Tuesday's control-flow exercises | Conditions and loops | push, pull, pull requests |
| Wed | `week1/Wednesday/` | Organizes test data, removes duplicates and summarizes results | Lists, dictionaries, sets, collections | Branches and merging |
| Thu | `week1/thursday/` | Contains reusable test utilities | Functions, lambdas, decorators | Consolidating completed work |
| Fri | `week1/friday/` | Validates test results and generates text and CSV reports | Classes, properties, classmethods, staticmethods, inheritance | Summary branch, pull request and annotated tag |

## How to run the Friday program

Requires Python 3.8 or later. From the repository root:

```bash
python week1/friday/check_exercise.py
python week1/friday/run_report.py
```

On systems using `python3`, replace `python` with `python3`.

The checker should report `24/24 checks passed`.
The driver prints three rejected inputs, text and CSV reports,
a pass rate of 50.0%, and `Results created: 4`.

The class diagram is in `week1/friday/docs/class-diagram.mermaid`.

## What I learned this week

- Python: I practised organizing code into functions and classes.
  In Friday's program, property setters validate status and duration
  before storing them.
- Git: I practised making focused commits and developing on feature
  branches. I also learned how to consolidate daily projects into one
  repository and use a pull request to review changes.
- Testing mindset: Invalid IDs, misspelled statuses and negative durations
  should be rejected before they affect report totals.

## What was hardest, and what I would do differently

Understanding how the base reporter's `line_count()` calls a subclass's
`render()` was challenging. Next time, I would trace a small example
before implementing the full hierarchy.

## My commit history, honestly

- A clear commit message:
  `Add TestResult with validation and alternative constructors`
- A vague earlier message and a clearer replacement:
  `Create thursday` → `Add Thursday project folder placeholder`
- I kept the original history rather than rewriting earlier commits.

## Next steps

- Practise properties, classmethods and polymorphism with smaller examples.