# G04 / B71 written proof and source review

C126 is accepted for the stated finite periodic Ising heat-bath model.
The transform gives a positive three-site-local frustration-free operator with
ground state `sqrt(pi)` and exact inverse-time gap
`a[1-tanh(2b)]`. Multiplying by a supplied action constant converts the spectrum
to energy units but does not derive physical dynamics or that constant. The
source audit supports this as a standard stochastic-parent construction; it
does not support an independent physical-Hamiltonian claim.

## Manual algebra audit

Let `D=diag(pi)` and let `Q` act on functions by rows. The map
`(Uf)_sigma=sqrt(pi_sigma) f_sigma` is unitary from `L^2(pi)` to counting
space, so

```
A=-U Q U^(-1)=-D^(1/2) Q D^(-1/2).
```

Detailed balance gives
`sqrt(pi_sigma/pi_eta) Q_(sigma,eta)
 =sqrt(pi_eta/pi_sigma) Q_(eta,sigma)`, hence `A` is real symmetric. Pulling
back the Dirichlet form gives the displayed nonnegative quadratic form in the
draft. Irreducibility at finite `b` leaves only constants in `ker(-Q)`, so
`ker A` is one-dimensional and spanned by `sqrt(pi)`.

For a flip at site `i`, write
`S=sigma_(i-1)+sigma_(i+1)` and
`theta=tanh(2b)`. The row-generator flip rate is

```
r_i(sigma)=(a/2)[1-sigma_i tanh(bS)].
```

Detailed balance makes the transformed off-diagonal entry

```
-sqrt(r_i(sigma) r_i(sigma^i))=-a/[2 cosh(bS)].
```

If the neighbours agree, their product is `+1`, `S=+/-2`, and the coefficient
of `X_i` is `sech(2b)`. If they disagree, their product is `-1`, `S=0`, and the
coefficient is `1`. Thus with `s=sech(2b)`,
`c_+=(1+s)/2` and `c_-=(s-1)/2`, the draft's
`c_+ + c_- Z_(i-1)Z_(i+1)` is correct. The diagonal coefficient is the
unchanged escape rate and equals the displayed
`(a/2)[I-(theta/2)Z_i(Z_(i-1)+Z_(i+1))]`.

The alternative identity
`h_i=a(I-U E_i U^(-1))` verifies positivity without relying on the Pauli
expansion: conditional expectation `E_i` is an orthogonal projection in
`L^2(pi)`, so `h_i>=0`, `h_i^2=a h_i`, `||h_i||=a`, and
`h_i |Omega> = 0`.
The explicit coefficients show that the conjugated term depends only on
`i-1,i,i+1`; the global diagonal transform introduces no longer-range support.
For `N=3` those neighbours are distinct, although each three-site support is
the full ring. Overlapping terms need not commute.

Unitary equivalence preserves the entire spectrum. C124's written proof gives
the exact gap and its magnetization eigenfunction, so C126 correctly obtains
`gap(A)=a[1-tanh(2b)]` with eigenvector `UM`. No source theorem is imported for
this exact specialization. At `b=0`, the formula reduces to
`h_i=a(I-X_i)/2`, which checks the signs and normalization manually.

For an action-valued constant `K_action`, `H=K_action A` has energy gap
`K_action a[1-tanh(2b)]`, and
`exp(-tH/K_action)=U exp(tQ) U^(-1)`. The corresponding real-time unitary
`exp(-itH/K_action)` is a newly specified quantum evolution, not the original
Markov transition law. Rescaling `Q` leaves `pi` fixed and rescales the gap;
rescaling `K_action` changes the energy normalization independently; in
`exp(-itH/K_action)` the same factor cancels, so this alone does not change
the constructed time evolution.
The draft's physical-dependency conclusion follows.

## Source match and limits

Henley PDF p. 7, Eq. (3.7), supplies the detailed-balance symmetrization for
unequal weights and states locality inheritance for a local classical energy.
Castelnovo et al. PDF pp. 8--10 and 12--15, Eqs. (8)--(15) and (19)--(28),
supply positive local blocks, the square-root Boltzmann zero mode, equality of
relaxation and excitation spectra, and the freedom of move-rate coefficients,
including a Glauber choice. Their probability-column convention is the
transpose of C126's function-row convention. The apparent inverse ordering of
the diagonal factors is therefore consistent.

The source symbol `K=beta J` is dimensionless and is not C126's action-valued
`K`. The audit found no source that derives a physical clock or action scale
from the stationary Gibbs law. It also found no exact printed match for the
three-site Ising heat-bath Pauli formula within the bounded search. That
formula remains a reviewed project derivation. No novelty inference follows
from the absence of a match in three queries.

Proof status proposed to coordinator: **written proof reviewed**. Literature
status proposed: **general stochastic-parent mapping established; exact C126
Ising specialization derived under bounded coverage; no novelty claim**. No
numerical or symbolic verification scripts were created or run.

## Coordinator acceptance

The coordinator independently checked the weighted-space unitary, Dirichlet
form, local two-sign blocks, projection identity, N=3 indexing and zero-coupling
normalization. C124 supplies the full-spectrum bound; locality alone is not
used to infer it. Source page indices were corrected to one-based anchors,
and the key transform, ground-state, spectral and rate-choice equations were
visually verified as recorded in the companion. C126 is accepted as a written
derived specialization of the established mapping, with no novelty claim.
Physical dynamics, action selection and further limits remain open premises.
