# State

Updated 2026-09-16. Read this page and the note it points to; AGENTS.md
governs. Older files in this directory are context.

## Goal

Prove the Yang--Mills existence and mass-gap conjecture (Jaffe--Witten;
[digest](../notes/millennium-problem-definitions.md)). Progress is measured
in theorems with explicit $L$, $a$, $g$ dependence and in the removal of
one obligation at a time.

## What is in hand

- **Two ends of the problem are known, and the middle is the problem.**
  At strong coupling the lattice theory has a gap uniform in the volume
  (Osterwalder--Seiler cluster expansion, in units of $1/a$). At small
  volume the zero-mode sector has a gap $\delta_1g^{2/3}\hbar c/L$ proven
  positive for every $L$ ([G07](../notes/low-dimensional-mass-gap.md)
  §3.3, from C133) and Lüscher's expansion carries it to one loop. Neither
  end survives its own limit: the strong-coupling gap is tied to $a$, the
  small-volume gap decays as $1/L$. The mass gap is the statement that the
  crossover, near $z=M(0^+)L\simeq2$ in Lüscher--Münster's variable, hands
  over to a limit $m>0$ in units set by the running coupling.
- **Dimensional shape** ([C131--C132](../claims/LEDGER.md)): classical
  $d=4$ Yang--Mills carries no constant, so any finite gap is
  $m=a^{-1}F(g^2(a)\hbar)$ with $F\to0$ along the continuum curve; in
  $d=3$ the coupling itself is the mass unit. The gap-to-unit equivalence
  holds in $d=2,3$ and fails in $d=4$.
- **Mechanism in the solved sector**: the gap of the constant modes is the
  uncancelled transverse zero-point energy along the abelian valleys
  ([G08](../notes/action-floor-yang-mills-gap.md)); supersymmetric
  cancellation removes it (de Wit--Lüscher--Nicolai).
- **Rigorous constructions available for import**: $d=2$ (Driver,
  Gross--King--Sengupta, Lévy; Witten's exact solution); $d=3$ finite
  volume by stochastic quantisation ([Chevyrev review](../docs/Chevyrev_StochasticYM_2202.13359v2.md));
  $d=4$ finite-volume ultraviolet stability (Balaban; Magnen--Rivasseau--
  Sénéor), no gap. Reading levels for all of these are in B78.

## Next steps (each a note)

1. **Obligations map for the Hamiltonian lattice route.** Write the exact
   chain from the Kogut--Susskind Hamiltonian on a finite lattice to the
   Jaffe--Witten statement: (i) unique ground state and gap at every finite
   lattice, proved in writing (positivity-improving semigroup in the group
   basis); (ii) the strong-coupling gap uniform in $L$, cited with its
   hypotheses; (iii) the continuum target as
   $\liminf_{a\to0}\,(a\,\Delta_{a,L})/(a\Lambda(g(a)))>0$ uniformly in
   $L$, with the order of limits stated; (iv) which of (i)--(iii) the
   small-volume expansion controls. Deliverable: a note that turns "prove
   the mass gap" into a finite list of named theorems, each with its
   current status.
2. **The $d=3$ case as the first target.** The coupling is the mass unit,
   so no transmutation is needed; formulate the gap conjecture
   $m=C\,g^2\hbar^2/c$ with $C>0$ and identify which finite-volume
   estimate from the $d=3$ stochastic construction would give it.
3. **The crossover in the zero-mode model.** Determine whether the
   next-to-leading terms of Lüscher's expansion (the coupling of the
   constant modes to the first nonzero momentum modes) raise or lower the
   $1/L$ gap, and whether a variational bound on the full torus Hamiltonian
   can be written with the zero-mode ground state as trial state.

## Supporting

The Galileo area/necessity question (N01, N02) and the $h>0$ analogy
(G07, G08, C131--C133) serve the goal as heuristics. Publication drafts
wait for author input.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows; at most one
sequential source worker. Commit and push after each result.
