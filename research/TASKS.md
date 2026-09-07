# Task queue

The coordinator alone updates this board. Statuses: ready, active, review, done,
waiting (with a concrete dependency). “Done” means the stated acceptance condition
is met. Source tasks record either their completed coverage or an access-limited
handoff with the remaining dependency.

| ID | Status | Scope / acceptance condition | Suggested role | Depends |
| --- | --- | --- | --- | --- |
| P00 | done | Restartable programme, buildable LaTeX drafts, source/claim protocols and successful checks | Coordinator | — |
| B01 | done | Six primary bibliography leads; identifiers/abstracts reviewed and shared metadata integrated | Luna + coordinator | Programme |
| H01 | done | NATP00385 normalized, diplomatic and XML archived; focused passage audit and coverage record | Sol + coordinator | Programme |
| M01 | done | Constant-force no-gap proposition; Jacobi/Hessian distinction; free-kernel test; conditional two-arm distinguishability derivation | Coordinator | Existing note |
| R01 | done | All three propositions and supporting calculations internally audited; two scope clarifications incorporated | Independent reviewer | M01 |
| H02 | ready | Locate Classical Scholia editions/witnesses; six-entry coverage matrix and lawful access attempts | Luna search, Sol collation | H01 contextual distinction |
| H03 | waiting | Read all six scholia in an identified edition; compare relevant manuscript deletions; audit 1687-delay claim chronologically | Historical analyst + reviewer | H02 access |
| B02 | ready | At most 6 primary sources: central-potential existence, collision regularisation, action-angle/EBK; distinguish exact from semiclassical | Luna | Programme |
| M02 | ready | Classical IVP assumptions for smooth central forces; explicit radial Kepler collision example and continuation convention | Sol derivation, coordinator review | C002 |
| M03 | active | Oscillator Hessian versus Hamiltonian spectra; free line versus circle and large-volume gap closure | Coordinator derivation, sequential review | M01 |
| B04 | done | Per-result literature audit of M03 spectra, action variable, winding and finite-speed sector bounds; coordinator source checks recorded | Luna librarian, coordinator verification | M03 draft |
| B05 | done | Retrospective per-result literature audit of C001–C008, with exact matches and consequence classifications | Luna librarian, coordinator verification | Current ledger |
| H04 | done | Cone-section passage verified in Xylander 1570 pp. 823–824; bounded early-modern reception search | Luna librarian, coordinator visual verification | User cone question |
| H05 | ready | Author-specific cone reception: Newton Plutarch references and Leibniz continuum corpus; separate ownership, quotation and use | One Luna/Sol source worker | H04 |
| M04 | done | Exact free Gaussian blocking, semigroup parameter and bridge concentration; oscillatory counterpart; readable paper and checks | Coordinator | Rivero 1998/1999 |
| B06 | done | Prior-art and assumption audit of each M04 result; source corrections verified and integrated | One Luna librarian | M04 draft |
| M05 | done | Two-regulator quadratic audit: exact normalization, joint action-defect limit, stationary phase and explicit scaling map; reviewed paper and checks | Coordinator | M04/B06 |
| B07a | done | Wilson–Kogut §12.2 common-correlation-length construction read; reference-observable test implemented in M05 | Coordinator source reading | M04 |
| B07b | ready | Tangent-groupoid quantization theorem: exact hypotheses, limit topology and completion scope; return one test for the strong target | One Luna/Sol source worker | M04 |
| B08 | done | Four-source, 13-page per-result prior-art and proof audit of M05, reviewed by coordinator | One Sol medium librarian | M05 draft |
| M06 | ready | Test force/acceleration control and a strict-speed relativistic action on the shrinking oscillations; state the action-defect survival criterion and review it | Coordinator, then one small librarian | M05/B08 |
| A01 | done | Reviewed finite-speed action observable, reversible-generator positivity and persistent-flight limits; C018–C021, PDF and 16 exact checks | Coordinator + B09 | M05 and sharpened user target |
| B09 | done | Four-source per-result literature/assumption audit; 12 PDF pages plus APS abstract; coordinator verification and source-to-model comparison integrated | One Luna medium librarian | A01 draft |
| A02 | done | Reviewed collision bath: physical-time action relaxation, mass/rate plateau and scaling countermodels; C022–C024 and 15 checks | Coordinator + B10 | A01/B09 |
| B10 | done | Three-source A02 audit; seven worker pages plus one coordinator page; constants and source assumptions verified | One Luna medium librarian | A02 draft |
| A03 | done | Arbitrary-partition chord error, exact Gaussian refinement consistency, fixed-preparation action estimator and one-node cost; C027–C029, B12 and nine checks | Coordinator + Luna medium audit | User reminder; M05/A02 |
| B12 | done | Bounded prior-art/assumption audit of A03 using existing bridge and Newton routes; coordinator source verification | One Luna medium librarian | A03 draft |
| A05 | done | Elastic physical-cut test, sharp midpoint support/variance bound, ballistic convolution drift theorem; C030–C032, twelve checks and B13 | Coordinator + Luna medium | A03/B12 |
| B13 | done | Six-page A05 source/proof audit; collision and memory ingredients separated from derived support/convolution results | One Luna medium librarian | A05 draft |
| A06 | complete | Velocity-resolved return bridge, midpoint atom, conditioning version and consistent cut/action limits; C033–C034 | Coordinator + sequential Luna medium B14 | 12 symbolic checks, 45 rational partition cases |
| B14 | complete | Cinque occupation-law and return-bridge prior-art audit; coordinator corrected discovery-source attribution | Luna medium, sequential | C033–C034 reviewed |
| P01 | done | Critical review of six proposed directions; composition/checkerboard/gap priorities with explicit premises and preserved acceptance gates | Coordinator + B15 | A06/B14 |
| B15 | done | Bounded checkerboard journal metadata/abstract and book-location leads; direct formula reading still pending | One Luna medium, sequential, coordinator review | P01; companion records access limits |
| H06 | done | Twelve pre-1901 primary sources stored in `docs/classics/` with companions, checksums and BibTeX: least-action origins, parabola geometry, vanishing quantities, the cone passage and the Gregory preface; access failures recorded | Fable session, no subagents | [batch note](../references/batches/H06.md) |
| P02 | done | Independent-session verification for A08/A09/G01: product-chain composition and bath countertest, cubic bridge-midpoint onset with exact sampler, gap/slow-mode test, continuation routes; 28 exact checks, no claim IDs | Fable session, no subagents | P01; [checks note](../notes/composition-crossover-gap-checks.md) |
| A08 | ready | Composition universality: all-positive-mass domain, nonnegative coefficient, COM/relative covariance, preparation and correlated/full-law countertests; short note, five checks, per-result audit | Coordinator then one Luna low librarian | P01; next main task |
| A09 | ready | Necessary crossover window and conditioned midpoint moments; direct checkerboard source passages, real/complex recurrences and nonrelativistic scaling; audit each result | Coordinator then one Luna medium librarian | B15 leads; A08 coefficient premises |
| A07 | ready | Bounded-acceleration return with opposite endpoint velocities: sharp duration and kinetic-action bounds, speed/force scaling and sampled-cut limit | Coordinator, then one small librarian | A06/B14; M06 connection |
| A04 | ready | Spatial collision-clock diagnostic with relative-speed incoming bias and density/velocity scaling | Coordinator, then one small librarian | A02/B10; secondary to A03 |
| B11 | ready | Resume saved polygon/receding-centre audit; original worker failed auth without artifacts, later B12–B15 ran successfully | One Sol medium librarian | Drafts and 12 checks available; after A08 priority |
| B03 | ready | At most 6 primary sources on quantum speed limits, finite-resource bounds and relativistic propagation; specify time/observable definitions | Luna | Programme |
| Q01 | ready | Compare Hardy and Chiribella–D'Ariano–Perinotti axiom systems; identify classical countermodels and where action units enter | Coordinator | B01 reviewed |
| G01 | ready | Finite-state susceptibility/gap product and two-state equality; hidden slow-mode test, energy normalization, Dirac-branch versus vacuum gap; audited extension for M03 | Coordinator then one small sequential reviewer | C019; P01; M03 retains existing acceptance gates |
| C01 | ready | Companion map: finite-c mechanics, heat/Poincare coercivity, NS/YM; explicit non-implications and candidate transferable estimate | Analyst | Existing Millennium notes |
| F01 | waiting | Lean feasibility: crossover real-arithmetic lemma first, quadratic no-gap family second; pin toolchain and audit axioms, no `sorry` | Sol formalisation, reviewer | A09 acceptance and tooling decision |
| W01 | waiting | Revise technical manuscript from accepted claims only; citation/notation/proof audit, reproducible PDF | Scientific writer + reviewer | R01 and next accepted result |

## Worker task envelope

Each dispatch names the task ID, inputs, allowed output paths, a finite source/page
budget, review criteria and stopping condition. Use `agents/PROTOCOL.md` and the
matching role card. Delegate to Sol or Luna sequentially; wait for each worker
and review its handoff before continuing or dispatching again. End each search
at its stated budget with findings and the next question.

## Next bounded session

Execute A08 from `research/ACTION_FIELD_TARGET.md`, then A09 and G01 as assessed
in `reviews/six-directions-2026-09-08.md`. A07 remains the bounded-force
diagnostic. A06/B14 are complete. The user reaffirmed the
continuum limit of cut points as the central problem. A02/B10 are complete;
their collision mechanism is a diagnostic of supplied scales. M06 remains a
supporting force-control calculation, A04 a secondary spatial-clock test.
B07b retains the tangent-groupoid theorem reading.
M05/B07a/B08 are complete. M03 retains its draft and completed B04
audit; its independent mathematical review and build integration remain.
H02 continues from `references/batches/H02-seeds.md`; H05 uses H04's exact
cone-passage witnesses.
Q01 has a literature-grounded starting pair and full-proof reading as its first
step. F01 controls the decision to introduce formalisation tools. Completed-task
handoffs are under `research/handoffs/`.
