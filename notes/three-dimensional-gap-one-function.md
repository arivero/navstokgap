# Three-dimensional Yang--Mills: conditional scaling and the physical gap limit

For a **constructed physical** pure Yang--Mills theory in three spacetime
(two space) dimensions, with no additional parameters and a fixed square-torus
shape, dimensional covariance gives

$$\Delta(L)=E_3 f(x),\qquad E_3=\hbar^2c g_{\rm cl}^2,
\qquad x=\hbar g_{\rm cl}^2L.$$

The positive finite infinite-volume gap would require
$\lim_{x\to\infty}f(x)=C\in(0,\infty)$, together with physical spectral
convergence and reconstruction. Dimensional analysis alone proves none of
these existence or positivity statements. The constant-mode matrix model and
a volume-uniform strong-coupling lattice estimate control different regimes;
neither transports itself to that limit. The current-variable kinetic scale
$N/(2\pi)$ of Karabali--Nair is not an established full physical gap constant.
New research remains suspended; this note maintains the separate continuum
obligation and the exact normalization tests.

## Physical units and the one-variable form

Use a connection-valued field with
$S=(4g_{\rm cl}^2)^{-1}\int F^a_{\mu\nu}F^a_{\mu\nu}\,d^3x$ and weight
$e^{-S_E/\hbar}$. Then $[1/g_{\rm cl}^2]=\mathrm{action}\,\mathrm{length}$.
Put $\lambda_3=\hbar g_{\rm cl}^2=1/\ell_g$, which is an inverse length,
and $E_3=\hbar c\lambda_3$. The classical coupling by itself is not a mass
when physical $\hbar,c$ remain explicit. The mass unit is
$\mu=E_3/c^2=\hbar^2g_{\rm cl}^2/c$.

On $T_L^2\times\mathbb R$, if the gap depends only on those constants and $L$,
the [dimensional theorem](action-unit-dimensional-selection.md) makes it $E_3$
times a function of $x=L/\ell_g$. Vacuum-energy shifts leave a defined
excitation gap unchanged; that observation does not establish ultraviolet
construction or spectral convergence. The
[low-dimensional treatment](low-dimensional-mass-gap.md) owns the field
normalization and solved matrix/circle comparisons.

## Constant modes: an exact truncation and a conditional small-volume use

For $SU(2)$ in temporal gauge, take constant spatial components
$\vec a_1,\vec a_2$. With $F_{0i}=c^{-1}\dot a_i$ and
$F_{12}=\vec a_1\times\vec a_2$, their Lagrangian and Hamiltonian are

$$L_0=\frac{L^2}{2g_{\rm cl}^2c}|\dot{\vec a}|^2
 -\frac{L^2c}{2g_{\rm cl}^2}|\vec a_1\times\vec a_2|^2,$$

$$H_0=\frac{g_{\rm cl}^2c}{2L^2}\sum_{i=1}^2|\vec p_i|^2
 +\frac{L^2c}{2g_{\rm cl}^2}|\vec a_1\times\vec a_2|^2,
\qquad[a_i^a,p_j^b]=i\hbar\delta_{ij}\delta^{ab}.$$

This is C133 with $D=2$, $m_{\rm eff}=L^2/(g_{\rm cl}^2c)$ and
$g_B^2=L^2c/g_{\rm cl}^2$. Dilation gives the energy unit

$$\hbar^{4/3}g_B^{2/3}m_{\rm eff}^{-2/3}
 =\hbar^{4/3}c(g_{\rm cl}^2)^{1/3}L^{-2/3}
 =\frac{\hbar c}{L}x^{1/3}=E_3x^{-2/3}.$$

The **truncated** Gauss-invariant gap is therefore
$\Delta_{0,\rm inv}(L)=\delta_{\rm inv}^{(2)}E_3x^{-2/3}$, with
$\delta_{\rm inv}^{(2)}\ge\delta_1^{(2)}>0$ from the invariant-sector theorem.
The unrestricted scalar or matrix first gap cannot silently replace this
physical-sector coefficient. This cross-product proof is $SU(2)$; general
$SU(N)$ constant-mode conclusions need their corresponding matrix theorem.

Transport to a full physical finite-volume theory would give
$f(x)=\delta_{\rm inv}^{(2)}x^{-2/3}[1+o(1)]$ **if** the nonzero-mode coupling,
renormalization and sector/domain controls make the relative error vanish.
The earlier wording treated that error as already controlled merely by analogy
with Lüscher's four-dimensional small-volume method. It is not proved here.
The natural scaling parameter $x^{1/3}$ is dimensional bookkeeping, not a
remainder estimate. The [Feshbach argument](weak-coupling-feshbach-reduction.md)
states the distinct complement, Schur and effective-Hamiltonian obligations;
a finite-matrix gap alone does not satisfy them.

## The lattice route and its strong-coupling end

On the periodic square lattice with $N_s$ sites per side, use

$$H_{a,L}=\frac{\hbar c}{a}\left[
 \frac{g_{\rm lat}^2}{2}\sum_\ell(-\Delta_\ell)
 +\frac{2}{g_{\rm lat}^2}\sum_p
 (N-\operatorname{Re}\operatorname{tr}U_p)\right],
\qquad g_{\rm lat}^2=\lambda_3a.$$

Here $N$ is colour rank, $N_s=L/a$ is lattice size and $g_{\rm lat}$ is
dimensionless. The [finite-lattice theorem](mass-gap-obligations-lattice.md)
gives a unique physical ground state and
$\Delta_{a,L}=(\hbar c/a)\delta(g_{\rm lat};N_s,G)>0$.
The [strong-coupling theorem](strong-coupling-uniform-gap.md) with spatial
$\nu=2$, $\Lambda_0=\{0,1\}^2$, two links and one plaquette per site gives

$$\beta=\frac{8N}{g_{\rm lat}^4C_2}
 =\frac{16N^2}{g_{\rm lat}^4(N^2-1)},\qquad
 g_0^{(2)}(N)=\left[
 \frac{16N^2}{(N^2-1)\beta_*(2,\{0,1\}^2)}\right]^{1/4},$$

$$\Delta_{a,L}\ge\gamma_2\frac{g_{\rm lat}^2}{2}C_2\frac{\hbar c}{a},
\qquad g_{\rm lat}\ge g_0^{(2)}(N),$$

uniformly in $N_s$. The unspecified theorem constants $\beta_*,\gamma_2$
retain their source hypotheses; they are not numerical continuum estimates.

At fixed $\lambda_3,L$, taking $a\to0$ sends $g_{\rm lat}\to0$ with
$x=g_{\rm lat}^2N_s$ fixed and
$\Delta_{a,L}/E_3=\delta(g_{\rm lat};N_s,G)/g_{\rm lat}^2$.
A finite-volume continuum spectral theorem would need

$$\frac{\delta(g_{\rm lat};x/g_{\rm lat}^2,G)}{g_{\rm lat}^2}\longrightarrow f(x).$$

For the volume-first lattice route define
$\delta_\infty(g_{\rm lat})=\liminf_{N_s\to\infty}\delta(g_{\rm lat};N_s,G)$
and $c_3(g_{\rm lat})=\delta_\infty(g_{\rm lat})/g_{\rm lat}^2$.
At strong coupling $c_3\ge\gamma_2C_2/2$. A finite positive limit
$c_3\to C$ near zero, plus construction, matching of limit orders and surviving
physical spectral weight, is the continuum target. Positivity and a common
lower bound at **every** intermediate bare coupling form a sufficient optional
strengthening, not a necessary all-coupling theorem for the continuum problem.
The strong-coupling lower bound does not control the required weak-coupling end.

For compact $U(1)$ the all-coupling Villain gap can coexist with a massless
fixed-$\lambda_3$ continuum limit. The
[Villain proof](villain-monopole-refinement.md) retains normalized measure bounds,
its essential monopole suppression and the distinct massive Gaussian scaling
trajectory. The former Debye prefactor with dimensionless $\beta/a^3$ is not
a mass-squared formula in the present physical units and is withdrawn here.
These Euclidean source results are not automatically a theorem for the
Kogut--Susskind Hamiltonian just defined.

In four dimensions the usual scaling target instead has a transmutation
factor: up to its specified higher-order running factors,
$\delta_\infty(g)/g^2$ must vanish like
$g^{-2}e^{-1/(2b_0g^2)}$. This is the required trajectory shape if a physical
gap survives, not an estimate proved from the strong-coupling end. The
three-dimensional energy unit is simpler, but a nonzero spectral coefficient
is still an independent dynamical question.

## Construction boundary and consequence for STATE

Chandra--Chevyrev--Hairer--Shen construct a renormalized local evolution in
**auxiliary stochastic time**, with possible blow-up; the cited result supplies
neither global survival, an invariant measure nor OS reconstruction
([2024 introduction](https://arxiv.org/pdf/2201.03487), passage reading
recorded in [refinement](refinement-composition-and-limit.md)).
Karabali--Nair's $N/(2\pi)$ is a current-variable kinetic scale
([1996 equations (28)--(29)](https://arxiv.org/pdf/hep-th/9602155), passage),
not a proved full gap. The cited 2026 outline likewise leaves that proof open;
its source boundary is kept in the refinement treatment.

Conditional on the physical construction and limit, the question is whether
$f(x)$ has a positive finite limit. A lower bound $f(x)\ge f_->0$ for
$x\ge x_0$ would supply the positive side only after that construction; one
still needs finiteness and an appropriate spectral limit. The matrix proof,
conditional small-volume transport, strong lattice estimate and continuum
limit remain separate. This note stays distinct from the solved
low-dimensional models because it owns the explicit $\nu=2$ lattice thresholds,
normalization and unresolved field-theoretic limit, not another matrix-gap proof.
