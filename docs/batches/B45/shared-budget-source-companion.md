# B45 source companion: shared-budget projection and optimal recovery

## Scope and result

This bounded audit asks whether prior literature states the exact synchronous
projection/lift for (n) identical bounded-force signals with the pointwise
(\ell^r) record ball, or the derived long-time factor

\[
 n^{1-3/(2r)}
\]

in the canonical risk product. Within two discovery queries and two selected
primary passages, no exact mechanical match was found. The norm-duality and
minimax-centre ingredients are standard optimal-recovery ideas; the mechanical
copy-count exponent remains a derived consequence of the R14 model, with
novelty unassessed.

## Sources and exact coverage

1. Mahmood Ettehad and Simon Foucart, “Instances of Computational Optimal
   Recovery: Dealing with Observation Errors,” *SIAM/ASA Journal on
   Uncertainty Quantification* 9 (2021), 1438–1456,
   DOI: 10.1137/20M1328476, https://epubs.siam.org/doi/10.1137/20M1328476.
   **Passage 1 (abstract, metadata/abstract level; publisher HTML lines
   53–72):** identifies worst-case optimal recovery from inaccurate data,
   including boundedness models, Chebyshev centres, and convex optimization.
   This supports the general minimax/centre framing, but the accessible page
   does not expose a theorem specifying a pointwise (L^r) shared record ball,
   synchronous mechanical lifts, or the R14 risks.

2. Venkat Chandrasekaran, Benjamin Recht, Pablo A. Parrilo and Alan S.
   Willsky, “The Convex Geometry of Linear Inverse Problems,” *Foundations of
   Computational Mathematics* 12 (2012), 805–849, arXiv:1012.0621,
   https://arxiv.org/html/1012.0621v3. **Worker selection 2 (Introduction and
   §2.1; passage level reported):** defines convex-hull
   induced gauges/norms and describes robust recovery from linear information
   through convex geometry, symmetry and duality. It supplies standard
   convex-norm context only; it does not contain R14's trajectory tube,
   equal-error lift, or canonical risk exponent.

## Exact queries and coverage limits

Query 1: `site:epubs.siam.org optimal recovery worst case error norm ball information operator dual norm radius`

Query 2: `site:arxiv.org optimal recovery convex symmetric uncertainty set norm duality minimax radius linear information`

The first query led to Ettehad–Foucart. The second led to the Chandrasekaran
et al. arXiv paper and related recovery literature. Search results were used
only for discovery; the two passages above were the selected readings. No
exhaustive prior-art search, source download, or novelty claim is justified.

## Findings and boundaries

The sources establish broad precedents for worst-case recovery with bounded
observation errors, convex uncertainty geometry, symmetry and norm-based
robust recovery. They do not state the exact identity that the aggregate
average record and the full-record centre projection have the same scalar
minimax risks under identical force/mass classes and the synchronous lift.
They also do not match the finite-horizon function (V(s)), the centre risks
with (E_n=\varepsilon n^{-1/r}), or the saturated product

\[
H_n^{\rm sat}=n^{1-3/(2r)}H_1^{\rm sat}.
\]

Thus norm duality is an established mathematical input, while the mechanical
exponent is a derived model result. In particular, (r=3/2) invariance is not
located as a literature theorem. The audit preserves the distinction between
full-record information and its scalar aggregate image.

## Source-to-model suggestion

Test composition by partitioning (n) constituents into blocks. Give each
block an independently stated pointwise ℓ^r-budget and compare it with one
global budget. The two experiments are equivalent only after specifying the
readout/resource rule that combines block records; otherwise regrouping changes
the norm ball and hence the effective (E_n) and exponent. This is the next
decisive check for whether the (r=3/2) invariance survives apparatus-budget
composition without silently changing preparation.

No numerical or symbolic verification script was created or run.

## Coordinator verification

Rechecked SIAM's abstract and metadata (authors, 2021, volume 9, pp. 1438–1456)
and arXiv v3's author/version header and Introduction, especially the convex
hull examples leading to norm balls. The worker's line ranges do not locate
the claimed passages in v3: its Introduction begins at HTML line 62 and §2.1
at line 111. Prefer section anchors; the worker did not pin its read version.
The two-source budget was observed, but grouping Introduction and §2.1 as a
single passage is broader than two short passage selections overall.
The norm inequality in R14 is proved directly; these sources supply contextual
precedent, not a cited proof of the mechanical projection or exponent.
