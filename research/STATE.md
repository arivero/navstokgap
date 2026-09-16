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
2. **Done: T2 in Hamiltonian form.**
   [The strong-coupling note](../notes/strong-coupling-uniform-gap.md)
   checks Yarotsky's gap-stability hypotheses for the Kogut--Susskind
   Hamiltonian: $\Delta_{a,L}\ge\gamma(g^2/2)C_2\hbar c/a$ uniformly in the
   lattice size for $g\ge g_0(N)=(48N^2/[(N^2-1)\beta_*])^{1/4}$, with
   infinite-volume ground state and exponential clustering. Blind to the
   abelian/non-abelian distinction, which is T2$'$.
3. **Done: upper bounds on the lattice gap ($d=4$).**
   [Feynman--Bijl note](../notes/lattice-gap-upper-bounds.md): for any
   gauge-invariant $f(U)$, $\Delta\le\frac{\hbar cg^2}{2a}\sum_\ell\langle|\nabla_\ell f|^2\rangle/\operatorname{Var}f$;
   plaquette bound $\hbar cg^2N/(a\operatorname{Var}\operatorname{Re}\operatorname{tr}U_p)$;
   strong-coupling gap of order $g^2\hbar c/a$ on both sides; for $U(1)$
   the electric trial operator is gauge invariant and
   $\Delta\le2\hbar c\hat S(k)/(ag^2\langle\cos\theta_p\rangle)$ (Coulomb
   phase gapless through the sine structure factor); for non-abelian $G$
   no c-number-coefficient operator linear in $E$ is gauge invariant
   (proved), so the photon-type excitation must carry a string whose
   electric cost blocks that channel. New upper-side target
   T$_{\rm fin}$: the same inequality for Wilson-flowed observables with
   an $a$-uniform flow-Jacobian bound (the finiteness half $m<\infty$).
3b. **Next: the weak-coupling end on the lattice.** Variational upper
   bound (and lower bound if reachable) on the Kogut--Susskind gap at
   small $g$ on a lattice with side small against $\hbar c/\Lambda$, using
   the constant-mode ground state of C133 as trial state; connect
   $\Delta_{a,L}$ with the continuum corner $\delta_1g^{2/3}\hbar c/L$ and
   locate the regime where neither expansion applies.
4. **Done: the $d=3$ formulation.**
   [One function of one variable](../notes/three-dimensional-gap-one-function.md):
   $\Delta(L)=g^2\hbar^2c\,f(x)$, $x=g^2\hbar L$, with
   $f(x)=\delta_1^{(2)}x^{-2/3}[1+o(1)]$ at $x\to0$ from C133 ($D=2$) and
   the conjecture $f\to C\in(0,\infty)$; on the lattice the ratio
   $\delta_\infty/g_{\rm lat}^2$ is bounded below at strong coupling by the
   $\nu=2$ Yarotsky bound and the conjecture is its positivity for all
   $g_{\rm lat}$, linear at both ends, no transmutation. Next in $d=3$: a
   lower bound $f(x)\ge f_->0$ on an interval beyond the small-volume
   expansion.
5. **The crossover in the zero-mode model.** Sign of the next-to-leading
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
