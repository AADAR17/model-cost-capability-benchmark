# Curated PR Dataset

25-40 real, merged Pull Requests (target was met at 26), each spread across
5 categories, used as the test cases for the code-review model benchmark.

Each `PR-XX.md` file contains: repo, PR number, category, title, author,
status, the real diff, and the real human review comments (our ground truth).

## Fidelity note (applies to every file in this folder)

Pulled via web fetch through an intermediate summarization layer — raw
GitHub API and `.diff` endpoints are blocked in this session (repo-scoping
and egress policy, respectively). Every PR was individually verified: real
repo, real PR number, real title, real author, real merge status, and at
least one real quoted review comment. Diffs are high-confidence but not a
byte-exact guarantee, especially for larger/more complex PRs — flagged
per-file where a diff is large enough that summarization risk is higher.

## Index

| ID | Category | Repo | PR # | Title |
|---|---|---|---|---|
| PR-01 | Bug/Correctness | pandas-dev/pandas | 34473 | fix to_json for numbers larger than sys.maxsize |
| PR-02 | Bug/Correctness | pandas-dev/pandas | 34875 | DF.__setitem__ creates extension column when given extension scalar |
| PR-03 | Bug/Correctness | pandas-dev/pandas | 21235 | pct change bug issue 21200 - #21235 |
| PR-04 | Bug/Correctness | pandas-dev/pandas | 10265 | BUG: Ensure 'coerce' actually coerces datatypes |
| PR-05 | Bug/Correctness | pandas-dev/pandas | 19849 | BUG: names on union and intersection for Index were inconsistent (GH9943 GH9862) |
| PR-06 | Bug/Correctness | pandas-dev/pandas | 23539 | BUG/REF: TimedeltaIndex.__new__ |
| PR-07 | Security | django/django | 21506 | Refs #36560, CVE-2026-35193 -- Recognized qualified cache-control directives |
| PR-08 | Security | django/django | 21145 | Fixed #37053 -- Added validate=True to base64.b64decode() calls |
| PR-09 | Security | django/django | 19525 | Refs CVE-2025-48432 -- Ensured log_response is used anywhere a response is logged |
| PR-10 | Performance | redis/redis | 15618 | Improve batch mutation performance of hash template keys |
| PR-11 | Performance | redis/redis | 15397 | Improve RESTORE REPLACE performance for new keys |
| PR-12 | Performance | redis/redis | 15699 | Fix SETBIT and BITFIELD string growth accounting |
| PR-13 | Performance | redis/redis | 15695 | Honor selective propagation for effect commands queued via alsoPropagate() |
| PR-14 | Performance | redis/redis | 15545 | Fix signed overflow in BITFIELD i64 checks |
| PR-15 | Performance | redis/redis | 15519 | Improve hash template test coverage and refactor RDB save/load |
| PR-16 | Design/Feature | scikit-learn/scikit-learn | 26120 | FEA add TunedThresholdClassifier meta-estimator to post-tune the cut-off threshold |
| PR-17 | Design/Feature | scikit-learn/scikit-learn | 33354 | FEA Categorical split support for DecisionTree*, and RandomForest* |
| PR-18 | Design/Feature | scikit-learn/scikit-learn | 4294 | [MRG+1] Make cross-validators data independent + Reorganize grid_search, cross_validation and learning_curve into model_selection |
| PR-19 | Design/Feature | numpy/numpy | 8247 | ENH: Add __array_ufunc__ |
| PR-20 | Design/Feature | numpy/numpy | 16935 | ENH: implement NEP-35's like= argument |
| PR-21 | Design/Feature | numpy/numpy | 9998 | ENH: Nditer as context manager |
| PR-22 | Maintainability | microsoft/vscode | 116856 | Remove editorOpenWith |
| PR-23 | Maintainability | microsoft/vscode | 35528 | Make WorkbenchActionRegistry just a forwarder |
| PR-24 | Maintainability | microsoft/vscode | 80050 | chore: update tsc target |
| PR-25 | Maintainability | microsoft/vscode | 53487 | Remove PPromise |
| PR-26 | Maintainability | microsoft/vscode | 321168 | Voice Mode: migrate from vendored libs to VS Code patterns |
