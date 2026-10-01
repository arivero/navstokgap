# Note scores: novelty and mathematical correctness (Fable referee pass, 2026-10-02)

**Status: partial.** Batches 1--4 of 35 are scored (29 notes, all in the Yang--Mills/gauge area, alphabetical through `mass-gap-obligations-lattice`); the session stopped at its usage limit. The machine-readable record, including every referee's issue list, reported dependencies, the batch plan and the correction queue, is `research/note-scores.json`. Resume by running the remaining batches (ids 5--35 in that file's `batches` list) with the same brief, one Fable subagent at a time.

## Method

Each note was read in full by a Claude Fable 5.1 subagent that had not seen the Opus audit of [2026-10-01](../notes/corpus-audit-2026-10-01.md), under one rubric. **Novelty** (0--10) is literature novelty as far as the referee knows the literature: 0--2 textbook or internal bookkeeping, 3--5 known results in a new setting or a route closure, 6--8 a result or construction the referee does not know from the literature, 9--10 a theorem specialists would care about. **Correctness** (0--10) is correctness of what the note claims at the level it claims: 10 every claim proved as stated, 7--9 minor slips, 4--6 a real gap or overstatement affecting a stated conclusion, 0--3 a central error. A note is scored in its corrected state; honest open parts are not penalised.

**Correction rule.** Correctness at most 5, or 6 with at least one issue the referee marked major, sends the note to GPT-6 Astra (codex, medium effort) with the referee's issue list and the Opus audit comment; Astra corrects the note in place with a dated correction box, builds its PDF and commits (`Correct <slug>:` commits, Astra trailer). A fresh Fable subagent then rescores the corrected text (column "rescore").

## Corrections made so far

| Note | First C | Commit | Rescore N / C |
|:--|--:|:--|:--|
| confinement-scale-bands | 5 | 2dd68dd | 2 / 8 |
| agmon-ground-state-suppression | 6 | 0620f95 |  / corrected-awaiting-rescore |
| flow-instability-large-field | 4 | 74f10cb |  / corrected-awaiting-rescore |
| flow-jacobian-truncation-error | 6 | (see git log) |  / corrected-awaiting-rescore |
| gapped-set-critical-coupling | 5 | (see git log) |  / corrected-awaiting-rescore |
| ground-state-measure-transfer | 5 | (see git log) |  / running |

Pending in the queue (scored low, not yet corrected): large-field-action-lower-bound, large-field-entropy-count, kogut-susskind-strong-coupling-explicit, large-field-operator-inequality.

Observations from the first four batches: novelty clusters at 2--4 for the closed Hamiltonian/flow/large-field routes, which the referees read as standard techniques transplanted to the lattice Hamiltonian; the correctness distribution reproduces the Opus audit's low set almost note for note, and every correction so far raised the rescored correctness to 7 or above.

## Scores

| Note | Kind | N | C | Rescore N / C | Correction | Worst issue |
|:--|:--|--:|--:|:--|:--|:--|
| abelian-misses-the-box | synthesis | 2 | 7 |  |  | minor: Single transition and interval shape of the gapped set are not rigorous; monotonicity of the gap in g is unproved. |
| agmon-global-not-local | obstruction | 3 | 8 |  |  | minor: 'Answered in the negative' overstates: Proposition 4 of the identities note shows the comparison route fails, not that Gibbs domination is false. |
| agmon-ground-state-suppression | derivation | 3 | 6 | 3 / 9 | corrected-awaiting-rescore | major: A single relaxation path bounds the Agmon distance from above; a decay estimate needs a lower bound over all paths. Superseded by the global/local note. |
| blocking-criterion-monotone | obstruction | 2 | 8 |  |  | minor: Block Hamiltonian gap uses the closed flux loop 2C_2g^2; with open boundary links the block gap may be a single-link C_2g^2/2, making beta_block larger still. |
| blocking-step-obstruction | exploratory | 2 | 7 |  |  | minor: Plaquettes crossing a face number about 2M^2, not M^2; 6M^2 undercounts by a factor 2 unless half-attributed. Conclusion direction unaffected. |
| confinement-scale-bands | synthesis | 3 | 5 | 2 / 8 | rescored | major: Gibbsianness of a block-spin image (van Enter-Fernandez-Sokal) does not make three iterated steps with constants 'standard'; the blocked interaction is not Wilson form and re-mixing is not shown. |
| dobrushin-uniqueness-wilson | theorem | 4 | 8 |  |  | minor: Passage from Follmer covariance bound to spectral support of the transfer matrix omits support-size prefactors and the time-zero-algebra and density argument; correct in outline. |
| finiteness-half-flowed-susceptibility | derivation | 3 | 8 |  |  | minor: Continuum temporal-gauge Hamiltonian with functional derivatives is formal; only the lattice version is actually a theorem, as Proposition 3's hypotheses implicitly concede. |
| flow-before-decimation | obstruction | 1 | 7 |  |  | major: Claims a proved suppression e^{-lambda n} of n excess plaquettes; only a global excess bound survives after the global/local correction. Addendum is stale. |
| flow-conjugation-truncation | obstruction | 3 | 8 |  |  | minor: Displayed W_tKW_t^* = -Delta_{Phi^*g}+Q_t drops the first-order term; correct operator is a weighted Laplacian (metric Phi^*g, Haar measure) plus potential. |
| flow-instability-large-field | obstruction | 3 | 4 | 2 / 9 | corrected-awaiting-rescore | major: Growth rate claimed +2gB; the stated spectrum gives -omega^2 = gB - k^2 <= gB, so the full linearised flow grows like exp(gB s), half the exponent of the bound. |
| flow-jacobian-truncation-error | derivation | 3 | 6 | 2 / 9 | corrected-awaiting-rescore | major: Relative error of the conjugated kinetic operator is identified with the kernel's Gaussian tail; the operator is quadratic in DPhi_t and no operator-norm or relative-bound statement is proved. |
| flowed-bound-free-field | derivation | 2 | 9 |  |  | minor: The spectral reading and the double-commutator ratio are the same f-sum identity evaluated twice; 'share no step' overstates independence, though the arithmetic check is valid. |
| four-dimensional-composition | derivation | 3 | 7 |  |  | major: The anchored-norm and Schur-test bounds, and the derivative chain (29), are asserted with loose constants; the claim 'proves finite one-step matching' rests on them unverified. |
| four-dimensional-parallel-log | derivation | 3 | 8 |  |  | minor: Status says the 3D determinant had no independent review; the header says Fable rederived Theorem 1(a),(b). One statement is stale. |
| gapped-set-critical-coupling | derivation | 3 | 5 |  | corrected-awaiting-rescore | major: Finite-volume gap vanishing along a subsequence is equated with infinite-volume spectral data; no convergence of correlators or limit theory is established. |
| gaussian-blocking-coupling | derivation | 2 | 8 |  |  | minor: lambda_D and the 'geometric heat-time normalization' are used without definition in this note; reader must fetch the composition note. |
| ground-state-measure-transfer | derivation | 2 | 5 |  | running | major: Estimates for the isotropic Wilson measure are said to hold for |Omega|^2 verbatim, but Omega is the ground state of the a_t->0 anisotropic limit; no transfer argument. |
| kogut-susskind-strong-coupling-explicit | theorem | 4 | 6 |  | pending | major: Counts only shapes whose first plaquette contains l_0; shapes reaching l_0 later are missed. Note concedes this class is not rigorous. |
| large-field-action-lower-bound | derivation | 1 | 4 |  | pending | major: A field strength constant on a block and zero outside violates the Bianchi identity; also flow at radius l smears it by O(1), not O(a/l). Sharpness unproved. |
| large-field-entropy-count | derivation | 2 | 5 |  | pending | major: Weight bound e^{-S} e^{CN} assumes each unstable direction contributes a bounded factor; no argument, and the regions' entropy is not the saddle's mode count. |
| large-field-operator-inequality | obstruction | 3 | 6 |  | pending | major: Claims every Hamiltonian route to the energy-excess inequality loses a surface term; only one splitting is analysed, so the no-go is overstated. |
| lattice-gap-upper-bounds | theorem | 4 | 8 |  |  | minor: Scaling O(a^3 t^{-3/2}) is inconsistent with the concluded bound C hbar c/sqrt(8t); dimensional counting gives O(a t^{-1/2}). Target only, but misstated. |
| lattice-truncation-uniform | derivation | 2 | 7 |  |  | minor: C and c are never computed; the Schur-type form bound turning kernel decay into a relative operator error is only outlined. |
| lieb-robinson-kogut-susskind | theorem | 3 | 7 |  |  | major: A divergent upper bound on v does not show the lattice light cone opens faster than c; stated as a consequence. |
| low-dimensional-mass-gap | synthesis | 3 | 8 |  |  | minor: Hypotheses (V>=0 continuous on R^n) exclude the k=-1 and k=-2 special cases that are then discussed under it. |
| magnetic-energy-identities | obstruction | 3 | 8 |  |  | minor: 'Answered in the negative' overstates: Proposition 4 shows one comparison function fails; no theorem excludes every argument from the eigenvalue equation. |
| mass-gap-conditional-theorem | synthesis | 2 | 5 |  |  | major: H1 and H2 give no convergence of Schwinger functions or OS axioms; existence of the continuum theory is a separate obligation, so the completeness claim overstates. |
| mass-gap-obligations-lattice | synthesis | 2 | 8 |  |  | minor: With V = 2 sum_p (N - Re tr U_p), the bound is V <= 4N|P|, not 2N|P|; the Kato conclusion is unchanged. |

## Consequence for STATE

No research claim changes. Seven closed-route gauge notes now carry dated correction boxes (see the table); the remaining thirty-one batches, the dependence graph (`research/note-graph.md`, tooling prepared) and the catalog score fields are the next bookkeeping unit.
