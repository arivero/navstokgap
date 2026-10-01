# The confinement scale in three bands, with published numbers, and the verification restated gauge-invariantly

Later qualifications: [reasons to stop](reasons-to-stop-as-research.md) rejects the proposed crossover certificate as a currently available route; [mass-gap openings](mass-gap-openings.md) §1 warns of scalar softening; [the October 1 audit](corpus-audit-2026-10-01.md) §3 identifies the unsupported blocking and continuum claims.

> **Correction (2026-10-02).** The earlier claim that three strong-side
> blocking steps are standard once mixing is certified is withdrawn.
> Gibbsianness does not bound the generated interaction, preserve Wilson
> form, or establish mixing at successive scales. The identification of
> a coarse Wilson-loop expectation with polymer activity is heuristic;
> the unsourced activity threshold $2\times10^{-3}$ is withdrawn. So are
> the claim that six steps constitute the whole continuum problem, the
> comparison making band B more strongly mixing than band A, and the
> unsourced series singularities at $\beta_W=3.5$--$4$. The table below
> gives continuum-scaled estimates, not measured lattice masses or
> uniform boundary-mixing bounds. Box sides $3$--$5$ are trial sizes,
> not certified sufficient sizes; $\sigma a^2$ is an area coefficient,
> not a boundary-influence decay rate. The physical energy conversion
> is corrected to $8.42\,\hbar c\,{\rm fm}^{-1}\simeq1.66$ GeV.
> The original $216$--$2000$ link count is retained with its explicit
> four-dimensional, free-boundary convention; the earlier description
> as merely a few hundred links was inconsistent with that convention.

This note gives an exact gauge-symmetry observation and a numerical
orientation map for pure $SU(3)$ Wilson theory in four Euclidean
dimensions. It corrects the proposed single-link block test in
[the Dobrushin note](dobrushin-uniqueness-wilson.md) §4 and
[the finite-verification note](intermediate-region-finite-verification.md).
The scale estimates motivate possible sub-block mixing tests; they
supply neither such a certificate nor a quantitative blocking bridge
nor a continuum existence or mass-gap theorem.

**Elitzur empties the interior single-link test.** Let $V$ be a set of
links and $s$ a site all of whose incident links lie in $V$. A gauge
transformation at $s$ preserves the Wilson conditional Gibbs measure
$\mu_V^\omega$ for every fixed external boundary condition $\omega$.
It acts on any incident link by arbitrary left or right multiplication
in $SU(3)$. Its marginal is consequently Haar, independently of
$\omega$. Thus the single-link boundary influence $\rho_V(x,y)$
vanishes for every link $x$ with such an endpoint. A sum of these
single-link influences sees only the remaining boundary layer. This
observation alone proves no uniqueness or decay of joint interior
observables: identical one-link marginals need not give identical
joint distributions.

A useful **target** is instead a sub-block estimate, with $d$ measured
in the link interaction graph,
$$\big\|\mu_V^{\omega}\big|_W-\mu_V^{\omega'}\big|_W\big\|_{\rm TV}
\ \le\ C\,|W|\,e^{-\gamma d(W,y)},
\qquad W\subseteq V,
$$
for boundary conditions differing at the external link $y$. Gauge
symmetry removes the orbit variables at sites whose incident links
all lie in $W$. Closed-loop observables then provide nontrivial tests
of the invariant content. A selected set of small Wilson-loop traces
is not asserted to determine the full marginal; boundary-attached
observables and the full joint invariant distribution may also be
needed. The single-link Dobrushin test of the Dobrushin note §2 is
unaffected: conditioning on all other links removes the free gauge
transformation used above.

The displayed inequality is a target decay form, not by itself a
finite-size certificate. On one fixed box an arbitrarily large $C$
can make it vacuous. A theorem would require an applicable quantitative
finite-size criterion, a verified contraction margin and control of
the resulting constants across volumes. No equivalence to complete
analyticity for this gauge specification is proved here.

**Published scales give orientation, not certified box sizes.** Use
$r_0/a$ from Necco and Sommer (Nucl. Phys. B 622 (2002) 328;
metadata level) and the continuum estimate $r_0\mu_{0^{++}}=4.21$
from [Morningstar and Peardon](https://arxiv.org/abs/hep-lat/9901004)
(Phys. Rev. D 60 (1999) 034509; abstract read, numerical input retained
at metadata level). Here $\mu_{0^{++}}$ is an inverse length and the
rest energy is $E_{0^{++}}=\hbar c\mu_{0^{++}}$. The continuum-scaled
columns use
$$\mu_{0^{++}}a=\frac{4.21}{r_0/a},\qquad
\frac{\xi}{a}=\frac{r_0/a}{4.21},\qquad
\sigma a^2=\frac{1.35}{(r_0/a)^2},$$
where $r_0^2\sigma\simeq1.35$ is an orienting string-tension input;
$\sigma$ has units of inverse area, with physical tension $\hbar c\sigma$.

| $\beta_W$ | $g^2=6/\beta_W$ | $r_0/a$ | scaled $\mu_{0^{++}}a$ | scaled $\xi/a$ | scaled $\sigma a^2$ |
| --- | --- | --- | --- | --- | --- |
| $5.7$ | $1.05$ | $2.92$ | $1.44$ | $0.70$ | $0.16$ |
| $6.0$ | $1.00$ | $5.37$ | $0.78$ | $1.28$ | $0.047$ |
| $6.2$ | $0.97$ | $7.38$ | $0.57$ | $1.75$ | $0.025$ |
| $6.4$ | $0.94$ | $9.74$ | $0.43$ | $2.31$ | $0.014$ |

*Caveat, 2026-09-23, retained.* Near $\beta_W\simeq5.7$ the Wilson
axis passes beside the endpoint of the fundamental--adjoint
first-order line, where the scalar glueball softens (Heller 1995;
metadata level, [openings note](mass-gap-openings.md) §1). The measured
lattice $\xi/a$ can therefore exceed the scaled value $0.70$. Even a
measured vacuum correlation length would not certify mixing uniformly
over all boundary conditions.

A trial box with $R=3$--$5$ **sites per axis in four dimensions**, with
only internal nearest-neighbour links integrated, has
$$|V|=4(R-1)R^3=216,\ 768,\ 2000\qquad(R=3,4,5).$$
There are $R^3$ choices of transverse coordinates and $R-1$ links in
each of four directions. This is hundreds to two thousand links;
three-dimensional spatial slices have a different count. Neither the
scalar estimate nor $\sigma a^2\simeq0.16$ fixes a sufficient $R$.
An area law concerns large loop areas. Temporal decay in a given
channel is governed by its lowest energy with nonzero overlap;
a flux-tube energy depends on its length and receives corrections.
Replacing any of these by a boundary-influence rate $\sigma a^2$
is an unproved heuristic.

## 1. Three bands of the coupling

The boundaries below label the original comparison, not proven phase
boundaries or the optimal reach of every method.

| band | $\beta_W$ | status |
| --- | --- | --- |
| A | $<0.0135$ | single-link Dobrushin condition holds; fixed-cutoff Wilson transfer gap in the local-observable sector, uniformly in volume |
| B | $0.0135$ to about $5.7$ | outside that sufficient condition; confinement is physically expected, but no mixing certificate is supplied here |
| C | above about $5.7$ | scaled $\xi/a$ grows in the table; weak-coupling RG control toward the continuum remains an open obligation |

For band A the exact sufficient threshold from the one-link estimate is
$\beta_W<\tfrac14\log(19/18)$. The convenient $g^2>444$ implies it:
$\log(19/18)=\int_{18}^{19}dt/t>1/(18.5)=2/37=24/444$,
by strict convexity of $1/t$ and the midpoint integral bound.
The normalized positive Wilson transfer operator $\mathcal T$ then has
an energy-gap bound on the cyclic local-observable sector
$$\Delta_W\ge\frac{\hbar c}{a}
\log\frac{1}{18(e^{24/g^2}-1)}>0,$$
as explained in [the Dobrushin note](dobrushin-uniqueness-wilson.md)
§§2--3 (written derivation read). The volume uniformity is at fixed
$a,g^2$; this is not a continuum limit.

*Band B is a proposed sharpness problem.* The crude sufficient
criterion leaves a wide interval. It does not follow that band B is
more mixing than band A: as $\beta_W\to0$ the measure approaches a
product of independent Haar links, and the Dobrushin decay bound
improves without limit. Nor does the table establish $\xi/a<1$
throughout band B. The all-representation activity estimate in
[the Wilson note](wilson-strong-coupling-explicit.md) is of order
$\beta_W$ with a quoted sufficient activity scale of order $0.0057$;
the leading fundamental activity is a different normalization.
Changing surface entropy counts alone is not a proved extension to
$\beta_W\sim0.1$. The earlier assertion of series singularities at
$3.5$--$4$ is withdrawn for lack of a source or specified series.

*Band C is an RG target.* For orientation only, the one-loop
pure-$SU(3)$ running has $b_0=11/(16\pi^2)$ and
$$\frac{1}{g^2(2a)}-\frac{1}{g^2(a)}=-2b_0\log2
\simeq-0.0966.$$
Going from $g^2=1/2$ to $g^2=1$ therefore takes
$1/0.0966\simeq10.4$ doublings in this approximation. At fixed physical
correlation length, a decrease of $\xi/a$ from $10$ to $1$ takes
$\log_2 10\simeq3.32$ doublings kinematically. Neither count establishes
constructive control, locates gap formation, or proves a gap of order
$\hbar c/a$ throughout band B.

## 2. What the verification costs, restated

For the trial boxes just defined, the un-gauge-fixed bulk integral has
$8|V|=1728,6144,16000$ real dimensions, since $\dim SU(3)=8$.
External links entering plaquettes meeting $V$ give an additional
boundary supremum over $8|\partial V|$ variables, once that boundary
link set is specified. Gauge reduction may decrease the number of
independent coordinates, but does not provide a certified marginal
bound.

A verification would have to control joint sub-block distributions
uniformly over those boundary conditions, satisfy a quantitative
finite-size criterion with margin, and state its channel and decay
rate. No such verification is performed here. The proposed small
boxes are exploratory sizes; the earlier claim of a three-to-four
order reduction in the required problem size is withdrawn because
no sufficient size is known. The later
[reasons-to-stop note](reasons-to-stop-as-research.md) (relevant passages
read) rejects physical-crossover certification as a currently supplied
route and redirects effort toward weak-side RG. Its historical box
counts do not replace the explicit four-dimensional count above.

## 2b. A heuristic meeting scale, not a six-step theorem

*From the weak side.* The one-loop count suggests about ten doublings
from $g^2=1/2$ to $g^2\simeq1$. It does not establish that the first
seven steps are controlled or that only three steps are open. Uniform
fluctuation bounds, generated-interaction bounds and iteration remain
required even in the weak-coupling part of the proposed trajectory.

*From the strong side: the area-law illustration.* Choose coarse
links as ordered products of straight fine links. Then a coarse
plaquette is exactly the holonomy of a $2^k\times2^k$ fine loop after
$k$ doublings. If one models its normalized expectation by the pure
area term $e^{-\sigma a^2 4^k}$ with $\sigma a^2=0.16$, the estimates
are $0.53$, $0.077$, $3.6\times10^{-5}$ for $k=1,2,3$.
These are values of that heuristic model: perimeter terms, prefactors,
finite-loop effects and lattice artifacts are omitted. In particular,
the asymptotic area law need not approximate a $2\times2$ loop.

An expectation is not a polymer activity or a bound on the norm of an
interaction. The blocked measure generally contains interactions
beyond Wilson plaquettes. The former $2\times10^{-3}$ threshold had
no specified activity norm or source and is withdrawn; no conclusion
that three doublings reach band A follows. A Migdal--Kadanoff
fourth-power recursion (Kadanoff, Ann. Phys. 100 (1976) 359;
metadata level) is likewise a heuristic in four dimensions and
supplies no certified step count or error comparison here.

A measurable block map has a well-defined pushforward probability
measure. Representing it by a summable Gibbs interaction requires
additional hypotheses on that map and measure. The abstract of
[van Enter, Fernández and Sokal](https://arxiv.org/abs/hep-lat/9210032)
(J. Stat. Phys. 72 (1993) 879; abstract read) explicitly distinguishes
regularity on the RG map's domain from examples of non-Gibbsian
images. This reference is not a quantitative theorem for the present
$SU(3)$ map. Even if a suitable Gibbs representation were established,
three steps would still require explicit bounds on every generated
interaction, stability or renewed mixing estimates, and a justified
comparison with a strong-coupling criterion. None is supplied here.

*The meeting point is a proposed target.* A reference interaction near
$\beta_W=5.7$--$6$ is suggested by the numerical scales. A certified
box there would concern that interaction and its proven stability
neighbourhood; it would not automatically certify all smaller
$\beta_W$ or all its blocked images. The earlier identifications
$g_{\rm DS}^2\simeq1$ and $g_{\rm RG}^2\ge1$ are conjectural targets,
not thresholds established by this note.

**The former "whole problem in one sentence" claim is withdrawn.**
The map motivates studying a few physical scales around order-one
coupling, but does not reduce the continuum mass-gap problem to six
blocking steps. [The conditional-theorem note](mass-gap-conditional-theorem.md)
organizes proposed mixing and RG hypotheses; invoking it here does not
discharge them. Continuum existence, Osterwalder--Schrader or Wightman
axioms, nontriviality, and a finite positive physical spectral gap
remain separate obligations, as the October 1 audit §3 emphasizes.

## 3. What this changes

The exact correction is the Haar-marginal obstruction to an interior
single-link test. A joint sub-block criterion is a research target;
its constants, applicability and sufficient box size remain open.
The three bands and blocking counts are orientation, not an established
connection between the explicit strong-coupling region and the
physical crossover.

For the conventional scale choice $r_0=0.5$ fm, the retained continuum
ratio gives
$$\mu_{0^{++}}=\frac{4.21}{r_0}=8.42\,{\rm fm}^{-1},\qquad
E_{0^{++}}=8.42\,\hbar c\,{\rm fm}^{-1}\simeq1.66\,{\rm GeV},$$
using $\hbar c\simeq0.1973$ GeV fm. If mass is expressed as a mass
rather than an energy, $M_{0^{++}}=E_{0^{++}}/c^2\simeq1.66$ GeV$/c^2$.
This is a lattice-literature benchmark with a chosen physical scale,
not a proved continuum gap or a requirement that a lower-bound proof
recover that central numerical value.

## 4. Consequence for STATE

Retain the exact interior Haar-marginal obstruction and the explicit
fixed-cutoff strong-coupling criterion. Treat the scale table,
$R=3$--$5$ trial boxes, area-law blocking illustration and proposed
crossover meeting point as orientation only. Withdraw the claims that
one such box certifies band B, that three subsequent strong-side steps
are standard, or that six steps settle the continuum theory. The
later reasons-to-stop correction points toward quantitative weak-side
RG and control of generated interactions; this note supplies no new
certificate, blocking theorem or continuum construction.
