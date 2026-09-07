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
| A02 | review | Elastic refreshed-bath draft derives physical-time action relaxation, mass/rate plateau and bath-scaling countermodels; 15 checks pass; B10 audit pending | Coordinator, then one small librarian | A01/B09 |
| B10 | active | Audit A02 collision law, invariant moments/covariance, physical-time observable and scaling countermodels; at most three sources and eight selected pages | One Luna medium librarian | A02 draft |
| B03 | ready | At most 6 primary sources on quantum speed limits, finite-resource bounds and relativistic propagation; specify time/observable definitions | Luna | Programme |
| Q01 | ready | Compare Hardy and Chiribella–D'Ariano–Perinotti axiom systems; identify classical countermodels and where action units enter | Coordinator | B01 reviewed |
| G01 | waiting | Choose one gap notion/model; prove a bound with operator domain, parameter dependence and gap-closing limits | Analyst + adversarial reviewer | M03, Q01 as relevant |
| C01 | ready | Companion map: finite-c mechanics, heat/Poincare coercivity, NS/YM; explicit non-implications and candidate transferable estimate | Analyst | Existing Millennium notes |
| F01 | waiting | Lean feasibility spike for positive quadratic action values approaching zero; pin toolchain, state/axiom audit, no `sorry` | Sol formalisation, reviewer | M01 and tooling decision |
| W01 | waiting | Revise technical manuscript from accepted claims only; citation/notation/proof audit, reproducible PDF | Scientific writer + reviewer | R01 and next accepted result |

## Worker task envelope

Each dispatch names the task ID, inputs, allowed output paths, a finite source/page
budget, review criteria and stopping condition. Use `agents/PROTOCOL.md` and the
matching role card. Delegate to Sol or Luna sequentially; wait for each worker
and review its handoff before continuing or dispatching again. End each search
at its stated budget with findings and the next question.

## Next bounded session

Execute A02 from `research/ACTION_FIELD_TARGET.md`. Start with a bounded source
task only when a specific mechanical-model choice needs it; retain explicit
momentum exchange, environment parameters and the correlation invariant test.
A01/B09 are complete. M06 remains a supporting force-control calculation.
B07b retains the tangent-groupoid theorem reading.
M05/B07a/B08 are complete. M03 retains its draft and completed B04
audit; its independent mathematical review and build integration remain.
H02 continues from `references/batches/H02-seeds.md`; H05 uses H04's exact
cone-passage witnesses.
Q01 has a literature-grounded starting pair and full-proof reading as its first
step. F01 controls the decision to introduce formalisation tools. Completed-task
handoffs are under `research/handoffs/`.
