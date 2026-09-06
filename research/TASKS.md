# Task queue

The coordinator alone updates this board. Statuses: ready, active, review, done,
waiting (with a concrete dependency). “Done” means the acceptance condition is met,
not that the larger scientific question is settled. Source tasks may finish with
an honest access-limited handoff, never with fabricated content.

| ID | Status | Scope / acceptance condition | Suggested role | Depends |
| --- | --- | --- | --- | --- |
| P00 | done | Restartable programme, buildable LaTeX drafts, source/claim protocols and successful checks | Coordinator | — |
| B01 | done | Six primary bibliography leads returned; identifiers/abstracts reviewed and shared metadata integrated; no full proof audit | Luna + coordinator | Programme |
| H01 | done | NATP00385 normalized, diplomatic and XML archived; focused passage audit, not full manuscript/corpus reading | Sol + coordinator | Programme |
| M01 | done | Constant-force no-gap proposition; Jacobi/Hessian distinction; free-kernel test; conditional two-arm distinguishability derivation | Coordinator | Existing note |
| R01 | done | All three propositions and supporting calculations internally audited; two scope clarifications incorporated | Independent reviewer | M01 |
| H02 | ready | Locate Classical Scholia editions/witnesses; six-entry coverage matrix and lawful access attempts | Luna search, Sol collation | H01 contextual distinction |
| H03 | waiting | Read all six scholia in an identified edition; compare relevant manuscript deletions; audit 1687-delay claim chronologically | Historical analyst + reviewer | H02 access |
| B02 | ready | At most 6 primary sources: central-potential existence, collision regularisation, action-angle/EBK; distinguish exact from semiclassical | Luna | Programme |
| M02 | ready | Classical IVP assumptions for smooth central forces; explicit radial Kepler collision example and continuation convention | Sol derivation, coordinator review | C002 |
| M03 | ready | Oscillator Hessian versus Hamiltonian spectra; free line versus circle and large-volume gap closure | Sol calculation, reviewer | M01 |
| B03 | ready | At most 6 primary sources on quantum speed limits, finite-resource bounds, relativistic propagation; no time-operator shortcuts | Luna | Programme |
| Q01 | ready | Compare Hardy and Chiribella–D'Ariano–Perinotti axiom systems; identify classical countermodels and where action units enter | Coordinator | B01 reviewed |
| G01 | waiting | Choose one gap notion/model; prove a bound with operator domain, parameter dependence and gap-closing limits | Analyst + adversarial reviewer | M03, Q01 as relevant |
| C01 | ready | Companion map: finite-c mechanics, heat/Poincare coercivity, NS/YM; explicit non-implications and candidate transferable estimate | Analyst | Existing Millennium notes |
| F01 | waiting | Lean feasibility spike for positive quadratic action values approaching zero; pin toolchain, state/axiom audit, no `sorry` | Sol formalisation, reviewer | M01 and tooling decision |
| W01 | waiting | Revise technical manuscript from accepted claims only; citation/notation/proof audit, reproducible PDF | Scientific writer + reviewer | R01 and next accepted result |

## Worker task envelope

Each dispatch names the task ID, inputs, allowed output paths, a finite source/page
budget, review criteria and stopping condition. Use `agents/PROTOCOL.md` and the
matching role card. Run independent tasks concurrently only when outputs are
disjoint. No worker should search indefinitely because a preferred thesis was not
supported.

## Next bounded session

Execute M03, with H02 in parallel using `references/batches/H02-seeds.md`.
Q01 now has a literature-grounded starting pair, but their full proofs still need
reading. Do not install a large formalisation stack merely to make the programme
appear rigorous. Completed-task handoffs are under `research/handoffs/`.
