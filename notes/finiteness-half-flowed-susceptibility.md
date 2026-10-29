# The finiteness half of the mass gap is the nonvanishing of one smeared susceptibility

The requirement $m<\infty$ of the Jaffe--Witten statement reduces to an
exact inequality between two ground-state quantities. For any
gauge-invariant local scalar $\varphi$ built from the spatially smeared
field, with $\langle\varphi\rangle=0$,
$$m\ \le\ \frac{g^2\hbar c}{2}\;\frac{\big\langle\,|D_\varphi|^2\,\big\rangle_0}{\chi_\varphi},
\qquad
D_\varphi=\int d^3y\;\frac{\delta\varphi(y)}{\delta A^a_i(0)},\qquad
\chi_\varphi=\int d^3z\;\big\langle\varphi(z)\varphi(0)\big\rangle_0^{\rm c},$$
at fixed regularization, with $g=g(a)$. The continuum version requires
a limit of the full weighted numerator and the susceptibility as below. Both sides are intensive: the volume
cancels between the numerator and the denominator, which is what makes
the zero-momentum operator the right trial excitation and the plaquette
of [the upper-bound note](lattice-gap-upper-bounds.md) the wrong one.
The inequality is the energy-weighted sum rule, $m$ bounded by the mean
excitation energy carried by $\varphi$, so its content is: **if some
local gauge-invariant observable has nonvanishing zero-momentum
fluctuations in the vacuum, the theory has an excitation of finite
energy.** Conversely $m=\infty$ forces every such susceptibility to
vanish, that is, the vacuum is an eigenstate of every smeared
gauge-invariant operator. Spatial gradient flow supplies a candidate smearing; its needed
Hamiltonian equal-time continuum estimates remain hypotheses; what is assumed, and
stated as hypothesis (F1), is that the equal-time flowed correlators
have continuum limits, which is not Lüscher's four-dimensional theorem
but its Hamiltonian counterpart. In free Maxwell theory the explicit ratio carries $g^{-2}$, cancelling
the prefactor in the bound, which is $4.26\hbar c/\sqrt{8t}$; since the bound cannot fall below $m$, the
flow time at which that scaling must break down is the correlation
length $\hbar c/m$. In free Maxwell theory the scaling persists for all
$t$ and the bound correctly tends to $m=0$. The inequality itself is the
textbook single-mode (Feynman--Bijl) bound; what is specific here is the
zero-momentum intensive form, the flow as the smearing that makes it
cutoff-independent, and the identification with the finiteness half of
the Millennium statement. Constants explicit; nothing promoted.

## 1. The continuum bound

Take the temporal-gauge Hamiltonian in the convention of
[G07](low-dimensional-mass-gap.md) Proposition 7, with $g$ dimensionless
and $[A]=L^{-1}$:
$$H=\int d^3x\;\Big[\frac{g^2c}{2\hbar}\,\Pi^a_i\Pi^a_i
+\frac{\hbar c}{4g^2}\,F^a_{ij}F^a_{ij}\Big],
\qquad\big[A^a_i(x),\Pi^b_j(y)\big]=i\hbar\,\delta^{ab}\delta_{ij}\delta^3(x-y),$$
obtained from $S=-\frac{\hbar}{4g^2}\int F^a_{\mu\nu}F^{a\mu\nu}d^3x\,c\,dt$
with $\Pi^a_i=(\hbar/g^2c)\dot A^a_i$.

**Proposition 1.** Let $O$ be a real functional of the spatial field
$A$ alone, gauge invariant, with $\langle O\rangle_0=0$ and
$O\Omega\in D(H)$. Then
$$E_1-E_0\ \le\ \frac{g^2\hbar c}{2}\;
\frac{\displaystyle\int d^3x\;\Big\langle\Big|\frac{\delta O}{\delta A^a_i(x)}\Big|^2\Big\rangle_0}
{\big\langle O^2\big\rangle_0}.$$

*Proof.* $O\Omega\perp\Omega$, so by min-max
$E_1-E_0\le\langle O\Omega,(H-E_0)O\Omega\rangle/\|O\Omega\|^2$, and
$2\langle\Omega,O(H-E_0)O\Omega\rangle=\langle\Omega,[O,[H,O]]\Omega\rangle$
since $[O,[H,O]]=2OHO-O^2H-HO^2$. The magnetic term commutes with $O$.
For the electric term, $[\Pi^a_i(x),O]=-i\hbar\,\delta O/\delta A^a_i(x)$
and
$$\big[O,[\Pi^a_i\Pi^a_i,O]\big]=-2\big[\Pi^a_i,O\big]^2
=2\hbar^2\Big|\frac{\delta O}{\delta A^a_i}\Big|^2,$$
so $[O,[H,O]]=\frac{g^2c}{2\hbar}\cdot2\hbar^2\int d^3x|\delta O/\delta A|^2
=g^2\hbar c\int d^3x|\delta O/\delta A|^2$. Divide by $2\langle O^2\rangle$. $\square$

Only the electric term contributes: the bound measures how much the
trial observable is disturbed by the conjugate field, which is the same
quantity that Section 2 of
[the action-floor note](low-dimensional-mass-gap.md#conditional-orbit-area-bounds-and-state-counting) identifies as
the carrier of $\hbar$.

## 2. Zero momentum makes the bound intensive

Let $\varphi(x)$ be a gauge-invariant local scalar with
$\langle\varphi\rangle_0=0$ and take $O=\int_Vd^3y\,\varphi(y)$ in a
periodic box of volume $V$. Write
$$D^a_i(x)=\frac{\delta O}{\delta A^a_i(x)}=\int_Vd^3y\;\frac{\delta\varphi(y)}{\delta A^a_i(x)} .$$
By translation invariance of the ground state, $\langle|D(x)|^2\rangle_0$
does not depend on $x$, so the numerator of Proposition 1 is
$V\langle|D|^2\rangle_0$, while
$\langle O^2\rangle_0=\int_V\int_V\langle\varphi(y)\varphi(y')\rangle^{\rm c}_0=V\chi_\varphi$
with $\chi_\varphi=\int d^3z\,\langle\varphi(z)\varphi(0)\rangle^{\rm c}_0$.
The volume cancels:

**Corollary 2.** For every such $\varphi$ and every $V$,
$$\Delta_V\ \le\ \frac{g^2\hbar c}{2}\;\frac{\langle|D_\varphi|^2\rangle_0}{\chi_\varphi}\,,$$
and if $\Delta_V\to m$ and both ground-state quantities converge, the
same bound holds for $m$.

Dimensions: $\delta/\delta A(x)$ carries $L^{-3}/[A]=L^{-2}$, so
$[\langle|D|^2\rangle]=[\varphi]^2L^2$ and $[\chi]=[\varphi]^2L^3$; the
ratio is an inverse length and $g^2\hbar c$ times it is an energy. The
plaquette of [the upper-bound note](lattice-gap-upper-bounds.md) fails
precisely because it is a single cell rather than a zero-momentum sum:
its variance is an ultraviolet quantity that vanishes in the continuum
limit while its gradient does not.

## 3. Spectral reading and two checks

Inserting a complete set of eigenstates,
$$\langle\Omega,[O,[H,O]]\Omega\rangle=2\sum_n(E_n-E_0)\,\big|\langle n|O|\Omega\rangle\big|^2,
\qquad\langle O^2\rangle_0=\sum_n\big|\langle n|O|\Omega\rangle\big|^2,$$
so Proposition 1 states that $m$ is at most the mean excitation energy
weighted by the spectral weight of $O$: the $f$-sum rule. Two
consequences.

*Conserved observables.* If $[H,O]=0$ the numerator vanishes and the
bound reads $\Delta\le0$. With a unique ground state this is consistent
only if $\langle O^2\rangle_0=0$: a conserved gauge-invariant observable
cannot fluctuate in a nondegenerate vacuum, since $O\Omega$ would be a
second state of energy $E_0$. The bound therefore detects vacuum
degeneracy, and is vacuous exactly in that case.

*Free Maxwell.* Here $m=0$ and the bound is a positive number for every
flow time; Section 5 shows it tends to zero as the smearing grows, which
is the correct behaviour for a gapless theory and a check that the
bound is not empty.

## 4. What must be smeared, and the hypothesis

A local operator at a point has divergent gradient in the continuum, so
$\varphi$ must be built from a smeared field. The gauge-covariant
smearing is the gradient flow: on the spatial field at fixed time,
$$\partial_s B_i=D_jG_{ji},\qquad B_i|_{s=0}=A_i,\qquad
G_{ij}=\partial_iB_j-\partial_jB_i+[B_i,B_j],$$
the three-dimensional, equal-time counterpart of Lüscher's flow
(arXiv:1006.4518v3, equations (1.1)--(1.2), passage level via the
[local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md)), with
smearing radius $\sqrt{8t}$ at flow time $t$ and the lattice form given
by his equation (1.4). Take
$\varphi=\varphi_t=\tfrac14G^a_{ij}G^a_{ij}\big|_{s=t}-\langle\cdot\rangle_0$.

Lüscher's renormalization statement is for the four-dimensional flow in
the Euclidean functional integral: expectation values of local
gauge-invariant expressions in the flowed field are finite without
further renormalization. The object needed here is the equal-time
Hamiltonian correlator of the spatially flowed field, which his theorem
does not cover. State it as a hypothesis:

> **(F1)** For fixed flow time $t>0$, the equal-time ground-state
> susceptibility $\chi_{\varphi_t,a}$ converges to a finite strictly
> positive limit $\chi_t$, and the complete weighted numerator
> $g(a)^2\langle|D_{\varphi_t,a}|^2\rangle_0$ converges to a finite
> limit $K_t$, as $a\to0$ along the scaling curve (after the specified
> volume limit).

On any fixed lattice both quantities are finite and positive and
Corollary 2 holds unconditionally, so (F1) is entirely a statement about
the continuum limit. Its first half is the flow's renormalization
property in the Hamiltonian framework; its second half, $\chi>0$, is
nontriviality: the vacuum is not an eigenstate of the flowed energy
density.

**Proposition 3 (the finiteness half).** Assume the continuum theory
exists with a unique vacuum and translation invariance, that the
finite-volume gaps converge to $m$, and (F1) for one flow time $t$.
Then
$$m\ \le\ \frac{\hbar c}{2}\,\frac{K_t}{\chi_t}\ <\ \infty .$$

This gives the $m<\infty$ clause conditional on the weighted numerator,
the positive susceptibility and spectral-limit hypotheses. The remaining clause, $m>0$, is
untouched: nothing above excludes $m=0$.

## 5. The free Maxwell check and the coupling correction

The coefficient $g^2$ in the variational bound is cancelled by the
$g^{-2}$ dependence of the ratio of the two free-field observables.
Dimensional analysis alone cannot determine this coupling dependence.
The following is an exact Gaussian calibration; extending it to an
interacting theory near its confinement scale requires nonperturbative
control, and an upper bound cannot prove a positive gap.

### 5a. Free ground state

Take the abelian case of the Hamiltonian of §1,
$$H=\int d^3x\;\Big[\frac{g^2c}{2\hbar}\,\Pi_i\Pi_i+\frac{\hbar c}{2g^2}\,b_ib_i\Big],
\qquad b_i=\varepsilon_{ijk}\partial_jA_k,
\qquad[A_i(x),\Pi_j(y)]=i\hbar\delta_{ij}\delta^3(x-y),$$
in Coulomb gauge $\partial_iA_i=0$, two transverse polarizations. In
Fourier modes each transverse mode is an oscillator of mass
$M=\hbar/(g^2c)$ and frequency $\omega_k=ck$, since
$\tfrac12M\omega_k^2=\hbar ck^2/(2g^2)$ matches the magnetic term. Its
ground-state width gives
$$\big\langle\hat A_i(k)\hat A_j(k')\big\rangle_0=(2\pi)^3\delta^3(k+k')\,P^{\rm T}_{ij}(k)\,\frac{\hbar}{2M\omega_k}
=(2\pi)^3\delta^3(k+k')\,P^{\rm T}_{ij}(k)\,\frac{g^2}{2k},$$
with $P^{\rm T}_{ij}=\delta_{ij}-\hat k_i\hat k_j$. Dimensions:
$[\hat A]=L^2$, $[(2\pi)^3\delta^3]=L^3$, and $g^2/2k$ is a length.

### 5b. Equal-time flow

For an abelian field the flow equation of §4
reduces to $\partial_sB_i=\Delta B_i-\partial_i(\partial_jB_j)$, and a
transverse initial field stays transverse, so
$$\hat B_i(t,k)=e^{-tk^2}\hat A_i(k),\qquad
\hat b_i(t,k)=i\varepsilon_{ijl}k_j\,e^{-tk^2}\hat A_l(k).$$
The flow time has dimension of length squared; the conventional
smearing radius is $\sqrt{8t}$. Set
$\varphi_t=\tfrac12\big(b_t\!\cdot\!b_t-\langle b_t\!\cdot\!b_t\rangle_0\big)$,
of dimension $L^{-4}$.

### 5c. Susceptibility

Write $G_{ij}(z)=\langle b_{t,i}(z)b_{t,j}(0)\rangle_0$. Using
$\varepsilon_{iab}\varepsilon_{jcd}k_ak_cP^{\rm T}_{bd}(k)=k^2P^{\rm T}_{ij}(k)$
(the longitudinal part of $P^{\rm T}$ drops because
$\varepsilon_{iab}k_a\hat k_b=0$),
$$\tilde G_{ij}(k)=k^2P^{\rm T}_{ij}(k)\,\frac{g^2}{2k}\,e^{-2tk^2}
=\frac{g^2k}{2}\,e^{-2tk^2}\,P^{\rm T}_{ij}(k).$$
For a Gaussian field Wick's theorem gives
$\langle\varphi_t(z)\varphi_t(0)\rangle^{\rm c}_0=\tfrac12\sum_{ij}G_{ij}(z)^2$
(two pairings), so by Parseval, with
$\sum_{ij}[P^{\rm T}_{ij}]^2=\operatorname{tr}P^{\rm T}=2$,
$$\chi_{\varphi_t}=\int d^3z\,\langle\varphi_t\varphi_t\rangle^{\rm c}
=\frac12\int\frac{d^3k}{(2\pi)^3}\,\frac{g^4k^2}{2}\,e^{-4tk^2}
=\frac{g^4}{4}\cdot\frac1{2\pi^2}\int_0^\infty\!dk\,k^4e^{-4tk^2}.$$
With $\int_0^\infty k^4e^{-\alpha k^2}dk=3\sqrt\pi/(8\alpha^{5/2})$ and
$\alpha=4t$, so $(4t)^{5/2}=32t^{5/2}$,
$$\chi_{\varphi_t}=\frac{g^4}{4}\cdot\frac1{2\pi^2}\cdot\frac{3\sqrt\pi}{256\,t^{5/2}}
=\frac{3g^4}{2048\,\pi^{3/2}\,t^{5/2}} .$$
Dimension: $[\chi]=[\varphi]^2L^3=L^{-5}$ and $t^{5/2}\sim L^5$, as required.

### 5d. Gradient term

By Parseval $O=\int d^3y\,\varphi_t=\tfrac12\int\frac{d^3k}{(2\pi)^3}k^2e^{-2tk^2}|\hat A(k)|^2+\text{const}$,
so
$$D_i(x)=\frac{\delta O}{\delta A_i(x)}=\big(-\Delta\,e^{2t\Delta}A\big)_i(x)
=\big(\nabla\times b_{2t}\big)_i(x),\qquad
\hat D_i(k)=k^2e^{-2tk^2}\hat A_i(k),$$
the curl of the magnetic field at twice the flow time. Hence
$$\big\langle|D|^2\big\rangle_0=\int\frac{d^3k}{(2\pi)^3}k^4e^{-4tk^2}\cdot2\cdot\frac{g^2}{2k}
=g^2\cdot\frac1{2\pi^2}\int_0^\infty\!dk\,k^5e^{-4tk^2}
=\frac{g^2}{2\pi^2}\cdot\frac1{64\,t^3}=\frac{g^2}{128\,\pi^2\,t^3},$$
using $\int_0^\infty k^5e^{-\alpha k^2}dk=1/\alpha^3$. Dimension:
$[\varphi]^2L^2=L^{-6}$ and $t^3\sim L^6$, as required.

### 5e. The bound and coupling cancellation

$$\frac{\langle|D|^2\rangle}{\chi}
=\frac{g^2}{128\pi^2t^3}\cdot\frac{2048\,\pi^{3/2}t^{5/2}}{3g^4}
=\frac{16}{3\,g^2\sqrt{\pi t}},$$
$$m\ \le\ \frac{g^2\hbar c}{2}\cdot\frac{16}{3g^2\sqrt{\pi t}}
=\frac{8}{3\sqrt\pi}\,\frac{\hbar c}{\sqrt t}
=\frac{16\sqrt2}{3\sqrt\pi}\,\frac{\hbar c}{\sqrt{8t}}\approx4.26\,\frac{\hbar c}{\sqrt{8t}} .$$

**Correction.** The earlier version inferred
$m\le Cg^2\hbar c/\sqrt{8t}$ from dimensional analysis, assigning the
pure numbers $k_1,k_2$ no coupling dependence. The computation shows
$\chi\propto g^4$ while $\langle|D|^2\rangle\propto g^2$, so the ratio
carries $g^{-2}$ and the bound is of order $g^0$. The corrected
statement is that the perturbative bound is
$4.26\,\hbar c/\sqrt{8t}\,[1+O(g^2)]$, with the coupling entering only
through the corrections. The $t$-dependence $1/\sqrt{8t}$ of the earlier
note stands.

### 5f. Two-photon sum-rule check

By the spectral reading of §3, the
bound equals the mean excitation energy weighted by the spectral weight
of $O$. In the free theory $O$ is quadratic in $\hat A$ and creates two
photons of momenta $k$ and $-k$, of total energy $2\hbar ck$, with
weight proportional to
$\big[k^2e^{-2tk^2}\big]^2\big[g^2/2k\big]^2\,k^2\,dk\propto k^4e^{-4tk^2}dk$
after the phase-space factor. Therefore
$$\frac{\int_0^\infty 2\hbar ck\cdot k^4e^{-4tk^2}dk}{\int_0^\infty k^4e^{-4tk^2}dk}
=2\hbar c\,\frac{1/(64t^3)}{3\sqrt\pi/(256\,t^{5/2})}
=2\hbar c\cdot\frac{4}{3\sqrt{\pi t}}
=\frac{8}{3\sqrt\pi}\,\frac{\hbar c}{\sqrt t},$$
the same number. The agreement checks Proposition 1, the intensive form
of Corollary 2 and the Gaussian computation against each other, since
both evaluate the same spectral sum rule by different arithmetic routes.


In a weakly coupled regime the free value is a perturbative orientation,
not a uniform confinement-scale bound. Its decrease at large flow time
is consistent with a gapless photon; monotonic convergence of the
interacting spectral mean to the lowest energy is not proved.

## 6. Status

| claim | status |
| --- | --- |
| Proposition 1, the bound with explicit constants | proved |
| Corollary 2, intensive zero-momentum form | proved |
| $f$-sum rule reading, conserved-observable check | proved |
| finiteness of the lattice bound at fixed $a$ | proved |
| (F1), continuum limit of the flowed equal-time correlators | hypothesis; the flow's renormalization in the Hamiltonian framework |
| $\chi>0$ | hypothesis; nontriviality |
| Free Maxwell ratio and two-photon mean | exact calibration, §5 |
| $m>0$ | untouched |

The single-mode bound and the use of smeared operators as glueball
interpolators are standard; the statement being recorded is the
reduction of the Millennium finiteness clause to the positivity of one
flowed susceptibility, with the constants and hypotheses written out.

## 7. Consequence for STATE

The upper side of the problem is now in the same shape as the lower
side: an exact inequality at fixed cutoff, plus one renormalization
hypothesis for the continuum. The two hypotheses are different in kind.
(F1) concerns flowed observables, which are expected to be renormalized
by Lüscher's four-dimensional result and whose Hamiltonian counterpart
is a bounded, self-contained question; the dressed-vacuum problem of
[the Schur note](weak-coupling-feshbach-reduction.md) concerns the state itself.
The next steps this suggests, in order: use the explicit free-field calibration in §5; then state the Hamiltonian flow-renormalization question as its own
target, since both the upper-side (F1) and the lower-side dressing are
instances of it.
