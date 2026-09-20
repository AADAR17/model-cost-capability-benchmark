# Rubric v1 — Code Review Quality Scoring

## Approach
Reuse PR-Agent's own native structured output fields rather than inventing a
rubric from scratch — the tool already encodes a severity philosophy in its
`/review` prompt ("be thorough on clear bugs/security, be certain before
flagging lower-severity concerns"). Config to enable these fields:
`config/pr_agent_overrides.toml` (this repo).

## Primary severity signal (per PR, per model)
- **`risk_level`**: `low | medium | high` — PR-Agent's own overall risk rating
- **`merge_recommendation`**: `safe_to_merge | merge_with_caution | changes_required`

## Category mapping (used to segment results, not asked of the model directly)
Every curated PR is pre-tagged into one of 5 categories (see `data/curated_prs/README.md`):
Bug/Correctness, Security, Performance, Design/Feature, Maintainability.

## Scoring dimensions
1. **`risk_level` match** — does the model's risk_level agree with what the real PR
   turned out to need (e.g. a Security-category PR should trigger medium/high)?
2. **`merge_recommendation` match** — same logic against the real outcome.
3. **Issue-catch rate** — did the model's individual review comments surface the
   same problem(s) the real human reviewer raised (ground truth, stored per-PR)?
4. **Critical-miss rate** (guardrail metric) — specifically for Security/Bug-
   correctness PRs: did the model fail to flag something the real reviewer
   caught? Reported explicitly, never folded into an average.

## LLM-as-judge
A separate model call scores each of the 4 reviewer-models' output against:
(a) the rubric above, and (b) the real human review comments stored in each
`data/curated_prs/PR-XX.md` file.

## Human calibration
~20% of the 26 PRs (≈5) get hand-scored by the project owner before trusting
the judge on the rest. Agreement % is the headline calibration number.

## Status
- [x] Approach decided and documented
- [x] Config override written (`config/pr_agent_overrides.toml`)
- [x] Ground truth (real review comments) exists for all 26 PRs
- [ ] Judge prompt itself — written in Phase 2, once the harness runs
- [ ] Calibration sample selected and hand-scored — Phase 2
