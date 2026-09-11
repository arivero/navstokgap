# B46 bounded source companion: independent blocks and global budgets

## Result and coverage

This audit covers R15/C086 (exact retained block records and full versus aggregate records) and C087 (equal block exponent and resource-set comparison). Two discovery queries and two short primary passages were inspected. Neither inspected passage states the R15 mechanical identities, its synchronous bounded-acceleration lift, or the (r=3/2) copy-count comparison. The norm and support-function ingredients are established mathematics; the R15 formulas and resource-set distinction are derived consequences of its stated apparatus model. This is bounded coverage, not a novelty claim.

## Sources and passages

1. V. Temlyakov, “On optimal recovery in (L_2),” arXiv:2010.03103v1 (2020), https://arxiv.org/html/2010.03103v1. **Passage level:** §1 Introduction, recovery definitions through equation (1.1), HTML lines 43–55 (selected passage). It defines optimal recovery and Kolmogorov-width characteristics for centrally symmetric compact classes and records the ordering (d_m\le\varrho_m^*\le\varrho_m). The setting is function recovery from samples, with (L_p) error; it does not address Cartesian block fibres or mechanical phase coordinates.

2. V. Chandrasekaran, B. Recht, P. A. Parrilo and A. S. Willsky, “The Convex Geometry of Linear Inverse Problems,” arXiv:1012.0621v3 (2012), https://arxiv.org/html/1012.0621v3. **Passage level:** §2.1 Definition, lines 111–123 (one short subsection). For a centrally symmetric atomic set it identifies the gauge of the convex hull as a norm and its support function as the dual norm, then formulates recovery under a linear measurement map. This supports the R15 use of norm geometry and support-function language, but gives no product-fibre additivity or trajectory lift.

## Queries and limits

Query 1: `site:arxiv.org optimal recovery product spaces Cartesian uncertainty sets norm ball composition`

Query 2: `site:arxiv.org block separable uncertainty sets l^p norm robust recovery product`

Search results were discovery only. The two passages above were the selected readings; no additional query family, source download, or exhaustive search was undertaken.

## Claim matching

* C086, exact risks (Q_A=\sum_jw_jq(T,E_j)), (P_A=\sum_jn_jp(T,E_j)), and the full-record versus aggregate distinction: **derived consequence**. Temlyakov supplies a general optimal-recovery framing, while Chandrasekaran supplies convex gauge/support terminology. Neither has the bounded-force path strip, the equal-error synchronous lift, or the blockwise Cartesian support calculation. The strict aggregate momentum inequality for unequal (E_j) follows from R15's written concavity argument and is not a source match.
* C087, the equal-block factor (k a^{1-3/(2r)}), the ratio (k^{3/(2r)}), and equality at (r=\infty): **derived consequence** of the R15 normalization and saturation functions. The sources do not state this exponent or an action-valued product.
* The set comparison (\mathcal E_{\rm blocks}=\prod_j\{\|e^{(j)}\|_r\le\epsilon_j\}) versus a global (\ell^r) ball: **derived model classification**, with general norm-ball context only. The inclusion radius (B=(\sum_j\epsilon_j^r)^{1/r}) is an elementary written norm calculation; neither passage supplies it for apparatus blocks.

## Source-to-model test

Use the source norm/support viewpoint to require the next physical model to declare its uncertainty set before composing blocks. For a proposed finite-duration apparatus, compute the target support over (i) a Cartesian product of independently allowed block errors and (ii) one jointly budgeted (\ell^r) ball, while holding force, mass, record duration and estimator access fixed. A difference in support radii is a resource change, not a regrouping identity; only an explicitly supplied combining budget can justify transferring the global (r=3/2) conclusion.

No numerical or symbolic verification script was created or run.

## Coordinator corrections

Verified Temlyakov v1 metadata and §1 definitions through (1.1), and
Chandrasekaran et al. v3 §2.1, equations (2)–(3). The worker
Temlyakov line numbers pointed outside the passage in the current HTML; the
versioned section/equation anchors above replace them. Corrected the worker
C087 factor from k^(1-3/(2r)) to k a^(1-3/(2r)); the proof note
already had the correct factor. A coordinator attempt at Temlyakov v2 returned
404 before v1 was verified. No additional discovery searches were made.
