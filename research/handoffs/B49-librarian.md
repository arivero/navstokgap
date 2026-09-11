# B49 librarian handoff

- **Task:** B49 bounded audit for R18, variational-flow/contraction methods and closest position uncertainty/backreaction precedent.
- **Role:** librarian audit; no descendants.
- **Requested model/effort:** gpt-5.6-luna, low. Effective settings were not independently reported.
- **Date:** 2026-09-11.
- **Inputs:** `notes/position-preparation-ambiguity.md`; `docs/batches/B48/fixed-preparation-source-companion.md`; `docs/batches/B47/fixed-calibration-source-companion.md`; R17 handoff; Principia-action and bibliography instructions.
- **Outputs:** `docs/batches/B49/position-preparation-source-companion.md`.

## Source coverage

Fresh search queries (exact strings) were:

1. `Hermann Krener nonlinear controllability observability canonical primary paper PDF observability rank condition`
2. `"Theorem 3.1" "If Sigma satisfies the observability rank condition" Hermann Krener`

One primary source was read at passage level: Hermann and Krener, “Nonlinear
Controllability and Observability,” IEEE TAC AC-22(5), 1977, DOI
10.1109/TAC.1977.1101601, author PDF
<https://www.math.ucdavis.edu/~krener/1-25/10.IEEETAC77.pdf>, Theorem 3.1,
Lemma 3.2 proof and surrounding text, printed p. 734 (one selected page).
The passage defines indistinguishability through flow-generated output
derivatives and proves full observability rank implies local weak
observability. The scan had no embedded text; indexed source text was used
after the author-hosted PDF retrieval. No exact novelty or exhaustive coverage
is claimed.

B48 contraction coverage and B47 Sideris smooth-flow coverage were reused as
explicitly inherited material, without fresh reading. B48's source is the
Frankfurt lecture chapter, PDF pp. 4–5; B47's source is Sideris chapter 6.1.
The B49 source companion reports the inherited scope and does not recast it as
fresh evidence. Total fresh selected pages: 1 of the allowed 4. Total web
searches: 2 of the allowed 2. Total fresh primary sources: 1 of the allowed 2.

## Findings and proof review

The direct match is a local rank-to-injectivity theorem for output-derived
observables. It supports R18's plan to differentiate the augmented record map,
but R18 must prove its mechanical rank, compact-box uniformity, and either an
inverse margin or contraction self-map. Rank failure alone does not establish
an ambiguity fibre. The closest position/backreaction evidence remains the
project's own R18 derivation: unknown positions affect final momenta at order
lambda squared, including the receiver and clock terms.

I read the full R18 draft. The proof's central construction is coherent under
its stated smooth finite-time flow, pulse-design, fixed-width, and cutoff
margin assumptions. The main point to flag is scope: the lower-triangular
response and negative diagonal calculation establish existence for the chosen
pulse design, not every admissible design; and the contraction yields a local
common-record fibre only after the uniform derivative estimate and receiver
shell chart constants are fixed. The final risk/area inequalities are
deterministic reconstruction bounds and should remain separate from disturbance
or universal action claims.

## Next bounded task

R19 should assemble the Jacobian after adding final probe positions and initial
clock phase, test full rank versus an integrated kernel on the fixed positive
position box, and quantify whichever compact margin or fibre construction the
result permits. Suggested source-to-model details are in the B49 companion.
