# State

Updated 2026-10-28. **Active direction: Newton action necessity.** Read
[AGENTS.md](../AGENTS.md), then the
[recent Newton synthesis](../notes/newton-dimock-balaban-guide.md#recent-newton-synthesis).
The synthesis consolidates the October 27--28 calculations and links to
their proofs, checks and countermodels. This page is the live queue;
[dependencies](dependencies.md), [obstructions](obstructions.md), the
[book map](book-map.md) and the full [catalog](../notes/index.md) route
the wider corpus.
The receiver compilation now contains the full R03/R04 cut and memory proofs;
the Newton synthesis incorporates the two-regulator bridge result.

## Goal

Determine whether a consistent completion of Newtonian mechanics requires
a nonzero physical $\hbar$, from independently justified premises. Test
the strong thesis that Newton's theory is only a large-action regime of
a positive-$\hbar$ theory against classical completions, full records and
reversible dynamics. A conditional covariance floor, a constructed quantum
family, and an identification of its action scale with physical $\hbar$
are three distinct claims. **The general necessity and uniqueness claims
remain open.**

Keep $\hbar$ explicit. For a specified characteristic action $S_0$,
$\epsilon=\hbar/S_0\to0$ is a separate limit from time refinement and
record resolution; a large-$S_0$ physical family must be specified.

The other main proof goal is continuum existence and a positive finite
physical mass gap for pure $SU(3)$ Yang--Mills on $\mathbb R^4$. The
eventual comparison includes QCD with zero and nonzero quark masses as a
symmetry benchmark, not a third full construction programme
([three continuum limits](../notes/three-continuum-limits.md)). The gauge
frontier is retained below; Newton is first in the current queue.

## In hand

- **Refinement and quantum construction.** Arbitrary-partition Newton
  polygons construct a unique causal solution under the stated Lipschitz
  certificate. Smooth coherent-packet means converge at
  $O(\hbar+|\pi|)$, with widths $O(\sqrt\hbar)$, to that solution. A
  specified $C^{1,1}$ lift gives an $O(\sqrt\hbar)$ comparison with a
  supplied quantum parameter. These are scoped constructions, not a
  universal classical-to-quantum theorem or a proof of necessity
  ([synthesis](../notes/newton-dimock-balaban-guide.md#recent-newton-synthesis)).
- **Cusp, stability and floors.** Reversible phase-state dynamics with
  affine-canonical and closure premises, or a different $W_2$-continuity
  and canonical-copy premise with actual Gaussian cusp transport, each
  force a positive covariance-action infimum. Both have classical
  witnesses with supplied scales; the first theorem's point compatibility
  may be vacuous when points are excluded. Fine nondisturbing joint
  classical records force the infimum to zero
  ([history and continuity](../notes/cusp-history-records-continuity.md)).
- **Classical countermodels and records.** The reversible full-history
  model retains branch-selection information. The entropy-floor witness
  survives the canonical copy mixer and actual cusp flow but fails one
  selective Gaussian-meter test. Its Gaussian-mixture repair survives
  that meter and copying but fails a nonlinear canonical shear. The meter
  counterexample uses increasingly large preparation apertures; the
  history model has no constructed finite-dimensional local apparatus
  ([meter](../notes/gaussian-meter-entropy-floor.md),
  [history](../notes/cusp-history-records-continuity.md)). These written
  results are unrefereed; selective internal checks are identified in
  their individual notes.
- **Earlier Newton results.** The [Planck paper](../notes/planck-gap-paper.md)
  gives quantum record and disturbance bounds under supplied quantum
  kinematics. The [reachability proof](../notes/zero-branch-reachability.md)
  shows that the coherent-stream contrast needs a coherence premise: an
  incoherent packet attachment recovers the classical swarm for quadratic
  forces. Kepler and relativistic thresholds retain their fixed-interval
  and domain-selection qualifications
  ([self-sufficiency](../notes/self-sufficiency-contrast.md)).
- **Gauge and comparison.** The [mass-gap position](../notes/mass-gap-position.md)
  separates finite-lattice and strong-coupling results from the open
  continuum construction, nontriviality and physical gap. The
  [refinement synthesis](../notes/refinement-composition-and-limit.md)
  and [halving atlas](../notes/halving-atlas.md) supply common insertion
  laws and the dimension-by-dimension map.

## Next

1. **Independent physical premises.** Test whether a specified apparatus
   and its complete retained records justify a preparation, terminal
   readout or uniform response law without assuming the desired floor.
   Account for memory, calibration, apertures, energy and limiting order.
   Compare any proposed law with the exact classical history, fine-record,
   entropy and Gaussian-meter countermodels in the recent synthesis.
2. **Groupoid control and renormalization.** Test the scale relation in
   Rivero's [1997 toy RG triangle](https://arxiv.org/pdf/dg-ga/9710026)
   and [1998 two-regulator proposal](https://arxiv.org/pdf/quant-ph/9803035)
   by specifying the actual normalized blocking/control maps, increments,
   generated interactions and observables. The
   [synthesis dictionary](../notes/newton-dimock-balaban-guide.md#recent-newton-synthesis)
   separates the groupoid deformation, a bare action regulator, mesh and
   effective $\hbar$. Its exactly normalized free Gaussian block-and-scale
   test retains every nonnegative action parameter, including zero. Derive
   rather than assume any physical scale selection or running law for an
   interacting or record-sensitive construction.
3. **From a floor to quantum structure.** Determine what further
   independently motivated composition and nonlinear-dynamics premises
   distinguish a commutative state restriction from quantum states and
   instruments, and whether any selected scale is universal and equals
   $\hbar/2$ in covariance action. The existing Gaussian central limit
   fixes a conditional Gaussian sector, not arbitrary states or dynamics.
   The earlier [recording notebook](../notes/sed-closure-under-recording.md)
   and [score-constrained model](../notes/score-constrained-ensemble.md)
   retain their complete-controller and branch-dependent protocol tests;
   composition closure there selects no positive coefficient by itself.
4. **Construction and verification.** The universal
   [classical-to-quantum lifting conjecture](../notes/classical-quantum-existence-conjecture.md)
   remains open beyond its specified Lipschitz class. The
   [Lean targets](../notes/lean-verification-quantum-newton.md) are written
   specifications, not compiled quantum proofs; fixed-$\hbar$ product
   convergence, joint-limit ray separation and operator ordering are
   different claims.
5. **Retained gauge frontier.** For the SU(2) mid-plane, extend the
   retained-barrier weak-strip estimates (116) and (112), and the centered
   quadratic source test (177), to the nonlinear source bound (113),
   physical recoupling, group comparison, SU(3) constants and stable
   iteration ([small-field notebook](../notes/su2-midplane-small-field.md)).
   For four dimensions prove depth-uniform generated-action matching and
   remainder control ([composition](../notes/four-dimensional-composition.md),
   §7). Continuum reconstruction, physical spectral weight and the
   renormalized H1--H3 small-volume bridge remain separate
   ([Feshbach](../notes/weak-coupling-feshbach-reduction.md)); a gap at
   every bare coupling is not assumed necessary
   ([scaling correction](../notes/mass-gap-openings.md)).

Thermodynamic cost, phase consistency, radiation calibration and
Leibniz-continuity arguments retain their own assumptions; none alone
has selected a universal positive action. Their exact failures and
surviving statements are in [obstructions](obstructions.md). The
[October 1 handout](handoffs/HANDOFF-2026-10-01-CLAUDE-NEWTON.md),
[September 23 handout](handoffs/HANDOFF-2026-09-23.md) and
[October 1 corpus audit](../notes/corpus-audit-2026-10-01.md) are dated
historical snapshots; maintained notes and their corrections govern reuse.

## Constraints

No numerical or symbolic verification scripts. Build only changed
scientific notes with `make paper NOTE=<slug>`; never perform a routine
full paper rebuild. Do not use subagents under the current user direction.
Keep physical $\hbar$ explicit. Do not reinstall bulky Lean tooling;
consult sister-repository sources as needed. Commit and push completed
work with the requested model attribution.
