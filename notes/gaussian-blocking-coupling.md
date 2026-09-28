# Gaussian product blocking: the tree-level coupling never moves

**After refereeing (GPT-6 Astra), 2026-09-28.** G1: **REFINE**, with
corrections applied below. The alias sum, its normalization, the $n=0$
contribution and the closedness/projector argument are **ACCEPT**.
Iteration is **REFINE**: the covariance must be bounded near nonzero
aliases; the centred $O(K^2)$ conclusion requires that order for the
input. Constants may grow with iteration depth. Each unstaggered index
pair uses a staggered index outside that pair; the witnesses may differ
between pairs. The harmonic mode is separate from $K\to0$.
The sharp-blocking caution is **ACCEPT**: the
[composition note](four-dimensional-composition.md), Theorem 2, proves
an explicit divergent covariance bound. Its §3 checks that the delta
constraint in Bietenholz--Wiese retains spatial averaging.

**Result, 2026-09-28 (Claude; G1 refereed with refinements above).** For
the free lattice gauge field in $D$ dimensions with heat time $t$, one
isotropic product-blocking step $a\mapsto2a$ gives

$$C'(K)=2^{4-D}t\,[P_{\rm cont}(\hat K)+O(K)]$$

on exact 2-forms, with $O(K^2)$ in plaquette-centred conventions for
the nearest-plaquette input (Theorem G1). The coefficient is exactly
$\lambda_D(2a)^{4-D}$. The statement holds for positive input covariances
supported on exact forms, bounded near nonzero aliases, with the same
small-momentum expansion. It iterates at every finite depth. The four
directional integrations compose by Fubini, preserving the tree-level
coupling in the geometric heat-time normalization. In $1+3$, $t$ stays
fixed.

**Consequence for cell 4.** In (15) and the many-steps remark of the
[four-dimensional note](four-dimensional-parallel-log.md), the Gaussian
zero-momentum normalization introduces no matching shift. The one-loop
endpoint term depends on the full shape and its non-abelian background
completion, including generated cubic and quartic vertices. The average
rate needs $c_n=o(n)$; logarithmic growth of $c_n$ suffices. Growth of
shape parameters needs a separate estimate relating it to $c_n$.

**Caution.** Sharp product blocking retains fluxes through sharp
surfaces. Their ultraviolet boundary fluctuations obstruct a finite
nondegenerate covariance fixed point (composition note, Theorem 2).
[Bell--Wilson 1975](https://doi.org/10.1103/PhysRevB.11.3431)
(metadata and abstract) supplies the Gaussian fixed-point framework.
[Bietenholz--Wiese 1996](https://doi.org/10.1016/0550-3213(95)00678-8)
(§3, equations (3.1)--(3.6), passage) uses spatially averaged gauge
variables even with an exact delta constraint. These are distinct
choices of blocking map.

## 1. Setting

Take $G=\mathbb R$ (colour components decouple) on a periodic lattice
of spacing $a$, link variables $A$, fluxes $\phi=dA$ and weight
$\prod_p e^{-\phi_p^2/(2t)}$. After gauge reduction the flux covariance
is $tP(k)$, the orthogonal projector onto exact 2-forms for $k\ne0$.
The harmonic sector is set aside. Here zero-momentum coefficient means
the limit through nonzero momenta after the bulk limit; one may also
adjoin a constant harmonic background with its Maxwell action.

Product blocking sums the two fine links along each coarse link.
Stokes gives

$$(B\phi)_{\mu\nu}(X)=\sum_{a,b\in\{0,1\}}
 \phi_{\mu\nu}(2X+ae_\mu+be_\nu).$$

This composes the Gaussian pushforwards of Proposition 1 of the
[series/parallel note](series-parallel-gauge-refinement.md).

## 2. Theorem G1 and proof

*Alias sum.* With unitary Fourier transforms,
$k_n=K/2+\pi n$, $n\in\{0,1\}^D$, and

$$\begin{aligned}
 (B\phi)^\wedge_{\mu\nu}(K)
 &=2^{-D/2}\sum_n f_{\mu\nu}(k_n)\hat\phi_{\mu\nu}(k_n),\\
 f_{\mu\nu}(k)&=(1+e^{ik_\mu})(1+e^{ik_\nu}),\\
 C'(K)&=2^{-D}t\sum_n F(k_n)P(k_n)F(k_n)^*,
 \quad F=\operatorname{diag}f.
\end{aligned}$$

*The term $n=0$.* Here
$|f_{\mu\nu}(K/2)|^2=16\cos^2(K_\mu/4)\cos^2(K_\nu/4)$.
The lattice projector is $P_{\rm cont}(\hat K)+O(K)$.
With the phases at plaquette centres, the curl uses $2\sin(k_j/2)$,
the block factors become $4\cos(K_\mu/4)\cos(K_\nu/4)$, and the error
is $O(K^2)$. The contribution is therefore
$2^{4-D}t[P_{\rm cont}(\hat K)+O(K^2)]$ in this convention.

*Staggered terms.* If either $n_\mu$ or $n_\nu$ is 1, the corresponding
factor in $f_{\mu\nu}$ is $O(K)$. If both are zero, choose
$n_\lambda=1$ outside the pair. On the exact subspace, closedness gives

$$d_\lambda\phi_{\mu\nu}
 =d_\nu\phi_{\mu\lambda}-d_\mu\phi_{\nu\lambda},
 \qquad d_j=e^{ik_j}-1.$$

For $|K|\le1$, its component functional has norm at most
$|K|/(4\cos(1/4))\le |K|/2$. Equivalently, applying the inequality to
$Pe_{\mu\nu}$ and using
$\langle e_{\mu\nu},Pe_{\mu\nu}\rangle=\|Pe_{\mu\nu}\|^2$
gives $\|Pe_{\mu\nu}\|\le |K|/2$.
When both form factors are unsuppressed, use this bound twice in
$P_{\mu\nu,\rho\sigma}=\langle Pe_{\mu\nu},Pe_{\rho\sigma}\rangle$;
each pair may choose its own staggered witness. When a form factor is
suppressed it supplies the corresponding power. Every contribution is
$O(K^2)$.

More explicitly, put $m=\binom D2$. The columns give
$\|PF^*\|\le2\sqrt m|K|$. For a general covariance $C=PCP$ with
$\|C\|\le M$ near the nonzero aliases, their total contribution has
operator norm at most

$$2^{-D}(2^D-1)4mM|K|^2.$$

*Iteration.* Assume in addition
$C(k)=t[P_{\rm cont}(\hat k)+O(k)]$ at the origin (or the centred
$O(k^2)$ version for that stronger conclusion). The preceding bound
handles the nonzero aliases, and the small-momentum hypothesis handles
$n=0$. The output retains exact support by Stokes and is bounded away
from the origin. Hence induction multiplies $t$ by $2^{4-D}$ at each
finite step. The nearest-plaquette input and all its finite iterates
have the centred $O(k^2)$ property. The remainder constants need no
bound uniform in iteration depth for this conclusion.

Fubini composes the directional integrations. Their constant-flux
coefficient agrees with the reference geometric heat times; the
matrix defect and the full composed kernel are given in Theorem 1 of
the composition note. $\square$

## 3. What the theorem leaves to the interacting theory

The abelian Gaussian has no loop correction to the coupling. In a
non-abelian background the determinant depends on its background
Hessian, so G1 fixes only the tree-level normalization. The full
momentum dependence and the background vertices need separate bounds.
The composition note gives an exact determinant continuity criterion
and states the remaining vertex and infrared estimates explicitly.

## 4. Consequence for STATE

G1 closes the Gaussian zero-momentum part at every finite depth.
Follow the composition note for sharp-blocking shape growth and the
one-loop matching criterion; the average-rate condition is $c_n=o(n)$.
