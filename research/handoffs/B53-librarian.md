# B53 librarian handoff

- **Task:** Audit R22 proposed C100--C101, with emphasis on local/global structural identifiability, the actual equal-energy distinct-speed pair, and positive-coupling persistence.
- **Role/model/effort:** bounded librarian; requested Luna-low (no independent worker was launched); effective model/effort not independently reported.
- **Date:** 2026-09-11.
- **Inputs:** `notes/global-clock-speed-ambiguity.md`; B51 and B52 source companions; Principia-action and bibliography skill capsules.
- **Output:** `docs/batches/B53/global-clock-source-companion.md`.

## Source route and coverage

One web query targeted primary/open identifiability literature. The selected source was Raue et al., *BMC Systems Biology* 4 (2010), PMC full text, https://pmc.ncbi.nlm.nih.gov/articles/PMC3050741/. Three passage groups were read: model setup (HTML lines 134--142), local/global definitions and Hessian ambiguity diagnostic (180--190), and application examples of small eigenvalues/large variance (244--246, 301--313). Evidence level is passage; this is not a full read or exhaustive prior-art search.

## Findings

The source precisely supports the logical distinction needed by R22: local identifiability excludes collisions only near a reference point, while global identifiability ranges over the full domain. It also gives a sensitivity/Hessian diagnostic for trade-off directions. It does not establish C100's exact Hamiltonian shell crossing, fixed eight-record equality, or C101's exact continuation under positive coupling and canonical risk product. Those remain written model results, separately from the standard IVT/implicit-function method and from any risk-product claim.

R23 idea: add final clock momentum to the output and test global injectivity/equal-record branches; persistence after the pulse could distinguish speed branches, but local rank is insufficient for the full-shell question.

## Checks and stopping

No Python or other numerical/symbolic verification was performed. Budget stopped after one query, one source, and three selected passage groups. Coordinator should verify source lines and review the R22 derivation before claim acceptance; novelty remains unassessed.
