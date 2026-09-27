# The zero-spacing limit for any plaquette action and any dimension

**Result, 2026-09-27.** The [series/parallel note](series-parallel-gauge-refinement.md)
worked with the heat-kernel action. Here the question is how the
$a\to0$ limit depends on the choice of plaquette action, and on the
dimension.

1. **Two semigroups.** A series move convolves plaquette weights, so it
   multiplies their character coefficients; heat kernels form a family
   closed under it. A parallel move multiplies weights pointwise, so it
   adds their logarithms; exponential families $e^{-\beta V}$ with a
   fixed potential (for example Wilson) are closed under it. In the small-field regime the two
   agree: for $U(1)$ the product of two heat kernels is exactly a heat
   kernel at the parallel heat time $st/(s+t)$ plus shifted terms whose
   mixture weights are $O(e^{-2\pi^2/(s+t)})$ (Proposition 1).
2. **Two dimensions, any action** (Theorem 2). The possible continuum
   limits under infinitesimal symmetric class-function plaquette refinement
   with finite representation exponents are exactly the
   symmetric conjugation-invariant Lévy exponents; for compact connected
   simple $G$ they are
   $\psi(R)=\frac{\sigma^2}2C_2(R)+\int(1-{\rm Re}\,\chi_R/d_R)\,d\nu$,
   with $\psi(R)=\lim a^{-2}(1-\hat c_R(a))$. Yang--Mills is the Gaussian
   member, $\nu=0$, selected by a Lindeberg condition on the action. A
   weight with an atom at a centre element produces a centre-vortex gas,
   and the circle spectrum becomes $E_R-E_0=\hbar cL\,\psi(R)$.
3. **Any dimension: an error budget per physical volume.** One
   refinement step leaves three kinds of error. The perturbative part is
   of relative order $t_n$, the plaquette heat time at step $n$. The
   candidate large-field bound scales as $a_n^{-D}e^{-c/t_n}$ per physical volume,
   with $c$ the minimal large-field action of the chosen lattice action
   in units of the inverse heat time. The jump part is the action's Lévy
   content. With $t\propto\lambda_Da^{4-D}$:
   - $D<4$: the displayed perturbative and exponential scales are
     summable at fixed $\lambda_D$, provided uniform bounds and stability
     supply this error budget;
   - $D=4$: the perturbative part resums into the running coupling, and
     the large-field part decays only as a power of $a$,
     $(a\Lambda)^{2b_0c}$, giving the sufficient strict power threshold $2b_0c>4$, that is
     $c>96\pi^2/(11N)$ for pure $SU(N)$: $c>43.1$ for $SU(2)$, $c>28.7$ for
     $SU(3)$, that is $12/(11N)$ of the instanton action. Instantons
     ($c=8\pi^2\approx79$) pass for every $N$; for lattice dislocations this
     is the known $6/11$ criterion of Pugh--Teper and Göckeler et al.
     (1989);
   - $D>4$: $t$ grows as $a\to0$ at fixed $\lambda_D$, so no small-field
     regime exists at short distances.

The exact two-dimensional classification and the higher-dimensional
error budget have different status. For $D\ge3$, uniform blocking,
observable normalization, large-field entropy and reconstruction must
still be controlled before asserting universality or equality of gaps.
The three scales organize that task.
The ingredients are established (character expansions, Poisson
summation, Hunt's classification of convolution semigroups, the
one-loop running); the organization by the two semigroups and the error
budget is the contribution, with no novelty claimed for the parts.

## 1. Series and parallel act on different coordinates of the weight

Let $w$ be a class-function probability density on a compact connected
Lie group $G$ (Haar measure normalized), symmetric,
$w(g^{-1})=w(g)$, with character coefficients
$\hat c_R=d_R^{-1}\int w\,\overline{\chi_R}\,dg\in[-1,1]$, so that
$w=\sum_Rd_R\hat c_R\chi_R$. Group metric as in the series/parallel note
§1 ($-\Delta\chi_R=C_2(R)\chi_R$).

- **Series.** Integrating out an edge shared by two faces convolves their
  weights, and $\widehat{(w_1*w_2)}_R=\hat c_R(w_1)\hat c_R(w_2)$. The heat
  kernels $k_t$, $\hat c_R=e^{-tC_2(R)/2}$, form the one-parameter family
  closed under this product with $t$ additive.
- **Parallel.** Two faces with the same holonomy combine by the
  pointwise product $w_1w_2$, and $\log(w_1w_2)=\log w_1+\log w_2$. The
  families $w_\beta\propto e^{-\beta V}$ with fixed $V$ are closed under
  this operation with $\beta$ additive; Wilson's $V=1-{\rm Re\,tr}\,U/N$
  is one.

**Proposition 1 (parallel product of $U(1)$ heat kernels).** With
$k_s(\theta)=\sum_{n\in\mathbb Z}e^{-sn^2/2}e^{in\theta}$ and
$\tau=st/(s+t)$,

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** normalized Haar measure supplies a missing factor $2\pi$; the small weights are mixture weights, with a separate pointwise ratio.

$$k_s(\theta)\,k_t(\theta)=\sqrt{\frac{2\pi}{s+t}}\sum_{m\in\mathbb Z}
e^{-2\pi^2m^2/(s+t)}\,k_\tau\!\Bigl(\theta+\frac{2\pi ms}{s+t}\Bigr).$$

*Proof.* Poisson summation gives $k_s(\theta)=2\pi\sum_wG_s(\theta+2\pi w)$
with $G_s(x)=(2\pi s)^{-1/2}e^{-x^2/(2s)}$. For Gaussians,
$G_s(x)G_t(y)=G_{s+t}(x-y)\,G_\tau\bigl((tx+sy)/(s+t)\bigr)$. Put
$x=\theta+2\pi w$, $y=\theta+2\pi w'$ and $m=w'-w$; the sum over $w$ at
fixed $m$ is $k_\tau(\theta+2\pi ms/(s+t))/(2\pi)$. Multiplying the
two initial factors $2\pi$ leaves the prefactor
$2\pi/\sqrt{2\pi(s+t)}$. $\square$

The $m=0$ term is the heat kernel at the parallel heat time, the
conductance rule of the series/parallel note §3. The terms $m\neq0$ are
shifted images, of relative mixture weight $e^{-2\pi^2m^2/(s+t)}$.
After normalizing the product to integrate to one, these weights give
an exponentially small total-variation correction to $k_\tau$. Pointwise,
the relative correction also contains
$k_\tau(\theta+2\pi ms/(s+t))/k_\tau(\theta)$; it need not be small
near the cut locus. For $s=t$ and $\theta=\pi$, a shifted term is of the
same leading exponential order as the unshifted term. Heat kernels close
exactly under series, and fixed-potential exponential families under parallel.
Both reduce to the Gaussian in the small-field regime, where they agree.

**A limit of validity for heat-kernel anisotropy.** Equation (1) of the
series/parallel note matches heat times to the continuum action in the
small-field regime. Refining one direction alone, for instance Euclidean
time at fixed spatial lattice, sends the transverse heat times to
infinity. Heat-kernel weights then become flat up to corrections
$e^{-tC_2/2}$, whereas the Kogut--Susskind limit needs a magnetic weight
$e^{-a_0V}$ with $a_0$ the time step. The Hamiltonian limit is reached
within the exponential family. The directional halvings of an isotropic
cycle change heat times only by factors of two, so the propositions of
that note are unaffected.

**Referee verdict, 2026-09-27: ACCEPT with scope.** At fixed spatial
spacing write $t_{jk}=B/a_0$, $B>0$. On a connected group the first
nonconstant eigenvalue gives $k_{B/a_0}=1+O(e^{-B C_{\min}/(2a_0)})$;
dividing its logarithm by $a_0$ gives zero magnetic potential. Equation
(1) remains a definition but this time-only heat-kernel family yields an
electric Hamiltonian with vanishing magnetic term. A spatial weight
$e^{-a_0V}$, together with temporal heat kernels, restores the desired
Hamiltonian. Other weights with that first-order expansion also work.

## 2. Two dimensions: the continuum limits of every plaquette action

In two dimensions every refinement is a series move (the series/parallel
note, §2). A face of area $A$ tiled by $A/a^2$ plaquettes of weight $w_a$
has, after integrating the interior edges, the weight whose coefficients
are $\hat c_R(a)^{A/a^2}$.

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** require finite exponents, use a general invariant diffusion tensor for nonsimple groups, and include the converse construction.

**Theorem 2.** Initially take $G$ compact, connected and simple, and let
$w_a\ge0$ be normalized symmetric class-function plaquette weights on
the lattice of spacing $a$, with $\hat c_R(a)\to1$ for every $R$. Suppose
that for every $R$ the limit

$$\psi(R)=\lim_{a\to0}\frac{1-\hat c_R(a)}{a^2}
=\lim_{a\to0}a^{-2}\int_G\Bigl(1-\frac{{\rm Re}\,\chi_R(g)}{d_R}\Bigr)
w_a(g)\,dg$$

exists and is finite. Then every face of area $A$ has the limiting coefficients
$e^{-A\psi(R)}$, and $\psi$ has the form

$$\psi(R)=\frac{\sigma^2}2C_2(R)+\int_{G\setminus\{e\}}
\Bigl(1-\frac{{\rm Re}\,\chi_R(g)}{d_R}\Bigr)\nu(dg),$$

with $\sigma^2\ge0$ and $\nu$ a conjugation-invariant symmetric measure
satisfying

$$\int_G\min\bigl(1,d(e,g)^2\bigr)\,\nu(dg)<\infty.$$
 The limiting semigroup is
Yang--Mills with $\lambda_2=\sigma^2$ when $\nu=0$ (including the
degenerate zero-diffusion case), and $\nu=0$ holds
when, for every $\varepsilon>0$,
$a^{-2}\int_{d(e,g)>\varepsilon}w_a\,dg\to0$.

*Proof.* Since $\hat c_R(a)\to1$,
$(A/a^2)\log\hat c_R(a)=-(A/a^2)(1-\hat c_R(a))(1+o(1))\to-A\psi(R)$.
Split the integral defining $\psi$ at $d(e,g)=\varepsilon$. Near the
identity, the invariant quadratic trace form is
$1-{\rm Re}\,\chi_R(e^X)/d_R=C_2(R)|X|^2/(2\dim G)+O(|X|^4)$.
Simplicity makes that trace form a scalar multiple of the chosen metric;
conjugation invariance alone would not justify averaging over all directions
in a general Lie algebra. This part converges to $\frac{\sigma^2}2C_2(R)$ with

$$\sigma^2=\lim_{\varepsilon\to0}\lim_{a\to0}\frac1{a^2\dim G}
\int_{d(e,g)<\varepsilon}|X|^2\,w_a(g)\,dg,\qquad g=e^X,$$

along a subsequence if needed. Away from
the identity, the measures $a^{-2}w_a\,dg$ restricted to
$\{d\ge\varepsilon\}$ have bounded mass (a finite sum of the functions
$1-{\rm Re}\,\chi_R/d_R$ over representations separating the points of
$G$ is continuous and positive off $e$, hence bounded below there), so a subsequence
converges weakly to $\nu$ on that set, conjugation invariant and
symmetric. The integrability of $\nu$ near $e$ follows from the bound on
the near part. The form of $\psi$ agrees with Hunt's classification of
convolution semigroups on Lie groups, restricted to central ones
([Hunt 1956](https://doi.org/10.1090/S0002-9947-1956-0079232-9),
metadata). A finite faithful representation controls both mass away from
$e$ and the truncated second moment near $e$, so compactness and the
uniqueness of these limiting Fourier coefficients produce a probability
convolution semigroup. Its continuity at area zero follows first on finite
character sums and then, by uniform approximation of central continuous
functions, weakly on $G$. The Lindeberg condition sets the far part to
zero. Under these finite-exponent hypotheses the converse holds as well:
if $\nu=0$, testing away from $e$ shows that the scaled tail masses vanish.
$\square$

For general compact connected $G$, the diffusion term is
$q_Q(R)=(2d_R)^{-1}\sum_{ij}Q_{ij}\operatorname{tr}(T_iT_j)$, where
$dR(E_i)=iT_i$ and $Q\ge0$ is an $\operatorname{Ad}G$-invariant covariance.
There is one scalar on each simple ideal and an arbitrary covariance on
the central torus. For example $G=U(1)^2$ permits
$q_Q(n_1,n_2)=(q_1n_1^2+q_2n_2^2)/2$ with $q_1\ne q_2$.
Inversion symmetry removes drift and symmetrizes the jump measure. The
single $\sigma^2C_2/2$ formula therefore needs the simple-group restriction
or an additional isotropy assumption.

Conversely, for any symmetric central Lévy semigroup $\mu_A$, take
$w_a\,dg=\mu_{a^2}*(k_{r_a}\,dg)$ with $r_a>0$ and $r_a/a^2\to0$.
These are smooth symmetric central densities and their limiting exponents
are those of $\mu_A$. This proves realizability of the entire stated class.
The classification concerns independent plaquette refinement and its
holonomy laws; additional regularity axioms for a particular continuum
field theory need separate verification.

The limiting objects are Lévy's two-dimensional Markovian holonomy
fields, which he constructs from Lévy processes on $G$
([Lévy, Astérisque 329](https://doi.org/10.24033/ast.785), metadata).
Theorem 2 adds only the lattice-side statement: which plaquette actions
lead to which member.

**Examples.** The Wilson action $w_a\propto e^{\beta_a{\rm Re\,tr}U}$ with
$\beta_a\propto1/(\lambda_2a^2)$ concentrates like a Gaussian of width
$\sqrt{\lambda_2}a$, satisfies the Lindeberg condition, and gives
Yang--Mills. A weight carrying an explicit centre-vortex fugacity,
$w_a=(1-\kappa a^2)k_{\lambda_2a^2}+\frac{\kappa a^2}2\bigl[k_{\lambda_2a^2}(z\,\cdot)
+k_{\lambda_2a^2}(z^{-1}\cdot)\bigr]$ with $z$ a generator of the centre
$\mathbb Z_N$ of $SU(N)$, gives
$\nu=\frac\kappa2(\delta_z+\delta_{z^{-1}})$ and

$$\psi(R)=\frac{\lambda_2}2C_2(R)+\kappa\Bigl(1-\cos\frac{2\pi k(R)}N\Bigr),$$

with $k(R)$ the $N$-ality. On a spatial circle of circumference $L$ the
refinement note's eq. (10) becomes $E_R-E_0=\hbar cL\,\psi(R)$: the vortex
gas adds an $N$-ality-dependent string tension. The limit is
action-dependent exactly through $(\sigma^2,\nu)$.

**Referee verdict, 2026-09-27: ACCEPT.** The example is a probability
mixture for $\kappa a^2\le1$. Its coefficient is
$e^{-\lambda_2a^2C_2(R)/2}[1-\kappa a^2(1-\cos(2\pi k(R)/N))]$.
For Euclidean time $T$ the cylinder area is $cLT$, giving the stated
energy of the circle transfer Hamiltonian with vacuum energy subtracted.
At $\lambda_2=0$ neutral representations can have zero energy too.

## 3. Any dimension: the error budget of one step

Let $t_n$ be the plaquette heat time at refinement step $n$, which by
eq. (1) of the series/parallel note scales as $\lambda_Da_n^{4-D}$ at fixed
physical coupling, and let $L$ be a fixed physical box side. One
directional step leaves three kinds of error.

- **Perturbative.** Coupling shifts and irrelevant operators of relative
  size $O(t_n)$ (Hypothesis P($\alpha$) and Proposition 7 of the
  series/parallel note).
- **Large-field.** Configurations far from the identity at the lattice
  scale, with action at least $c/t_n$, of density per physical volume
  about $a_n^{-D}e^{-c/t_n}$; here $c$ depends on the lattice action (for
  heat-kernel $U(1)$ it is the vortex constant of Theorem 5 there).
- **Jump.** The action's Lévy content, the part of $\nu$ in Theorem 2.

These scales become a sufficient error budget only when they bound
normalized measures or specified observables uniformly, with stability
under blocking. In $D\ge3$ plaquette constraints prevent inferring a
Lévy classification directly from the two-dimensional theorem.

| $D$ | $t_n$, fixed $\lambda_D$ | Perturbative | Large-field, $\sum(L/a_n)^De^{-c/t_n}$ |
| --- | --- | --- | --- |
| 2 | $\lambda_2a_n^2\to0$ | summable | summable; limit set by $(\sigma^2,\nu)$ |
| 3 | $\lambda_3a_n\to0$ | summable | summable faster than any power |
| 4 | $g^2(a_n)\to0$, logarithmically | resums into running | $\propto(a_n\Lambda)^{2b_0c-4}$, needs $2b_0c>4$ |
| $>4$ | $\lambda_Da_n^{4-D}\to\infty$ | no small parameter | no small-field regime |

**The perturbative column, with its sources.** For $D<4$, $t_n$ falls
geometrically along the dyadic sequence, so coupling shifts of relative
order $t_n$ sum to a finite renormalization: superrenormalizability.
For three-dimensional lattice Yang--Mills, Balaban's ultraviolet
stability is the constructive form of this statement in his
block-averaging scheme
([Balaban 1985](https://doi.org/10.1007/BF01229380), metadata). For
$D=4$ the heat time is the coupling itself, and each isotropic step
shifts $g^{-2}$ by the same amount, $-2b_0\log2$ at one loop, with
$b_0=11N/(48\pi^2)$ for pure $SU(N)$
([Gross and Wilczek 1973](https://doi.org/10.1103/PhysRevLett.30.1343);
[Politzer 1973](https://doi.org/10.1103/PhysRevLett.30.1346); metadata).
These shifts do not sum; they are the running coupling. Different
lattice actions share the first two coefficients of the running and
differ by a finite factor in $\Lambda$, computed at one loop for the
Wilson action by
[Hasenfratz and Hasenfratz (1980)](https://doi.org/10.1016/0370-2693(80)90118-5)
(abstract as indexed) and
[Dashen and Gross (1981)](https://doi.org/10.1103/PhysRevD.23.2340)
(metadata); for pure $SU(3)$ with the Wilson action the standard value is
$\Lambda_{\overline{\rm MS}}/\Lambda_{\rm lat}\approx28.81$
([Capitani 2003, review](https://doi.org/10.1016/S0370-1573(03)00211-4),
as indexed). The heat-kernel action as a lattice action is treated by
[Menotti and Onofri (1981)](https://doi.org/10.1016/0550-3213(81)90560-5)
(metadata). For $D>4$, $t_n$ grows as $a\to0$ at fixed $\lambda_D$;
lattice Monte Carlo finds a phase transition between the confining
strong-coupling regime and a weak-coupling spin-wave phase for $SU(2)$ in
five dimensions, and none in four
([Creutz 1979](https://doi.org/10.1103/PhysRevLett.43.553), abstract). A
continuum limit there would need a non-trivial ultraviolet fixed point,
and none is established.

**The four-dimensional threshold.** With $g^{-2}(a)=2b_0\log(1/(a\Lambda))$,
the convention of the refinement note §6, $e^{-c/g^2(a)}=(a\Lambda)^{2b_0c}$.
For pure $SU(N)$, $b_0=11N/(48\pi^2)$, so this particular leading-power
expression for density per physical volume vanishes iff

$$c>\frac2{b_0}=\frac{96\pi^2}{11N}:\qquad c>43.1\ (SU(2)),\qquad
c>28.7\ (SU(3)).$$

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** ACCEPT the strict power threshold; an action lower bound supplies only an upper density bound after entropy control, and equality requires prefactors and higher-loop terms.

For a dyadic sequence and a bound
$C a^{-4}[\log(1/a\Lambda)]^p e^{-c/g^2(a)}$, with fixed $p$ and
$g^{-2}=2b_0\log(1/a\Lambda)+O(\log\log(1/a\Lambda))$, the strict
inequality ensures summability regardless of these logarithmic powers.
At equality, an actual $n^{-p'}$ bound tends to zero if $p'>0$ and is
summable if $p'>1$. An upper estimate that grows below threshold proves
no survival or divergence. General defect families also need multiplicity,
size-modulus and interaction bounds.

A continuum instanton has $c=8\pi^2\approx79$, giving the density
$(a\Lambda)^{11N/3}a^{-4}$ of small instantons, which vanishes for every
$N\ge2$ because $11N/3>4$. Lattice actions admit dislocations, small
configurations of topological charge whose action lies below $8\pi^2$.
In units of the instanton action the threshold reads
$c/(8\pi^2)>12/(11N)$, which is $6/11$ for $SU(2)$: this is the known
dislocation criterion, found for the topological susceptibility by
[Pugh and Teper (1989)](https://doi.org/10.1016/0370-2693(89)91067-8)
(abstract: with the plaquette action the $SU(2)$ susceptibility diverges
in the continuum limit) and
[Göckeler, Kronfeld, Laursen, Schierholz and Wiese (1989)](https://doi.org/10.1016/0370-2693(89)90640-0)
(metadata), and stated in the form "smaller than 6/11 (for SU(2)) times
the continuum value of a one-instanton configuration" by
[DeGrand, Hasenfratz and Zhu (1996)](https://doi.org/10.1016/0550-3213(96)00301-X)
(passage). Suitably restrictive admissibility conditions can exclude
specific rough dislocations; the precise action and cutoff must be given
([Lüscher 1982](https://doi.org/10.1007/BF02029132), metadata, for lattice
topology). Applying the power criterion to another defect family requires
its own uniform density estimate. Higher-loop and determinant factors
matter particularly at the equality threshold.

**Correction (GPT-6 Astra referee), 2026-09-27 — REJECT the unconditional universality inference:** the three scales alone do not prove a common continuum theory.

**What this says about the mass gap.** If normalized blocking estimates,
iteration stability, large-field entropy control and continuum
reconstruction identify a common limit, its physical spectrum can then
be compared across regularizations. The expected dimensional forms are
$C_3\hbar c\lambda_3$ in $D=3$ and $C_4\hbar c\Lambda$ in $D=4$.
Proving the required common limit and its positive infrared threshold
remains part of the mass-gap map. The present error budget identifies
candidate sufficient estimates for that work.

## 4. Consequence for STATE

Item 1 of STATE gains its action and dimension dependence. The next
steps on this line are to state Hypothesis P($\alpha$) for a general
symmetric class-function action (second moment, large-field constant
and jump content as its data), and to connect the four-dimensional
large-field threshold to the H1 blocking hypothesis of the
[conditional theorem](mass-gap-conditional-theorem.md). For the joint
paper, Theorem 2 gives the two-dimensional row of the comparison for
every action at once, and the table gives the other rows.
