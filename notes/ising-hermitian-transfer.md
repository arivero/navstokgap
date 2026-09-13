# The Ising gap gives a conditional local parent Hamiltonian

The square-root Gibbs transform of C124 is a positive, three-site local,
frustration-free Hermitian operator with unique ground state
$\sqrt{\pi_{N,b}}$ and exact gap $a[1-\tanh(2b)]$. Multiplication by a supplied
action constant gives an energy-unit Hamiltonian. This construction preserves
the chosen stochastic clock and does not select physical dynamics or action
units. It resolves G04's finite-volume transfer decision.

## 1. Object, domain and transform

Use [C124's model](interacting-ising-gap.md): $N\ge3$ periodic spins,
$0\le b<\infty$, per-site refresh rate $a>0$ and stationary law
$\pi(\sigma)=Z^{-1}\exp(b\sum_i\sigma_i\sigma_{i+1})$.
The generator $Q=a\sum_i(E_i-I)$ acts on functions in complex $L^2(\pi)$;
$E_i$ is conditional expectation over spin $i$. Its time parameter is the
auxiliary sampling clock and $a$ has inverse-time units.

Let $D=\operatorname{diag}\pi$ and
$U:L^2(\pi)\to\mathcal H_N=(\mathbb C^2)^{\otimes N}$ be
$(Uf)_\sigma=\sqrt{\pi(\sigma)}f(\sigma)$. The codomain has the standard
counting inner product; $U$ is unitary between these two inner-product spaces.
All operators below have the entire finite-dimensional space as domain. Set

$$
A_N=-UQU^{-1}=-D^{1/2}QD^{-1/2}.
$$

Detailed balance makes this matrix Hermitian. Its quadratic form is

$$
\langle\psi,A_N\psi\rangle
=\frac12\sum_{\sigma,\eta}\pi(\sigma)Q_{\sigma\eta}
\left|\frac{\psi_\eta}{\sqrt{\pi(\eta)}}-
      \frac{\psi_\sigma}{\sqrt{\pi(\sigma)}}\right|^2\ge0,
$$

where diagonal terms vanish. Irreducibility implies a one-dimensional kernel,
spanned by the normalized vector

$$
|\Omega\rangle=Z^{-1/2}\sum_\sigma
 e^{(b/2)\sum_i\sigma_i\sigma_{i+1}}|\sigma\rangle.
$$

Its squared basis amplitudes reproduce the Gibbs probabilities. Regarding
those amplitudes and other vectors as physical quantum states requires a
state/measurement interpretation in addition to this Hilbert-space map.

## 2. Explicit local terms and their positivity

Write $Z_i|\sigma\rangle=\sigma_i|\sigma\rangle$ and let $X_i$ flip spin $i$.
Put $\theta=\tanh(2b)$, $s=\operatorname{sech}(2b)$,
$c_+=(1+s)/2$, $c_-=(s-1)/2$. Then

$$
A_N=\sum_i h_i,\qquad
h_i=\frac a2\left[I-\frac\theta2Z_i(Z_{i-1}+Z_{i+1})
 -(c_+I+c_-Z_{i-1}Z_{i+1})X_i\right].
$$

**Derivation.** For fixed neighbours with sum $S=\sigma_{i-1}+\sigma_{i+1}$,
the original flip rate is $r_i(\sigma)=a[1-\sigma_i\tanh(bS)]/2$.
Detailed balance gives transformed off-diagonal entry
$-\sqrt{r_i(\sigma)r_i(\sigma^i)}=-a/[2\cosh(bS)]$.
The diagonal entry is unchanged. Since $S=0,\pm2$, the off-diagonal
coefficient equals $c_++c_-\sigma_{i-1}\sigma_{i+1}$, giving the formula.
The two neighbours are distinct even for $N=3$; all indices are cyclic.

Alternatively $h_i=a(I-UE_iU^{-1})$. Each $E_i$ is an orthogonal projection,
so $h_i\ge0$, $h_i^2=ah_i$ and $h_i|\Omega\rangle=0$. Thus the sum is
frustration-free, although its overlapping terms need not commute. Each term
has norm $a$ and support in the three sites $i-1,i,i+1$; the global density
transform has not introduced interactions of growing range. For a fixed
neighbour block the local ground vector has components proportional to
$e^{bS/2},e^{-bS/2}$, which also checks the square-root and sign conventions.
At $b=0$, $h_i=a(I-X_i)/2$ and the ground state is the product of plus-$X$
vectors. These statements are direct finite-dimensional derivations.

## 3. Exact gap, normalization and limits (C126)

Unitary equivalence and C124 give

$$
\operatorname{gap}(A_N)=a[1-\tanh(2b)].
$$

The corresponding nonzero eigenvector is $U M$ with
$M(\sigma)=\sum_i\sigma_i$, orthogonal to $|\Omega\rangle$ by spin-flip
symmetry. This is an all-mode spectral statement, inherited from C124 rather
than inferred from locality or the ground state alone.

For a supplied constant $K>0$ with action units, define $H_N=K A_N$.
Its ground energy is zero and its excitation gap in energy units is

$$
\Delta_N=Ka[1-\tanh(2b)].
$$

For $K_N\ge K_0>0$, $a_N\ge a_0>0$, $0\le b_N\le B<\infty$,
$\Delta_N\ge K_0a_0[1-\tanh(2B)]$ uniformly in $N$. These are bounds on a
sequence of finite-volume Hamiltonians. They do not construct an infinite-volume
Hilbert representation or establish a continuum gap. Fixed total refresh rate
replaces $a$ by $a/N$ and closes the gap. Growing $b_N$ or vanishing $K_N$
can close it as well when the other parameters stay fixed.

## 4. Which physical premise has been supplied?

The exact semigroup identity is

$$
 e^{-tH_N/K}=Ue^{tQ}U^{-1}.
$$

It identifies the transformed sampling semigroup with imaginary-time evolution
of the constructed operator, in the same time units. Defining the unitary
$e^{-itH_N/K}$ is mathematically possible but is an additional choice of
real-time evolution; it is not the original stochastic transition law.

| Input | Use | What remains to identify physically |
| --- | --- | --- |
| Positive Gibbs law and detailed balance | Unitary weighted-space transform and Hermiticity | Physical state and observable interpretation |
| Single-site heat-bath generator | Three-site terms and exact inherited gap | Why this generator governs physical imaginary time |
| Per-site rate $a$ | Overall spectral rate scale | Conversion from sampling time to physical time |
| Supplied action constant $K$ | Converts inverse time to energy and sets phase units | Positive universal action normalization |
| Uniform $K,a,b$ bounds | Finite-volume energy-gap lower bound | Their physical origin and any further limit construction |

The classical energy function $-J\sum_i\sigma_i\sigma_{i+1}$ used to prepare
$\pi$ is not the constructed $H_N$: the latter has off-diagonal spin flips
and coefficients depending on $b=\beta J$ and $Ka$. Knowledge of $J$ and
$\beta$ fixes neither the refresh clock nor a universal action constant.
For the same $\pi$, replacing $Q$ by $\lambda Q$, $\lambda>0$, preserves
the ground state and locality while multiplying every excitation gap by
$\lambda$. Holding $Q$ fixed and varying $K$ independently gives the other
normalization freedom. Thus the map yields a conditional stochastic-parent
Hamiltonian; an independent physical identification is still a premise.

## 5. Evidence and strategic consequence

Written proof and literature status are recorded separately in the ledger.
The [B71 audit](../references/batches/B71.md) matches the established
detailed-balance parent mapping in Henley and Castelnovo et al.; the explicit
Ising term is a derived specialization. The [written review](../reviews/ising-hermitian-B71.md)
checks its coefficients and inherited gap. No novelty is asserted.

G04 stops at the explicit finite-volume operator. Additional Ising spectra
would not select its clock or action scale. A further operator task requires
an independently specified physical dynamics whose imaginary-time generator
can be compared with this one. The quantum track's reversible-descent premise is selected next: test whether
a specified interacting mechanical orientation flow closes on C125's moment
coordinates. [STATE](../research/STATE.md) owns that bounded decision.
