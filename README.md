# verify-ai-reviews-fixture

The two-commit diff used to compare a wrapper agent with a plain agent that calls a review CLI.
The second commit carries one planted defect; `ground-truth.md` names it and is kept out of the fixture repository that `make-fixture.sh` builds.

- `fixture/commit-1/`, `fixture/commit-2/`: the files of each commit.
- `make-fixture.sh <empty dir>`: builds the two-commit git repository from them (one copy per trial). Build copies outside this checkout, so a reviewer working in a copy cannot walk up to `ground-truth.md`.
- `ground-truth.md`: the answer, fixed before any trial.
