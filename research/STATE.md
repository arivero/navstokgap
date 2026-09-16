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

1. **Done: obligations map.**
   [The lattice-route note](../notes/mass-gap-obligations-lattice.md)
   turns the conjecture into six named statements: T1 (finite-lattice gap,
   proved), T2 (strong-coupling gap uniform in volume; Euclidean form
   established, Hamiltonian form open), T2$'$ (no Coulomb phase at any
   coupling; false for $U(1)$), T3 (the scaling limit
   $\delta_\infty(g)/(a\Lambda_{\rm lat}(g))\to m/(\hbar c\Lambda)$), T4
   (existence with the axioms) and S (the small-volume corner
   $z(L)=\delta_1g^{2/3}[1+O(g^{2/3})]$). The conjecture is T2$'$ with T3,
   given T4.
2. **Next: T2 in Hamiltonian form.** Prove
   $\Delta^{\rm phys}_{a,L}\ge c(N)g^2\hbar c/a$ for $g\ge g_0(N)$ uniformly
   in the lattice size, for the Kogut--Susskind Hamiltonian, handling the
   unbounded electric term (truncation of link representations with
   control, or relative boundedness of the magnetic term). Output: a value
   of $g_0(N)$ and the argument that later work must push toward zero.
3. **The $d=3$ case.** The coupling is the mass unit; formulate
   $m=C\,g^2\hbar^2/c$ and identify the finite-volume estimate of the
   stochastic construction that would give $C>0$.
4. **The crossover in the zero-mode model.** Sign of the next-to-leading
   terms of Lüscher's expansion for the gap; a variational bound on the
   torus Hamiltonian with the zero-mode ground state as trial state.

## Supporting

The Galileo area/necessity question (N01, N02) and the $h>0$ analogy
(G07, G08, C131--C133) serve the goal as heuristics. Publication drafts
wait for author input.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows; at most one
sequential source worker. Commit and push after each result.
