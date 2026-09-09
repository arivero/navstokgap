# Task queue

The coordinator alone updates this board. Statuses: ready, active, review, done,
waiting (with a concrete dependency). “Done” means the stated acceptance condition
is met. Source tasks record either their completed coverage or an access-limited
handoff with the remaining dependency.

| ID | Status | Scope / acceptance condition | Suggested role | Depends |
| --- | --- | --- | --- | --- |
| P00 | done | Restartable programme, buildable LaTeX drafts, source/claim protocols and successful checks | Coordinator | — |
| R03 | done | Fixed-energy receiver cut maps, nonsemigroup position kernel, reset freezing limit and phase-state restoration; C062–C063 | Coordinator + Luna-low B33 | [R03 handoff](handoffs/R03.md) |
| B33 | done | Two cached primary pages, zero searches; cut-state source/proof audit and coordinator coverage correction | One Luna low, sequential | R03 |
| R04 | done | Exact three-body memory, canonical/physical tagged momentum conversion, two-time phase recovery and cooling countertest; C064–C065 | Coordinator + Luna-low B34 | [R04 handoff](handoffs/R04.md) |
| B34 | done | Two searches, three primary pages; Zwanzig elimination and Hermann–Krener observability, coordinator source/proof review | One Luna low, sequential | R04 |
| R05 | ready | Specify a classical mechanical readout of R04 tagged phase; track accuracy, disturbance and resources under refinement, testing quiet/scalable preparations before any action-floor inference | Coordinator then bounded librarian | R04/B34; observability conditioning |
| P03 | done | Repository-wide synthesis review, I003 corrections with provenance, B27 benchmark and revised priorities; written review and document checks | Coordinator + sequential B27 | A13 |
| B27 | done | Boyer relativistic Kepler threshold: three queries, four primary PDF pages, metadata and coordinator visual review | One Sol medium | P03 |
| M07 | done | Kepler threshold and softened-core closure integrated into gap laboratory; C052–C053, regular orbit domain, critical endpoint and parameter limits | Coordinator + sequential Luna-low B28 | [M07 handoff](handoffs/M07.md); M03 remains separately gated |
| B28 | done | Bounded softened-core audit; two queries, no new primary pages, coordinator corrected escape-energy wording | One Luna low, sequential | C052–C053; B27 source reuse |
| A15 | done | Circular conditional/transport variance, window-ratio bound and canonical covariance estimator; C054–C055 | Coordinator + sequential Luna-low B29 | [A15 handoff](handoffs/A15.md) |
| B29 | done | Two-query, two-page rms-emittance audit and A15 written-proof review | One Luna low + coordinator | A15 |
| A16 | done | Exact external-potential dilation and conditional zero-infimum theorem C056–C057; couplings, preparation and force constraints explicit | Coordinator + Luna-low B30 | [A16 handoff](handoffs/A16.md) |
| B30 | done | Two-query, two-HTML-source scaling audit; coordinator source and written-proof review | One Luna low, sequential | C056–C057 |
| A17 | done | Fixed smooth force-bounded potential has stable small circles of vanishing action; independent speed floor gives positive circular bound C058–C059 | Coordinator + Luna-low B31 | [A17 handoff](handoffs/A17.md) |
| B31 | done | Two queries, one primary source Sections II–III; circular balance/stability audit and coordinator review | One Luna low | A17 |
| A18 | done | Sharp orbit-action bound for regular closed trajectories from total curvature, force ceiling and speed floor; C060–C061 | Coordinator + Luna-low B32 | [A18 handoff](handoffs/A18.md) |
| B32 | done | Milnor printed pp. 248, 254; one-query primary-source audit and coordinator visual/proof review | One Luna low | A18 |
| A19 | ready | Replace pointwise speed floor by peak momentum or kinetic excursion, allowing turning-point stops; prove force-limited excursion cost or identify missing premise | Coordinator then one bounded librarian | C060 and A07 |
| R02 | ready | Audit scalar and matrix finite-propagation candidates in I003; conservation, Fourier convention and noise model explicit; prior-art audit before claim promotion | Coordinator then one small librarian | P03 corrections |
| G03 | ready | Extend G02 beyond independent products using an explicit interaction estimate and uniform observable calibration | Coordinator then sequential librarian | C045–C046 |
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
| H07 | done | Second pre-1901 batch: Newton Book III rules and General Scholium, Lagrange Part II Sections I and III, Helmholtz 1886–87, Hertz 1899 Introduction, Planck 1901; companions, checksums, BibTeX | Fable session, no subagents | [batch note](../references/batches/H07.md) |
| H08 | done | Cut-paradox sources: Heath's Method note, Physics VI.9, Diogenes IX, al-Shahrastānī and Maimonides, Zhuangzi with Legge, Mohist Canons, Liu Hui, Galileo's First Day, Cavalieri's letters and treatises; I003 idea entry | Fable session, no subagents | [batch note](../references/batches/H08.md) |
| H09 | done | H08 follow-ups: 1634 letter verified on page images (no. 2992, 2 October 1634), De generatione I.2 in Greek and French, Guldin Book IV page images with preface transcription, Aquinas SCG III.69 and Scotus II d.2, and test 1 of I003 as a draft note with checks | Fable session, no subagents | [batch note](../references/batches/H09.md) |
| I003 | review | Idea entry pushed to draft theorems: light-cone rigidity to first-order systems in both faces, the commutator scale as the obstruction, the double-limit obstruction with a rounding model, remark 2 versus 3 with premises; two notes, two check scripts, prior-art list | Fable session, no subagents | Review and audit pending; [note](../notes/i003-double-limit-rigidity.md) |
| P02 | done | Independent-session verification for A08/A09/G01: product-chain composition and bath countertest, cubic bridge-midpoint onset with exact sampler, gap/slow-mode test, continuation routes; 28 exact checks, no claim IDs | Fable session, no subagents | P01; [checks note](../notes/composition-crossover-gap-checks.md) |
| A08 | done | Conditional mass universality and positive-reference theorem, product-state closure and preparation/correlation tests; C035–C036, five checks, PDF | Coordinator + sequential Luna-low B16 | P01/P02; reviewed |
| B16 | done | Two-search/two-page composition prior-art audit; coordinator verified formula images and corrected titles | One Luna low, sequential | C035–C036 |
| A09 | active | A09a/A09b complete; preparation independence and physical quantum-role selection remain | Coordinator then one small sequential librarian | B15–B18; C035–C040 |
| A09a | done | Exact beta midpoint mixture, full crossover limits and common-finite-window mass constraint; C037–C038, 29 checks, seven numerical comparisons, PDF | Coordinator + Luna-medium B17 | C033, P02; reviewed |
| B17 | done | Two-search prior-art audit; Cinque pp. 3–4 and DLMF 10.32.1, coordinator source/proof review | One Luna medium, sequential | C037–C038 |
| A09b | done | Primary recurrence, normalized basis map, strong wavepacket and nonrelativistic limits; measured-cut countertest C039–C040 | Coordinator + Luna-medium B18 | 28 exact checks, three mode tests, PDF |
| B18 | done | Modern checkerboard passage audit and measured-cut addendum; coordinator source/proof review | One Luna medium, sequential | C039–C040; older original pages remain B15 |
| A07 | done | Sharp reversal duration and kinetic cost, parameter/excess-cost limits and uniform sharp polygon bound C043–C044 | Coordinator + Luna-low B21 | 27 finite checks and PDF |
| B21 | done | Bounded-control and Lipschitz-variance prior-art audit; corrected envelope sign, elementary specialization | One Luna low, sequential | C043–C044; coordinator proof and source review |
| A04 | ready | Spatial collision-clock diagnostic with relative-speed incoming bias and density/velocity scaling | Coordinator, then one small librarian | A02/B10; secondary to A03 |
| B11 | ready | Resume saved polygon/receding-centre audit; original worker failed auth without artifacts, later B12–B15 ran successfully | One Sol medium librarian | Drafts and 12 checks available; after A08 priority |
| B03 | ready | At most 6 primary sources on quantum speed limits, finite-resource bounds and relativistic propagation; specify time/observable definitions | Luna | Programme |
| Q01 | ready | Compare Hardy and Chiribella–D'Ariano–Perinotti axiom systems; identify classical countermodels and where action units enter | Coordinator | B01 reviewed |
| G01 | done | Susceptibility/gap product, hidden-label family and complete-observable lower gap bound C041–C042; explicit energy units | Coordinator + Luna-low B20 | 20 checks and PDF; M03 retains separate gates |
| B20 | done | Green–Kubo source and bounded spectral/frame audit; Sokal discovery-only | One Luna low, sequential | C041–C042, coordinator review |
| G02 | done | Injective-velocity fixed-plateau closing-gap family and local-frame independent-product bound C045–C046; 14 grouped checks and expanded PDF | Coordinator; saved Luna-low audit | [G02 handoff](handoffs/G02.md) |
| B22 | done | Product-chain source and weak-observability audit; source images, metadata, clock and proof-index correction verified | One Luna low, sequential | C045–C046; coordinator review |
| A10 | done | Finite conservative harmonic receiver covariance, exact action observable, centre-motion alternatives and necessary large-receiver bound C047; 15 checks and PDF | Coordinator + Luna-low B23 | [A10 handoff](handoffs/A10.md) |
| B23 | done | Ford–Kac–Mazur/Zwanzig harmonic-bath audit, coordinator source-image and proof review; reported nine-page coverage corrected | One Luna low, sequential | C047; assigned six pages, worker exceeded by three |
| A11 | done | Periodic-chain density, noncommuting limits, joint regime and fixed-phase speed-support obstruction C048–C049 | Coordinator + Luna-low B24 | Receiver paper §§5–6; exact and numerical checks |
| B24 | done | Three-page Ford–Kac–Mazur audit, zero searches; coordinator transcription and proof review | One Luna low, sequential | C048–C049 |
| A12 | done | Two-speed Poisson hard-point gas generates rate $\rho u$ and plateau $mu/\rho$; C050 and cooling test | Coordinator + one Luna-low B25 | Existing collision paper §5; [handoff](handoffs/A12.md) |
| B25 | done | Jepsen-gas covariance and Markov interpretation; corrected initial-state distinction | One Luna low, sequential | C050; worker exceeded five-page scope |
| A13 | done | Ordered counterpropagating streams give periodic tag and zero plateau at fixed mechanical scales and mean rate; C051 | Coordinator + one Luna-low B26 | Collision paper §6; [handoff](handoffs/A13.md) |
| B26 | done | Ordered-preparation prior-art audit: two queries, two HTML sources; no exact match in coverage | One Luna low, sequential | C051; coordinator metadata and proof review |
| A14 | ready | Independent stationary renewal streams at fixed mean gap: Palm residual law, tagged variance growth and gap-variance dependence | Coordinator then one bounded librarian | A13/B26; test quantitative preparation control, including near-ordered limits |
| S01 | done | Action-target skill upgrade and source-idea context-recovery skill, AGENTS hook and local routing validation | Coordinator, no additional worker | [handoff](handoffs/restart-skills-2026-09-08.md) |
| C01 | ready | Companion map: finite-c mechanics, heat/Poincare coercivity, NS/YM; explicit non-implications and candidate transferable estimate | Analyst | Existing Millennium notes |
| F01 | waiting | Lean feasibility: crossover real-arithmetic lemma first, quadratic no-gap family second; pin toolchain and audit axioms, no `sorry` | Sol formalisation, reviewer | A09 acceptance and tooling decision |
| W01 | waiting | Revise technical manuscript from accepted claims only; citation/notation/proof audit, reproducible PDF | Scientific writer + reviewer | R01 and next accepted result |

## Hard verification constraint

No Python numerical or symbolic verification scripts may be created or run.
This applies to coordinator and all workers, overriding historical check-script
instructions in task descriptions and handoffs. Use written derivations and
source/proof review. `make check` is document/source integrity only. No language
substitution to evade this rule; new computational verification needs user direction.

## Worker task envelope

Each dispatch names the task ID, inputs, allowed output paths, a finite source/page
budget, review criteria and stopping condition. Use `agents/PROTOCOL.md` and the
matching role card. Delegate to Sol or Luna sequentially; wait for each worker
and review its handoff before continuing or dispatching again. End each search
at its stated budget with findings and the next question.

## Next bounded session

Start R05 from the completed R04/B34 receiver-memory test: specify the
mechanical readout and test precision, disturbance and resource scaling.
Preserve A19 below as a supporting mechanical calculation. R04 established
C064–C065; see its handoff.

Start A19's peak-excitation test, allowing speed to vanish at turning points.
A18/B32 completed the sharp closed-trajectory action bound C060–C061.
A17/B31 completed the fixed-potential small-circle and positive floor tests.
A16/B30 completed the conditional dilation obstruction C056–C057.
A15/B29 completed the circular bound-system comparison, C054–C055.
M07/B28 completed the
Kepler benchmark and softened-core countertest (C052–C053). I004 and P03 carry the rationale.
R02 owns the repaired finite-propagation draft; A17 tests the fixed-force class.
The A06/A09a consolidation is complete; the review maps remaining opportunities.
For the next bounded transport test, A14 replaces ordered streams by independent stationary renewal streams
at fixed mean gap. Derive the Palm residual law and tagged variance growth;
test whether mixing supplies a uniform bound as gap variance decreases.
A13 holds mass, speed, density and mean collision rate fixed while closing
the response through periodic cancellation.
A12 derives the Markov clock from Poisson gaps; its plateau depends on preparation.
A04's equal-mass spatial-clock subcase is covered by A12; general velocity laws
retain incoming-speed bias. A09 retains the physical scale-selection
target. A08/B16 and A06/B14 are complete. The user reaffirmed the
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
