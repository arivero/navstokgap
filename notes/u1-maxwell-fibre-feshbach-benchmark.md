# A gauge-invariant nonconstant-mode Feshbach benchmark in $3+1$ dimensions: free $U(1)$ Maxwell theory

This is a positive benchmark for workstream A.  It gives a periodic,
gauge-invariant regulator in which the nonconstant-mode projection, its
energy separation, and its Schur complement are all exact.  The model is
the Gaussian (Maxwell) $U(1)$ gauge theory, not non-abelian Yang--Mills;
its purpose is to isolate the A1/A2 interface before interactions and
non-abelian fibre geometry are introduced.

The result is complementary to the massive scalar B/D benchmark in
[$U(1)$ Gaussian blocking and OS reconstruction](u1-gaussian-blocking-os-benchmark.md):
here the emphasis is a gauge quotient and nonconstant-mode Feshbach split,
not a supplied mass or a continuum mass-gap claim.

## 1. Periodic Gaussian gauge regulator and its physical quotient

Let $\Lambda_{a,L}$ be the cubic spatial lattice with spacing $a$, $N_s$
sites per direction, and $L=N_sa$.  Write $C^q(\Lambda;\mathbb R)$ for
real lattice $q$-cochains, with coboundary $d$ and the translation-invariant
lattice inner product.  A Gaussian $U(1)$ connection is a real one-cochain
$A$, with gauge transformation
\[
 A\longmapsto A+d\chi.                                      \tag{1}
\]
The local gauge-invariant field strength is $dA$.  Compact $U(1)$ large
gauge transformations identify the three harmonic holonomies modulo
$2\pi$; they act only in the harmonic factor below.  The nonconstant
Gaussian connection is equivalently the topologically trivial Maxwell
sector.  Thus this is a gauge-invariant Gaussian/Maxwell regulator, rather
than the compact Wilson action with its non-Gaussian plaquette potential.

The discrete Hodge decomposition gives a gauge-invariant identification
of the physical configuration quotient,
\[
 C^1(\Lambda;\mathbb R)/dC^0(\Lambda;\mathbb R)
 \simeq \mathcal H^1\oplus\mathcal T,
 \qquad
 \mathcal T=\{A:\ d^*A=0,\ A\perp\mathcal H^1\},           \tag{2}
\]
where $\mathcal H^1$ is the three-dimensional harmonic-cochain space.
No particular Coulomb-gauge representative is part of the statement:
(2) is a decomposition of the quotient equipped with its induced inner
product.  Upon quantization, the physical Hilbert space factorizes as
\[
 \mathcal H_{\rm phys}=\mathcal H_{\rm harm}\otimes
 \mathcal F(\mathcal T_\mathbb C).                          \tag{3}
\]
Here $\mathcal H_{\rm harm}=L^2(U(1)^3)$ may be used when the large-gauge
identifications are retained.  Its constant function is the harmonic
vacuum.  The transverse factor is the usual bosonic Fock space; Gauss'
law has already removed the longitudinal lattice modes.

After normal ordering its nonconstant part, the positive Hamiltonian is
\[
 H_{a,L}=H_{\rm harm}\otimes1+1\otimes H_\perp,
 \qquad
 H_\perp=\sum_{k\ne0}\sum_{\lambda=1}^2
 \hbar c\,q_a(k)\,a^*_{k,\lambda}a_{k,\lambda},             \tag{4}
\]
with lattice momentum and dispersion
\[
 k_i=\frac{2\pi n_i}{L},\quad n_i\in\{0,\ldots,N_s-1\},
 \qquad
 q_a(k)=\frac2a\left(\sum_{i=1}^3\sin^2\frac{k_i a}{2}\right)^{1/2}.
                                                                    \tag{5}
\]
Equation (4) follows directly by diagonalizing $d^*d$ on $\mathcal T$.
For every $k\ne0$ its eigenspace has the two transverse polarizations;
the exact separation of the harmonic modes is a consequence of
$d\mathcal H^1=0$.

## 2. Exact nonconstant-mode lower bound

The smallest nonzero value of (5) is attained at one lattice unit of
momentum:
\[
 q_{a,\min}=\frac2a\sin\frac\pi{N_s}
 \ge\frac{2\pi}{L}\left(1-\frac{\pi^2}{6N_s^2}\right).     \tag{6}
\]
The inequality uses $\sin x\ge x(1-x^2/6)$ for $0\le x\le\pi/2$.
Let $\Omega_\perp$ be the transverse Fock vacuum and set
\[
 P=1_{\rm harm}\otimes
 |\Omega_\perp\rangle\langle\Omega_\perp|,
 \qquad \bar P=1-P.                                         \tag{7}
\]
Both projections are defined after taking the gauge quotient (2), and
therefore preserve the physical, gauge-invariant Hilbert space.

> **Theorem 1 (exact Maxwell A1/A2 fibre benchmark).**
> On the periodic Gaussian $U(1)$ regulator (4),
> \[
> \bar P H_{a,L}\bar P
> \ge \bar P\bigl(H_{\rm harm}+\hbar c\,q_{a,\min}\bigr)\bar P,
>                                                                    \tag{8}
> \]
> and the Feshbach off-diagonal is identically zero,
> \[
> B:=PH_{a,L}\bar P=0.                                       \tag{9}
> \]
> In particular, fibrewise over every harmonic state, the first
> nonconstant excitation costs at least the positive energy in (6), and
> \[
> B(D-E)^{-1}B^*=0                                            \tag{10}
> \]
> whenever the fibre resolvent is defined.  Thus the relative-Schur form
> used in A2 holds with $\epsilon=\eta=0$.

*Proof.*  A vector in $\operatorname{ran}\bar P$ has at least one
transverse oscillator quantum.  Each term in (4) is nonnegative, so its
$H_\perp$ energy is at least $\hbar c q_{a,\min}$, which proves (8).
The two summands in (4) act on separate tensor factors and conserve the
transverse particle number.  Hence $P$ reduces $H_{a,L}$ and (9) follows.
Equation (10) is immediate. $\square$

The comparison with the A1 scale is explicit: for fixed physical $L$,
$q_{a,\min}\to2\pi/L$ as $a\downarrow0$.  In this exactly solvable gauge
model the role of the desired nonconstant-mode estimate is therefore
realised with no support, gauge-fixing, or volume-dependent error.

## 3. What the benchmark isolates for non-abelian A

The proof exposes the three ingredients that a non-abelian fibre
construction must retain:

1. **Gauge quotient before projection.**  The split in (2) is defined on
   physical degrees of freedom, so $P$ is gauge invariant rather than a
   projection on a chosen link coordinate.
2. **A uniform fast-sector separation.**  The exact lower bound is the
   lattice dispersion (6), which has a controlled continuum limit at
   fixed $L$.
3. **A quantitative off-diagonal statement.**  The abelian Hamiltonian
   conserves transverse particle number, yielding (9).  In a non-abelian
   theory the background-dependent fibre and interaction replace this
   equality by the relative Schur estimate requested in A2.

The harmonic $U(1)^3$ factor has intentionally been retained as a slow
sector; this note asserts a positive nonconstant-fibre estimate and makes
no claim about a full Yang--Mills continuum construction.  The next A
step is therefore sharply specified: construct a gauge-covariant dressed
non-abelian replacement for (7), control the fibre quantum metric, and
replace the exact zero in (9) by a cutoff-uniform relative bound.
