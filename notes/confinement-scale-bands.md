# The confinement scale in three bands, with published numbers, and the verification restated gauge-invariantly

Two corrections to the finite-verification statement of
[the Dobrushin note](dobrushin-uniqueness-wilson.md) §4 and
[the finite-verification note](intermediate-region-finite-verification.md),
and a map of the region with numbers taken from the literature.

**Elitzur empties the single-link form of the block criterion.** Let
$V$ be a box of links and $s$ a site all of whose links lie in $V$. The
gauge transformation at $s$ is a measure-preserving bijection of the
Gibbs measure $\mu_V^\omega$ for every boundary condition $\omega$, so
the marginal of any link with an endpoint at $s$ is invariant under all
left (or right) translations of $SU(3)$ and is therefore the Haar
measure, whatever $\omega$ is. The single-link influence $\rho_V(x,y)$
vanishes for every link $x$ with an interior endpoint, and the sum
$\sum_{x\in V}\sum_{y\notin V}\rho_V(x,y)$ receives contributions only
from links with both endpoints on the boundary layer. That form of the
criterion yields uniqueness and carries no information about the
interior; the verification must use the **mixing form on sub-blocks**,
which is the form equivalent to complete analyticity and the one that
yields exponential decay: for every $W\subseteq V$ and every $y\notin V$,
$$\big\|\mu_V^{\omega}\big|_W-\mu_V^{\omega'}\big|_W\big\|_{\rm TV}\ \le\ C\,|W|\,e^{-\gamma\,d(W,y)}
\qquad(\omega,\omega'\text{ differing at }y).$$
Since the gauge-variant part of the marginal on $W$ is uniform over the
gauge orbit at the interior sites of $W$, the content of this condition
is the conditional distribution of the gauge-invariant functions of the
links in $W$, the traces of small Wilson loops, and that is how a
verification should be organized. The single-link Dobrushin condition
of [the Dobrushin note](dobrushin-uniqueness-wilson.md) §2 is
unaffected, because it conditions on all other links and no gauge
symmetry survives the conditioning.

**The boxes are small where the verification is needed.** With the
scale $r_0/a$ of Necco and Sommer (Nucl. Phys. B 622 (2002) 328) and
the scalar glueball mass $r_0m_{0^{++}}=4.21$ of Morningstar and Peardon
(Phys. Rev. D 60 (1999) 034509), both at metadata level and used for
orientation only, the glueball correlation length in lattice units is

| $\beta_W$ | $g^2=6/\beta_W$ | $r_0/a$ | $m_{0^{++}}a$ | $\xi/a$ | $\sigma a^2$ |
| --- | --- | --- | --- | --- | --- |
| $5.7$ | $1.05$ | $2.92$ | $1.44$ | $0.70$ | $0.16$ |
| $6.0$ | $1.00$ | $5.37$ | $0.78$ | $1.28$ | $0.047$ |
| $6.2$ | $0.97$ | $7.38$ | $0.57$ | $1.75$ | $0.025$ |
| $6.4$ | $0.94$ | $9.74$ | $0.43$ | $2.31$ | $0.014$ |

using $r_0^2\sigma\simeq1.35$ for the string tension. At $\beta_W=5.7$ the
glueball correlation length is below one lattice spacing, and a mixing
verification would concern boxes of side $3$ to $5$, that is $216$ to
$2000$ links, in place of the $10^4$ to $10^6$ links estimated earlier
from a correlation length of $1$ to $10$. The slowest influence is
carried by the flux-tube channel, $\sigma a^2\simeq0.16$ per lattice
unit at $\beta_W=5.7$, which sets the box side rather than the glueball
mass. Constants explicit where they are ours; nothing promoted.

## 1. Three bands of the coupling

| band | $\beta_W$ | status |
| --- | --- | --- |
| A | $<0.0135$ | gapped, proved by hand: Dobrushin single-link condition, $g^2>444$ |
| B | $0.0135$ to about $5.7$ | mixing with $\xi/a<1$ by the published data; no rigorous method reaches it |
| C | above about $5.7$ | $\xi/a$ grows, asymptotic scaling sets in near $6$ to $6.5$; the renormalization group's domain |

*Band B is a sharpness problem.* The theory there is, by the data, more
strongly mixing than anything band A contains, yet no expansion
converges with rigorous constants: the polymer expansion of
[the Wilson note](wilson-strong-coupling-explicit.md) reaches
$\beta_W\simeq0.0057$, the Dobrushin condition $0.0135$, and an ideal
entropy constant for plaquette surfaces, of order $10$ to $15$ in place
of $20e$, would bring the expansion to $\beta_W\sim0.1$. The
strong-coupling series itself has singularities near $\beta_W\simeq3.5$
to $4$, so even the true radius of convergence ends inside band B. The
gap between $0.1$ and $5.7$ is a factor of $50$ in $\beta_W$ with no
small parameter, in a regime where the correlation length is less than
one lattice unit. This is the band the finite verification addresses,
and Section 2 says what it costs.

*Band C is the renormalization group's.* From $g^2=1/2$ ($\beta_W=12$)
to $\beta_W=6$ ($g^2=1$) is $1/0.0966\simeq10$ one-loop doublings, over
which $\xi/a$ falls from its asymptotic-scaling value to about one. The
stretch where $\xi/a$ passes from about $10$ to about $1$ is three
doublings wide at one loop. The physically nontrivial part of the
problem, the place where the gap forms, is this stretch; everything in
band B is, physically, already gapped with a gap of order $\hbar c/a$.

## 2. What the verification costs, restated

A mixing verification at $\beta_W\simeq5.7$ with boxes of side $R=3$ to
$5$ involves rigorous bounds on the conditional distribution of small
Wilson loops inside $V$, with $216$ to $2000$ link variables, uniformly
over the boundary condition, with the bound decaying in the distance
from the boundary change at a rate consistent with $\sigma a^2\simeq0.16$.
The uniformity over boundary conditions is a supremum over a compact
set of dimension $8|\partial V|$, of order $10^3$ to $10^4$, of a function
defined by an integral over $8|V|$ dimensions. No rigorous numerical
method known to the author evaluates such a quantity with certified
bounds today; the problem is nevertheless three to four orders of
magnitude smaller in the number of variables than the earlier estimate,
and it sits at a coupling where the theory's correlation length is
below the lattice spacing, so that a certified bound on a single small
box would settle band B at that coupling.

## 3. What this changes

The finite verification is restated gauge-invariantly and at its true
size. The decision it asks for is unchanged in kind and smaller in
scale. Bands A and C are as before; band B is where a certified
computation on a box of a few hundred links would connect the
hand-proved region to the physical crossover, and band C remains the
renormalization group's, ten doublings from $g^2=1/2$ to the crossover
at one loop. The glueball gap along the trajectory is then, in physical
units, $m_{0^{++}}=4.21/r_0\simeq1.66\,\hbar c\,{\rm fm}^{-1}$ by the same
data, which is what a proof would have to reproduce as a positive
number.

## 4. Consequence for STATE

The Dobrushin note's specification is corrected: the block criterion in
its single-link form is emptied by Elitzur and the mixing form on
sub-blocks, organized around the conditional distribution of small
Wilson loops, is the one to verify. The verification's size is
corrected downward to boxes of side $3$ to $5$ at $\beta_W\simeq5.7$,
where $\xi/a<1$ by the published data. The three bands separate the
sharpness problem (B, a factor $50$ in $\beta_W$ with $\xi/a<1$) from the
physical problem (C, three doublings where $\xi/a$ passes from $10$ to
$1$).
