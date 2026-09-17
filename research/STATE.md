# State

Updated 2026-09-17. Read this page and the note it points to; AGENTS.md
governs. Older files in this directory are context.

## Goal

User direction, 2026-09-17: the $SU(3)$ mass-gap attack is stuck at the
map in the position note, and the active goal returns to the **Planck
gap**: a logical argument, from Newton-age materials, that $h>0$ in the
Galileo comparison, where Newton explicitly took the inertial--parabola
area to zero (Lemmas X--XI) to mark the difference between free and
forced motion. The mass-gap sections below are retained as context and
are no longer the queue.

## What is in hand for the Planck gap

[The mark-floor note](../notes/newton-mark-floor.md) (N02) settles the
form of the argument. Newton's limit has no geometric floor (every
partition's impulses, sagittas and areas vanish with the mesh). A floor
follows for *recorded* comparisons from three premises stated in Newton's
optics: least corpuscle impulse $p$ (Query 29), least mark length equal to
the interval of fits $\Lambda=1/89000$ inch (Book II Part III Prop. XVIII),
and the mark trade-off $\delta\,\Delta\ge\Lambda p$ between a mark's
resolution and the indeterminacy of the impulse it delivers (M3). Then
$	au\Delta E=F^2	au^3/2m>8\Lambda p$, the inertial--fall area exceeds
$8v\Lambda p/3F$, and Democritus insertion of marks stops at the mesh
$	au_*=(16m\Lambda p/F^2)^{1/3}$; on the modern identification
$\Lambda p=h/2$ the floor is $4h$. Keeping Newton's determinate fits and
dropping M3 is an exact countermodel with floor zero (the far-screen
recovery of the recoil), so M3 is the single premise carrying $h>0$: an
indeterminacy premise, statable by Newton and denied by him. Q14's
dimensional gate explains why both a least length and a least impulse
are needed and why they enter as a product.

## Next steps for the Planck gap (each a note)

1. **Does M3 have a consistency derivation?** Require that marks on
   probes obey the same premise as marks on bodies, and ask whether any
   deterministic record model survives without the far-screen loophole;
   this is where a non-commuting record structure (G07's two scale-free
   non-commuting structures) must enter, or where the argument stops.
2. **Phase-space form.** State Theorem 1 of the mark-floor note for a
   general force law and for the C070--C071 force lens, whose canonical
   area $2F^2\ell^3/3m$ is the same combination, so the floor is a
   statement about the lens rather than the parabola.
3. **Opticks companion.** A `docs/classics/` companion for Book II Part
   III Props. XII--XVIII, Book II Part I Obs. 13 and Queries 1 and 29
   (pre-1901 source; cited from the 1730 text without one).

## Paused goal: $SU(3)$ mass gap (2026-09-16 to 2026-09-17)

Prove the existence of a mass gap for **$SU(3)$ in four dimensions**
(user direction, 2026-09-16; Jaffe--Witten statement in the
[digest](../notes/millennium-problem-definitions.md), narrowed from all
compact simple groups to the physical case). Progress is measured in
theorems with explicit $L$, $a$, $g$ dependence and in the removal of one
obligation at a time. [The SU(3) constants](../notes/su3-constants.md)
fix every number: $C_2=4/3$, $\dim G=8$, centre $\mathbb Z_3$,
$b_0=11/(16\pi^2)$, $\beta=54/g^4$, $v\le261c/g^2$, $\Delta V=\frac{16}3(3|\mathcal P|-V)$,
$|\nabla V|^2\le48V$, and about $21$ renormalization doublings from
$g_{\rm UV}^2=1/2$.

## What is in hand

[The position note](../notes/mass-gap-position.md) is the synthesis: six
named statements, T1 and T2 proved here, the finiteness clause reduced
to T4 plus one nonvanishing flowed correlator, two routes closed by
computation (real-space blocking; expansion around the free theory), and
three places where the non-abelian structure is isolated. Read it first;
the items below are the working queue.

## Next steps (each a note)

The position note carries the current coupling map (strong side explicit
at $g^2\ge176$ for the Wilson transfer matrix, weak side crude at
$1/g^2\gtrsim10^2$, intermediate region between) and the division of
labour; consult it before opening a new item.

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
3i. **Done: Lieb--Robinson for Kogut--Susskind.**
   [Note](../notes/lieb-robinson-kogut-susskind.md): the unbounded part
   of the Hamiltonian is a sum of commuting single-link Laplacians, so
   the interaction picture generated by it leaves a time-dependent
   bounded finite-range interaction of unchanged norm and support, and
   the standard theorem applies. Velocity $v=2eaJ/\hbar\le32eNc/g^2$ with
   $J=16N\hbar c/(g^2a)$, uniform in volume. Consequences: strong-coupling
   correlation length $\xi\le C'aN/(\gamma C_2g^4)$ by the clustering
   theorems; the lattice light cone exceeds $c$ for $g^2<32eN$, so
   relativistic causality is recovered only along the scaling curve;
   openness of $\mathcal G$ now rests on one missing ingredient, a gap
   stability theorem that does not assume frustration-freeness (the
   Kogut--Susskind Hamiltonian is frustration-free only at $g=\infty$).
3j. **Done: the one-step blocking inequality.**
   [Note](../notes/blocking-step-obstruction.md): with blocks of $M^3$
   sites, $6M^2$ straddling plaquettes per block of norm
   $4N\hbar c/(ag^2)$, the naive Schur estimate $\|B\|^2/\Delta_M$ exceeds
   the gap by $M^4N^2/(g^4\delta^2)$. Lemma 1$'$ identifies the waste: that
   estimate measures the **boundary energy**, which is a constant shift
   and costs nothing; what enters the gap is the **variation** of the
   Schur term. A connected estimate replacing $(\sum_p\|w_p\|)^2$ by
   $\sum_p\|w_p\|^2$ turns $M^4$ into $M^2$ and closes one step when
   $g^4\gtrsim8\sqrt{6C}MN/(\gamma C_2)$, a fixed threshold. Since the
   coupling grows toward the infrared, the induction closes above that
   threshold, and reaching it from the cutoff takes
   $n\simeq(1/(2b_0\log2))(g_{\rm UV}^{-2}-g_{\rm thr}^{-2})$ doublings,
   of order thirty for $SU(2)$ at $g_{\rm UV}^2=1/2$. **The difficulty is a
   finite number of steps in the intermediate regime**, each generating
   couplings outside the Kogut--Susskind family.
3k. **Done, negative: blocking gains nothing.**
   [Note](../notes/blocking-criterion-monotone.md): Yarotsky's §2 is a
   polymer expansion (Lemma 1: $\|T_I\|\le(2\alpha e^{t_0\beta/\alpha})^{|I|}$;
   Lemma 3: weights damped exponentially in the excited region), so the
   connected estimate the blocking step wanted **is available**, and his
   theorem applies directly to a lattice of blocks. The criterion is then
   $\beta_{\rm block}=24M^2N/(g^2\delta(g;M))$, and $\delta(g;M)$ is flat in
   $M$ at strong coupling (flux-loop energy $2C_2g^2$) and falls like
   $1/M$ at small volume, so $\beta_{\rm block}/\beta_{\rm direct}\simeq3M^2/8$:
   **blocking is strictly worse than no blocking**, at every coupling.
   This corrects §§4--5 of the previous note. Boundary grows like $M^2$,
   gap does not grow; the only gain available is a redefinition of the
   coupling, which is the renormalization step itself.
3l. **Done: the flow cannot serve as the change of variables.**
   [Note](../notes/flow-conjugation-truncation.md): the Wilson flow is a
   diffeomorphism of $G^{\mathcal E}$, hence unitarily implemented by
   $(W_t\psi)(U)=\rho_t(U)^{1/2}\psi(\Phi_t(U))$, so conjugation preserves
   the spectrum. It sends the magnetic term to the flowed action
   (monotonically decreased) and the electric term to the
   Laplace--Beltrami operator of the pulled-back metric, of range
   $\sqrt{8t}$. Free case: exact cancellation, $e^{-2tk^2}$ against
   $e^{+2tk^2}$, frequencies $ck$ unchanged. A locality-based criterion
   would improve by $e^{-4tk^2}$, which only shows that such criteria are
   **not conjugation-invariant**: the gain is charged in full to the
   truncation restoring locality. Three routes to $m>0$ that avoid the
   constructive step are now closed by computation.
3m. **Done: the truncation error of a flow step.**
   [Note](../notes/flow-jacobian-truncation-error.md): the linearized
   flow is $\partial_s\delta B_\mu=D^2\delta B_\mu+2[G_{\mu\nu},\delta B_\nu]$,
   so by Kato's inequality and Duhamel the Jacobian obeys
   $|D\Phi_t(x,y)|\le e^{2t\|G\|_\infty}K^{\rm free}_t(x-y)$. Truncating at
   range $R=\kappa\sqrt{8t}$ costs $\exp[2t\|G\|_\infty-2\kappa^2]$, so the
   step is accurate **exactly when $\|G\|_\infty\lesssim\ell^{-2}$**: the
   small-field condition of constructive RG, derived rather than assumed,
   and the reason Balaban's programme splits small- from large-field
   regions. The flow's monotonicity gives $\|G\|_{L^2}$ only; the missing
   estimate is the $L^\infty$ bound, and the Hamiltonian framework has no
   probabilistic route around it.
3n. **Done: the obstruction is the large-field tail.**
   [Note](../notes/typical-field-strength-window.md): the free flowed
   field has $\langle|b_t|^2\rangle=g^2/(16\pi^2t^2)$, so
   $t\langle|b_t|^2\rangle^{1/2}=g/(4\pi)$, independent of $t$ and $a$.
   The truncation error $\exp[2t\|G\|_\infty-2\kappa^2]$ is then below
   $e^{-1}$ on typical configurations at **any** coupling, with range
   factor $\kappa\ge\sqrt{g/4\pi+1/2}$: the small-field condition is a
   statement about the supremum, not about the typical size. The tail
   obeys $\mathbb P(\|b_t\|_\infty>\eta/t)\lesssim V(8t)^{-3/2}e^{-8\pi^2\eta^2/g^2}$,
   which the Euclidean measure absorbs (Balaban's large-field split, here
   derived rather than assumed) and for which the Hamiltonian framework
   has no counterpart, since it has a state and no integration over
   configurations.
   **The Hamiltonian route of this programme terminates here**, in a
   well-defined way.
4. **Done, correcting the previous two: truncation is free on the lattice.**
   [Note](../notes/lattice-truncation-uniform.md): the lattice flow is
   coupling-independent ($g^2$ cancels $1/g^2$ in Lüscher's (1.4)), a
   doubling is dimensionless flow time $t/a^2=1/2$, and compactness gives
   $a^2\|G\|_\infty\le\pi$, so $2t\|G\|_\infty\le c_A\pi$: a pure number.
   Truncating at range $Ka$ costs $Ce^{-cK}$ uniformly in coupling,
   spacing, volume; $K=3$ suffices. The large-field difficulty is a
   statement about the **composition** of many steps at fixed physical
   scale, not about one step. Conjugation is exact, truncation cheap, and
   neither coarsens the theory: **the obstruction is decimation**.
5. **Done, negative: flowing before decimating changes nothing.**
   [Note](../notes/flow-before-decimation.md): $\Phi_t$ is a bijection of
   the configuration space, so $\|V\circ\Phi_t\|_\infty=\|V\|_\infty$ even
   though $V\circ\Phi_t\le V$ pointwise; and conjugation is unitary, so the
   block gap is unchanged. Hence $\beta_{\rm block}$ is exactly as before
   and blocking still loses by $3M^2/8$. More generally any criterion
   depending on $H_0$ through its spectrum and on $\phi$ through
   $\|\phi\|_\infty$ is invariant under (conjugation, composition with the
   flow). **Every norm-based method in this programme is now exhausted**,
   each closed by computation.
6. **Done: the Agmon bound.**
   [Note](../notes/agmon-ground-state-suppression.md): the configuration
   space is a closed Riemannian manifold, so the Agmon identity
   $A'\int|\nabla(e^\rho\Omega)|^2+\int(B'V-e_0-A'|\nabla\rho|^2)e^{2\rho}\Omega^2=0$
   holds with no boundary term, giving
   $\int e^{2(1-\delta)d}\Omega^2\le C(\delta)$ for the Agmon distance $d$ in
   the metric $\sqrt{(B'V-e_0)/A'}$, $B'/A'=4/g^4$. A configuration with
   $n$ excess plaquettes sits at distance $\simeq n\sqrt{2v}/g^2$, so the
   ground-state measure suppresses it like $e^{-2n\sqrt{2v}/g^2}$: **the
   coupling dependence of the Euclidean Wilson weight**, strong exactly at
   weak coupling where the renormalization steps live. This is the
   Hamiltonian counterpart of the large-field estimate.
7. **Done, correcting item 6: the Agmon bound is global.**
   [Note](../notes/agmon-global-not-local.md): carrying out the distance
   estimate with constants gives
   $d\ge\frac{4}{3g^2}f_0^{3/2}/\|\nabla V\|_\infty$ with
   $\|\nabla V\|_\infty\le2\sqrt{2N|\mathcal E|}$, **extensive**. So the bound
   controls the global excess, $\int_{\{V-\bar v\ge w|\mathcal P|\}}\Omega^2\le
   C\exp[-\frac{2\sqrt2}{3}\frac{w^{3/2}}{g^2\sqrt N}|\mathcal P|]$, and gives
   nothing for a fixed local region in a large volume. Structural reason:
   Agmon's forbidden region is defined by the total potential exceeding
   the total energy, and a local excess never makes an extensive total
   exceed its mean. The Euclidean weight factorizes over plaquettes and
   therefore gives the local statement for free.
8. **Done, negative: pointwise Gibbs domination fails too.**
   [Note](../notes/magnetic-energy-identities.md). Two exact identities
   fall out: $\Delta V=4C_2(N|\mathcal P|-V)$, since $V$ shifted by its Haar
   mean is a Laplacian eigenfunction, and $|\nabla V|^2\le16V$ for $SU(2)$.
   They give an exact ground-state sum rule (Proposition 3) tying
   $\operatorname{Var}_\Omega(V)$ to kinetic quantities. And they make the
   comparison attempt explicit: $\varphi=e^{-\lambda V/2}$ satisfies
   $L\varphi\ge0$ only above $V_*\simeq N|\mathcal P|$, so the maximum
   principle again bounds $\Omega$ only by its **global** excess.
   **Structural reason, stated once:** every inequality derived from
   $-A'\Delta\Omega+(B'V-e_0)\Omega=0$ compares total potential with total
   energy, and $e_0$ is extensive; the Euclidean weight factorizes over
   plaquettes and separates configurations locally by construction.
9. **Done: consolidation and specialization.**
   [The position note](../notes/mass-gap-position.md) is rewritten as one
   argument: seven closed routes in two families, with the reason the
   ground-state family fails stated once (the eigenvalue equation carries
   the extensive $e_0$; the Euclidean weight factorizes).
   [The SU(3) note](../notes/su3-constants.md) evaluates every constant
   for the narrowed goal and records the two features $SU(2)$ lacks, a
   complex defining representation and a $\mathbb Z_3$ centre.
10. **Done: the ground-state measure is the Euclidean time-slice marginal.**
   [Note](../notes/ground-state-measure-transfer.md): for the
   Kogut--Susskind Hamiltonian as the $a_t\to0$ limit of the anisotropic
   Wilson transfer matrix (Lüscher 1977; Creutz 1977, metadata),
   $|\Omega|^2d\mu$ is the time-slice marginal of $e^{-S_E/\hbar}$, so every
   **local** Euclidean estimate transfers to the ground state. The
   obstruction of items 7--8 was a feature of the representation: the
   eigenvalue equation carries the extensive $E_0$ and compares totals,
   the Euclidean weight factorizes over plaquettes and compares locally.
   The large-field estimate then has its standard scale-invariant form:
   coherent field $\eta/\ell^2$ over a block of side $\ell$ costs
   $S_E/\hbar\simeq\eta^2/(4g^2)$, **independent of $\ell$ and $a$**, so the
   suppression is $e^{-c\eta^2/g(\ell)^2}$, matching the independent
   free-field Gaussian tail $e^{-8\pi^2\eta^2/g^2}$.
11. **Done, answered no: the growth factor is sharp.**
   [Note](../notes/flow-instability-large-field.md): the curvature
   operator $(Mu)_\mu=2[G_{\mu\nu},u_\nu]$ is **symmetric** (the
   antisymmetry of $\operatorname{ad}$ and that of $G_{\mu\nu}$ cancel on
   transposing), so it attains $+2\|G\|_\infty$, and in a constant
   chromomagnetic background the eigenvector is the charged gluon in the
   lowest Landau level with aligned spin, $\omega^2=k_\parallel^2-gB$: the
   **Nielsen--Olesen mode** (Nucl. Phys. B144 (1978) 376, metadata). Under
   the gradient flow it grows at exactly $2\|G\|$, saturating the Duhamel
   bound. Consistent with monotonicity because a constant chromomagnetic
   field is a saddle of the action, stationary under the flow with a
   negative Hessian direction. So **the flow smooths small fields and
   amplifies large ones**, the crossover of item 10 is real, and the
   large-field region must be excluded rather than flowed.
12. **Done: the large-field entropy is beaten.**
   [Note](../notes/large-field-entropy-count.md). Not divergent: the
   configuration space is compact, so $S_E$ attains a minimum on the
   closed constraint set with nonnegative Hessian on the tangent cone.
   The count of unstable directions in a constant background
   $gB=\eta/\ell^2$ on a block of side $\ell$ is
   (Landau degeneracy $gB\ell^2/2\pi$) $\times$ ($k_3^2+k_4^2<gB$, giving
   $gB\ell^2/4\pi$) $=\eta^2/(8\pi^2)$, **independent of $\ell$ and $a$**,
   against the action cost $\eta^2/(4g^2)$: ratio $2\pi^2/g^2$, uniform in
   $\eta$ and the scale. So the large-field sum converges for
   $g^2\lesssim20$ and the answer is "slow, not divergent", with the
   slowness quantified as a fraction $g^2/(2\pi^2)$ of the exponent.
13. **Done: the large-field corner is closed as an estimate problem.**
   [Note](../notes/large-field-action-lower-bound.md). Writing the
   constraint in the variable the action measures,
   $K_\eta=\{\ell^{-4}\int_{\rm block}|G_t|^2\ge\eta^2/\ell^4\}$ with
   $\sqrt{8t}=\ell$, the bound is two steps: the flow decreases $S_E$, and
   the flowed action exceeds its restriction to the block. So
   $\inf_{K_\eta}S_E/\hbar\ge\eta^2/(4g^2)$, **uniform in $\ell$, $a$, the
   volume and the group**, and **sharp** (a field of magnitude
   $\eta/\ell^2$ on the block attains it). The Nielsen--Olesen instability
   does not obstruct it: every descent direction lowers the flowed block
   average and so leaves $K_\eta$; the constant field is a saddle of the
   unconstrained action and a minimizer of the constrained one. Corner
   assembled: cost $\eta^2/(4g^2)$, entropy $\eta^2/(8\pi^2)$, truncation
   error $e^{2\eta}$, net weight
   $\exp[-\frac{\eta^2}{4g^2}(1-Cg^2/2\pi^2)]$, all scale-invariant.
14. **Done: the large-field region needs an operator inequality, and the
   measure statement is weaker.**
   [Note](../notes/large-field-operator-inequality.md). Positive facts:
   truncation inside $Q$ costs only range $K\gtrsim\eta_\infty/(4c)$ (the
   earlier competition was a fixed-$K$ artifact); IMS localization at
   radius $2a$ costs $L_B\le C_L(\hbar c/a)g^2/\eta^2$, $C_L=32\pi^2c_0^2/3$,
   on the transition region; positive rare perturbations are harmless,
   $\operatorname{gap}(H+W)\ge\operatorname{gap}(H)-\langle\Omega,W\Omega\rangle$.
   The obstruction is the sign: the chain needs
   $\chi_Q(H-E_0)\chi_Q\ge c_1(\hbar c/a)(\eta^2/g^2)\chi_Q^2$, and its
   Hamiltonian proof loses $C_V|\partial N|\,\hbar c/a$ on $P$ (cutting
   the vacuum costs zero-point energy per shared link), a negative
   perturbation of the order that binds regardless of the measure of its
   support. The Euclidean polymer expansion consumes measure statements
   directly, which is why the constructive programme is Euclidean.
   Division of labour: Hamiltonian for T1, T2, small volume, upper
   bounds, final gap extraction; Euclidean for the renormalization steps.
   Coupling map for $SU(3)$: weak-coupling expansion for $1/g^2\gtrsim10^2$
   with crude constants, strong coupling for $54/g^4\le\beta_*$, and an
   intermediate region where the gap forms, $10^3$ doublings wide with
   these constants and $20$ if the weak side reaches $g^2\sim1/2$.
15. **Done: the strong-coupling threshold made explicit.**
   [Note](../notes/strong-coupling-threshold-explicit.md). Following
   Yarotsky's proof with numbers (bounded perturbation, optimal
   $\alpha=t_0\beta_0$, activity $2et_0\beta_0e^{64t_0}$ per perturbed site,
   Kotecký--Preiss with entropy $c\simeq220$, $t_0\ge7.1$) gives
   $\beta_*\simeq e^{-465}$ and $g_0^2\simeq10^{101}$ for $SU(3)$: the region
   T2 covers is empty in practice. A direct expansion (Kirkwood--Thomas,
   Datta--Kennedy, or Osterwalder--Seiler) has radius
   $\beta\lesssim1/(12e)$, i.e. $g_0^2\sim40$--$70$. The intermediate
   region's width is set by the weak side. **Done for the Wilson transfer matrix:**
   [note](../notes/wilson-strong-coupling-explicit.md). The character
   expansion is a polymer gas of closed plaquette surfaces (smallest: a
   cube, six plaquettes), activity per plaquette $\rho=d_fc_f/c_0=1/g^2$
   for $SU(3)$ to leading order; Kotecký--Preiss with plaquette adjacency
   $20$ and $n\ge6$ converges for $20e^2\rho\le0.84$; a tube has four
   plaquettes per unit length, so correlations decay at rate
   $4\log(1/(176\rho))$; link reflection positivity transfers this to
   $H_W=-(\hbar c/a)\log\mathcal T$. Result: $SU(3)$ gapped uniformly in
   volume for $g^2\ge176$ with the fundamental alone, and rigorously for
   all representations for $g^2\ge1056$ with
   $\Delta_W\ge(\hbar c/a)\,4\log(g^2/1056)$, via $c_0\ge1$ (Jensen) and
   $\sum_{r\ne0}d_rc_r\le e^{\beta_W}-1$ (dimension count of tensor powers).
   **Done for Kogut--Susskind too:**
   [continuous-time note](../notes/kogut-susskind-strong-coupling-explicit.md).
   Duhamel expansion in the plaquette term with exact electric decay
   between insertions; Gauss's law gives $|S_k|\ge4$; Kotecký--Preiss
   with $a=n+\lambda|\operatorname{supp}|$; the entropy $64|S_{k-1}|$ of the
   next insertion cancels against the denominator $1/((\varepsilon-\lambda)|S_{k-1}|)$.
   Result: $\Delta_{\rm KS}\ge\frac83g^2(1-\theta)\,\hbar c/a$ for
   $g^4\ge\max(3132/\theta,\,783/\sqrt{\theta(1-\theta)})$, so $g^2\ge79$
   gives $\frac43g^2$ and $\gamma\to4$ in the adjacent-growth class; the
   general shapes are counted by a spanning tree of consecutive
   touchings at a factor $24$ per insertion, giving the rigorous
   threshold $g^2\ge388$ for the same gap. Both
   regularizations now have $g_0^2\sim10^2$.
   [The target box](../notes/strong-coupling-target-box.md): the
   expansion survives gauge-invariant $q$-link corrections of local norm
   $\eta$ and a deformation $\eta_E$ of the electric term, with
   tolerance $\eta_*\simeq g^2(1-\eta_E)/(6e\,2^q)$: at $g^2=100$,
   $\eta\le0.29$ for plaquette-like terms and $\eta\le0.0066$ for
   two-plaquette terms. The mass-gap problem is now the statement that a
   renormalization scheme that is an exact low-energy reduction keeps
   the effective Hamiltonian in this class and reaches $g^2\sim10^2$;
   the intermediate region is where that is open, and the finish line
   is a box with numbers.
   [Why the abelian theory misses the box](../notes/abelian-misses-the-box.md):
   the expansion is group-blind, so compact $U(1)$ is gapped in the box
   too; the difference is the flow, $b_0=0$ for pure $U(1)$ (free photon
   is a fixed point at every weak coupling, Guth; Fröhlich--Spencer) and
   $b_0=11/(16\pi^2)$ for $SU(3)$. The mass gap is the statement that the
   running does not stop before the box.
16. **Done: the intermediate region as a finite verification.**
   [Note](../notes/intermediate-region-finite-verification.md). The
   Wilson measure is a lattice spin system with compact spins, product
   a priori measure and finite-range interaction, so the
   Dobrushin--Shlosman complete-analyticity conditions (JSP 46 (1987)
   983) and the Martinelli--Olivieri strong-mixing conditions (CMP 161
   (1994) 447, 487) apply; Elitzur is no obstruction. Any of them at a
   coupling $\beta_W$ gives uniform exponential decay, hence via link
   reflection positivity a gap of $H_W$ uniformly in volume. They are
   finite computations on boxes of a few $\xi/a$, open in the
   interaction norm, so intervals are covered by finitely many checks;
   feasible in principle exactly in the intermediate region. The box
   becomes the verified interval with its openness radius as tolerance.
   **A sufficient route: the trajectory of effective interactions from
   $g\to0$ enters the open set $\mathcal{CA}$ of completely analytical
   interactions**, which contains Wilson at $g^2>444$; its two-number
   form is $g_{\rm RG}^2\ge g_{\rm DS}^2$ (note §4b: sufficient not
   necessary; target is a set in interaction space; only the trajectory
   matters; oscillation bounds cannot improve on the single-link
   threshold, blocks help only through internal screening). Neither
   number is known; the verification is numerics outside this
   repository's rules.
   [Dobrushin note](../notes/dobrushin-uniqueness-wilson.md): the
   single-link Dobrushin condition for the Wilson action is checkable by
   hand, one staple changes, $\rho\le e^{4\beta_W}-1$, $18$ neighbours, so
   $\alpha\le18(e^{4\beta_W}-1)<1$ for $g^2>148N=444$; Künsch's decay plus
   reflection positivity give $\Delta_W\ge(\hbar c/a)\log(g^2/432)$,
   the best rigorous Wilson threshold. The block
   (Dobrushin--Shlosman) criterion is the finite verification, stated as
   a specification: $\sum_{x\in V}\sum_{y\notin V}\rho_V(x,y)<|V|$.
   [What would unblock](../notes/what-would-unblock.md), the review's
   negative results: Griffiths-type inequalities break for $SU(N)$ (signed
   recoupling in the dual gas, no $O(N)$ form, non-ferromagnetic
   interaction), and the centre-based ones that exist (Mack--Petkova,
   Tomboulis--Yaffe) concern the string tension, whose comparison
   theory deconfines at weak coupling; chessboard gives large deviations, not mixing; infrared
   bounds need Gaussian domination, absent on a non-abelian manifold;
   Knabe needs frustration-freeness; exact dualities are abelian; gauge
   fixing moves $444$ to about $330$ only. Two unblocking routes: a
   correlation inequality for $SU(3)$ (new mathematics) or the
   computer-assisted block verification (a rules decision).
   [Bands note](../notes/confinement-scale-bands.md), two corrections:
   Elitzur makes single-link marginals of interior links Haar, so the
   single-link block criterion is blind to the interior and the mixing
   form on sub-blocks (conditional distribution of small Wilson loops)
   is what a verification computes; and published data (Necco--Sommer
   $r_0/a$, Morningstar--Peardon $r_0m_{0^{++}}=4.21$) give $\xi/a=0.70$
   at $\beta_W=5.7$, so the boxes are of side $3$ to $5$, $216$ to $2000$
   links, three to four orders below the earlier estimate. Three bands:
   A, $\beta_W<0.0135$, proved; B, up to $5.7$, $\xi/a<1$ with no rigorous
   method (a factor $50$ in $\beta_W$ beyond any expansion); C, the
   renormalization group's, ten doublings from $g^2=1/2$, of which three
   carry $\xi/a$ from $10$ to $1$. The meeting point located (§2b): band
   B is crossed by two blocking steps ($u\to u^4$ per doubling, Kadanoff
   1976, heuristic; block-spin images Gibbsian under strong mixing, van
   Enter--Fernández--Sokal 1993), so the verification is needed at one
   coupling, $\beta_W\simeq6$, $g^2\simeq1$, $\xi/a\simeq1$, boxes of
   side $3$ to $5$; $g_{\rm DS}^2\simeq1$ conditional on that box and the
   requirement on the other side is $g_{\rm RG}^2\ge1$. Corrected: the
   area law with $\sigma a^2\simeq0.16$ gives coarse activities $0.53$,
   $0.077$, $3.6\times10^{-5}$ at $k=1,2,3$, so band B takes **three**
   steps (Migdal--Kadanoff's $u\to u^4$ overestimates). **In one
   sentence: the mass gap for $SU(3)$ is the control of about six
   consecutive blocking steps at order-one coupling, uniformly in
   volume**, three from the weak side and three from the strong.
17. **Done: the map as one conditional theorem.**
   [Note](../notes/mass-gap-conditional-theorem.md). H1: at every
   blocking step before the last, the integrated fluctuations cluster
   exponentially at the step's scale (rate $\gamma_*$), and the
   trajectory arrives within radius $r$ of a reference interaction
   $\Phi_0$; H2: $\Phi_0$ (Wilson at $\beta_W\simeq6$) is strongly mixing
   on one box of side $3$ to $5$ with margin covering radius $r$.
   Conclusion: decay at rate $\min(\gamma_*,\gamma')/2^K$ per fine unit,
   transfer-matrix gap by reflection positivity uniformly in volume,
   and $m\ge\hbar c\min(\gamma_*,\gamma')/a_*$ in the continuum, with
   $a_*\simeq0.1$ fm; the true rate is $ma_*\simeq0.78$ by the data. A
   proof of the mass gap for $SU(3)$ consists of H1 and H2; nothing
   else is missing.
18. **Direction (user, 2026-09-17): the reasons to stop are reasons to
   research.** [Note](../notes/reasons-to-stop-as-research.md). A
   Griffiths-type inequality transfers control from weaker to stronger
   coupling only (string tension and zero-mean channels monotone), so it
   would replace band B's three steps by H2 and leave the weak side
   untouched; GKS-II for $SU(2)$, $SU(3)$ is open (the single-site
   character-cone condition holds in every case computed; the plaquette
   term is not in a product cone). A certified verification at
   $\beta_W\simeq6$ is beyond every certified method (dimension $10^3$ to
   $10^4$); certified polymer enumeration reaches $\beta_W\sim1$. So the
   research is H1, in two parts: H1a sharpness (no explicit constant
   exists for one small-field step) and H1b the last three doublings.
   **Line opened: one Euclidean small-field blocking step for $SU(3)$
   with explicit constants**, deliverable $g^2_{\rm pert}$, the weak-side
   counterpart of $0.0135$.
   [Part 1, Gaussian level](../notes/small-field-step-gaussian.md):
   intertwining averaging $Wd=\bar dW_0$ (sixteen two-link paths per
   coarse link); Feynman gauge makes the step $32$ copies of one scalar
   conditional-Gaussian problem (massless field given tube averages);
   exact decomposition with $C_{\rm fl}=g^2(P(-\Delta)P)^{-1}|_K$ and
   $\bar S_2=\frac1{2g^2}\langle\bar f,(WGW^T)^{-1}\bar f\rangle$; block
   Poincaré $\langle f,-\Delta f\rangle\ge\frac49\|f\|^2$ on tube-mean-zero
   $f$ (tube $2^3\times3$ box, $\lambda_2=1$, weighted-mean correction
   $\frac18$, bond multiplicity $2$), so $\|C_{\rm fl}\|\le\frac94g^2$ and
   rms link fluctuation $\le\frac32g$; sharp constant in $[\frac49,4]$;
   coarse form is Wilson at the same $g^2$ (4D scale invariance).
   **Sharpness begins at the propagator**: generic Combes--Thomas gives
   decay rate $7\times10^{-4}$ per lattice unit against a true rate of
   order one.
   [Part 1b](../notes/small-field-step-decay-and-threshold.md): the
   literature (Dimock §2.4, read from arXiv text; Balaban 1984) proves
   the decay with no explicit constant ("$M$ sufficiently large"); the
   soft-constraint operator $-\Delta+aQ^TQ$ is local with gap $\frac29$
   for $a\ge130$ and Combes--Thomas rate $1.7\times10^{-3}$ (proved); the
   order-one rate is reduced to a zero-free strip of the explicit
   folded-symbol denominator $D=|\hat w|^2+\hat k^2R$ (set up, not done).
   Threshold shape: tree-graph covariance sums $\simeq72/\kappa^4$,
   adjacency $20e$, cubic vertex $C_3g$ with $C_3\sim20$, so
   $g_{\rm pert}\simeq\kappa^4/(1.1\times10^4C_3)$: $g^2_{\rm pert}\sim10^{-12}$
   at an ideal $\kappa=\frac12$, $10^{-35}$ at the proved rate (scaling
   estimate, labelled). **The weak side's explicit deficit is twelve
   orders of magnitude in $g^2$ against the physical onset $g^2\simeq1$,
   where the strong side's is a factor $400$.** H1a closed as not viable
   by constant-chasing; H1 is a methods problem at order-one coupling,
   and the map ends there.
19. **Aside, recorded at the user's request:**
   [holography in the lowest dimensions](../notes/holography-lowest-dimensions.md).
   At $d=0$ the bulk is a one-manifold classified by its endpoints: one
   point gives $\Omega(x)$ (Hartle--Hawking), two give the propagator, which
   read as a state on its endpoints is the thermofield double at
   $\beta=2T$, with the gap as the disentanglement rate of the two ends
   (a cut at an intermediate time is the semigroup property and inserts
   nothing), none
   gives $\operatorname{Tr}e^{-\beta H/\hbar}$, $k>2$ give Feynman graphs
   (Schwinger parameters as einbein moduli); a 0d scalar integral has a
   bare graph as bulk and a matrix integral thickens it to a surface
   ('t Hooft). At $d=1$ it is the Schwarzian/SYK system, gapless; the holographic gap
   mechanism is a capped-off infrared geometry at large $N$.
20. **Done: the $d=3$ formulation.**
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

While the mass gap was the goal, the Galileo area/necessity question
(N01, N02) and the $h>0$ analogy (G07, G08, C131--C133) served it as
heuristics; since 2026-09-17 the roles are reversed and the mass-gap
map is the supporting material. Publication drafts wait for author input.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows; at most one
sequential source worker. Commit and push after each result.
