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
3a. **Done: Polyakov-average bound.**
   [Note](../notes/polyakov-average-gap-bound.md): exact
   $\Delta\le\hbar cg^2N/(4L\operatorname{Var}\bar P_i)$ with $\bar P_i$ the
   transverse-averaged spatial Polyakov loop; at weak coupling in a small
   box the zero-mode expectation values make it $(\hbar c/L)g^{2/3}$ times
   $2\langle|\xi_i|^2\rangle/\operatorname{Var}(|\xi_i|^2)$ (upper side of
   the corner S); in infinite volume a gap $m$ forces the Polyakov-loop
   transverse susceptibility below $\hbar cg^2NL/(2mc^2)$ (necessary
   condition for T3); empty at strong coupling.
3b. **Done: Feshbach reduction of the weak-coupling lower bound.**
   [Note](../notes/weak-coupling-feshbach-reduction.md): a proved
   Schur-complement gap-transfer lemma ($\operatorname{gap}(H)\ge\operatorname{gap}(PHP)-\eta$
   when $\bar PH\bar P\ge\mu>a_1$) applied with $P$ = nonzero-mode vacuum
   reduces $\Delta\ge\delta_1^{(3)}g^{2/3}(1-Cg^{2/3})\hbar c/L$ on the cutoff
   torus to (H1) one-quantum cost $\ge(2\pi/L)(1-Cg^{2/3})$ for excited
   nonzero modes, (H2) Schur error $\eta\le Cg^{4/3}/L$ of the $W_2$, $W_3$
   couplings, (H3) gap of $h_3$ plus the even zero-point potential $U(a)$.
   The smallness parameter is $g^{2/3}$ throughout; (H1) fails exactly at
   the crossover $z\simeq2$.
3c. **Done: valley potential.** [Note](../notes/torus-valley-potential.md):
   along the abelian valley the one-loop energy of all modes is exactly
   $U(a)=\frac{2}{\pi^2L}\Phi(La)$, $\Phi(b)=\sum'_m(1-\cos m\cdot b)/|m|^4$
   (Poisson summation; divergent part $a$-independent under a periodic
   cutoff). $U=2|a|+\frac{C_M}{3\pi^2}L|a|^2+\cdots$: the linear term is the
   $k=0$ charged modes, which are C133's four transverse oscillators, so
   the field theory reproduces the G07/G08 mechanism term by term; the
   nonzero-mode correction is $O(g^{4/3}/L)$ with $C_M<0$; $U$ is bounded by
   $O(1/L)$, periodic, with minima at the centre holonomies (electric-flux
   sectors). The crossover $z\simeq2$ is where the holonomy delocalizes.
3d. **Done: (H2) is an ultraviolet problem.**
   [Note](../notes/schur-error-ultraviolet.md): with the fibered vacuum
   the Berry term has Schur error $\simeq\frac{g^{8/3}}{96\pi^2}\log(\Lambda L)\langle|\partial_\xi\psi|^2\rangle\hbar c/L$,
   relative order $g^2\log(\Lambda L)$ (one-loop running); the cubic
   coupling gives a constant two-loop vacuum shift $\sim g^2(\Lambda L)^4\hbar c/L$
   (harmless by the refined lemma with constant shifts) and an energy
   slope $\theta\sim g^2(\Lambda L)^2$ that must be $<1$. So the bare-fiber
   reduction proves the small-volume gap only for $g\ll1/N_s$ (fixed
   lattice, $g\to0$); the renormalized regime $g^2\log N_s\ll1$ needs a
   dressed nonzero-mode vacuum with cutoff-uniform bounds, a T4-type
   renormalization theorem. The corner S splits into (1a) fixed-lattice
   theorem, provable now, and (1b) renormalized theorem.
3e. **Done: the finiteness half.**
   [Note](../notes/finiteness-half-flowed-susceptibility.md): the
   continuum Feynman--Bijl bound with explicit constants,
   $\Delta\le\frac{g^2\hbar c}{2}\int\langle|\delta O/\delta A|^2\rangle/\langle O^2\rangle$
   (only the electric term contributes); at zero momentum it becomes
   intensive, $m\le\frac{g^2\hbar c}{2}\langle|D_\varphi|^2\rangle/\chi_\varphi$,
   which is the $f$-sum rule. Hence $m<\infty$ reduces to
   $\chi_\varphi>0$ for one smeared gauge-invariant observable: if the
   vacuum is not an eigenstate of the flowed energy density, a
   finite-energy excitation exists. Unconditional at fixed lattice;
   the continuum needs (F1), the Hamiltonian counterpart of the flow's
   renormalization. Perturbative scaling $m\le Cg^2\hbar c/\sqrt{8t}$,
   which must fail at $\sqrt{8t_*}\simeq Cg^2\hbar c/m$: the bound
   contains its own consistency condition. $m>0$ untouched.
3f. **Done: free-field value of the flowed bound.**
   [Note](../notes/flowed-bound-free-field.md): for the flowed magnetic
   energy density in the free theory,
   $\chi=3g^4/(2048\pi^{3/2}t^{5/2})$ and
   $\langle|D|^2\rangle=g^2/(128\pi^2t^3)$, so the ratio is
   $16/(3g^2\sqrt{\pi t})$ and the bound is
   $m\le\frac{8}{3\sqrt\pi}\hbar c/\sqrt t\approx4.26\,\hbar c/\sqrt{8t}$:
   **the coupling cancels** (correcting the $g^2$ of the previous note).
   Checked independently by the two-photon $f$-sum rule, which gives the
   same number by a disjoint route. Consequence: weak coupling proves
   nothing, since the bound only reaches $m$ at $\sqrt{8t_*}\simeq4.26\hbar c/m$,
   where the coefficient is nonperturbative.
3g. **Done: the upper side is closed.**
   [Moment hierarchy](../notes/moment-hierarchy-upper-bounds.md): with
   $M_k=\int E^kd\rho$ the moments of the spectral measure of one flowed
   zero-momentum correlator, $m\le M_{k+1}/M_k$ for every $k$, and the
   ratios decrease as $k$ decreases (log-convexity). The $f$-sum bound
   $M_1/M_0$ of the previous notes is the **weakest** member; the next
   one, $m\le\hbar C_0(0)/\int_0^\infty C_0(\tau)d\tau$, needs no gradient
   term and no equal-time smearing, hence **eliminates hypothesis (F1)**
   in favour of Lüscher's own four-dimensional statement. Free-field
   check: $1.504$, $1.329$, $1.128$ in units $\hbar c/\sqrt t$, decreasing.
   Finiteness clause reduced to T4 plus $C_0\not\equiv0$. Also proved
   that **no bound of this type can give $m>0$**: $d\rho=e^{-\hbar c\kappa/E}dE$
   has all negative moments finite with $m=0$.
3h. **Done: T2$'$ restated as absence of a phase transition.**
   [Note](../notes/gapped-set-critical-coupling.md): with
   $c(g)=\liminf_{N_s}\delta(g;N_s)$ and $\mathcal G=\{g:c(g)>0\}$, T1 gives
   $\delta>0$ at every finite volume (the gap is continuous in $g$ there,
   by analytic perturbation theory), T2 gives $[g_0,\infty)\subset\mathcal G$,
   and T2$'$ is $\mathcal G=(0,\infty)$. A vanishing $c$ requires either
   infinite-volume vacuum degeneracy or a diverging correlation length,
   so **T2$'$ = no zero-temperature bulk phase transition**, and on the
   second-order branch = the asymptotically free limit is the only
   continuum limit. $\mathcal G$ is everything iff it is open and closed;
   openness is a volume-uniform stability question (technical: needs a
   Lieb--Robinson bound for unbounded electric terms), **closedness is the
   conjecture**, and for $U(1)$ the gapped set is open and fails
   closedness at $g_c$.
3i. **Next:** the openness half, i.e. volume-uniform stability of the
   gap under a change of coupling. Sub-question to settle first: a
   Lieb--Robinson bound for the Kogut--Susskind Hamiltonian, whose
   electric term is unbounded; the truncation of link representations
   with controlled error is the candidate route, and it is the same
   truncation the Schur note needs.
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
