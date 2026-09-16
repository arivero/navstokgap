# The mass gap: current position of this programme

This is the synthesis of the notes written since the goal was set to a
proof of the Yang--Mills existence and mass-gap conjecture. It states
what has been proved here, what has been imported, what has been ruled
out, and what remains, with constants explicit and each claim labelled.

The short version: the conjecture decomposes into six named statements,
of which two are proved here and one is imported. The clause
$m<\infty$ is closed as far as variational methods reach, and reduced to
the existence of the theory plus the nontriviality of one flowed
correlator. The clause $m>0$ is untouched, and **seven routes to it have
been closed by explicit computation**, in two families: those built from
operator norms and spectra, and those built from the ground state of the
Hamiltonian. Both families fail for reasons now stated exactly, and the
second failure identifies what the Euclidean formulation supplies that
the Hamiltonian one does not.

## 1. The decomposition

[The obligations map](mass-gap-obligations-lattice.md) turns
"prove the mass gap" into six statements about the Kogut--Susskind
Hamiltonian
$$H=\frac{\hbar c}{a}\Big[\frac{g^2}{2}\sum_{\ell}(-\Delta_\ell)
+\frac2{g^2}\sum_p\big(N-\operatorname{Re}\operatorname{tr}U_p\big)\Big],
\qquad \Delta_{a,L}=\frac{\hbar c}{a}\,\delta(g;N_s,G).$$

| | statement | status |
| --- | --- | --- |
| T1 | finite lattice: unique physical ground state, $\delta>0$ | **proved here** |
| T2 | $\delta\ge\gamma(g^2/2)C_2$ for $g\ge g_0$, uniform in volume | **proved here** from an imported theorem; explicit for the Wilson transfer matrix, $g^2\ge176$ |
| T2$'$ | $\liminf_{N_s}\delta>0$ for every $g>0$ | open; false for $U(1)$ |
| T3 | $\delta_\infty(g)/(a\Lambda_{\rm lat}(g))\to m/(\hbar c\Lambda)\in(0,\infty)$ | open |
| T4 | continuum infinite-volume theory with the axioms | finite-volume ultraviolet stability known |
| S | small volume: $\Delta=\delta_1g^{2/3}\hbar c/L\,[1+O(g^{2/3})]$ | upper side proved, lower side fixed-lattice only |

The conjecture is T2$'$ together with T3, given T4, and
[the critical-coupling note](gapped-set-critical-coupling.md) shows that
T2$'$ is exactly the absence of a zero-temperature bulk phase
transition, hence on its second-order branch the uniqueness of the
continuum limit.

## 2. What is proved here

**T1** ([obligations map](mass-gap-obligations-lattice.md) §2): compact
resolvent, a simple strictly positive ground state, a positive gap
inherited by the physical sector, for every $a$, $N_s$, $g$ and compact
connected $G$.

**T2 in Hamiltonian form** ([T2 note](strong-coupling-uniform-gap.md)):
the electric term is classical in the Peter--Weyl partition and the
magnetic term is a bounded range-$\{0,1\}^3$ perturbation with
$\beta=48N^2/[g^4(N^2-1)]$, so Yarotsky's theorem gives
$\Delta_{a,L}\ge\gamma(g^2/2)C_2\hbar c/a$ for $g\ge g_0$, uniformly in
the lattice size, with exponential clustering.

**A Lieb--Robinson bound** ([note](lieb-robinson-kogut-susskind.md)):
velocity $v\le32eNc/g^2$, uniform in volume, because the unbounded part
of $H$ is a sum of commuting single-link Laplacians; hence a
strong-coupling correlation length $\xi\le C'aN/(\gamma C_2g^4)$.

**Upper bounds** ([note](lattice-gap-upper-bounds.md),
[Polyakov note](polyakov-average-gap-bound.md)): the Feynman--Bijl
inequality with explicit constants; the strong-coupling gap pinned to
order $g^2\hbar c/a$ on both sides; the abelian gap bounded by the
plaquette-sine structure factor; the proof that **no operator linear in
the electric field with c-number coefficients is gauge invariant for a
non-abelian group**; and a necessary condition on the Polyakov-loop
susceptibility.

**The finiteness clause reduced**
([moment hierarchy](moment-hierarchy-upper-bounds.md)): $m\le M_{k+1}/M_k$
for every $k$, with the ratios decreasing, so the $f$-sum rule is the
weakest member and the next one,
$m\le\hbar C_0(0)/\int_0^\infty C_0$, needs only T4 and
$C_0\not\equiv0$. The free-field value of the weakest member is
$4.26\,\hbar c/\sqrt{8t}$, computed in closed form and confirmed by an
independent sum rule ([free-field note](flowed-bound-free-field.md)).

**Exact structural identities**
([note](magnetic-energy-identities.md)): $\Delta V=4C_2(N|\mathcal P|-V)$,
so the magnetic energy shifted by its Haar mean is a Laplacian
eigenfunction; $|\nabla V|^2\le16V$ for $SU(2)$; and an exact
ground-state sum rule tying $\operatorname{Var}_\Omega(V)$ to kinetic
quantities.

**Flow facts** ([conjugation](flow-conjugation-truncation.md),
[lattice truncation](lattice-truncation-uniform.md)): the Wilson flow is
a diffeomorphism of $G^{\mathcal E}$, unitarily implemented, so
conjugation preserves the spectrum; the lattice flow carries no coupling
and a doubling is dimensionless flow time $1/2$, so truncating the
conjugated Hamiltonian at range $Ka$ costs $Ce^{-cK}$ with pure
constants.

## 3. Seven closed routes

| route | why it closes |
| --- | --- |
| variational upper bounds, for $m>0$ | a spectral measure with all negative moments finite can have $m=0$ |
| expansion around the free theory | the bound reaches $m$ only at the confinement scale, where its coefficient is nonperturbative |
| blocking by projection | the boundary grows like $M^2$ while the block gap does not; the criterion worsens by $3M^2/8$ |
| conjugation by the flow | the spectrum is invariant, so the gain is the truncation, which is cheap |
| flow before decimation | sup norms are bijection-invariant and spectra conjugation-invariant |
| Agmon estimate on the ground state | $\|\nabla V\|_\infty$ is extensive, so it bounds the global excess only |
| pointwise Gibbs domination | the comparison function bites only above the extensive threshold $V_*\simeq N|\mathcal P|$ |

The first five exhaust the methods built from operator norms and
spectra; the last two exhaust the standard ways of extracting a local
statement from the ground-state eigenvalue equation. Each closure is a
computation with explicit constants.

**The reason the last two fail, stated once.** Every inequality derived
from $-A'\Delta\Omega+(B'V-e_0)\Omega=0$ compares the total potential
with the total energy, and $e_0$ is extensive, so it separates
configurations only by their global excess. The Euclidean weight
$e^{-S_w}=\prod_pe^{-(2/g_E^2)V_p}$ factorizes over plaquettes and
separates them locally by construction. That is the structural advantage
of the Euclidean formulation, derived here rather than assumed.

## 4. Where the non-abelian structure has been isolated

Three statements distinguish the groups, and any proof of T2$'$ must use
one of them.

1. *The commutator potential* of the zero-momentum sector is identically
   zero for an abelian group; where present, the transverse zero-point
   energy confines the valley and produces the gap
   $\delta_1\hbar^{4/3}g^{2/3}m^{-2/3}$
   ([G07](low-dimensional-mass-gap.md), claim C133).
2. *Gauge invariance blocks the photon channel*: no c-number-coefficient
   operator linear in $E$ commutes with Gauss's law for a non-abelian
   group, so the excitation through which the abelian gap closes must
   carry a Wilson line ([upper-bound note](lattice-gap-upper-bounds.md)
   Proposition 6).
3. *The one-loop valley potential*
   $U(a)=\frac{2\hbar c}{\pi^2L}\Phi(La)$ vanishes identically in the
   abelian theory, so the holonomy is free
   ([valley note](torus-valley-potential.md) §3b).

## 5. What remains

| obligation | kind |
| --- | --- |
| T2$'$: closedness of the gapped set | the conjecture |
| openness of the gapped set | technical: gap stability without frustration-freeness |
| T3 | the conjecture, given T2$'$ |
| T4 | construction |
| local large-field control | available via the transfer-matrix identification: $|\Omega|^2$ is the Euclidean time-slice marginal |
| the large-field region itself | closed in measure (cost $\eta^2/(4g^2)$ sharp, entropy $\eta^2/(8\pi^2)$); the Hamiltonian chain needs an operator inequality there, whose proof loses $C_V|\partial N|\hbar c/a$ on the small-field side, a negative perturbation that binds; the polymer expansion consumes measure statements instead |

The pattern across every note is uniform: **statements uniform in the
cutoff are renormalization statements, and statements local in space
need a local weight.** The strong-coupling theorem is uniform in the
volume at fixed cutoff; the small-volume theorem is fixed-lattice; the
flowed bounds are finite at fixed lattice and need the flow's
renormalization in the continuum; the ground-state estimates are global
because the eigenvalue equation is.

## 6. Assessment

The route that survives is the constructive one: conjugate by the flow,
which is exact; truncate, which is cheap, inside the large-field region
too once the range grows like $\eta$; decimate, which is the problem;
and iterate about twenty-one times for $SU(3)$ from $g_{\rm UV}^2=1/2$
([SU(3) constants](su3-constants.md) §3). The identification of
$\Omega^2$ with the Euclidean time-slice marginal
([transfer note](ground-state-measure-transfer.md)) imports every local
Euclidean estimate, and the large-field region is then closed in
measure: cost $\eta^2/(4g^2)$, sharp; entropy $\eta^2/(8\pi^2)$; the
flow's growth there is the Nielsen--Olesen mode and cannot be improved.
What the Hamiltonian chain of lower bounds consumes from that region is
an operator inequality, whose proof loses a negative term of order
$\hbar c/a$ on the small-field side, of exactly the kind that binds
([operator-inequality note](large-field-operator-inequality.md)). The
Euclidean polymer expansion consumes the measure statements directly,
which is the reason the constructive programme is Euclidean, now stated
as a computation.

**The coupling map for $SU(3)$.** Three regions, with numbers:

| region | statement | source |
| --- | --- | --- |
| strong, $g^2\ge1056$ ($176$ with the fundamental alone) | $\Delta_W\ge(\hbar c/a)\,4\log(g^2/1056)$, uniform in volume, Wilson transfer matrix | [explicit note](wilson-strong-coupling-explicit.md) |
| strong, $g^2\ge388$ ($79$ in the adjacent-growth class) | $\Delta_{\rm KS}\ge\frac43g^2\,\hbar c/a$, approaching $\frac83g^2$, Kogut--Susskind | [continuous-time note](kogut-susskind-strong-coupling-explicit.md) |
| weak, $1/g^2\gtrsim10^2$ | small-field expansion applies, crude window $C_1g\le\eta\le C_2$ | [operator-inequality note](large-field-operator-inequality.md) §4 |
| intermediate, $10^{-2}\lesssim g^2\lesssim4\times10^2$ | no expansion applies; a finite-volume mixing condition (Dobrushin--Shlosman) would give the gap coupling by coupling | [finite-verification note](intermediate-region-finite-verification.md) |

The strong boundary is explicit and the weak one is crude; the width of
the intermediate region in one-loop doublings is set almost entirely by
the weak side, about $10^3$ with the present window and about $20$ if
the small-field expansion reaches $g^2\sim1/2$
([threshold note](strong-coupling-threshold-explicit.md) §4). The
Kogut--Susskind threshold from Yarotsky's theorem, made explicit, is
$g_0^2\sim10^{101}$ and plays no role in the map.

**Division of labour.** Hamiltonian methods for T1, T2, the small-volume
theorem, the upper bounds, the exact identities and the final gap
extraction; the Euclidean polymer expansion for the renormalization
steps; and, for the intermediate region, the finite-volume mixing
conditions, which reduce the gap at a given coupling to a finite
verification and turn the problem into the meeting of two numbers, the
reach $g_{\rm RG}^2$ of the small-field renormalization and the reach
$g_{\rm DS}^2$ of the verification
([finite-verification note](intermediate-region-finite-verification.md)).

What this programme has added is a map with constants: six named
statements, two proved, the finiteness clause reduced to a single
correlator, seven routes closed with explicit numbers, the large-field
region closed in measure and its obstruction in norm identified, three
places where the non-abelian structure is isolated in a usable form,
the exact identities and sum rule of Section 2, and explicit thresholds
on both sides of the intermediate region. Several of the closures are
corrections of claims made earlier in the same series, and each is
recorded with the computation that forced it.
