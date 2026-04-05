# Evolve Research Loop — [YOUR PROJECT NAME]

You are running an automated evolve-research loop. Each loop iteration is one experiment. The goal: through repeated experimentation, evolve the project until [YOUR GOAL HERE].

---

## Before Each Loop — Read the Log

1. **Read `progress.md`** (if it exists).
   - Understand what was changed in prior loops.
   - Review results and quality notes from previous runs.
   - Identify what worked, what failed, and what to try next.
   - If progress.md doesn't exist yet, this is loop 1 — start fresh.

---

## Loop Steps

### Step 1 — Plan the Experiment

Based on progress.md (or fresh start), decide what to test this iteration:
- [DESCRIBE WHAT VARIABLES YOU WANT TO EXPERIMENT WITH]
- [DESCRIBE WHAT FILES/CONFIGS TO CHANGE]
- Any hypothesis about what will improve the results

Write down your experiment plan before making changes.

### Step 2 — Make Changes

Based on your experiment plan, make targeted edits to:
- [LIST YOUR PROJECT'S KEY FILES TO EDIT]
- [LIST CONFIG FILES, PROMPTS, SETTINGS, ETC.]

Keep changes focused and trackable. Don't rewrite everything at once — iterate.

### Step 3 — Run the Test

[DESCRIBE HOW TO RUN YOUR PROJECT'S TEST/BUILD/PROCESS]

```bash
# Example:
# python my_script.py
# npm run build
# pytest tests/
```

Wait for it to complete.

### Step 4 — Evaluate the Output

[DESCRIBE HOW TO CHECK IF THE RESULTS ARE GOOD]

- Read output files, logs, generated artifacts
- Check for errors, quality issues, regressions
- Compare to previous loop results

Rate the output on:
- **Quality**: X/10 — [what "quality" means for your project]
- **Correctness**: X/10 — [does it work as expected?]
- **Improvement**: X/10 — [is it better than last loop?]
- **Overall**: X/10

### Step 5 — Log Results in progress.md

Append to `progress.md` (create if it doesn't exist):

```markdown
## Loop N — [Date/Time]

### Experiment
- **What was tested**: [description]
- **Hypothesis**: [what you were trying to improve]

### Changes Made
- [List every change made]

### Results
- **Quality**: X/10 — [notes]
- **Correctness**: X/10 — [notes]
- **Improvement**: X/10 — [notes]
- **Overall**: X/10 — [notes]

### Key Observations
- [What worked well]
- [What failed or was weak]

### Next Loop Plan
- [What to try next based on these results]
```

---

## Key Files Reference

| File | Purpose |
|---|---|
| `task.md` | This file — loop instructions |
| `progress.md` | Experiment log — read before each loop, write after each loop |
| [ADD YOUR PROJECT FILES HERE] | [PURPOSE] |

## Evolution Strategy

1. **Early loops**: Explore different approaches, understand baseline, identify weak areas
2. **Mid loops**: Target the weakest areas with focused improvements
3. **Later loops**: Fine-tune for polish and edge cases
4. **Goal**: [YOUR END-STATE GOAL]
