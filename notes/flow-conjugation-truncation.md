# Gauge flow as a unitary change of variables: invariance and truncation

On a finite lattice, gauge gradient flow is a diffeomorphism of the
compact configuration space. Its unitary implementation preserves the
spectrum and the norm of every transformed multiplication operator.
Pointwise action reduction therefore does not reduce the corresponding
worst-case norm. A changed local decomposition or projection may still
change the bounds available to a proof, but it requires independent
control of the generated terms and of any truncation or relative error.
Neither unitary equivalence nor action decrease proves a mass gap.

## 1. Exact invariances

On $\mathcal M=G^{\mathcal E}$, the Wilson flow
$$\dot V_s(x,\mu)=-g^2\{\partial_{x,\mu}S_w(V_s)\}V_s(x,\mu),
\qquad V_0=U,$$
has a smooth all-time flow on the compact finite-dimensional manifold;
$\Phi_t^{-1}=\Phi_{-t}$. Lüscher, arXiv:1006.4518v3, (1.4) and the
following sentence (passage-level reading in the
[local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md)), supplies
the finite-lattice flow and action monotonicity. Let
$\rho_t=|\det D\Phi_t|$ relative to Haar measure and define
$$(W_t\psi)(U)=\rho_t(U)^{1/2}\psi(\Phi_t(U)).$$
Change of variables proves $W_t$ is unitary. Hence $W_tHW_t^*$ has
exactly the spectrum, multiplicities and gap of $H$. Also
$$W_tM_fW_t^*=M_{f\circ\Phi_t},\qquad
\|f\circ\Phi_t\|_\infty=\|f\|_\infty,$$
because $\Phi_t$ is onto. Thus any criterion using only the spectrum of
$H_0$ and the norm of $\phi$ is unchanged under *the same unitary
conjugation* of the pair. This does not show invariance under an unrelated
new splitting or under projection: flow can mix links and change the
supports and hypotheses of a local theorem.

For the Kogut--Susskind Hamiltonian
$$H=\frac{\hbar c}{a}\left[\frac{g^2}{2}K+\frac2{g^2}V\right],\quad
K=\sum_\ell(-\Delta_\ell),\quad
V=\sum_p(N-\operatorname{Re}\operatorname{tr}U_p),$$
flow gives $0\le V\circ\Phi_t\le V$ for $t\ge0$, while its supremum is
unchanged. It follows that
$\langle\psi,(V\circ\Phi_t)\psi\rangle\le\langle\psi,V\psi\rangle$
for a fixed state $\psi$; if both state and observable are transformed
consistently, their expectation is unchanged. In particular this is no
proof that the physical ground-state measure has uniform local
large-field tails. The corrected [Agmon analysis](agmon-ground-state-suppression.md)
controls integrated global excess only; the
[magnetic identities](magnetic-energy-identities.md) show that its simple
Gibbs-comparison repair does not supply the missing local estimate.

## 2. The kinetic term and the free example

The electric operator becomes a second-order operator whose coefficients
are determined by the pullback metric and the Jacobian. Flow mixes links:
the transformed operator is generally nonlocal. The scale $\sqrt{8t}$
is a smoothing radius, not a strict finite interaction range. Bounds on the flow Jacobian do not by themselves prove relative operator-error
bounds for a truncated Hamiltonian; the one-step distinction is explained below.

In a finite-volume regularized free abelian model in Coulomb gauge, a
nonzero mode obeys $A_k\mapsto e^{-tk^2}A_k$ and the Jacobian is a
constant. With a canonical momentum convention consistent with the
Hamiltonian, the transformed quadratic coefficients acquire reciprocal
factors $e^{-2tk^2}$ and $e^{+2tk^2}$, so their product and oscillator
frequency $\omega_k=c|k|$ are unchanged. This illustrates the exact
unitary result. Treating the ratio of those coefficients as a Yarotsky
smallness parameter is not justified: Fourier modes are not the local
site decomposition required by that theorem and a free mode's
coordinate and momentum are unbounded. The former assertion that an
arbitrary local criterion can always be improved without limit by
conjugation is withdrawn.

### One lattice step: coupling cancellation and local derivatives

For the stated Wilson normalization the $g^2$ in the flow equation
cancels the $1/g^2$ in the action. At fixed dimensionless time, the
finite-lattice vector field is therefore independent of $g$. Choosing
$\sqrt{8t}=2a$ gives $t/a^2=1/2$. The link-local vector field has bounded
derivatives at fixed compact group and bounded lattice incidence. More
explicitly, write its linearization in link coordinates as $\dot J=A(s)J$
with $A_{xy}=0$ beyond a fixed interaction distance and row sums bounded
by $B$, uniformly in the lattice size. Expanding the integral equation,
a matrix element at graph distance $d$ can receive a contribution only
after at least $d$ local factors, so
$$\|J_{xy}(t)\|\le\sum_{n\ge d}\frac{(B|t|)^n}{n!}.$$
Here time and $B$ are in lattice units, and any finite-range edge in
$A$ is one step of this graph. This elementary bound is uniform in
volume and coupling under the stated derivative and frame bounds; its
constants depend on the group and local geometry. It controls the first
flow derivative, not automatically the inverse derivative, Jacobian
potential, unbounded kinetic form or full Hamiltonian truncation. The
former claim $Ce^{-cK}$ for the relative operator error and the assertion
that $K=3$ suffices are withdrawn: no constants or relative-form proof
were provided. Compactness also does not itself prove normalized
large-field rarity or multiscale stability.

## 3. What an RG step must add

Suppose a scale change constructs effective operators $H^{(n)}$ at
$\ell_n=2^na$, with a specified low-energy subspace, generated
interactions and a spectral comparison. Relative Schur bounds can
ignore a common scalar shift but must control the state-dependent
remainder and the complementary energy denominator; see
[the Feshbach reduction](weak-coupling-feshbach-reduction.md), including its ultraviolet correction. A candidate
truncation must be compared with the exact transformed operator in a
suitable domain and relative-form norm, with constants uniform in volume
and with enough control across the cutoff trajectory. One-loop running
can estimate how many doublings might be needed, but it is not a proof
of the effective action or its arrival in a gapped region.

A state-relative bound, for example
$$\langle\psi,\phi\psi\rangle\le\epsilon\langle\psi,(H-E_0)\psi\rangle
 +\eta\|\psi\|^2$$
on a specified low-energy domain, could exploit more information than a
supremum norm. Such a bound, the relevant probability estimates, and
stability after projection are independent obligations. The
[blocking analysis](blocking-criterion-monotone.md) gives conditional
surface-to-gap comparisons; it does not prove that projection blocking
is always worse at every coupling.

## 4. Consequence for STATE

Exact flow preserves spectra and transformed norms. The free cancellation
and the failure of the global Agmon bound to yield a local state estimate
make the missing ingredients explicit: controlled generated interactions,
relative errors and physical spectral transfer. No general no-go theorem
for all norm-based methods, all reblockings or all constructive routes is
claimed.
