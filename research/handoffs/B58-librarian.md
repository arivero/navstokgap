# B58 librarian handoff

- Task: bounded audit of the Borsuk–Ulam step in `notes/calibrated-displacement-ambiguity.md`.
- Role/date: librarian; 2026-09-12.
- Requested model/effort: Luna, low; effective model/effort not independently reported.
- Inputs: `notes/calibrated-displacement-ambiguity.md`, `references/IDEA_BRIDGES.md` (R27 card), `docs/batches/B57/energy-symmetry-source-companion.md`.
- Output: `docs/batches/B58/calibrated-displacement-source-companion.md`.

## Source and coverage

Primary university-hosted source: Arora, Ailon, Tourlakis, Princeton University,
*Lecture 13: Topological Non-Constructive Methods*,
https://www.cs.princeton.edu/courses/archive/spr05/cos598B/lec13.pdf, PDF p. 1,
Theorem 1 and lines defining `S^n` and antipodes. Passage read. One search query,
two source retrievals, and four or fewer passage/page checks were used. A
Chicago-hosted student exposition was corroborative only. No exhaustive or
broad novelty search was performed; novelty and exact prior-art status remain
unassessed.

## Finding

The source states precisely that every continuous `f:S^n -> R^n` has an
antipodal pair with equal images. Therefore R27's map `f_lambda:S^10 -> R^10`
gets an exact equal-record pair if continuity of the chart and flow record map
is available. The theorem does not support the apparatus model, energy
constraints, derivative bounds, or quantitative risk estimate. Those are
conditional model derivations. The companion flags the nonlinear-chart and
coordinate-separation points for coordinator review.

## Next bounded task

Coordinator should verify R25's uniform derivative estimates and the full-state
norm bookkeeping, then separately address whether a pair differing in both `x`
and `P` can be forced. No descendants were used; no numerical or symbolic
verification scripts were created or run.
