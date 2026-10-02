# Strong coupling for abelian and non-abelian gauge theories: a shared existential gap

Both compact $U(1)$ and $SU(3)$ have a volume-uniform strong-coupling
Kogut--Susskind gap by the
[Yarotsky application](strong-coupling-uniform-gap.md), with an
existential threshold. The
[continuous-time expansion](kogut-susskind-strong-coupling-explicit.md)
does not currently provide an explicit uniform threshold for either
group. Their weak sides differ: for $SU(3)$,
$$\frac{d\,g^2}{d\log a}=2b_0g^4+O(g^6),\qquad b_0=\frac{11}{16\pi^2}>0,$$
whereas the continuum pure photon has no perturbative self-interaction,
$b_0=0$. A massless weak-coupling phase of compact lattice $U(1)$ is
supported by Guth (Phys. Rev. D 21 (1980) 2291) and Fröhlich--Spencer
(Commun. Math. Phys. 83 (1982) 411; both metadata level). The perturbative
running does not determine the whole lattice phase diagram or establish
a constructive arrival in the strong-coupling region.

**Correction, 2026-10-02.** The earlier uniform $4\lambda$ bound, an
explicit threshold of the same size as for $SU(3)$, and a target box
at $g^2\sim4\times10^2$ depended on the withdrawn continuous-time
count. They are withdrawn here. The finite-volume electric-loop result
below survives; the volume-uniform theorem instead uses Yarotsky with
an existential threshold. The earlier exact coupling-set and flow
equivalences also exceeded the cited perturbative and phase results;
[the corrected coupling-set note](gapped-set-critical-coupling.md)
separates them. The original text remains in Git history.

## 1. The strong-coupling region does not distinguish the groups

For compact $U(1)$ take the magnetic term
$(2/g^2)\sum_p(1-\cos\theta_p)$ and electric term
$(g^2/2)\sum_\ell n_\ell^2$. The least nonzero electric eigenvalue per
link is $\varepsilon=g^2/2$. The plaquette operator
$w_p=e^{i\theta_p}+e^{-i\theta_p}$ has norm $2$ and shifts the four
link charges by $\pm1$. Gauss's law allows decomposition of a nonzero
charge network into closed charged cycles. On a periodic cubic lattice
with $N_s\ge4$, every nonempty support has at least four links. A
plaquette loop attains this minimum, so the physical electric gap is
exactly $2g^2$ in units $\hbar c/a$.

Writing $P=3N_s^3$, the magnetic operator after removal of its scalar
constant has norm at most $2P/g^2$. The two-eigenvalue min--max argument
of the corrected Kogut--Susskind note therefore gives
$$\left(2g^2-\frac{4P}{g^2}\right)\frac{\hbar c}{a}
\le\Delta^{\rm phys}_{a,L}\le
\left(2g^2+\frac{4P}{g^2}\right)\frac{\hbar c}{a},\qquad L=N_sa.$$
At fixed $N_s$, $\Delta^{\rm phys}_{a,L}/(g^2\hbar c/a)\to2$.
The lower bound is extensive and supplies no volume-uniform threshold.
A nonpositive lower bound is uninformative.

The former adjacent-growth calculation controls a restricted history
class. It misses histories reaching a test link later and does not
establish true-vacuum decay; changing the gauge group does not repair
those gaps. Uniformity at sufficiently strong coupling follows instead
from the group-general Yarotsky application. Its constants depend on
the chosen local interaction range.

## 2. What differs is the weak-side flow

The [target-box note](strong-coupling-target-box.md) now provides an
existential strong-coupling region for a specified family of finite-range
local corrections. Its edge and tolerance are not the former
continuous-time numerical values. An effective Hamiltonian must satisfy
its hypotheses before its gap can be transferred.

For $SU(3)$, perturbative asymptotic freedom gives
$g^2(2a)=g^2(a)+2b_0\log2\,g^4(a)+O(g^6)$ at weak coupling, with
$2b_0\log2\simeq0.0966$. A proposed route is to control all generated
corrections until the effective Hamiltonian enters that region. This
requires a constructive reduction and spectral transfer; absence of an
intermediate fixed point is not an equivalent proof. The
[position note](mass-gap-position.md) §6 identifies the region where
neither the perturbative expansion nor a strong-coupling theorem applies.

For continuum pure $U(1)$, perturbative running is absent to all orders.
That is not an exact blocking identity for the compact lattice action
at every coupling. The weak-coupling massless phase and the existential
strong-coupling gap do not alone identify the entire gapped set as one
interval or locate its boundary.

## 3. Non-abelian mechanisms and their limits

[The position note](mass-gap-position.md) §4 isolates the commutator
potential of the zero-mode sector, the absence of a gauge-invariant
operator linear in the non-abelian electric field, and the one-loop
valley potential. These are distinct mechanisms: a small-volume
confining potential, a missing photon observable, and a perturbative
correction. They motivate the non-abelian route but do not establish
the full continuum gap from the beta function alone.

## 4. What this settles and what it leaves

Both groups have a gap at sufficiently strong coupling by the
existential theorem. Compact $U(1)$ also has a massless weak phase.
For $SU(3)$ the perturbative slope is positive, but controlled arrival,
scaling and continuum reconstruction remain open. The strong-coupling
edge and tolerance in this Hamiltonian comparison are existential.

## 5. Consequence for STATE

Use the group-general existential strong-coupling theorem and the
explicit finite-volume bound above. Do not reuse the withdrawn uniform
$4\lambda$ rate or numerical box location. A non-abelian continuum gap
still requires controlled reduction, scaling and reconstruction;
perturbative running alone is insufficient. This written correction
supplies no new explicit volume-uniform threshold.
