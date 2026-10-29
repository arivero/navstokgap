# Rare gauge configurations and signed operator comparisons

**Maintained result.** Positive perturbations obey a min–max gap bound priced
by their ground-state expectation. A negative well admits a localized trial
state priced by its depth and the ground-state-weighted localization cost.
Small support probability alone supplies neither that cost nor a sign-sensitive
spectral bound. These exact statements do not close every Hamiltonian route.

The IMS identity below is exact. Its displayed lattice coefficient
$C_L=32\pi^2c_0^2/3$ is conditional on the stated link-response,
pointwise-field and neighbourhood/tail assumptions. The proposed local energy
excess and vacuum surface subtraction remain estimates to prove. An absolute
flow-kernel tail is not a Hamiltonian relative bound, and a continuum action
floor is not a normalized lattice probability theorem.

## Exact perturbation inequalities

**Proposition 1.** Suppose $H$ is semibounded with a normalized ground state $\Omega$, and its first two variational spectral levels define the gap. Assume the positive form perturbation is defined and $\langle\Omega,W\Omega\rangle<\infty$. If $W\ge0$ then
$\operatorname{gap}(H+W)\ge\operatorname{gap}(H)-\langle\Omega,W\Omega\rangle$.

*Proof.* $E_1(H+W)\ge E_1(H)$ by min-max, and
$E_0(H+W)\le\langle\Omega,(H+W)\Omega\rangle=E_0+\langle\Omega,W\Omega\rangle$.
$\square$

So a positive perturbation of size $D$ on a set of ground-state measure
$\varepsilon$ costs the gap at most $D\varepsilon$, and with
$\varepsilon=e^{-c\eta^2/g^2}$ and $D=O(\hbar c/a)$ that is negligible.

**Proposition 2.** A negative perturbation $-W$ with $W\ge D\,\mathbf 1_A$
on a set $A$ of ground-state measure $\varepsilon$ produces a state of
energy at most $E_0+L_A-D$, where $L_A=K\int|\nabla\chi_A|^2\Omega^2/\|\chi_A\Omega\|^2$
is the localization cost of a cutoff $\chi_A$ supported in $A$.

*Proof.* The trial state $\chi_A\Omega/\|\chi_A\Omega\|$ has energy
$E_0+L_A$ in $H$ by the exact identity
$\langle\chi\Omega,(H-E_0)\chi\Omega\rangle=K\int|\nabla\chi|^2\Omega^2$,
and $-W$ lowers it by at least $D$. $\square$

The probability of $A$ enters the normalized cost $L_A$ through the
weighted cutoff and its norm. A trial energy below $E_0$ when $D>L_A$
shows possible spectral reorganization; it does not by itself determine a
new excitation gap. Rare-set geometry and sign must accompany its measure.

## IMS identity and a conditional lattice coefficient

For $H=K(-\Delta)+V$ on a Riemannian manifold and smooth
$\chi_1^2+\chi_2^2=1$, the IMS formula (Cycon, Froese, Kirsch and
Simon, *Schrödinger Operators*, Springer 1987, Theorem 3.2; metadata
level) is the identity
$$H=\chi_1H\chi_1+\chi_2H\chi_2-K\big(|\nabla\chi_1|^2+|\nabla\chi_2|^2\big).$$
On $G^{\mathcal E}$ with $K=(\hbar c/a)(g^2/2)$ per link, take
$\chi_P=\cos\theta(f_B)$, $\chi_Q=\sin\theta(f_B)$ with $\theta$ rising
from $0$ to $\pi/2$ as the flowed block density
$f_B=\ell\int_B|B_t|^2d^3x$ rises from $\eta^2$ to $4\eta^2$, at
$\ell=2a$ and $\sqrt{8t}=\ell$. Then
$|\nabla\chi_P|^2+|\nabla\chi_Q|^2=\theta'(f_B)^2|\nabla f_B|^2$ with
$\theta'=\pi/(6\eta^2)$, and
$$\frac{\partial f_B}{\partial\theta_{\rm link}}=2\ell a\int_BB_t(x)\,K_t(x-y)\,d^3x\ \le\ 4c_0\,\frac{\eta a}{\ell},$$
under the additional assumed link-response and pointwise-field bounds that yield the displayed derivative estimate. They do not follow from the block $L^2$ constraint. A Gaussian kernel has tails, so restricting to the stated neighbourhood also requires a truncation/tail estimate.
Summing over the $3(2\ell/a)^3$ links of the smearing neighbourhood,
$|\nabla f_B|^2\le384c_0^2\eta^2\,\ell/a=768c_0^2\eta^2$ at $\ell=2a$, so
$$L_B\ \le\ \frac{\hbar c}{a}\frac{g^2}2\cdot\frac{\pi^2}{36\eta^4}\cdot768c_0^2\eta^2
=\frac{32\pi^2c_0^2}{3}\,\frac{\hbar c}{a}\,\frac{g^2}{\eta^2}.$$
Two remarks. The general-$\ell$ form carries a factor $\ell/a$, so
localizing at a scale far above the lattice is expensive and the
localization must be done one doubling at a time, in the variables of
the current scale. And $L_B$ is a multiplication operator supported on
the transition region of block $B$, whose ground-state measure requires a separate estimate: its coefficient is small against $\hbar c/a$ by $C_Lg^2/\eta^2$
if a separate normalized probability estimate is available. No such estimate is proved by this localization calculation.

## The local energy-excess target

For the large-field sector to contribute only harmlessly to $R$, the
step needs
$$\chi_Q(H-E_0)\chi_Q\ \ge\ c_1\,\frac{\hbar c}{a}\,\frac{\eta^2}{g^2}\,\chi_Q^2 ,$$
a *local energy excess*: configurations with a large flowed field in a
block have energy above the vacuum by the field's energy. This is an unproved operator target. The continuum Euclidean inequality in
[the lower-bound note](large-field-action-lower-bound.md). A proposed Hamiltonian comparison splits $H=H_N+H'$ with $N$ the neighbourhood of the
block and uses two facts: $V_N\ge(\hbar c/a)(2/g^2)c_1\eta^2$ on $Q$, under an additional lattice potential/flow comparison; and an upper bound on $E_0-E_0(H-V_N)$, the energy the
neighbourhood's magnetic terms add to the vacuum. The second is where the
loss occurs. The crude bound uses the ground state of $H-V_N$, which is
Haar-flat on the interior links and gives
$\langle V_N\rangle_{\rm Haar}=(\hbar c/a)(2N/g^2)|N|_p$, of the same
order $1/g^2$ as the excess and useless. The intended zero-point estimate has order $O(1)\cdot(\hbar c/a)|N|_p$, and the proposed trial state would extend the outside vacuum smoothly into $N$; the cut
then costs $O(\hbar c/a)$ per shared link, an amount
$$C_V\,\frac{\hbar c}{a}\,|\partial N|$$
that is subtracted *everywhere*, including on $P$. The proposed bound would have the schematic form
$$H-E_0\ \ge\ \Big[\frac{2c_1\eta^2}{g^2}-C_V|N|_p\Big]\frac{\hbar c}{a}\,\mathbf 1_Q
\ -\ C_V|\partial N|\,\frac{\hbar c}{a}\,\mathbf 1_P ,$$
and the second term is a negative perturbation of order $\hbar c/a$ on
the small-field region, whose effect requires an independent localization estimate; Proposition 2 alone does not classify the resulting gap. The window in which the first term is positive,
$$\eta\ \ge\ C_1g,\qquad C_1^2=\frac{C_V|N|_p}{2c_1}\ \simeq\ 160\ \text{for a }4a\text{ neighbourhood},$$
together with the small-angle requirement of the perturbative decimation
on $P$, $\eta/4\le C_2$, in this bookkeeping is nonempty only for $g\le4C_2/C_1$, that is
$1/g^2\gtrsim10^2$ with these crude constants. Even inside the window
the $P$-side loss remains.

## Consequence for STATE

A constructive polymer argument can use normalized measure estimates directly
under its own convergence hypotheses. A Hamiltonian lower-bound chain needs
operator comparisons with signs, domains and accumulated errors controlled.
Neither formalism has its missing estimates discharged by choosing it. The
surface loss above diagnoses the specified trial construction; it proves no
universal failure of Hamiltonian methods or success of a Euclidean continuum
gap construction. Keep the [flow locality](flow-jacobian-truncation-error.md),
[action/entropy](large-field-action-lower-bound.md) and
[ground-state transfer](ground-state-measure-transfer.md) hypotheses separate.
