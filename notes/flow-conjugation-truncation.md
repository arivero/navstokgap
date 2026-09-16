# Conjugation by the flow preserves the spectrum, so the renormalization step is a truncation

The gradient flow is a diffeomorphism of the compact configuration space
$G^{\mathcal E}$, so it is implemented by a unitary on
$L^2(G^{\mathcal E})$ and conjugation by it leaves every eigenvalue of the
Kogut--Susskind Hamiltonian unchanged. Under that conjugation the
magnetic term becomes the flowed action, which the flow decreases
monotonically, and the electric term becomes the Laplace--Beltrami
operator of the pulled-back metric together with a Jacobian potential.
In the free case the two effects cancel exactly: the magnetic
coefficient of the mode $k$ is multiplied by $e^{-2tk^2}$ and the
electric one by $e^{+2tk^2}$, leaving the frequencies $\omega_k=ck$
untouched. Reading the conjugated Hamiltonian as "classical part plus
perturbation" and applying the strong-coupling criterion of
[the T2 note](strong-coupling-uniform-gap.md) would give
$$\beta\ \longmapsto\ \beta\,e^{-4tk^2},$$
an arbitrarily large improvement of a criterion whose conclusion, the
gap, cannot have changed. The resolution names the content of a
renormalization step: **the criterion presupposes a local decomposition,
the conjugated electric term is nonlocal with range $\sqrt{8t}$, and any
gain is charged entirely to truncating that nonlocality**. A change of
variables moves the difficulty and never removes it; the truncation error
is the difficulty. This closes the last of the three ways of avoiding the
constructive step that this programme has tried, and it states in one
line what such a step must control. Constants explicit; nothing
promoted.

## 1. The flow is a unitary change of variables

On a finite lattice the Wilson flow
$$\dot V_s(x,\mu)=-g^2\big\{\partial_{x,\mu}S_w(V_s)\big\}V_s(x,\mu),
\qquad V_0=U,$$
has a unique smooth solution for all $s\in\mathbb R$ (Lüscher,
arXiv:1006.4518v3, equation (1.4) and the sentence following it; passage
level via the [local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md)),
so $\Phi_t:U\mapsto V_t$ is a diffeomorphism of the compact manifold
$\mathcal M=G^{\mathcal E}$ with smooth inverse $\Phi_{-t}$.

**Proposition 1.** Let $\rho_t=\big|\!\det D\Phi_t\big|$ be the Jacobian of
$\Phi_t$ with respect to the Haar measure $\mu$. Then
$$(W_t\psi)(U)=\rho_t(U)^{1/2}\,\psi\big(\Phi_t(U)\big)$$
is unitary on $L^2(\mathcal M,\mu)$, and for any self-adjoint $H$ the
operator $W_tHW_t^*$ has the same spectrum, multiplicities and gap.

*Proof.* Change of variables: for $\psi,\varphi\in L^2$,
$\int\overline{(W_t\psi)}(W_t\varphi)\,d\mu=\int\rho_t\,\overline{\psi(\Phi_t U)}\varphi(\Phi_tU)\,d\mu(U)
=\int\overline\psi\varphi\,d\mu$ since $\rho_t\,d\mu=\Phi_t^*d\mu$.
Surjectivity follows from $W_t^{-1}=W_{-t}$ up to the Jacobian cocycle.
Unitary conjugation preserves the spectrum. $\square$

## 2. The conjugated Hamiltonian

Write $H=\frac{\hbar cg^2}{2a}K+\frac{2\hbar c}{ag^2}V$ with
$K=\sum_\ell(-\Delta_\ell)$ and $V(U)=\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)$.

**Magnetic term.** For a multiplication operator,
$W_tM_VW_t^*=M_{V\circ\Phi_t}$, computed directly from the definition:
the two Jacobian factors cancel. So the magnetic potential becomes the
**flowed action**, and $S_w(V_t)$ is a monotonically decreasing function
of $t$ (Lüscher, immediately after (1.4)), whence
$$0\ \le\ V\circ\Phi_t\ \le\ V .$$

**Electric term.** $K$ is the Laplace--Beltrami operator of the product
bi-invariant metric on $\mathcal M$. Conjugation by $W_t$ gives the
Laplace--Beltrami operator of the pulled-back metric
$\Phi_t^*\,\mathrm g$, together with a first-order term and a potential
built from $\rho_t$ and its derivatives:
$$W_tKW_t^*=-\Delta_{\Phi_t^*\mathrm g}+Q_t,\qquad
Q_t=\rho_t^{1/2}\big(\Delta_{\Phi_t^*\mathrm g}\,\rho_t^{-1/2}\big),$$
the standard ground-state transform. The pulled-back metric is no longer
a product over links: $D\Phi_t$ mixes links within the flow radius
$\sqrt{8t}$, so the conjugated kinetic operator has **range
$\sqrt{8t}$**.

## 3. The free case: exact cancellation

For the abelian theory in Coulomb gauge the flow is the heat equation
(as in [the free-field note](flowed-bound-free-field.md) §2), so
$\Phi_t$ is the linear map $A\mapsto e^{t\Delta}A$, its Jacobian is a
constant, and $W_t$ is the induced unitary with no potential term. The
conjugated Hamiltonian is, mode by mode,
$$W_tHW_t^*=\int\!\frac{d^3k}{(2\pi)^3}\Big[\frac{g^2c}{2\hbar}\,e^{+2tk^2}\big|\hat\Pi(k)\big|^2
+\frac{\hbar c}{2g^2}\,k^2e^{-2tk^2}\big|\hat A(k)\big|^2\Big],$$
since the conjugate momentum transforms by the inverse transpose of the
map on the fields. Each mode is an oscillator of frequency
$$\omega_k=\sqrt{\big(c\,e^{+2tk^2}\big)\big(c\,k^2e^{-2tk^2}\big)}=ck,$$
independent of $t$, as Proposition 1 requires. The flow makes the
potential smaller and the kinetic term correspondingly stiffer, and the
product is invariant.

## 4. What this does to a locality-based criterion

The criterion of [the T2 note](strong-coupling-uniform-gap.md) compares
the norm of the perturbation with the local gap of the classical part:
$\beta=\|\phi\|/(\text{local gap})$. Applied to the conjugated
Hamiltonian, mode by mode in the free case, the magnetic norm carries
$e^{-2tk^2}$ and the local gap of the kinetic term carries $e^{+2tk^2}$,
so
$$\beta\ \longmapsto\ \beta\,e^{-4tk^2},$$
which can be made as small as desired by taking $t$ large. On a lattice
the modes run to $k\sim\pi/a$, so at flow time $t=(Ma)^2$ the improvement
factor reaches $e^{-4\pi^2M^2}$. Since the spectrum is unchanged, no
statement about the gap can follow from this improvement.

**Where the criterion loses its validity.** Yarotsky's hypotheses require
the classical part to be a sum of single-site terms and the perturbation
to have finite range. After conjugation, the kinetic operator has range
$\sqrt{8t}$ and the decomposition into single-link terms is gone. The
apparent gain is therefore the price of dropping a hypothesis, and a
criterion that keeps the hypothesis must first **truncate** the
conjugated kinetic operator back to finite range. Truncation changes the
operator, and the resulting gap bound applies to the truncated
Hamiltonian; its relation to the original is exactly the truncation
error.

**Corollary 2.** Any gap criterion formulated through a local
decomposition into classical part and small perturbation fails to be
invariant under unitary changes of variables, and can be improved
without limit by conjugation. Consequently the improvement obtained in a
renormalization step is charged in full to the truncation that restores
locality, and no change of variables by itself improves a spectral
bound.

## 5. The three closed routes

This completes a set. Of the ways to reach $m>0$ while avoiding the
constructive step, the notes have now closed:

| route | why it closes | note |
| --- | --- | --- |
| expansion around the free theory | the bound reaches $m$ only at the confinement scale, where the coefficient is nonperturbative | [free field](flowed-bound-free-field.md) §7 |
| real-space blocking by projection | boundary grows like $M^2$, block gap does not grow; criterion worsens by $3M^2/8$ | [blocking criterion](blocking-criterion-monotone.md) |
| change of variables by the flow | spectrum is invariant, so the gain is the truncation error | this note |
| upper bounds of any kind | finite negative moments are compatible with $m=0$ | [moment hierarchy](moment-hierarchy-upper-bounds.md) §5 |

Each was closed by a computation with explicit constants rather than by
an appeal to difficulty, and together they say the same thing: the only
place a proof of $m>0$ can come from is a controlled truncation, applied
a finite number of times, with the error at each step small compared with
the gap at that scale.

## 6. What a truncation must satisfy

The requirement can now be stated with the constants of this programme.
Let $H^{(n)}$ be the theory at scale $\ell_n=2^n a$, with gap
$\Delta_n\ge\kappa\,\hbar c\,g_n^2/\ell_n$ in the regime where the
criterion applies, and let $T_n$ be the truncation to range $\ell_n$
following the conjugation. A proof needs
$$\big\|H^{(n)}-T_nW_{t_n}H^{(n)}W_{t_n}^*T_n^*\big\|_{\rm relative}\ \ll\ \Delta_n
\qquad\text{for each of the }n\simeq\frac{1}{2b_0\log2}\Big(\frac1{g_{\rm UV}^2}-\frac1{g_{\rm thr}^2}\Big)$$
steps, with the norm taken in the relative sense of
[the Schur note](schur-error-ultraviolet.md) Lemma 1$'$, so that constant
shifts are free. The flow radius $\sqrt{8t_n}$ must be of order $\ell_n$
for the conjugation to reduce the action at the right scale, and the
truncation error is governed by the decay of the flow Jacobian
$D\Phi_{t_n}$ beyond that radius, which for the free case is Gaussian in
$|x|/\sqrt{8t_n}$ and in the interacting case is the object the
construction must bound.

## 7. Consequence for STATE

The three ways of avoiding the constructive step are closed, and the step
itself is stated in the form the constants of this programme give it: a
conjugation by the flow at radius $\ell_n$ followed by a truncation whose
relative error must stay below the gap at that scale, iterated a finite
number of times. The next tractable item is the decay of the flow
Jacobian $D\Phi_t$ on the lattice, which controls the truncation error
and which the free case fixes exactly; that is a bounded question about
the flow equation and is the natural next note.
