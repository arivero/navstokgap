# A $3+1$-dimensional massive $U(1)$ Gaussian benchmark: exact fluctuation blocking and OS reconstruction

**Result — a positive benchmark for workstreams B and D.**  A massive
complex Gaussian scalar in four Euclidean dimensions, with its global
$U(1)$ symmetry, supplies a complete example in which the blocking and
continuum-reconstruction interfaces of the mass-gap assembly are realised.
It is not Yang--Mills, its mass is a supplied relevant parameter, and it
makes no claim about the Clay problem.  Its use is diagnostic: it proves
that the H1$_{\rm gap}$, H1$_{\rm OS}$ and H3 architecture is nonempty and
identifies the exact estimates a non-abelian construction would need to
replace.

The blocking here is a local **Gaussian Markov kernel**, obtained from a
finite-range covariance decomposition, rather than a deterministic link
block map.  This distinction is retained throughout.  The theorem below
therefore proves B/D for a $3+1$-dimensional $U(1)$-*symmetric scalar*
model, not for a compact $U(1)$ gauge theory or for Wilson $SU(3)$.

## 1. The model and its continuum target

Let $\Phi=(\phi^1+i\phi^2)/\sqrt2$ be a complex scalar; its global
$U(1)$ action is $\Phi\mapsto e^{i\alpha}\Phi$.  On the four-dimensional
lattice $a\mathbb Z^4$, take two independent real centered Gaussian fields
with covariance
\[
 C_a=\hbar\,(-\Delta_{\rm lat}+(am)^2)^{-1},\qquad m>0,     \tag{1}
\]
in lattice units.  Here $m$ has inverse-length units and
$-\Delta_{\rm lat}$ is the dimensionless nearest-neighbour lattice
Laplacian.  The dimensionless lattice field represents
$a\,\phi_{\rm cont}$: for $f\in\mathcal S(\mathbb R^4)$ use the scaled
pairing
\[
 \Phi_a(f)=a^3\sum_{n\in\mathbb Z^4}f(an)\varphi(n).       \tag{1a}
\]
With this convention its covariance tends to (2).  The lattice covariance
is translation invariant and invariant under the global $U(1)$ rotation of
the two real components.

The intended continuum covariance on Schwartz test functions is
\[
 C_m(f,g)=\hbar\int_{\mathbb R^4}
 \frac{\overline{\widehat f(p)}\widehat g(p)}
 {p_0^2+|\mathbf p|^2+m^2}\,\frac{d^4p}{(2\pi)^4}.           \tag{2}
\]
It is the standard massive complex free field.  The physical one-particle
energy is
\[
 E(\mathbf p)=\hbar c\sqrt{|\mathbf p|^2+m^2},               \tag{3}
\]
so a reconstruction with this covariance has energy gap $\hbar c m$.
The supplied scale $m$ is explicit; this benchmark does not generate it.

## 2. The finite-range input and the Gaussian block kernel

We use the following standard finite-range decomposition input.  For
$d\ge3$, the massive lattice resolvent has a decomposition into positive
covariances
\[
 C_a=\sum_{j=0}^{K-1}\Gamma_{a,j}+C_{a,K},                   \tag{4}
\]
where, for a fixed dyadic block factor $L\ge2$ and a fixed $R<\infty$,
\[
 \Gamma_{a,j}(x,y)=0\quad\hbox{if}\quad |x-y|_\infty>RL^j\quad
 \text{(lattice units)}.                                    \tag{5}
\]
The residual $C_{a,K}$ is positive.  The infinite version of (4) converges
to $C_a$.  The fixed $L$ may be chosen dyadic; an $L$-block is then a finite
bundle of binary blocks.  Thus the B interface below is the fixed-factor
version of H1$_{\rm gap}$; the telescoping proof in the assembly theorem is
unchanged after $2^K a$ is replaced by $L^K a$.

This is the finite-range decomposition of the massive lattice resolvent;
see Brydges--Guadagni--Mitter,
[*J. Stat. Phys.* **115** (2004) 415--449](https://doi.org/10.1023/B:JOSS.0000019818.81237.66),
whose theorem supplies positive finite-range components in dimensions
$d\ge3$.  Only positivity, (4), and (5) are used below.

Let $\zeta_j$ be independent centered Gaussian fields of covariance
$\Gamma_{a,j}$ and let $\varphi_K$ have covariance $C_{a,K}$, independent
of them.  Then
\[
 \varphi_j=\zeta_j+\varphi_{j+1},\qquad
 \varphi_0=\sum_{r=0}^{K-1}\zeta_r+\varphi_K.               \tag{6}
\]
For a bounded local observable $F$ of $\varphi_j$, set
\[
 \mathcal E_jF(\varphi_{j+1})
 =\mathbb E_{\zeta_j}F(\zeta_j+\varphi_{j+1}).               \tag{7}
\]
Equation (7) is the block kernel.  It is local in the conditional sense
that its fluctuation covariance has the finite range (5).  It is a
Markov-kernel blocking, not a claim that $\varphi_{j+1}$ is a deterministic
function of $\varphi_j$.

## 3. Exact H1$_{\rm gap}$ transport for bounded local observables

Let $F,G$ have supports at distance $d_j$ in units of the $j$-th scale.
The conditional covariance identity is
\[
 \begin{split}
 &\langle F;G\rangle_{\varphi_j}
 -\langle\mathcal E_jF;\mathcal E_jG\rangle_{\varphi_{j+1}}\\
 &\hspace{2cm}=
 \mathbb E_{\varphi_{j+1}}
 \big[\operatorname{Cov}_{\zeta_j}
 (F(\zeta_j+\varphi_{j+1}),G(\zeta_j+\varphi_{j+1}))\big]. \tag{8}
 \end{split}
\]
If $d_j>R$, the restrictions of $\zeta_j$ seen by $F$ and $G$ are
independent by (5), so the right side of (8) vanishes.  If $d_j\le R$, its
absolute value is at most $4\|F\|_\infty\|G\|_\infty$.  Consequently, for
any selected $\gamma_*>0$,
\[
 \left|\langle F;G\rangle_{\varphi_j}
 -\langle\mathcal E_jF;\mathcal E_jG\rangle_{\varphi_{j+1}}\right|
 \le 4e^{\gamma_*R}\|F\|_\infty\|G\|_\infty
 e^{-\gamma_*d_j}.                                          \tag{9}
\]
All constants are independent of $a$, $j$, and the periodic volume.

**Proposition 1 (B interface, kernel form).**  The Gaussian block kernel
(7) satisfies H1$_{\rm gap}$ of
[the conditional assembly theorem](mass-gap-conditional-theorem.md), with
support buffer zero in the scale coordinates and the explicit constants
\[
 \gamma_*>0\ \text{arbitrary},
 \qquad C_j=4e^{\gamma_*R}.                                  \tag{10}
\]

*Proof.*  Equation (8) is the tower property for conditional covariance.
The finite-range independence proves the zero statement for $d_j>R$.
The elementary bound $|\operatorname{Cov}(X,Y)|\le4\|X\|_\infty\|Y\|_\infty$
gives the remaining case, and multiplying it by
$e^{\gamma_*R}e^{-\gamma_*d_j}\ge1$ for $d_j\le R$ gives (9). $\square$

This is an exact positive version of the scale-by-scale estimate: the
integrated fluctuation has no connected effect beyond its one-scale range.
For a gauge theory, establishing an analogue of (5) after a local,
gauge-covariant block operation is precisely the missing B problem.

## 4. H1$_{\rm OS}$ for a renormalized Weyl test algebra

The uniform sup-norm prefactor in (10) need not be summed over an
unbounded number of scales.  The assembly theorem explicitly permits a
specified OS-continuous seminorm instead.  In this Gaussian benchmark it
is exact.

For a real lattice test function $f$, let
\[
 W_j(f)=e^{i\langle\varphi_j,f\rangle},
 \qquad a_j(f)^2=(f,\Gamma_{a,j}f).                           \tag{11}
\]
The conditional Gaussian integral gives
\[
 \mathcal E_jW_j(f)=e^{-a_j(f)^2/2}W_{j+1}(f),                \tag{12}
\]
and conditional Cauchy--Schwarz gives, for Weyl observables,
\[
 \left|\langle W_j(f);W_j(g)\rangle-
 \langle\mathcal E_jW_j(f);\mathcal E_jW_j(g)\rangle\right|
 \le a_j(f)a_j(g).                                           \tag{13}
\]
Positivity and (4) give the summability identity
\[
 \sum_{j=0}^{K-1}a_j(f)^2
 \le(f,C_af).                                                 \tag{14}
\]
For lattice representatives of fixed smooth continuum test functions,
$(f,C_af)$ converges to (2) and is uniformly finite.  Thus
\[
 \sum_{j<K}a_j(f)a_j(g)
 \le \sqrt{(f,C_af)(g,C_ag)}                                 \tag{15}
\]
is uniform in the cutoff.

**Proposition 2 (H1$_{\rm OS}$, explicit seminorm version).**  The algebra
generated by Weyl observables with smooth compactly supported continuum
test functions has a cutoff-uniform renormalized fluctuation bound (15).
It realizes the OS-seminorm alternative to H1$_{\rm OS}$ in the assembly
theorem.

*Proof.*  Equations (12)--(13) are elementary Gaussian characteristic
function identities.  Sum the nonnegative quadratic forms in (11) using
(4), then apply Cauchy--Schwarz to the scale index. $\square$

The assertion is nontrivial in the required sense: it controls the entire
ultraviolet tower for a dense bounded test algebra, rather than only a
single correlation at one cutoff.

## 5. H3: the continuum limit and Osterwalder--Schrödinger reconstruction

For fixed Schwartz functions, the Fourier multiplier of the lattice
covariance converges pointwise to that of (2) and is dominated after
smearing.  Hence all Gaussian Schwinger functions converge by Wick's rule
to those with covariance $C_m$.  The global $U(1)$ symmetry is preserved
throughout because the two real components have the same covariance.

Reflection positivity can be seen directly.  Let $\theta$ reflect Euclidean
time and let $f$ be supported at positive times.  With
$\omega_{\mathbf p}=\sqrt{|\mathbf p|^2+m^2}$,
\[
 C_m(\theta f,f)=\hbar\int_{\mathbb R^3}
 \frac1{2\omega_{\mathbf p}}
 \left|\int_0^\infty e^{-\omega_{\mathbf p}t}
 \widehat f(t,\mathbf p)\,dt\right|^2
 \frac{d^3\mathbf p}{(2\pi)^3}\ge0.                         \tag{16}
\]
Gaussian positivity promotes (16) from linear observables to the
polynomial/Weyl algebra.  Translation and Euclidean rotation covariance
are immediate from (2).

The OS Hilbert space is the symmetric Fock space over
\[
 \mathcal H_1=L^2\!\left(\mathbb R^3,
 \frac{d^3\mathbf p}{(2\pi)^3 2\omega_{\mathbf p}\right)
 \otimes\mathbb C^2,                                        \tag{17}
\]
with Hamiltonian
\[
 H=d\Gamma(\hbar c\,\omega_{\mathbf p}).                   \tag{18}
\]
The two components implement the global $U(1)$ charge representation.  The
one-particle vectors created by smeared fields are nonzero and, together
with their Wick products, generate the Fock space.

**Theorem 3 (D interface and positive continuum gap).**  The lattice
Gaussian Schwinger functions converge to an OS-positive, nontrivial
$3+1$-dimensional continuum $U(1)$-symmetric scalar theory.  Its local
spectral measures converge weakly for the Weyl test algebra, its local
vectors are dense in the OS Hilbert space, and
\[
 \operatorname{spec}(H)\cap(0,\hbar c m)=\varnothing,
 \qquad \inf\bigl(\operatorname{spec}(H)\setminus\{0\}\bigr)=\hbar c m. \tag{19}
\]

*Proof.*  Covariance convergence and Wick's rule prove convergence of the
Schwinger functions.  Equation (16) gives reflection positivity, and its
standard OS quotient/completion is the Fock space (17).  Time translation
acts by the second quantization (18).  The one-particle multiplication
operator has bottom $\hbar cm$; every non-vacuum Fock sector has energy at
least that value.  Smeared one-particle fields give nonzero local vectors,
and finite particle vectors are dense.  Finally, convergence of the
Euclidean two-point Laplace transforms for Weyl derivatives gives weak
convergence of their finite spectral measures; their support is closed
inside $[\hbar cm,\infty)$. $\square$

## 6. What this attaches to the main programme

This benchmark attaches B and D in the requested order:

- **B:** a finite-range positive fluctuation covariance makes the
  successive connected-correlation difference (8) exactly local, yielding
  the explicit H1$_{\rm gap}$ estimate (9).
- **D:** summable Weyl fluctuation seminorms give H1$_{\rm OS}$, while
  (16)--(19) give OS convergence, nontriviality, spectral-measure support,
  and a positive continuum threshold.

It also separates the genuine non-abelian tasks.  The finite-range input is
an imported Gaussian-resolvent theorem; the mass $m$ is supplied; the block
is kernel-valued; and global $U(1)$ symmetry is not local gauge invariance.
A successful $SU(3)$ extension must replace each of these features with a
local gauge-covariant construction while preserving the B/D estimates.

## 7. Consequence for STATE

There is now a complete positive $3+1$ benchmark for the B/D interfaces:
a massive global-$U(1)$ Gaussian scalar has exact fluctuation blocking,
uniform renormalized observable control, OS reconstruction and energy gap
$\hbar cm$.  It demonstrates the intended assembly without asserting that
a supplied scalar mass or a global symmetry solves the Yang--Mills
programme.  The next main interfaces are C (analytic one-box mixing) and
A (nonconstant gauge-mode control).
