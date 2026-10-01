# The mass gap: current position of this programme

Later corrections: [the critical-coupling note](gapped-set-critical-coupling.md) withdraws the phase-transition equivalences of T2$'$; [the transfer note](ground-state-measure-transfer.md) withdraws the verbatim transfer of Euclidean estimates; [the action lower-bound note](large-field-action-lower-bound.md) and [the entropy note](large-field-entropy-count.md) withdraw sharpness and the entropy reading of the mode count; [the instability note](flow-instability-large-field.md) and [the Jacobian note](flow-jacobian-truncation-error.md) withdraw sharp growth and the Hamiltonian truncation error; [the Kogut--Susskind note](kogut-susskind-strong-coupling-explicit.md) withdraws its explicit threshold; [the openings note](mass-gap-openings.md) §1 corrects the all-coupling requirement; [the October 1 audit](corpus-audit-2026-10-01.md) §3 lists this note's inconsistent numbers (relevant passages read).

> **Correction (2026-10-02).** This map kept several claims after their
> source notes corrected them, and it quoted thresholds that did not
> form one labelled set. The changes, made in place below:
>
> 1. *Phase reading of T2$'$.* The identification of T2$'$ with absence
>    of a zero-temperature bulk transition, and on a second-order branch
>    with uniqueness of the continuum limit, is **withdrawn**, following
>    the critical-coupling note. The statement that T2$'$ fails for
>    $SU(N\ge5)$ is **withdrawn**: the first-order bulk transition there
>    is numerical evidence for the Wilson action, a different operator,
>    and the spectral comparison with the Kogut--Susskind gap is missing.
>    "False for $U(1)$" is downgraded likewise: the massless phase is
>    proved for Euclidean actions (Guth for the Villain action;
>    Fröhlich--Spencer) and is not transferred to this operator here.
> 2. *Large field.* "The large-field region closed in measure" is
>    **withdrawn**. What survives is a continuum action floor
>    $\eta_F^2/(4g^2)$ for a flowed block, under flow and boundary
>    assumptions, with sharpness open; and a phase-space count
>    $\eta_b^2/(8\pi^2)$ for one unit-charge complex field in a constant
>    background, a model that bounds no entropy. The two $\eta$ are
>    different parameters. The verbatim import of Euclidean estimates into
>    the Kogut--Susskind ground state is **withdrawn**; the slice identity
>    stands. "The flow's growth cannot be improved" is withdrawn with the
>    instability note's sharpness claim.
> 3. *Truncation.* The Hamiltonian truncation error $Ce^{-cK}$ at range
>    $Ka$ (§2, §3, §6) is downgraded to a target: the corrected Jacobian
>    note keeps kernel-tail budgets and leaves their conversion into a
>    Hamiltonian error open.
> 4. *Thresholds.* For the $SU(3)$ Wilson transfer matrix the rigorous
>    thresholds are $g^2>444$ (Dobrushin) and $g^2\ge1056$ (polymer
>    expansion, all representations; $1059$ without the source's
>    linearization, §6); $176$ is the leading-activity figure only.
>    Their gap rates are now printed exactly, and the former
>    large-$g^2$ forms, which slightly overstate them, are marked
>    $\simeq$. For the
>    Kogut--Susskind Hamiltonian the volume-uniform gap rests on
>    Yarotsky's existential threshold, which his proof makes
>    $g_0^2\simeq10^{101}$; the explicit $g^2\ge388$ is withdrawn. The
>    weak side carries two labelled estimates: a necessary window
>    $1/g^2\gtrsim10^2$ with crude constants, and a one-step remainder
>    threshold $g^2\sim10^{-12}$ that assumes an unproved order-one
>    propagator decay rate ($\sim10^{-35}$ at the proved rate).
> 5. *Scope.* "Exhaust" (§3), "every inequality derived from" the
>    eigenvalue equation (§3) and "any proof of T2$'$ must use one of
>    them" (§4) are restricted to the routes, estimates and structures
>    examined here. The §5 row that equated T2$'$ with closedness of the
>    gapped set now states that T2$'$ needs openness as well.
> 6. *Smaller precisions.* $a_*$ is $0.1$ to $0.17$ fm, as in the
>    conditional theorem; the range of certified polymer enumeration is
>    the proved $\beta_W\lesssim10^{-2}$, replacing an unsourced
>    "$\beta_W$ of order one"; the valley potential is labelled a formal
>    one-loop calculation; §6 adds the doubling count for the
>    $10^{-12}$ weak boundary and a §8 states the consequence for STATE.

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
Hamiltonian. Each route fails for a reason stated with explicit
constants, and the second family's failure identifies what a factorized
Euclidean weight supplies that estimates drawn from the ground-state
eigenvalue equation do not. The strong-coupling thresholds are rigorous
and explicit for the Wilson transfer matrix; the weak-side thresholds
are labelled estimates; the large-field region remains open (§§5--6).

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
| T2 | $\delta\ge\gamma(g^2/2)C_2$ for $g\ge g_0$, uniform in volume | **proved here** from Yarotsky's theorem, with an existential $g_0$; following his proof with numbers gives $g_0^2\simeq10^{101}$ for $SU(3)$. The Wilson transfer matrix, a different operator, has explicit rigorous thresholds (§6) |
| T2$'$ | $\liminf_{N_s}\delta>0$ for every $g>0$ | open. $U(1)$: a massless phase is proved for Euclidean actions (Guth, Villain action; Fröhlich--Spencer), not transferred to this operator. $SU(N\ge5)$: numerical evidence of a first-order bulk transition for the Wilson action, a different operator |
| T3 | $\delta_\infty(g)/(a\Lambda_{\rm lat}(g))\to m/(\hbar c\Lambda)\in(0,\infty)$ | open |
| T4 | continuum infinite-volume theory with the axioms | finite-volume ultraviolet stability known |
| S | small volume: $\Delta=\delta_1g^{2/3}\hbar c/L\,[1+O(g^{2/3})]$ | upper side proved, lower side fixed-lattice only |

The conjecture is T3, given T4, with a gap $\delta_\infty>0$ on an
interval $(0,g_1)$ along the scaling curve. T2$'$, a gap of this
lattice operator at every coupling, is stronger, and the conjecture
does not need it (precision of 2026-09-23; the
[openings note](mass-gap-openings.md) §1 also records four ways in). For
$SU(N\ge5)$ the Wilson action shows a first-order bulk transition at
intermediate coupling in numerical studies. That proves no hole in the
gapped set of the Kogut--Susskind operator: the operators differ and
the spectral comparison is missing
([critical-coupling note](gapped-set-critical-coupling.md) §2,
correction of 2026-10-02). What
[the critical-coupling note](gapped-set-critical-coupling.md) proves is
that the finite-volume gap is continuous in $g$, and that openness of
the gapped set together with its closedness would give T2$'$ by
connectedness. Its former identification of T2$'$ with the absence of a
zero-temperature bulk transition, and with uniqueness of the continuum
limit, is withdrawn.

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
the lattice size, with exponential clustering. The threshold $g_0$ is
existential; following Yarotsky's proof with numbers gives
$g_0^2\simeq10^{101}$ for $SU(3)$
([threshold note](strong-coupling-threshold-explicit.md)), and the
explicit threshold $g^2\ge388$ of
[the continuous-time note](kogut-susskind-strong-coupling-explicit.md)
was withdrawn on 2026-10-02.

**A Lieb--Robinson bound** ([note](lieb-robinson-kogut-susskind.md)):
velocity $v\le32eNc/g^2$, uniform in volume, because the unbounded part
of $H$ is a sum of commuting single-link Laplacians; hence a
strong-coupling correlation length $\xi\le C'aN/(\gamma C_2g^4)$.

**Upper bounds** ([note](lattice-gap-upper-bounds.md),
[Polyakov note](polyakov-average-gap-bound.md)): the Feynman--Bijl
inequality with explicit constants; the strong-coupling gap pinned to
order $g^2\hbar c/a$ on both sides, the lower side for $g\ge g_0$; the abelian gap bounded by the
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
and a doubling is dimensionless flow time $1/2$, so the coefficients of
its linearization within one step are bounded by pure numbers. The
lattice note concluded that truncating the conjugated Hamiltonian at
range $Ka$ costs $Ce^{-cK}$ with pure constants. The corrected
[Jacobian note](flow-jacobian-truncation-error.md) (2026-10-02) keeps
only kernel-tail budgets and leaves their conversion into a Hamiltonian
truncation error open, so that conclusion is a target here.

## 3. Seven closed routes

| route | why it closes |
| --- | --- |
| variational upper bounds, for $m>0$ | a spectral measure with all negative moments finite can have $m=0$ |
| expansion around the free theory | the bound reaches $m$ only at the confinement scale, where its coefficient is nonperturbative |
| blocking by projection | the boundary grows like $M^2$ while the block gap does not; the criterion worsens by $3M^2/8$ |
| conjugation by the flow | the spectrum is invariant, so any gain is charged to truncating the nonlocal conjugated electric term |
| flow before decimation | sup norms are bijection-invariant and spectra conjugation-invariant |
| Agmon estimate on the ground state | $\|\nabla V\|_\infty$ is extensive, so it bounds the global excess only |
| pointwise Gibbs domination | the comparison function bites only above the extensive threshold $V_*\simeq N|\mathcal P|$ |

The first five are the routes built from operator norms and spectra
that this series tried; the last two are the two standard ways it tried
of extracting a local statement from the ground-state eigenvalue
equation. Neither list is shown to be exhaustive. Each closure is a
computation with explicit constants.

**The reason the last two fail, stated once.** Both estimates are
derived from $-A'\Delta\Omega+(B'V-e_0)\Omega=0$ and compare the total
potential with the total energy; $e_0$ is extensive, so they separate
configurations only by their global excess
([global/local note](agmon-global-not-local.md)). The Euclidean weight
$e^{-S_w}=\prod_pe^{-(2/g_E^2)V_p}$ factorizes over plaquettes, so a
local excess costs a local factor of the unnormalized weight. That is
the structural advantage of a factorized weight over these two
estimates. It falls short of local probability control, because
plaquettes share links and the normalization involves all of them
([transfer note](ground-state-measure-transfer.md) §2). The Hamiltonian
formulation has a configuration density too, $|\Omega|^2$, with an exact
slice identity ([transfer note](ground-state-measure-transfer.md) §1);
what is missing is a local large-field estimate for it, and measure
estimates do not by themselves give the signed operator comparisons a
Hamiltonian chain consumes ([Jacobian note](flow-jacobian-truncation-error.md),
correction of 2026-10-02).

## 4. Where the non-abelian structure has been isolated

Three statements distinguish the groups. They are the places this
series has isolated where a proof of T2$'$ could use structure that the
abelian theory lacks. They have distinct scopes, and none is by itself
a proof of a non-abelian gap
([critical-coupling note](gapped-set-critical-coupling.md) §4).

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
   abelian theory, so the holonomy is free; this is a formal one-loop
   calculation ([valley note](torus-valley-potential.md) §3b).

## 5. What remains

| obligation | kind |
| --- | --- |
| a gap on $(0,g_1)$ along the scaling curve | the conjecture's lattice half; T2$'$ would suffice for positivity, and T2$'$ follows from openness together with closedness of the gapped set |
| openness of the gapped set | unproved globally: needs volume-uniform gap stability; the stability route cited in the [critical-coupling note](gapped-set-critical-coupling.md) §5 has hypotheses not verified for the Kogut--Susskind Hamiltonian, including frustration-freeness |
| T3 | the conjecture, given that gap |
| T4 | construction |
| local large-field control | open. The slice identity is exact: $\langle\Omega,F\Omega\rangle$ is the long-time limit of normalized heat-semigroup expectations of the Kogut--Susskind Hamiltonian, and the squared Perron vector of a transfer matrix at fixed temporal spacing is the slice marginal of its Euclidean measure ([transfer note](ground-state-measure-transfer.md) §1); the Wilson-to-Kogut--Susskind limit needs ground-state projector convergence, and no Euclidean large-field estimate transfers verbatim |
| the large-field region itself | open; ingredients and obstruction in §6 (an action floor with sharpness open, a model mode count that bounds no entropy, and a crude Hamiltonian operator inequality that loses a binding negative term) |

The pattern across these notes is uniform: **statements uniform in the
cutoff are renormalization statements, and statements local in space
need a local weight.** The strong-coupling theorem is uniform in the
volume at fixed cutoff; the small-volume theorem is fixed-lattice; the
flowed bounds are finite at fixed lattice and need the flow's
renormalization in the continuum; the two ground-state estimates of §3
are global because the eigenvalue equation they start from carries the
extensive $e_0$.

## 6. Assessment

The route that survives is the constructive one: conjugate by the flow,
which is exact; truncate, where the kernel tails are cheap and their
conversion into a Hamiltonian error is open
([Jacobian note](flow-jacobian-truncation-error.md), correction of
2026-10-02); decimate, which is the problem; and iterate about
twenty-one times for $SU(3)$ from $g_{\rm UV}^2=1/2$
([SU(3) constants](su3-constants.md) §3). The
[transfer note](ground-state-measure-transfer.md) proves the slice
identity for $|\Omega|^2$; its former claim that the identity imports
every local Euclidean estimate is withdrawn, since the
Wilson-to-Kogut--Susskind limit needs ground-state projector convergence
and an isotropic estimate is not a bound for the anisotropic family.

The large-field region is open. Its ingredients are two. A continuum
action floor $\eta_F^2/(4g^2)$ holds for a flowed block whose $L^2$
field norm at flow time $\ell^2/8$ is at least $\eta_F$, under flow and
boundary assumptions, with sharpness open
([lower-bound note](large-field-action-lower-bound.md)). A phase-space
count $\eta_b^2/(8\pi^2)$, with $\eta_b=gB\ell^2$, holds for the
unstable modes of one unit-charge complex field in a constant
chromomagnetic background; it is a model that bounds no entropy
([entropy note](large-field-entropy-count.md)). The two $\eta$ are
different parameters, so their ratio is no action/entropy balance. In
that background the Nielsen--Olesen mode grows at rate at most $gB$ under
the linearized flow, and sharpness of the truncation bound is unproved
([instability note](flow-instability-large-field.md)). Normalized
rarity, polymer convergence and closure of the large-field corner are
not proved. What the Hamiltonian chain of lower bounds consumes from
that region is an operator inequality, whose proof in the
[operator-inequality note](large-field-operator-inequality.md) §4 loses
a negative term $C_V|\partial N|\hbar c/a$ on the small-field side, of
exactly the kind that binds. A Euclidean polymer expansion would
consume a measure statement instead, the suppression
$e^{-c\eta^2/g^2}$, which is a heuristic target here
([transfer note](ground-state-measure-transfer.md), lead). That is the
computed reason for the Euclidean choice in this series; it does not
show that every Hamiltonian route fails.

**The coupling map for $SU(3)$.** Three regions, with numbers:

| region | statement | source |
| --- | --- | --- |
| strong, Wilson transfer matrix: $g^2>444$ (Dobrushin) or $g^2\ge1056$ (polymer, all representations), both rigorous; $176$ is the leading-activity figure only | $\Delta_W\ge(\hbar c/a)\log[1/(18(e^{24/g^2}-1))]\simeq(\hbar c/a)\log(g^2/432)$, resp. $\Delta_W\ge(\hbar c/a)\,4\log[1/(176(e^{6/g^2}-1))]\simeq(\hbar c/a)\,4\log(g^2/1056)$, uniform in volume | [Dobrushin note](dobrushin-uniqueness-wilson.md), [polymer note](wilson-strong-coupling-explicit.md) |
| strong, Kogut--Susskind: explicit threshold withdrawn 2026-10-02 (formerly $g^2\ge388$, $79$ adjacent) | finite-volume bound $\frac83g^2-12|P|/g^2$ only; the volume-uniform KS gap rests on Yarotsky's existential threshold | [continuous-time note](kogut-susskind-strong-coupling-explicit.md) |
| weak: no coupling at which a step is proved with explicit constants | necessary window $C_1g\le\eta\le C_2$ for the Hamiltonian large-field inequality, nonempty only for $1/g^2\gtrsim10^2$ (crude constants); one explicit small-field blocking step has remainder threshold $g^2\sim10^{-12}$ if the propagator decay rate is of order one, which is unproved, and $g^2\sim10^{-35}$ at the proved rate (scaling estimates) | [operator-inequality note](large-field-operator-inequality.md) §4, [part 1b](small-field-step-decay-and-threshold.md) |
| intermediate, from the weak side's reach ($g^2\sim10^{-2}$ at best, on the crude window) to $g^2=444$ | no expansion applies; a finite-volume mixing condition (Dobrushin--Shlosman) would give the gap coupling by coupling | [finite-verification note](intermediate-region-finite-verification.md) |

The strong boundary is rigorous and explicit; the weak one is an
estimate. The polymer note's $1056=6\times176$ linearizes
$e^{6/g^2}-1\simeq6/g^2$; solving its criterion
$e^{6/g^2}-1\le0.84/(20e^2)=5.684\times10^{-3}$ exactly gives
$6/g^2\le\log(1.005684)=5.668\times10^{-3}$, that is $g^2\ge1059$,
from which the displayed rate is positive.

The width of the intermediate region in one-loop doublings,
$n=(1/g_{\rm weak}^2-1/g_{\rm strong}^2)/0.0966$ with
$2b_0\log2=0.0966$ for $SU(3)$, is set almost entirely by the weak side:

| weak boundary | $n$ |
| --- | --- |
| $1/g^2=10^2$ (crude window) | $\simeq10^3$ |
| $g^2=10^{-12}$ (one-step scaling estimate, order-one rate assumed) | $\simeq10^{13}$ |
| $g^2=1/2$ (if a small-field expansion reached it) | $\simeq21$ |

The first and last rows are from the
[threshold note](strong-coupling-threshold-explicit.md) §4; the middle
row is the same formula. The Kogut--Susskind threshold from Yarotsky's
theorem, made explicit, is $g_0^2\sim10^{101}$ and plays no role in the
map.

**The map as a theorem.**
[The conditional theorem](mass-gap-conditional-theorem.md) states the
whole map as two hypotheses, control of the blocking steps from the
weak side to the coupling where $\xi\simeq a$ (H1) and certified mixing
at that one coupling on one box (H2), with the conclusion
$m\ge\hbar c\min(\gamma_*,\gamma')/a_*$, where $a_*$ is the physical
spacing at the verified coupling, about $0.1$ to $0.17$ fm by the
published scale. Progress is progress on H1
or H2.

**The two reasons to stop, researched.** A Griffiths-type inequality
would transfer control from weaker to stronger coupling only and would
replace the strong-side steps, never the weak side
([research note](reasons-to-stop-as-research.md)); a certified
verification at $\beta_W\simeq6$ is beyond every certified method known
here. On the weak side, one explicit small-field step
([part 1](small-field-step-gaussian.md), [part 1b](small-field-step-decay-and-threshold.md))
has block Poincaré constant $\frac49$, fluctuation size $\frac32g$ per
link, and a proved propagator decay rate $\kappa\sim10^{-3}$ per lattice
unit, against an expected order-one value that no source proves. Its
remainder threshold scales as $\kappa^4$; a scaling estimate with crude
constants puts it at $g^2\sim10^{-12}$ if $\kappa$ is of order one and
at $g^2\sim10^{-35}$ at the proved rate. Even the first figure lies
**twelve orders of magnitude below the physical onset of the running at
$g^2\simeq1$**, where the strong side's deficit is a factor $400$ in
$\beta_W$. On that estimate, constant-chasing within this method does
not close the weak side, and H1 is a methods problem at order-one
coupling.

**Division of labour.** Hamiltonian methods for T1, T2, the small-volume
theorem, the upper bounds, the exact identities and the final gap
extraction; the Euclidean polymer expansion for the renormalization
steps; and, for the intermediate region, the finite-volume mixing
conditions, which make the gap at a given coupling follow from a finite
verification and turn the problem into the entry of the trajectory of
effective interactions into the open set of completely analytical
interactions, a sufficient route whose two-number form is the meeting
of the reach $g_{\rm RG}^2$ of the small-field renormalization with the
reach $g_{\rm DS}^2$ of the verification
([finite-verification note](intermediate-region-finite-verification.md)).

What this programme has added is a map with constants: six named
statements, two proved, the finiteness clause reduced to a single
correlator, seven routes closed with explicit numbers, for the
large-field region an action floor and a model mode count with its
closure still open and the norm obstruction met by the crude
Hamiltonian proof, three places where the non-abelian structure is
isolated, the exact identities and sum rule of Section 2, rigorous
explicit thresholds on the strong side of the intermediate region and
labelled estimates on its weak side. Several of the closures are
corrections of claims made earlier in the same series, and each is
recorded with the computation that forced it.

## 7. Where the map ends

The mass gap for $SU(3)$ in four dimensions is not proved here. The
strong side of the confinement scale carries rigorous explicit
thresholds and the weak side explicit estimates for one step, the two
standing reasons for stopping have been researched rather than left as
reasons, and what remains can be stated in one sentence.

*The two reasons, researched.* A Griffiths-type correlation inequality
would give monotonicity of the string tension and of decay rates in
channels with vanishing mean, and it transfers control from weaker to
stronger coupling only; on this map it replaces the three strong-side
blocking steps and leaves the weak side untouched, so it is a
simplification and not an unblocking. Even the vacuum-sector gap's
monotonicity would not follow, the truncated plaquette correlator
having two terms that both increase. A certified verification of the
mixing condition at $\beta_W\simeq6$ is a supremum over boundary
conditions of an integral in thousands of dimensions, while certified
polymer enumeration converges only where the expansion does, which the
explicit criteria here place at $\beta_W\lesssim10^{-2}$, with no proof
that it reaches $\beta_W\simeq6$; so it cannot be supplied where it is
needed, by any method known to this author.

*The asymmetry of the two sides.* The strong side is proved to
$\beta_W=0.0135$ (Dobrushin, $g^2>444$) against a physical crossover at
$5.7$, a factor of about $400$. The weak side, computed explicitly for
one blocking step, has its threshold controlled by the fourth power of
the fluctuation propagator's decay rate, which no source states
explicitly and which two explicit arguments put at $10^{-3}$ per
lattice unit against an expected order-one value. A scaling estimate
with crude constants puts the threshold at $g^2\sim10^{-12}$ even with
an order-one rate, which is assumed, twelve orders of magnitude below
the physical onset of the running at $g^2\simeq1$, and at
$g^2\sim10^{-35}$ with the proved rate. On these estimates, sharpening
constants within the present methods closes neither side, and the weak
side misses by a margin that no sharpening addresses.

*What is open.* Control of the renormalization steps at couplings where
the fluctuation is not small compared with the nonlinearity, with no
expansion in any parameter. That is the mass-gap problem for $SU(3)$,
stated as precisely as this programme can state it, and it is new
mathematics. The small-field steps at weaker coupling also lack
explicit constants (§6), a quantitative deficit on the same trajectory.

## 8. Consequence for STATE

Correction of 2026-10-02. STATE and other notes citing this map should
use the labelled thresholds of §6: $g^2>444$ (Dobrushin) and
$g^2\ge1056$ (polymer, all representations) for the $SU(3)$ Wilson
transfer matrix; Yarotsky's existential threshold, $g_0^2\simeq10^{101}$
when made explicit, for the Kogut--Susskind Hamiltonian; and estimates
only on the weak side. This map no longer supports a phase-transition
equivalence for T2$'$, a failure of T2$'$ for $SU(N\ge5)$, a closed
large-field region, a verbatim Euclidean transfer or a Hamiltonian
truncation bound. No STATE or catalog edit is made in this correction.
