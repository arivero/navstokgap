# P02: verified calculations for A08, A09 and G01

- **Task:** P02, independent verification and extension of the six proposed
  directions after the P01 review.
- **Role/model/effort:** interactive Claude Fable 5.1 session acting as an
  independent calculator; no subagents, no ultra effort, no external services
  beyond metadata web search.
- **Date:** 2026-09-08.
- **Inputs:** `reviews/six-directions-2026-09-08.md`, `references/batches/B15.md`,
  `notes/telegraph-return-bridge.md`, `papers/classical-action-field.tex`,
  `claims/LEDGER.md` C018–C034.
- **Outputs:** `notes/composition-crossover-gap-checks.md`,
  `scripts/six_direction_checks.py`, `out/six-direction-checks.json`,
  `scripts/telegraph_bridge_midpoint_sampler.py`, `formal/Crossover.lean`,
  Makefile entry, this handoff, one TASKS row and one STATE pointer.

## Findings

1. Composition holds inside the A01 chain class: the centre-of-mass velocity
   of two independent reversible chains is a reversible chain, and its C019
   plateau is the mass-weighted mean of the constituents'. Relative coordinate,
   sum rule, three-body Jacobi convexity and the review's cross covariance are
   verified. The A02 bath coefficient violates the composition premise by
   $2m_am_bs^2/[\nu(m_a+m_b)]$.
2. The C033 bridge midpoint has variance coefficient $H_*z^3/6+O(z^5)$ at
   small $z=\lambda T$ and plateau $H_*$; the $k=1$ moments are exact and an
   exact sampler confirms the curve. Position-only conditioning gives a
   quadratic onset instead. The stationary bound $\mathsf h\le H_*\Delta/\Delta_*$
   is saturated at leading order.
3. The C019 product bounds, the two-state equality and the review's slow-mode
   countertest are verified; the hidden label closes the gap to $2\epsilon$
   and leaves $H_*$ unchanged.
4. Both continuation routes to the Klein–Gordon form agree symbolically.
5. Kac 1974 is open access on Project Euclid; Sokal 1997 carries the
   autocorrelation inequality. Both are metadata-level leads.

## Checks and limits

`python3 scripts/six_direction_checks.py` passes 28 symbolic checks and is part
of `make check`. The sampler table uses seed 2026 with 200000 samples per row.
`formal/Crossover.lean` is uncompiled: Lean and Lake are absent on this machine.
No claim IDs were assigned and no accepted document was changed. Reference
metadata for the 1984 papers matched B15; the Caianiello attribution is from
memory and unverified.

## Next bounded task

A08 as defined in `research/ACTION_FIELD_TARGET.md`, using section 1 of the
note as the derivation draft and the bath countertest as the preparation
countermodel. A09 can start from the exact $k=1$ moments and extend the
expansion to the $k=2$ component.
