# The intermediate region as a finite verification: complete analyticity, the transfer matrix, and the two numbers whose meeting closes the proof

The intermediate region has been described in this series as the part
of the coupling range where no expansion applies. That is true of
expansions, and it leaves out a different class of rigorous tools: the
finite-volume criteria for exponential decay of correlations in lattice
spin systems, of which the Dobrushin--Shlosman conditions of *complete
analyticity* (J. Stat. Phys. 46 (1987) 983) and the strong-mixing
conditions of Martinelli and Olivieri (Commun. Math. Phys. 161 (1994)
447 and 487) are the standard forms; all references here are at
metadata level. The Wilson measure is a lattice spin system of exactly
their type: compact spins $U_\ell\in SU(3)$, a product a priori measure
(Haar), a translation-invariant finite-range interaction (the
plaquette term). Gauge invariance is a symmetry of the interaction and
no obstruction, since Elitzur's theorem (Phys. Rev. D 12 (1975) 3978)
only says that gauge-variant local observables have zero expectation.
Three consequences, each a chain of known results:

1. If a Dobrushin--Shlosman condition holds for the Wilson interaction
   at coupling $\beta_W$, then truncated correlations of all local
   observables decay exponentially, uniformly in boundary conditions,
   and by link reflection positivity the Wilson transfer matrix has a
   spectral gap: **the theory at $\beta_W$ is gapped, uniformly in the
   volume**.
2. The condition is a finite computation on boxes whose side is a few
   correlation lengths $\xi/a$, and the set of interactions satisfying
   it is open, so an interval of couplings is covered by finitely many
   verifications, each with an explicit radius.
3. The region where the verification is feasible in principle is the
   one where $\xi/a$ is moderate, that is precisely the intermediate
   region; the weak side, where $\xi/a=1/(a\Lambda)$ grows beyond any
   box, is the domain of the renormalization group, and the target box
   of [the target-box note](strong-coupling-target-box.md) may be
   replaced by the verified interval, whose openness radius supplies
   the tolerance.

So the mass-gap problem for $SU(3)$ on the lattice reduces to the
meeting of two numbers: $g_{\rm RG}^2$, the largest coupling up to which
a small-field renormalization argument delivers the effective
interaction inside the openness radius of the Wilson interaction; and
$g_{\rm DS}^2$, the smallest coupling at which a Dobrushin--Shlosman
condition has been verified. The proof closes when
$g_{\rm RG}^2\ge g_{\rm DS}^2$. Neither number is known today, the
verification is a computer-assisted task of a size far beyond present
practice, and this repository performs no numerics; what is new here is
that the intermediate region is a finite problem with a precise
statement rather than a region without tools. Constants where they
exist; nothing promoted.

## 1. The Wilson measure as a spin system

Sites: the links of $\mathbb Z^4$ (or of a periodic lattice). Spin
space: $SU(3)$, compact, with Haar measure $d\mu$. Interaction: for each
plaquette $p$,
$$\Phi_p(U)=-\frac{\beta_W}{N}\operatorname{Re}\operatorname{tr}U_p,\qquad\beta_W=\frac{2N}{g^2},$$
a bounded function of the four link variables of $p$, translation
invariant, of range one. The Gibbs measures in a box $\Lambda$ with
boundary condition $\bar U$ on the links outside $\Lambda$ are
$$d\mu_\Lambda^{\bar U}(U)=\frac{1}{Z_\Lambda^{\bar U}}\exp\Big[-\sum_{p\cap\Lambda\ne\emptyset}\Phi_p(U\vee\bar U)\Big]\prod_{\ell\in\Lambda}d\mu(U_\ell),$$
well defined for every $\bar U$, gauge-invariant or not. Gauge
transformations at interior sites are a symmetry of each
$\mu_\Lambda^{\bar U}$ restricted to interior links, so the expectation
of a gauge-variant interior observable vanishes for every $\bar U$
(Elitzur); gauge-invariant observables are the ones with content, and
nothing in the Dobrushin--Shlosman framework asks for more than
boundedness and finite range of $\Phi$.

## 2. The finite-volume criteria and what they imply

Dobrushin and Shlosman give a list of conditions on the finite-volume
Gibbs measures, proved equivalent, each of the form: for boxes of a
fixed side $R$ and all pairs of boundary conditions differing at one
site, the influence on the interior is small in a specified sense. Any
one of them implies: a unique infinite-volume Gibbs state; exponential
decay of truncated correlations of all local observables, with a rate
$m>0$ and uniformly in boundary conditions; analyticity of the free
energy and of the expectations of local observables in the interaction.
Martinelli and Olivieri prove that a weaker condition, strong mixing on
boxes of side $R$, suffices for the decay statement in the one-phase
region, for general (Part II) as well as attractive (Part I) systems.

**From decay to the gap.** The Wilson action is link-reflection
positive, so the transfer matrix $\mathcal T$ in the time direction is
self-adjoint and positive, $H_W=-(\hbar c/a)\log\mathcal T$, and for a
local observable $A$ orthogonal to the vacuum
$\langle A,\mathcal T^nA\rangle$ is a truncated Euclidean correlation at
time separation $n$. Exponential decay at rate $m$ for all local $A$
forces the spectral measure of every such $A$ to vanish above
$e^{-ma}$, so $\operatorname{gap}(H_W)\ge\hbar c\,m$ on the cyclic
subspace of local observables, as in
[the Wilson note](wilson-strong-coupling-explicit.md) §3. Uniformity in
the boundary conditions is what makes this hold on every spatial torus.

**Proposition.** If a Dobrushin--Shlosman or Martinelli--Olivieri
condition holds for the Wilson interaction at $\beta_W$, then the
lattice $SU(3)$ theory at that coupling has a unique vacuum and a
spectral gap $\Delta_W\ge\hbar c\,m>0$, uniformly in the spatial volume.

## 3. Covering an interval, and what "the box" becomes

*Openness.* The set of interactions satisfying a Dobrushin--Shlosman
condition on boxes of side $R$ is open in the norm
$\|\Phi\|=\sup_\ell\sum_{p\ni\ell}\|\Phi_p\|_\infty$, with a radius that
the condition's own margin fixes. A verification at $\beta_W^{(i)}$ on
side $R_i$ therefore covers an explicit interval around it, and a finite
interval $[\beta_1,\beta_2]$ is covered by finitely many verifications.

*Feasibility scales with $\xi/a$.* The side $R$ needed is a few
correlation lengths in lattice units; at strong coupling $\xi/a$ is
small and the condition is implied by the convergent expansion, while
toward weak coupling $\xi/a=1/(a\Lambda(g))$ grows like
$e^{1/(2b_0g^2)}$ and no box suffices. The condition is thus a tool for
the intermediate region and only for it.

*The box moves.* Whatever interval $[\beta_1,\beta_2]$ is verified, the
renormalization group of the weak-coupling side no longer has to reach
the strong-coupling threshold; it has to deliver an effective
interaction within the openness radius of the Wilson interaction at
some $\beta_W\in[\beta_1,\beta_2]$. The openness radius is the tolerance
that [the target-box note](strong-coupling-target-box.md) supplied by
hand, and the effective interaction is allowed to contain any
finite-range bounded terms, since the criteria are stated for general
finite-range interactions.

## 4. The two numbers

Define $g_{\rm DS}^2$ as the smallest coupling at which a
Dobrushin--Shlosman condition for the Wilson interaction has been
verified on some box, and $g_{\rm RG}^2$ as the largest coupling up to
which a rigorous small-field renormalization argument brings the
effective interaction within the openness radius of the Wilson
interaction at that coupling. Then:

- for $g^2\ge g_{\rm DS}^2$ the theory is gapped (Section 2);
- for $g^2\le g_{\rm RG}^2$ the effective theory at some coarser scale
  lies in the verified region and inherits its gap, provided the
  renormalization steps are exact low-energy reductions;
- **the mass gap holds on the whole lattice coupling range if
  $g_{\rm RG}^2\ge g_{\rm DS}^2$**, and T3 then concerns only the
  continuum limit along the trajectory.

Today $g_{\rm DS}^2$ is not below the strong-coupling threshold, no
verification having been attempted, and $g_{\rm RG}^2$ is not known to
exceed zero with an explicit constant. The physical expectation, from
the numerical evidence for a smooth crossover with $\xi/a$ of order
$1$--$10$ for $\beta_W$ between $5$ and $6.5$, is that a verification at
those couplings would need boxes of side $10$--$30$ and that
$g_{\rm DS}^2$ could in principle be brought to about $1$; the
verification itself, a rigorous bound on integrals over $SU(3)^{3R^4}$
with all boundary conditions, is beyond present computational practice
by a wide margin, and this repository performs no numerics.

**T3 in this framework.** Suppose the renormalization steps are exact
low-energy reductions and the trajectory from bare coupling $g$ enters
the verified interval after $n(g)$ doublings at an effective interaction
$\Phi_s(g)$. The gap in lattice units is then
$\delta(g)=2^{-n(g)}\,\delta_{\rm eff}(\Phi_s(g))$, with $\delta_{\rm eff}$
the gap of the verified theory at its own scale, and the ratio
$\delta(g)/(a\Lambda_{\rm lat}(g))$ of T3 depends on $g$ only through the
point $\Phi_s(g)$ at which the trajectory enters the interval. Its
convergence as $g\to0$ is therefore the statement that the trajectories
from different bare couplings converge to one curve as they reach the
interval, that is, that the irrelevant directions contract along the
flow; the strong-coupling threshold plays no role in it. The clause T3
is in this way absorbed into the same hypothesis on the renormalization
map as T2$'$, and the finite verification supplies the gap
$\delta_{\rm eff}$ with an explicit value at each point of the interval.

## 5. What this changes and what it does not

*Changes.* The intermediate region is a finite verification problem
with a precise statement, and the renormalization group's finish line
is an interval with an explicit openness radius rather than the
strong-coupling threshold. The three tools of the map, small-field
renormalization, finite-volume mixing conditions, and the
strong-coupling expansion, cover the coupling range if the first two
overlap.

*Does not change.* No step of the proof is completed here. The
verification is not performed, the small-field argument is not carried
out with constants, and the meeting of $g_{\rm RG}^2$ and $g_{\rm DS}^2$
is a conjecture supported by numerical evidence outside this
repository.

## 6. Consequence for STATE

The intermediate region has a rigorous finite reformulation: verify a
Dobrushin--Shlosman condition for the Wilson interaction on finite
boxes, transfer the decay to the gap through the transfer matrix, and
cover intervals by openness. The proof closes when the renormalization
group's reach $g_{\rm RG}^2$ meets the verified reach $g_{\rm DS}^2$.
Both are numbers, neither is known, and the second is the one that a
computation, outside this repository's rules, could in principle
produce.
