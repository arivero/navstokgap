# Compact U(1) under refinement: an explicit total-variation bound in three dimensions, and why it fails in four

**Result, 2026-09-27.** For the heat-kernel (Villain) $U(1)$ lattice gauge
theory on the periodic lattice $(\mathbb Z/N)^D$ of spacing $a$, physical
side $L=Na$ and plaquette heat time $t$, the lattice measure splits
exactly into a monopole-free part (the free photon together with the
physical flux sectors of the torus) and a gas of lattice monopoles with
Coulomb weights (Proposition 1; the duality of Banks, Myerson and Kogut).
A bound on the lattice Laplacian then gives:

- **$D=3$ (Theorem 2).** With $t=\lambda_3a\le1$,
  $$\bigl\|\mu_{a}-\mu_{a}^{\,0}\bigr\|_{\rm TV}\ \le\
  \frac{2(L/a)^3\,e^{-\pi^2/(6\lambda_3a)}}{1-e^{-\pi^2/(2\lambda_3a)}},$$
  where $\mu_a^0$ is the monopole-free measure. The monopole free-energy
  density per physical volume lies between
  $a^{-3}\cdot6e^{-2\pi^2/(3\lambda_3a)}$ (up to a factor tending to one)
  and $a^{-3}\cdot2e^{-\pi^2/(6\lambda_3a)}/(1-e^{-\pi^2/(2\lambda_3a)})$. At
  fixed $\lambda_3$ and $L$ everything compact vanishes faster than any
  power of $a$; along trajectories with $\lambda_3a\simeq c/\log(1/a)$ it
  stays finite. The flux sectors carry the weight
  $e^{-2\pi^2|m|^2/(\lambda_3L)}$, independent of $a$.
- **$D=4$ (Theorem 3, and a recorded failure).** With $t=g^2$, the same
  decomposition holds with flux-sector weight $e^{-2\pi^2|m|^2/g^2}$,
  independent of both $a$ and $L$, and the monopole-loop free energy per
  lattice cell lies between $12e^{-\pi^2/g^2}$ and
  $8e^{-\pi^2/(8g^2)}/(1-e^{-3\pi^2/(8g^2)})$, up to factors tending to one.
  The total-variation bound is then of order $(L/a)^4e^{-\pi^2/(8g^2)}$,
  which grows as $a\to0$ at fixed $g$. The criterion that closes the
  three-dimensional case fails here for an exact reason: the loop density
  per lattice cell is fixed by $g$ alone. The four-dimensional continuum
  statement (Driver's renormalized free field) needs observables and a
  coupling renormalization, which a partition-function bound cannot
  supply.

This is the first step of the $D=3$ programme of STATE carried out at the
level of the measure, with explicit $a$, $L$ and coupling, for the
smallest compact group. It sharpens Theorem 5 of the
[series/parallel note](series-parallel-gauge-refinement.md) (one step,
rate $e^{-\pi^2/(8t)}$) into a bound on the whole lattice measure with rate
$e^{-\pi^2/(6t)}$, and it puts numbers on the error-budget row of the
[zero-spacing note](zero-spacing-any-action.md). The duality is
established ([Banks, Myerson and Kogut 1977](https://doi.org/10.1016/0550-3213(77)90129-8),
metadata) and the continuum limit at fixed coupling is Gross's theorem
([Gross 1983](https://doi.org/10.1007/BF01210842), abstract as indexed);
the explicit total-variation bound and the flux-sector bookkeeping are
elementary consequences, with no novelty claimed.

## 1. The exact decomposition

Let $E$, $P$ and $C_3$ be the links, plaquettes and 3-cells of the
periodic hypercubic lattice $(\mathbb Z/N)^D$, $d$ the coboundary on
cochains, and $\Delta=dd^{\sf T}+d^{\sf T}d$ the Hodge Laplacian. The
heat-kernel measure on link angles $\theta\in[0,2\pi)^E$ is

$$\mu_a(d\theta)=\frac1Z\prod_{p\in P}k_t\bigl((d\theta)_p\bigr)\,
\frac{d\theta}{(2\pi)^{|E|}},\qquad
k_t(\phi)=\sum_{n\in\mathbb Z}e^{-tn^2/2}e^{in\phi}
=\sqrt{\frac{2\pi}t}\sum_{n\in\mathbb Z}e^{-(\phi+2\pi n)^2/(2t)}.$$

Write $\mathbb R^P=\operatorname{im}d\oplus\operatorname{im}d^{\sf T}\oplus\mathcal H$
(exact, coexact and harmonic 2-cochains; $\mathcal H$ is spanned by the
cochains constant on each of the $\binom D2$ plaquette orientations). For
$n\in\mathbb Z^P$ let $q=dn\in\mathbb Z^{C_3}$ (the monopole charges) and
$n_{\mathcal H}$ the harmonic projection of $n$.

**Proposition 1 (monopole decomposition).** $\mu_a$ is a mixture

$$\mu_a=\frac1Z\sum_{[n]\in\mathbb Z^P/d\mathbb Z^E}
w([n])\,\nu_{[n]},\qquad
w([n])=\exp\Bigl\{-\frac{2\pi^2}t\Bigl(q^{\sf T}(dd^{\sf T})^+q
+|n_{\mathcal H}|^2\Bigr)\Bigr\},$$

of probability measures $\nu_{[n]}$ on link angles, where $(dd^{\sf T})^+$ is
the pseudo-inverse on $\operatorname{im}d$ and $|\cdot|$ the Euclidean norm
on cochains. The classes $[n]$ with $q=0$ make up the monopole-free
measure $\mu_a^0$.

*Proof.* Insert the Poisson form of $k_t$ and exchange sum and integral.
The substitution $n\mapsto n+d\ell$, $\theta\mapsto\theta-2\pi\ell$
($\ell\in\mathbb Z^E$) groups the sum over $n$ into classes and extends the
angle integral to $\mathbb R^E$ modulo $2\pi$ times the integer closed
1-cochains, a lattice of full rank in the closed 1-cochains; the
remaining integrand depends on $\theta$ only through $\omega=d\theta$. So
the class $[n]$ contributes a constant times
$\int_{\operatorname{im}d}e^{-|\omega+2\pi n|^2/(2t)}d\omega$. Decompose
$n=n_{\rm ex}+n_{\rm co}+n_{\mathcal H}$ orthogonally. The exact part is
absorbed by translating $\omega$, and
$|n_{\rm co}|^2=(dn)^{\sf T}(dd^{\sf T})^+(dn)$ because
$n_{\rm co}=d^{\sf T}(dd^{\sf T})^+dn$. The remaining Gaussian integral is
the same for every class. $\square$

The classes are labelled by $q\in d\mathbb Z^P$ together with an integer
flux vector $m\in\mathbb Z^{\binom D2}$ through the coordinate 2-tori
(the integral cohomology of the torus is free). For fixed $q$ the harmonic
part is $n_{\mathcal H}=h(m)+y(q)$ with $h(m)$ the constant cochain of flux
$m$ and $y(q)$ an offset fixed by $q$. A cochain of flux $m_{\mu\nu}$ through
each $(\mu\nu)$ torus has value $m_{\mu\nu}/N^2$ on each of the $N^D$
plaquettes of that orientation, so

$$|h(m)|^2=N^{D-4}\sum_{\mu<\nu}m_{\mu\nu}^2 .$$

**Two elementary facts.** (i) Each Fourier mode of $\Delta$ on the
hypercubic lattice has eigenvalue $\sum_\mu4\sin^2(k_\mu/2)\le4D$, so
$\|dd^{\sf T}\|\le4D$ and $q^{\sf T}(dd^{\sf T})^+q\ge|q|^2/(4D)$ on
$\operatorname{im}d$. (ii) For $y$ fixed, the theta-type sum
$\sum_me^{-\alpha|h(m)+y|^2}$ lies between $e^{-\alpha|y|^2}\sum_me^{-\alpha|h(m)|^2}$
(pair $m$ with $-m$) and $\sum_me^{-\alpha|h(m)|^2}$ (its Fourier
coefficients are positive).

**The elementary monopole pair or loop.** For a single plaquette $p$, the
charge $q=d\,e_p$ is a nearest monopole pair ($D=3$) or an elementary
monopole loop ($D=4$), and $q^{\sf T}(dd^{\sf T})^+q=|P_{\rm co}e_p|^2$. By
translation invariance each plaquette has the same projections, so
$|P_{\rm ex}e_p|^2={\rm rank}\,d_1/|P|$ and
$|P_{\mathcal H}e_p|^2=\binom D2/|P|$. With
${\rm rank}\,d_1=|E|-(N^D-1)-D$:

$$D=3:\ |P_{\rm co}e_p|^2=\frac13\Bigl(1-\frac1{N^3}\Bigr),\qquad
D=4:\ |P_{\rm co}e_p|^2=\frac12\Bigl(1-\frac1{N^4}\Bigr).$$

For $D=3$ this agrees with the lattice Green's function:
$G(0)-G(e_1)=\frac16(1-N^{-3})$, so a nearest pair has energy
$2(G(0)-G(e_1))$.

## 2. Three dimensions: the theorem

**Theorem 2.** Let $D=3$, $N=L/a$, $t=\lambda_3a\le1$, and
$R=Z/Z^0$ the ratio of the full partition function to its monopole-free
part. Then

$$1+6N^3\exp\Bigl\{-\frac{2\pi^2}{3\lambda_3a}
-\frac{2\pi^2a^2}{\lambda_3L^3}\Bigr\}\ \le\ R\ \le\
\exp\Bigl\{\frac{2N^3e^{-\pi^2/(6\lambda_3a)}}{1-e^{-\pi^2/(2\lambda_3a)}}\Bigr\},$$

and

$$\|\mu_a-\mu_a^0\|_{\rm TV}\le1-\frac1R\le
\frac{2(L/a)^3e^{-\pi^2/(6\lambda_3a)}}{1-e^{-\pi^2/(2\lambda_3a)}}.$$

The monopole-free part is the free photon on the torus with the flux
sectors weighted by $\exp\{-2\pi^2|m|^2/(\lambda_3L)\}$.

*Proof.* The flux weight is $|h(m)|^2=N^{-1}|m|^2$ and $tN=\lambda_3L$.
Upper bound: by fact (ii) the sum over $m$ at fixed $q$ is at most its
value at $q=0$, so $R\le\sum_{q\in d\mathbb Z^P}
e^{-(2\pi^2/t)q^{\sf T}(dd^{\sf T})^+q}$. By fact (i) with $4D=12$ each term
is at most $e^{-(\pi^2/6t)|q|^2}$. Enlarge the sum to all of
$\mathbb Z^{C_3}$, $|C_3|=N^3$, and use
$\sum_{k\in\mathbb Z}e^{-\alpha k^2}\le1+2e^{-\alpha}/(1-e^{-3\alpha})$ (from
$k^2-1\ge3(k-1)$) with $\alpha=\pi^2/(6t)$, then $\log(1+x)\le x$.
Lower bound: keep $q=0$ and the $6N^3$ nearest pairs $q=\pm d\,e_p$
($3N^3$ plaquettes, two signs). Each pair has Coulomb energy at most
$\frac13$ and harmonic offset $|y|^2=|P_{\mathcal H}e_p|^2=N^{-3}$, and fact
(ii) gives the stated factor. Total variation: $\mu_a$ is the mixture
$R^{-1}\mu_a^0+(1-R^{-1})\mu_a^{\rm rest}$, so
$\|\mu_a-\mu_a^0\|_{\rm TV}\le1-R^{-1}\le\log R$. $\square$

**Reading.** In a box of fixed physical side, the lattice measure is
within total variation $O((L/a)^3e^{-\pi^2/(6\lambda_3a)})$ of the
monopole-free measure. At fixed $\lambda_3$ this tends to zero faster
than any power of $a$. By the summable-error criterion of the
[refinement note](refinement-composition-and-limit.md), Proposition 4, the
continuum question for the compact theory then reduces to that for the
free photon with flux sectors, which is Gaussian; Gross's theorem is the
continuum statement. The monopole free-energy density
$L^{-3}\log R$ lies between the two bounds in the summary. It stays
finite exactly when $e^{-c/(\lambda_3a)}\sim a^3$, that is along
$\lambda_3a\simeq c/(3\log(1/a))$ with $c$ between $\pi^2/6$ and $2\pi^2/3$:
the trajectories on which a Debye mass survives
([Göpfert--Mack 1982](https://doi.org/10.1007/BF01961240), abstract as
indexed). The exponents are bounds; the monopole self-energy of the
infinite lattice, $2\pi^2G(0)\approx4.99$ with $G(0)\approx0.2527$, lies
between them.

## 3. Four dimensions: the same bound, and why it fails

**Theorem 3.** Let $D=4$, $N=L/a$, $t=g^2$ with $g^2\le1$. Then

$$1+12N^4\exp\Bigl\{-\frac{\pi^2}{g^2}-\frac{2\pi^2}{g^2N^4}\Bigr\}\ \le\ R\
\le\ \exp\Bigl\{\frac{8N^4e^{-\pi^2/(8g^2)}}{1-e^{-3\pi^2/(8g^2)}}\Bigr\},$$

$\|\mu_a-\mu_a^0\|_{\rm TV}\le\log R$, and the flux sectors carry the
weight $\exp\{-(2\pi^2/g^2)\sum_{\mu<\nu}m_{\mu\nu}^2\}$.

*Proof.* As for Theorem 2, with $4D=16$, $|C_3|=4N^4$, $|h(m)|^2=|m|^2$,
$6N^4$ plaquettes and two signs for the elementary loops, loop energy at
most $\frac12$, and harmonic offset $N^{-4}$. $\square$

**The recorded failure.** In four dimensions the heat time is the
coupling itself, so at fixed $g$ the monopole-loop free energy per lattice
cell is a fixed number between the two bounds, and the total-variation
bound grows like $(L/a)^4$. The three-dimensional route, closeness of the
whole lattice measure to its Gaussian part, is unavailable in four
dimensions for an exact reason, and the free-energy density it
controls is a vacuum constant. The known continuum statement is
different in kind: the compact theory converges on its current sector to
a renormalized free electromagnetic field
([Driver 1987](https://doi.org/10.1007/BF01212424), abstract as
indexed), with the monopole loops renormalizing the charge. A
four-dimensional theorem in the insertion language therefore has to
control observables and a coupling shift per step, as Hypothesis P($\alpha$)
does, rather than the measure. This is the four-dimensional row of the
error budget in the zero-spacing note, now with the density per cell made
explicit: between $12e^{-\pi^2/g^2}$ and $8e^{-\pi^2/(8g^2)}$ up to factors
tending to one.

## 4. Consequence for STATE

Item 1 of STATE gains a measure-level theorem for $U(1)$ in $D=3$ with
explicit $a$, $L$, $\lambda_3$ (Theorem 2), and a recorded failure of the
same route in $D=4$ with its reason (Theorem 3). The non-abelian step that
corresponds to Theorem 2 needs a replacement for the Poisson
decomposition: for $SU(2)$ the exact kernel (11) of the series/parallel
note has image terms of both signs, so the mixture of Proposition 1 is not
available and the Laplace-remainder route of its Proposition 7 remains
the path.
