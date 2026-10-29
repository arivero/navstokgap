# Ising relaxation, local parent Hamiltonians and clock normalization

The periodic zero-field Ising heat-bath chain has the exact full relaxation
gap $a[1-\tanh(2b)]$ for every $N\ge3$, at per-site refresh rate $a>0$ and
finite ferromagnetic coupling $b\ge0$. Its square-root Gibbs transform is
an explicit positive three-site local Hermitian operator with that gap.
Multiplication by a supplied action $K>0$ gives an energy gap $K$ times
the rate. The invariant law fixes neither clock nor action normalization.
A volume-uniform relaxation gap also coexists with a growing global mixing
time. These are three different statements.

The exact Ising gap and detailed-balance parent construction are established
results. The proof below is self-contained, with C124/C126 source matches in
[B68](../references/batches/B68.md), [B71](../references/batches/B71.md) and
[B73](../references/batches/B73.md). Historical model/coordinator checks are
internal; no novelty is claimed.

## Gibbs law, refresh convention and the full generator

On $\Omega_N=\{-1,1\}^N$ with cyclic indices, $N\ge3$, put

$$\pi_{N,b}(\sigma)=Z^{-1}\exp\left(b\sum_i\sigma_i\sigma_{i+1}\right),
\qquad b=\beta J,\quad\theta=\tanh(2b).$$

$J$ has energy units, $\beta$ inverse energy and $b$ is dimensionless.
Independent rate-$a$ site clocks refresh from the conditional Gibbs law:

$$p_i(\sigma)=\frac12+\frac\theta4(\sigma_{i-1}+\sigma_{i+1}),\qquad
Q_N=a\sum_i(E_i-I).$$

A refresh may leave the spin unchanged. The actual flip rate is
$a[1-\theta\sigma_i(\sigma_{i-1}+\sigma_{i+1})/2]/2$.
Conditional expectations $E_i$ are orthogonal projections in $L^2(\pi)$,
so $Q_N$ is self-adjoint. Finite $b$ makes every flip probability positive
and the chain irreducible. The domain is the entire finite function space;
its centered-space gap has inverse-time units in the specified sampling clock.

A calibrated velocity $v_i=u\sigma_i$, $u>0$, is centered and has variance
$u^2$. The full vector identifies the configuration, but its linear span
does not cover every centered function; the following proof controls all modes.

## Exact all-mode gap

Couple two chains with the same clocks and refresh uniforms. With disagreement
indicators $D_i$ and Hamming distance $D=\sum_iD_i$, the refresh mismatch
probability is bounded by $\theta(D_{i-1}+D_{i+1})/2$. Hence

$$\mathcal L D\le-aD+\frac{a\theta}2\sum_i(D_{i-1}+D_{i+1})
 =-a(1-\theta)D.$$

Finite-state evolution and Gronwall give
$\mathbb ED_t\le e^{-rt}D_0$, $r=a(1-\theta)$. Therefore every function's
Hamming Lipschitz seminorm obeys
$\operatorname{Lip}(P_tf)\le e^{-rt}\operatorname{Lip}(f)$.
A nonconstant real eigenfunction with $-Q_Nf=\lambda f$ has positive finite
seminorm, so cancellation gives $e^{-\lambda t}\le e^{-rt}$ and
$\lambda\ge r$. Reversibility supplies a real eigenbasis; the estimate
covers every centered eigenmode without a size prefactor.

For $M=\sum_i\sigma_i$,

$$Q_N\sigma_i=-a\sigma_i+\frac{a\theta}2(\sigma_{i-1}+\sigma_{i+1}),
\qquad Q_NM=-a(1-\theta)M.$$

$M$ is centered and nonzero because every configuration has positive weight.
This matching eigenfunction proves

$$\boxed{\operatorname{gap}(-Q_N)=a[1-\tanh(2b)].}$$

For bounded mean velocity $V=uM/N$,
$\chi(V)=\operatorname{Var}_\pi(V)/\operatorname{gap}(-Q_N)$.
Its variance is positive at every finite $N$ without a claimed uniform lower
bound; $\chi(V)/\operatorname{Var}(V)$ detects the slow-mode time.
The action-valued response $2m\chi(V)$ additionally supplies a mass and
velocity calibration, as in [susceptibility](susceptibility-gap.md).

## The square-root Gibbs parent and its local terms

Let $D=\operatorname{diag}\pi$ and
$U:L^2(\pi)\to(\mathbb C^2)^{\otimes N}$,
$(Uf)_\sigma=\sqrt{\pi(\sigma)}f(\sigma)$. This is unitary between the
weighted and counting inner products. Define

$$A_N=-UQ_NU^{-1}=-D^{1/2}Q_ND^{-1/2}.$$

Detailed balance gives Hermiticity, and the exact Dirichlet form is

$$\langle\psi,A_N\psi\rangle=\frac12\sum_{\sigma,\eta}
 \pi(\sigma)Q_{\sigma\eta}
 \left|\frac{\psi_\eta}{\sqrt{\pi(\eta)}}-
 \frac{\psi_\sigma}{\sqrt{\pi(\sigma)}}\right|^2\ge0.$$

Irreducibility makes the kernel one-dimensional, spanned by

$$|\Omega\rangle=Z^{-1/2}\sum_\sigma
 e^{(b/2)\sum_i\sigma_i\sigma_{i+1}}|\sigma\rangle.$$

Let $Z_i$ be the diagonal spin and $X_i$ its flip. Put
$s_0=\operatorname{sech}(2b)$ and $c_\pm=(s_0\pm1)/2$. Then

$$A_N=\sum_i h_i,\qquad
h_i=\frac a2\left[I-\frac\theta2Z_i(Z_{i-1}+Z_{i+1})
 -(c_+I+c_-Z_{i-1}Z_{i+1})X_i\right].$$

For fixed neighbour sum $S=0,\pm2$, the transformed off-diagonal flip
entry is $-\sqrt{r_i(\sigma)r_i(\sigma^i)}=-a/[2\cosh(bS)]$;
its diagonal is unchanged. The coefficient is exactly
$c_++c_-\sigma_{i-1}\sigma_{i+1}$, proving the formula. The neighbours
are distinct for $N=3$ as required. Alternatively
$h_i=a(I-UE_iU^{-1})$, so $h_i\ge0$, $h_i^2=ah_i$,
$\|h_i\|=a$ and $h_i|\Omega\rangle=0$. Thus the parent is
frustration-free and three-site local; overlapping terms need not commute.
For fixed neighbours the local null vector is proportional to
$(e^{bS/2},e^{-bS/2})$. At $b=0$, $h_i=a(I-X_i)/2$ and the ground
state is the product of plus-$X$ vectors.

Unitary equivalence gives the exact gap of $A_N$, with nonzero eigenvector
$UM$. A supplied action $K>0$ defines $H_N=KA_N$, energy gap

$$\Delta_N=Ka[1-\tanh(2b)],\qquad
 e^{-tH_N/K}=Ue^{tQ_N}U^{-1}.$$

This is an imaginary-time identity in the chosen clock. The mathematical
unitary $e^{-itH_N/K}$ supplies a different real-time law, not the original
stochastic transition law. Neither the square-root amplitudes' physical
state interpretation nor a physical measurement rule follows from the
weighted-space coordinate change. The classical Ising energy
$-J\sum\sigma_i\sigma_{i+1}$ is also a different operator from this parent.

## Volume, coupling, global mixing and physical limits

Uniform bounds $K_N\ge K_0>0$, $a_N\ge a_0>0$ and $b_N\le B<\infty$
give $\Delta_N\ge K_0a_0[1-\tanh(2B)]$ for the finite-volume sequence.
Finite range alone is insufficient. At $b_N=(\log N)/4$ and fixed $a$,
the relaxation gap is $2a/(N+1)$. A fixed total refresh budget replaces
$Q_N$ by $Q_N/N$ and gives $a[1-\tanh(2b)]/N$ even at fixed coupling.
Vanishing $K_N$ separately closes the energy gap. These are different
parameter limits, not a fixed-coupling thermodynamic failure.

At fixed finite $a,b$ and fixed global total-variation tolerance,
Lubetzky–Sly's Corollary 3 gives

$$t_{\rm mix}^{(N)}(\epsilon)\sim\frac{\log N}{2a[1-\tanh(2b)]}.$$

The exact gap match (preprint p. 4) and mixing-time statement were read in
[B73](../references/batches/B73.md), using
[the primary preprint](https://arxiv.org/pdf/0909.4320v1) with the rate-$a$
conversion stated here. A uniform slow-mode rate can coexist with logarithmic
global equilibration time. Neither constructs an infinite-volume Hilbert
representation or a continuum quantum field.

The ground vector and locality survive $Q\mapsto\lambda Q$ while every
rate and parent gap scales by $\lambda$. Independently changing $K$ changes
energy normalization. Thus equilibrium weights, a physical time law and a
positive universal action unit remain separate inputs. The
[finite-depth cluster Hamiltonian](finite-depth-spin-gap.md) is a distinct
unitary-conjugation construction, not a second derivation of this stochastic
parent. The [field comparison](comparison-and-bridges.md) states the further
physical-operator and continuum obligations.

## Consequence for STATE

The interacting benchmark supplies an exact all-mode finite-volume gap and
an explicit local parent with known clock dependence. Its source evidence and
full proofs are maintained together. No further Ising spectrum is required to
understand the unresolved identification of a sampling generator, physical
Hamiltonian, time unit and physical $\hbar$.
