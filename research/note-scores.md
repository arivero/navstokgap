# Note scores: novelty and mathematical correctness (Fable referee pass, 2026-10-02)

**Status: partial, resumable.** 92 of 178 notes are scored (batches 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 of 35; the gauge area is complete, the Newton area is in progress); the session stopped at its usage limit. The machine-readable record, with every referee's issue list, reported dependencies, the batch plan and the correction queue, is `research/note-scores.json`. Resume by running the remaining batches with the same brief, one Fable subagent at a time, and the pending corrections with Opus 5.5 (user direction 2026-10-02: Opus at maximal effort whenever codex is out of quota).

## Method

Each note was read in full by a Claude Fable 5.1 subagent under one rubric, blind to the Opus audit of [2026-10-01](../notes/corpus-audit-2026-10-01.md) and to the codex assessment of the same day. **Novelty** (0--10) is literature novelty as far as the referee knows the literature: 0--2 textbook or internal bookkeeping, 3--5 known results in a new setting or a route closure, 6--8 a result or construction the referee does not know from the literature, 9--10 a theorem specialists would care about. **Correctness** (0--10) is correctness of what the note claims at the level it claims: 10 every claim proved as stated, 7--9 minor slips, 4--6 a real gap or overstatement affecting a stated conclusion, 0--3 a central error. A note is scored in its corrected state; honest open parts are not penalised. Three collections (refinement-results, halving-atlas, planck-gap-paper) restate earlier results; their novelty is read as what they add beyond the restated notes.

**Correction rule.** Correctness at most 5, or 6 with at least one issue the referee marked major, sends the note to a correction worker (GPT-6 Astra through codex at medium effort while its quota lasted, Claude Opus 5.5 afterwards) with the referee's issue list and the Opus audit comment; the worker corrects the note in place with a dated correction box, builds its PDF and commits (`Correct <slug>:` commits). A fresh Fable subagent then rescores the corrected text (column "rescore N / C").

## Corrections made

| Note | First C | Worker | Commit | Rescore N / C |
|:--|--:|:--|:--|:--|
| confinement-scale-bands | 5 | codex | 2dd68dd | 2 / 8 |
| agmon-ground-state-suppression | 6 | codex | 0620f95 | 3 / 9 |
| flow-instability-large-field | 4 | codex | 74f10cb | 2 / 9 |
| flow-jacobian-truncation-error | 6 | codex | (git log) | 2 / 9 |
| gapped-set-critical-coupling | 5 | codex | 08e78f7 | 2 / 9 |
| ground-state-measure-transfer | 5 | codex | 845757f | 2 / 9 |
| large-field-action-lower-bound | 4 | codex | 89004a5 | 1 / 9 |
| large-field-entropy-count | 5 | codex | c8b84b0 | 1 / 9 |
| kogut-susskind-strong-coupling-explicit | 6 | codex | dd152d1 | 3 / 8 |
| mass-gap-conditional-theorem | 5 | opus | 74d88a8 | 3 / 8 |
| mass-gap-position | 5 | opus | fca4a9d | 3 / 7 |
| schur-error-ultraviolet | 6 | opus | (git log) | running |
| strong-coupling-target-box | 3 | opus | 04ffc5e | 3 / 8 |
| wilson-strong-coupling-explicit | 6 | opus | 0869f8b | 4 / 8 |
| action-floor-yang-mills-gap | 5 | opus | 9431058 | corrected-awaiting-rescore |

Pending (scored low, not yet corrected): large-field-operator-inequality, mass-gap-openings.

**Status changes that the corrections forced.** The explicit volume-uniform Kogut--Susskind threshold $g^2\ge388$ was withdrawn (its anchored adjacent-shape count misses histories reaching the test link later; a second referee endorsed the withdrawal), and the Wilson polymer threshold was rederived with the sup-norm activity and the exact Kotecký--Preiss criterion, giving $g^2\ge1059$ with $176$ a leading-activity figure only; result T2 now rests on the Wilson transfer matrix alone (LLM.md row T2 and trap 17, the position, Dobrushin and conditional-theorem notes and both catalogs were propagated in commits d86e86b and 88644ba). The strong-coupling target box became existential (04ffc5e). The conditional theorem's H1/H2 were restated so that its conclusion follows, with an explicit existence hypothesis (74d88a8). The action-floor note's $d=4$ row now keeps $1/g_{\rm cl}^2$ as the classical action unit (9431058; ledger row C132 aligned).

Follow-ups recorded by the workers, not yet applied: (1) wilson-strong-coupling-explicit: 1056 threshold linearizes e^{6/g^2}-1; exact criterion g^2>=1059 (found by Opus while correcting mass-gap-position); title still says 176 (2) mass-gap-position now contradicts: mass-gap-obligations-lattice §4, mass-gap-openings §1, lattice-truncation-uniform lead, large-field-operator-inequality lead and §6, su3-constants §5 (3) mass-gap-position's 'one box' description of H2 understates the restated hypothesis (fix-conditional-theorem, 74d88a8) (4) dobrushin-uniqueness-wilson: its claim that the polymer rate exceeds the Dobrushin rate wherever both apply holds only for g^2 >~ 1.42e3 (fix-wilson) (5) mass-gap-openings (queued): also cites the withdrawn KS 388 and old 1056; brief must carry 1059/withdrawn (6) B79 source batch: page citation "p. 3" and missing J. Funct. Anal. 53 (1983) source for Simon (fix-action-floor)

## Comparison with the codex assessment and the Opus audit

A codex assessment of 2026-10-01 (`/tmp/navstokgap-note-scores-2026-10-01/`, novelty column handwritten, correctness largely inherited from the Opus audit) and the Opus audit's own correctness column are the two external references. On the notes scored by both, novelty agrees within one point for most; the larger differences are where the codex pass rated maps and route closures at 1 and the Fable referee at 3. Correctness differences are mostly notes corrected tonight (the large-field pair went from 4 to 9 after correction). The full three-way table is produced by `compare.py` in the scoring scratchpad and will be added when the pass completes.

## Scores

| Note | Kind | N | C | Rescore N / C | Correction | Worst issue |
|:--|:--|--:|--:|:--|:--|:--|
| abelian-misses-the-box | synthesis | 2 | 7 |  |  | minor: Single transition and interval shape of the gapped set are not rigorous; monotonicity of the gap in g is unproved. |
| action-floor-yang-mills-gap | derivation | 4 | 5 |  | corrected-awaiting-rescore | major: Hypothesis lists 1/g^2 but d=4 proof omits it; 1/g^2 has action dimension in d=4, so an action unit exists trivially. 'No constant at all' is wrong. |
| action-scale-dilation | obstruction | 2 | 9 |  |  | minor: Momentum is unchanged under the map; phrase reads as if momentum scales. Typo-level. |
| action-scale-obstructions | synthesis | 2 | 8 |  |  | minor: K = m_0 u_0^2/lambda_0 holds only as the long-window limit of the displacement coefficient; the window limit is not stated here. |
| action-unit-dimensional-selection | synthesis | 3 | 9 |  |  | minor: Invariant-function step invokes Buckingham without stating the regularity or group-action hypothesis under which g/Pi factors through dimensionless products. |
| additive-noise-marks | theorem | 4 | 9 |  |  | minor: Ozawa's condition is [y,D]=[N,p]=0 only; the note's hypothesis (N,D,X full apparatus operators) is a strict subclass. Identification overstated. |
| agmon-global-not-local | obstruction | 3 | 8 |  |  | minor: 'Answered in the negative' overstates: Proposition 4 of the identities note shows the comparison route fails, not that Gibbs domination is false. |
| agmon-ground-state-suppression | derivation | 3 | 6 | 3 / 9 | rescored | major: A single relaxation path bounds the Agmon distance from above; a decay estimate needs a lower bound over all paths. Superseded by the global/local note. |
| blocking-criterion-monotone | obstruction | 2 | 8 |  |  | minor: Block Hamiltonian gap uses the closed flux loop 2C_2g^2; with open boundary links the block gap may be a single-link C_2g^2/2, making beta_block larger still. |
| blocking-step-obstruction | exploratory | 2 | 7 |  |  | minor: Plaquettes crossing a face number about 2M^2, not M^2; 6M^2 undercounts by a factor 2 unless half-attributed. Conclusion direction unaffected. |
| bound-orbit-action-observable | derivation | 2 | 10 |  |  | minor: Invariance stated only for the selected plane and linear maps; honestly flagged, no general canonical invariance claimed. |
| bounded-acceleration-return | theorem | 2 | 10 |  |  | minor: Speed ceiling |v| <= u is imposed but plays no role in the bound; could be dropped or flagged as inactive. |
| causal-force-information | derivation | 2 | 10 |  |  | minor: Relativistic speed remark (F l/m < c) sits beside nonrelativistic dynamics; harmless but mixed. |
| classical-orientation-closure | obstruction | 2 | 9 |  |  | minor: The 'successively for every component' step (unit marginal forces factorisation of the measure) is asserted, not written out. |
| closed-orbit-force-action | theorem | 3 | 10 |  |  | minor: Canonical equals mechanical momentum assumed (scalar potential); vector-potential case correctly excluded but the force ceiling is then on dp/dt, not on the Lorentz force. |
| composition-universality | theorem | 3 | 8 |  |  | minor: Composition premise (whole-body coefficient equals centre coefficient of independent parts) is the entire physical content; theorem is near-tautological once assumed. |
| confinement-scale-bands | synthesis | 3 | 5 | 2 / 8 | rescored | major: Gibbsianness of a block-spin image (van Enter-Fernandez-Sokal) does not make three iterated steps with constants 'standard'; the blocked interaction is not Wilson form and re-mixing is not shown. |
| cut-measure-newton | theorem | 5 | 9 |  |  | minor: Calls D a diffusion constant while using it as a variance rate; the note itself distinguishes the two in §5b. |
| dobrushin-uniqueness-wilson | theorem | 4 | 8 |  |  | minor: Passage from Follmer covariance bound to spectral support of the transfer matrix omits support-size prefactors and the time-zero-algebra and density argument; correct in outline. |
| energy-depot-action-selection | derivation | 3 | 9 |  |  | minor: Gain on both quadratures breaks x-dot = p/m; acknowledged, but the model is then not a mechanical oscillator with a force law. |
| finite-horizon-minimax | theorem | 4 | 9 |  |  | minor: Reduction of minimax risk to the largest deviation hidden by the zero record is imported from R11 without restating the symmetry argument. |
| finiteness-half-flowed-susceptibility | derivation | 3 | 8 |  |  | minor: Continuum temporal-gauge Hamiltonian with functional derivatives is formal; only the lattice version is actually a theorem, as Proposition 3's hypotheses implicitly concede. |
| fixed-force-small-circles | obstruction | 2 | 9 |  |  | minor: Stability is only radial at fixed angular momentum (strict minimum of U_ell); stated, but 'stable circular orbits' in the lead reads stronger. |
| flow-before-decimation | obstruction | 1 | 7 |  |  | major: Claims a proved suppression e^{-lambda n} of n excess plaquettes; only a global excess bound survives after the global/local correction. Addendum is stale. |
| flow-conjugation-truncation | obstruction | 3 | 8 |  |  | minor: Displayed W_tKW_t^* = -Delta_{Phi^*g}+Q_t drops the first-order term; correct operator is a weighted Laplacian (metric Phi^*g, Haar measure) plus potential. |
| flow-instability-large-field | obstruction | 3 | 4 | 2 / 9 | rescored | major: Growth rate claimed +2gB; the stated spectrum gives -omega^2 = gB - k^2 <= gB, so the full linearised flow grows like exp(gB s), half the exponent of the bound. |
| flow-jacobian-truncation-error | derivation | 3 | 6 | 2 / 9 | rescored | major: Relative error of the conjugated kinetic operator is identified with the kernel's Gaussian tail; the operator is quadratic in DPhi_t and no operator-norm or relative-bound statement is proved. |
| flowed-bound-free-field | derivation | 2 | 9 |  |  | minor: The spectral reading and the double-commutator ratio are the same f-sum identity evaluated twice; 'share no step' overstates independence, though the arithmetic check is valid. |
| four-dimensional-composition | derivation | 3 | 7 |  |  | major: The anchored-norm and Schur-test bounds, and the derivative chain (29), are asserted with loose constants; the claim 'proves finite one-step matching' rests on them unverified. |
| four-dimensional-parallel-log | derivation | 3 | 8 |  |  | minor: Status says the 3D determinant had no independent review; the header says Fable rederived Theorem 1(a),(b). One statement is stale. |
| galileo-two-path-interference | theorem | 4 | 9 |  |  | minor: Non-commuting limits (12) hold only for relative averaging of 1/epsilon; absolute averaging gives commuting limits, as the post-review paragraph admits. The theorem's physical content is prescription-dependent. |
| gapped-set-critical-coupling | derivation | 3 | 5 | 2 / 9 | rescored | major: Finite-volume gap vanishing along a subsequence is equated with infinite-volume spectral data; no convergence of correlators or limit theory is established. |
| gaussian-blocking-coupling | derivation | 2 | 8 |  |  | minor: lambda_D and the 'geometric heat-time normalization' are used without definition in this note; reader must fetch the composition note. |
| ground-state-measure-transfer | derivation | 2 | 5 | 2 / 9 | rescored | major: Estimates for the isotropic Wilson measure are said to hold for |Omega|^2 verbatim, but Omega is the ground state of the a_t->0 anisotropic limit; no transfer argument. |
| hamiltonian-finite-closure | obstruction | 2 | 9 |  |  | minor: Precession formula and sign convention taken from hamiltonian-moment-descent without re-derivation; immaterial to the independence argument. |
| hamiltonian-moment-descent | obstruction | 2 | 10 |  |  | minor: Relation to B70 (the reconstruction theorem) is argued at the level of premises only; the cited theorem's exact hypotheses are not restated. |
| i003-double-limit-rigidity | exploratory | 2 | 8 |  |  | minor: Candidate theorem is unproved; obligations (pointwise continuity, matrix logarithm, generator differentiability) are named but no partial result is given. |
| indistinguishable-phase-bound | theorem | 3 | 9 |  |  | minor: Upper bound P*, Q* is imported from two-position-recovery; verified consistent here, but the note does not restate it. |
| intermediate-region-finite-verification | synthesis | 4 | 7 |  |  | minor: DS 1987 and MO 1994 hypotheses (finite vs compact spin space, cube vs torus geometry) not checked for SU(3) Haar links; gap uniformity on spatial tori asserted. |
| kogut-susskind-strong-coupling-explicit | theorem | 4 | 6 | 3 / 8 | rescored | major: Counts only shapes whose first plaquette contains l_0; shapes reaching l_0 later are missed. Note concedes this class is not rigorous. |
| large-field-action-lower-bound | derivation | 1 | 4 | 1 / 9 | rescored | major: A field strength constant on a block and zero outside violates the Bianchi identity; also flow at radius l smears it by O(1), not O(a/l). Sharpness unproved. |
| large-field-entropy-count | derivation | 2 | 5 | 1 / 9 | rescored | major: Weight bound e^{-S} e^{CN} assumes each unstable direction contributes a bounded factor; no argument, and the regions' entropy is not the saddle's mode count. |
| large-field-operator-inequality | obstruction | 3 | 6 |  | pending | major: Claims every Hamiltonian route to the energy-excess inequality loses a surface term; only one splitting is analysed, so the no-go is overstated. |
| lattice-gap-upper-bounds | theorem | 4 | 8 |  |  | minor: Scaling O(a^3 t^{-3/2}) is inconsistent with the concluded bound C hbar c/sqrt(8t); dimensional counting gives O(a t^{-1/2}). Target only, but misstated. |
| lattice-truncation-uniform | derivation | 2 | 7 |  |  | minor: C and c are never computed; the Schur-type form bound turning kernel decay into a relative operator error is only outlined. |
| leibniz-continuity-records | historical | 5 | 8 |  |  | minor: The iff needs the supremum confined to one body in one window; allowing repetition over fresh preparations makes P_* jump on both branches. Stated, but load-bearing. |
| lieb-robinson-kogut-susskind | theorem | 3 | 7 |  |  | major: A divergent upper bound on v does not show the lattice light cone opens faster than c; stated as a consequence. |
| local-detector-coincidences | derivation | 3 | 9 |  |  | minor: Monotonicity of the averaged responses f,g is assumed rather than derived from the response maps; a non-monotone averaged response would void (3). Stated as hypothesis (1). |
| low-dimensional-mass-gap | synthesis | 3 | 8 |  |  | minor: Hypotheses (V>=0 continuous on R^n) exclude the k=-1 and k=-2 special cases that are then discussed under it. |
| magnetic-energy-identities | obstruction | 3 | 8 |  |  | minor: 'Answered in the negative' overstates: Proposition 4 shows one comparison function fails; no theorem excludes every argument from the eigenvalue equation. |
| mark-cost-and-statistical-floor | theorem | 4 | 9 |  |  | minor: 'Exactly hbar/2' is a lower bound attained only by minimum-uncertainty probes; the text says >= correctly. |
| mass-gap-conditional-theorem | synthesis | 2 | 5 | 3 / 8 | rescored | major: H1 and H2 give no convergence of Schwinger functions or OS axioms; existence of the continuum theory is a separate obligation, so the completeness claim overstates. |
| mass-gap-obligations-lattice | synthesis | 2 | 8 |  |  | minor: With V = 2 sum_p (N - Re tr U_p), the bound is V <= 4N|P|, not 2N|P|; the Kato conclusion is unchanged. |
| mass-gap-openings | synthesis | 3 | 6 |  | pending | major: Claim delta_inf(g_b)=0 at first-order point cites gapped-set Corollary 3, withdrawn 2026-10-02; T2' failure for SU(N>=5) now unsupported. |
| mass-gap-position | synthesis | 3 | 5 | 3 / 7 | rescored | major: States T2' equals absence of bulk transition and uniqueness of continuum limit; gapped-set note withdrew these equivalences on 2026-10-02. |
| mechanical-interference-action | obstruction | 2 | 10 |  |  | minor: phi = W/I is an identity (W = E delta, I = E/omega), so it carries no content beyond phi = omega delta; the note half-admits this. |
| minimax-composition | theorem | 3 | 9 |  |  | minor: Constituent radii Q_i = eps_i, P_i = 2 sqrt(m F eps) and the horizon 4 sqrt(m eps/F) are imported from R11 (Seeber-Haimovich) without restatement of hypotheses. |
| moment-hierarchy-upper-bounds | derivation | 2 | 9 |  |  | minor: Lüscher's smoothness of flowed fields is an all-orders perturbative statement; treated as the sole input beyond T4 without saying so. |
| necessity-unit-and-indeterminacy | derivation | 2 | 9 |  |  | minor: The unit's dependence on k_B and c enters through the Rayleigh-Jeans normalisation; universality then reduces to Wien's law, which the note could say outright. |
| newton-indeterminacy-routes | derivation | 4 | 8 |  |  | minor: Generator identification 'up to sign' after pullback and the hybrid bookkeeping are asserted by reference to record-costs-disturbance, not written; adaptive extension is one sentence. |
| newton-insertion-action | derivation | 2 | 10 |  |  | minor: The two-arm label and absence of branch-dependent phases are assumptions, as stated; the quantum benchmark is protocol-dependent and the note says so. |
| newton-mark-floor | derivation | 5 | 8 |  |  | minor: With recoil weight tau/4m and deviation s/4 the minimisation gives F^2 tau^3 > 64 m Lambda p, not 128 (factor 2). |
| newton-record-parallel-move | derivation | 2 | 9 |  |  | minor: Information about the initial place equals sum sigma_j^-2 only if earlier kicks do not corrupt later records; with back-action it is smaller. |
| ordered-beam-preparation | infrastructure | 0 | 9 |  |  | minor: Summary of the proof ('uniform Palm residual time, exact cancellation over a period') is unverifiable from this note; score reflects the pointer only. |
| passive-threshold-events | obstruction | 2 | 9 |  |  | minor: Crossing iff W>Delta assumes the impulse is directed toward the barrier from exact rest at -l; stated only in passing. |
| planck-gap-derivation | theorem | 5 | 9 |  |  | minor: Finite recoil width does not by itself confine post-mark momentum to a bounded set; the converse half is unneeded and loosely argued. |
| planck-gap-paper | synthesis | 6 | 9 |  |  | minor: Says 'Six positions' but lists fifteen; 'the last four entries' refers to a stale ordering (Indian entries are no longer last). |
| planck-gap-probabilistic | theorem | 5 | 8 |  |  | minor: Spread bounds are applied to interaction-picture states, whose position spread is Delta(y - p t/m), not Delta y; a Schrodinger-picture variant (step displacement F dt^2/2m) gives the same inequality but is not written. |
| polyakov-average-gap-bound | theorem | 3 | 9 |  |  | minor: Lead quotes susceptibility bound with 4 m c^2, Corollary 2 with 2 m c^2 under Delta >= m c^2/2; constants differ by the stated factor, not an error but inconsistent presentation. |
| polygon-lift-phase | theorem | 6 | 9 |  |  | minor: Inequality d^2 <= K/kappa imports the Gaussian-mark covariance bound from the paper's Theorem 2; the 'equality approached by dense protocols' claim is asserted, not proved here. |
| principia-constant-force-action | derivation | 2 | 9 |  |  | minor: eps_phase from 'order-one relative phase' is a heuristic scale for one path pair, not a resolution threshold; the note says so but still names it a scale. |
| principia-fifth-postulate | synthesis | 4 | 8 |  |  | minor: Claimed 'for every state' but spectral projections presuppose the Schrodinger (regular) representation; hypothesis should say regular state. |
| reasons-to-stop-as-research | exploratory | 3 | 8 |  |  | minor: Cites 'sharpness of the flow's growth' from the instability note as in hand; that sharpness was withdrawn 2026-10-02. |
| schur-error-ultraviolet | derivation | 3 | 6 |  | running | major: Integrand k^2/(k k' k'' (sum)^2) over d^6k gives Lambda^3, so theta ~ g^2 (Lambda L)^3 and the condition is g << N_s^{-3/2}, not g << 1/N_s; error term C' g^2 N_s^2 likewise. |
| series-parallel-gauge-refinement | theorem | 5 | 8 |  |  | minor: Convergence of blocked Gaussian actions to a fixed point is asserted, not proved; note says so. |
| small-field-step-decay-and-threshold | obstruction | 3 | 7 |  |  | major: kappa^-4 factor comes from bounding the propagator by e^{-kappa|x-y|}; the true l1 norm is O(1), so the deficit is an artifact of the weighted-norm bound. |
| small-field-step-gaussian | derivation | 3 | 7 |  |  | minor: With W summing two links, W theta already equals the 2a-link angle; theta_c=2 f-bar would give g_c^2=4g^2, contradicting 'same g^2'. Normalisation slip. |
| strong-coupling-target-box | theorem | 3 | 3 | 3 / 8 | rescored | fatal: Rests on the KS note's criterion u<=1/2, 4Fu<=lambda, whose adjacent count misses rooted histories and whose general count is withdrawn; uniform gap not established. |
| strong-coupling-threshold-explicit | derivation | 3 | 7 |  |  | minor: The e^{t_0|Lambda_0|^2|I|} factor and the |Lambda_0|^3 vs ^2 remark rest on a passage-level reading; the threshold is what one route through the proof gives, not a proved optimum. |
| strong-coupling-uniform-gap | theorem | 4 | 9 |  |  | minor: Cites KS note's g_0^2=388, 79 and gamma->4 as rigorous; that note withdrew those volume-uniform claims on 2026-10-02, so this remark is stale. |
| su2-midplane-order-t | derivation | 5 | 7 |  |  | minor: Explicit symbol s_2 and the final numerator r^3+10r^2+4r-1248 are not independently verifiable here; the headline sign of delta^23 rests on them. |
| su2-midplane-small-field | derivation | 5 | 8 |  |  | minor: Uniformity as t->0 of amplitude mixed-jet suprema (D_J, J_2, J_3) is asserted via Sec. 4 analyticity, not written out; 'jet hypotheses discharged' leans on it. |
| su2-midpoint-exact | theorem | 3 | 9 |  |  | minor: The N_off and N_diag reductions are long; verified here only through the consistency relations and the referee's mu=1 recomputation, not line by line. |
| sun-midpoint-centre | theorem | 4 | 9 |  |  | minor: Per-cell exponent versus one-loop running is a formal heuristic; 'exceed the threshold' invites reading it as an estimate, which the text then disclaims. |
| three-dimensional-gap-one-function | synthesis | 2 | 8 |  |  | minor: f(x)=delta x^{-2/3}[1+o(1)] is asserted via Luscher-type perturbation theory, which is formal; presented as 'controlled perturbatively' rather than proved. |
| torus-valley-potential | derivation | 2 | 9 |  |  | minor: Remainder written O(|a|^3); the note's own a->-a invariance and smoothness of Phi-pi^2|b| give O(|a|^4). Conservative, not wrong. |
| typical-field-strength-window | exploratory | 2 | 7 |  |  | minor: 'Controlled at any coupling' replaces ||G||_inf by a free-field typical value; it is a heuristic about the free theory, not a bound for the interacting truncation. |
| uv-halving-ir-confinement | synthesis | 2 | 8 |  |  | minor: Summary says every term with 2b0*gamma>1 dies, while section 3 uses the per-volume threshold 4; the survival criterion is stated two ways. |
| villain-monopole-refinement | theorem | 3 | 9 |  |  | minor: R to infinity already follows from the single-loop bound; the extensive bound is needed for the observable separation, not for R itself. Wording blurs this. |
| weak-coupling-feshbach-reduction | derivation | 4 | 7 |  |  | minor: The [a,a].[Atilde,Atilde] cross term is order g^{4/3}, not g^{7/3}, and is quadratic in Atilde, so it belongs with W_2 (it gives the Nielsen-Olesen shift). |
| what-would-unblock | synthesis | 2 | 9 |  |  | minor: 'Exactly two things would unblock it' is stronger than a review bounded by the author's knowledge supports; the honest qualifier appears only later. |
| wilson-strong-coupling-explicit | theorem | 3 | 6 | 4 / 8 | rescored | major: Polymer weights need sup|f_p| or sum_r d_r^2 a_r, not sum_r d_r c_r/c_0; the number e^{beta_W}-1 survives via a direct sup-norm bound, but the written argument does not establish the 1056 line. |

## Consequence for STATE

T2 stands on the Wilson transfer matrix with threshold $g^2\ge1059$; the Kogut--Susskind explicit threshold is withdrawn. No other research claim changes. Remaining bookkeeping: the unscored batches, the pending corrections and rescores, the dependence graph (`research/note-graph.md`, tooling prepared in the scratchpad), and the catalog score fields.
