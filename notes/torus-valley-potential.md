# The one-loop potential along the abelian valley of the torus is periodic, reproduces C133's linear term at the origin, and saturates at order 1/L

For $SU(2)$ Yang--Mills on $T^3_L$ with a constant abelian background
$a=a_i^{\,3}T^3$, the zero-point energy of all modes, relative to $a=0$,
is the exact periodic function
$$U(a)=\frac{2\hbar c}{\pi^2L}\,\Phi(La),\qquad \Phi(b)=\sum_{m\in\mathbb Z^3\setminus\{0\}}\frac{1-\cos(m\cdot b)}{|m|^4}\ \ge0,$$ with $a$ of dimension inverse length ($[A]=L^{-1}$ in the convention of G07 Proposition 7), obtained by Poisson summation of the charged frequencies $\hbar c|k\pm a|$ over $k\in(2\pi/L)\mathbb Z^3$; the divergent part
of the sum is $a$-independent under any periodic regularization and
drops out. Near the origin $\Phi(b)=\pi^2|b|+\tfrac16C_M|b|^2+O(|b|^3)$
with $C_M=\lim_{b\to0}[\sum'_me^{im\cdot b}|m|^{-2}-2\pi^2/|b|]$, so $U(a)=2\hbar c|a|+\tfrac{C_M}{3\pi^2}\hbar cL|a|^2+\cdots$. The linear term $2\hbar c|a|$ is exactly the $k=0$ contribution, four oscillators of angular frequency $c|a|$ with zero-point energy $\tfrac12\hbar c|a|$ each, which are the transverse
oscillators of C133 along its abelian valley: the field-theory
computation reproduces the mechanism of [G07](low-dimensional-mass-gap.md)
and [G08](action-floor-yang-mills-gap.md) term by term. The nonzero
modes contribute the correction $U_\perp=U-2\hbar c|a|=O(\hbar cL|a|^2)$, of order $g^{4/3}\hbar c/L$ in the rescaled variables of
[the Feshbach note](weak-coupling-feshbach-reduction.md), which is the
input (H3) needs, with the sign of $C_M$ (negative for the cubic
lattice) deciding that the correction lowers the valley potential.
Globally $U$ is bounded by $2\hbar c\max\Phi/(\pi^2L)=O(\hbar c/L)$ and vanishes
exactly at $La\in2\pi\mathbb Z^3$, the holonomies that are central in
the fundamental representation: the confinement of the constant modes
along the valley is linear only for $La\ll1$, saturates at order $\hbar c/L$,
and has degenerate minima at the centre elements, which is the
small-volume origin of the electric-flux sectors. Since the zero-mode gap is $g^{2/3}\hbar c/L\ll\hbar c/L$, the ground state is localized at $La\sim g^{2/3}$
and never reaches the saturation; the crossover $z\simeq2$ is where it
does. Sources: this is the spatial-torus form of Weiss's finite-temperature
potential (Phys. Rev. D 24 (1981) 475, metadata), and it appears in the
small-volume literature (Lüscher 1983, abstract); the derivation below
is self-contained. Nothing here is promoted.

## 1. Frequencies in a constant abelian background

Let $a_i=\alpha_iT^3$, $i=1,2,3$, with $\vec\alpha\in\mathbb R^3$, and
write $a$ for $\vec\alpha$ when no confusion arises. Decompose the
adjoint fluctuation $\tilde A_i=\tilde A_i^3T^3+\tilde A_i^+T^++\tilde A_i^-T^-$.
The covariant derivative $D_j=\partial_j+[a_j,\cdot]$ acts on the neutral
component as $\partial_j$ and on the charged components as
$\partial_j\pm i\alpha_j$, so on the Fourier mode $e^{ik\cdot x}$,
$k\in(2\pi/L)\mathbb Z^3$, the charged components have covariant momentum
$k\pm a$. The quadratic form $\frac1{2g^2}\int|D_i\tilde A_j-D_j\tilde A_i|^2$
is, for a constant abelian background, the free transverse form with $k$
replaced by $k\pm a$ on the charged components, so after the usual
transverse gauge choice the frequencies are
$$\hbar\omega^{(0)}_k=\hbar c|k|\quad(\text{neutral, two polarizations}),$$
$$\hbar\omega^{(\pm)}_k=\hbar c|k\pm a|\quad(\text{charged, two polarizations each}),$$
for $k\ne0$. At $k=0$ the neutral components are the valley directions
themselves and the charged components of $\tilde A_j$ have frequency
$|a|$ for each of the two charges and, since there is no transversality
at $k=0$, for the components of $\tilde A_j$ orthogonal to the valley
in field space: with $a=\alpha_1T^3$ along $x_1$ only, these are the
charged parts of $\tilde A_2,\tilde A_3$, four real oscillators of angular frequency $c|a|$, while the charged parts of $\tilde A_1$ are gauge
directions of frequency zero removed by Gauss's law.

**The $k=0$ term is C133.** The SU(2) matrix model of C133 with
$\vec x_1=\lambda\hat n$, $\vec x_2=\vec x_3=0$ has potential
$\tfrac12g^2(|\vec x_1\times\vec x_2|^2+|\vec x_1\times\vec x_3|^2+\cdots)$,
whose transverse Hessian at that point gives the components of
$\vec x_2,\vec x_3$ orthogonal to $\hat n$, four oscillators of
frequency $g|\lambda|/\sqrt m$; in the field-theory variables of
[G07](low-dimensional-mass-gap.md) Proposition 7 ($m=\hbar L^3/(g^2c)$, $g_B^2=\hbar cL^3/g^2$) this frequency is $c|a|$. The zero-point energy $4\cdot\tfrac12\hbar c|a|=2\hbar c|a|$ is the confining term of
G07 Theorem 6(1) and the floor of G08 Theorem 2 along the valley.

## 2. Poisson summation

The zero-point energy of the fluctuations relative to $a=0$, summing two
polarizations and both charges, is
$$U(a)=\frac{\hbar c}2\sum_{k\in(2\pi/L)\mathbb Z^3}\sum_{\rm pol=1,2}\big(|k+a|+|k-a|-2|k|\big) =\hbar c\sum_{k\in(2\pi/L)\mathbb Z^3}\big(|k+a|+|k-a|-2|k|\big),$$ where the $k=0$ term is $2\hbar c|a|$ and the neutral modes cancel. Each term is
nonnegative by convexity of $|\cdot|$ and of order $|a|^2/|k|$, so the
sum diverges in three dimensions; under a periodic regularization
(lattice dispersion $\omega_{\rm lat}$ with the exact momentum grid) the
divergent part is $a$-independent, because $\sum_{k\in\text{grid}}\omega_{\rm lat}(k+a)$
is a periodic function of $a$ with period $2\pi/L$ whose mean over a
period is the $a$-independent Brillouin-zone integral. The $a$-dependent
part is obtained by Poisson summation. For $f(k)=|k|$ the distributional
Fourier transform is $\hat f(x)=\int|k|e^{-ik\cdot x}d^3k=-8\pi/|x|^4$ for
$x\ne0$ (the formula $\widehat{|k|^\alpha}=2^{\alpha+3}\pi^{3/2}\frac{\Gamma((3+\alpha)/2)}{\Gamma(-\alpha/2)}|x|^{-3-\alpha}$
at $\alpha=1$, with $\Gamma(-\tfrac12)=-2\sqrt\pi$), and
$$\sum_{k\in(2\pi/L)\mathbb Z^3}f(k+a)=\Big(\frac L{2\pi}\Big)^3\sum_{m\in\mathbb Z^3}\hat f(mL)\,e^{im\cdot La}$$
with the $m=0$ term the divergent, $a$-independent one. Hence
$$U(a)=\hbar c\Big(\frac L{2\pi}\Big)^3\sum_{m\ne0}\Big(-\frac{8\pi}{L^4|m|^4}\Big)\big(e^{im\cdot La}+e^{-im\cdot La}-2\big) =\frac{2\hbar c}{\pi^2L}\sum_{m\ne0}\frac{1-\cos(m\cdot La)}{|m|^4}=\frac{2\hbar c}{\pi^2L}\Phi(La).$$
Lattice corrections change $\hat f$ only at $|x|\lesssim a_{\rm lat}$,
while the $m\ne0$ terms live at $|x|=|m|L\ge L$, so they are
$O(a_{\rm lat}^2/L^2)$ relative.

Properties of $\Phi$: it is nonnegative, periodic with period $2\pi$ in
each component, invariant under the cubic group, bounded by
$2\sum'|m|^{-4}$, and zero exactly on $2\pi\mathbb Z^3$.

## 3. Expansion at the origin and the sign of the correction

$\Phi$ is not smooth at $0$. Its Laplacian is the periodic Green's
function $G(b)=\sum'_me^{im\cdot b}|m|^{-2}$, which has the Coulomb
singularity $2\pi^2/|b|$ at the origin (from $\int d^3m\,e^{im\cdot b}|m|^{-2}$)
and a finite remainder: $G(b)=2\pi^2/|b|+C_M+O(|b|^2)$, where $C_M$ is the
constant term of the periodic Coulomb Green's function of the cubic
lattice, the analytically continued Epstein sum $\sum'_m|m|^{-2}$.
Since $\Delta(\pi^2|b|)=2\pi^2/|b|$, the function $\Phi-\pi^2|b|$ has
Laplacian $C_M+O(|b|^2)$ near $0$, and the only quadratic form with cubic
symmetry and Laplacian $C_M$ is $\tfrac16C_M|b|^2$; so
$$\Phi(b)=\pi^2|b|+\tfrac16C_M|b|^2+O(|b|^3),\qquad
U(a)=2\hbar c|a|+\frac{C_M}{3\pi^2}\,\hbar cL|a|^2+O(\hbar cL^2|a|^3).$$ The linear term $2\hbar c|a|$ is the $k=0$ contribution of Section 1, so the nonzero modes contribute $$U_\perp(a)=U(a)-2\hbar c|a|=\frac{C_M}{3\pi^2}\hbar cL|a|^2+O(\hbar cL^2|a|^3),$$
with $C_M<0$ for the cubic lattice (lattice-sum tables; the sign is not
re-derived here and affects only the direction of a subleading
correction). In the rescaled variables $a=g^{2/3}\xi/L$ this is
$\frac{C_M}{3\pi^2}g^{4/3}|\xi|^2\,\hbar c/L$, of relative order $g^{2/3}$ to the zero-mode Hamiltonian $g^{2/3}h_3\,\hbar c/L$: the size that (H3) of the
Feshbach reduction assumes, now with its coefficient identified.

## 3a. General constant backgrounds at quadratic order

The abelian computation fixes the quadratic term of $U_\perp$ for every
constant background. For $|a|$ small against $2\pi/L$ each nonzero-mode
quadratic form is positive definite and depends smoothly on
$(a_1,a_2,a_3)\in(\mathfrak{su}(2))^3$, and the trace of the square root
of a smooth positive-definite family is smooth, so with a lattice
regularization $U_\perp$ is a smooth function near $a=0$ (the
non-smooth $|a|$ behaviour of $U$ comes only from the $k=0$ term). It is
invariant under the constant gauge transformations, which rotate the
three colour vectors $\vec a_i$ simultaneously, under the cubic group
acting on the spatial index, and under $a\to-a$. The quadratic
invariants of $(\vec a_1,\vec a_2,\vec a_3)$ under $SO(3)_{\rm colour}$
are the bilinears $\vec a_i\cdot\vec a_j$, and the only cubic-invariant
symmetric form in the spatial indices is $\delta_{ij}$, so
$$U_\perp(a)=c\,\hbar cL\sum_{i=1}^3|\vec a_i|^2+O(\hbar cL^2|a|^3),$$
with a single pure number $c$, which the abelian valley
($\vec a_i=\alpha_i\hat e_3$, $\sum_i|\vec a_i|^2=|\alpha|^2$) determines:
$c=C_M/(3\pi^2)$. The Landau-level structure of non-commuting
backgrounds enters only at the cubic order $O(\hbar cL^2|a|^3)$, which is
of relative order $g^{4/3}$ to the zero-mode Hamiltonian; (H3) at its
leading correction therefore needs no non-abelian spectral input beyond
the symmetry argument.

## 3b. The abelian theory in the same expansion

For compact $U(1)$ the constant modes commute, the quartic potential
vanishes, and the photons are neutral, so the one-loop potential of the
holonomy is identically zero: the constant-mode Hamiltonian is the free
Laplacian on the torus of holonomies, $H_0=\frac{e^2c}{2\hbar L^3}|p|^2$
with $a$ periodic of period $2\pi/L$, spectrum $e^2\hbar c|n|^2/(2L)$,
$n\in\mathbb Z^3$, gap $e^2\hbar c/(2L)$. The abelian small-volume gap is
linear in $e^2$, not $e^{2/3}$, because there is no commutator to confine
the holonomy and no charged mode to give it a potential; with $e$ fixed
by the absence of running, the $1/L$ decay is uncompensated and the
infinite-volume theory is gapless, in agreement with the Coulomb phase
of Guth and Fröhlich--Spencer. In the non-abelian theory both the
$g^{2/3}$ and the running of $g(L)$ come from the charged modes, the
former through the $k=0$ commutator term and the latter through the
logarithm in the quartic coefficient of $U$.

## 4. Saturation and the centre-degenerate minima

$U(a)\le2\hbar c\max\Phi/(\pi^2L)=O(\hbar c/L)$ for all $a$, while the $k=0$ term $2\hbar c|a|$ alone grows without bound. The linear confinement of the constant modes
along the abelian valley, which in C133 holds for all $|a|$, is in the
torus theory the small-$La$ regime of a bounded periodic function. The
minima of $U$ are at $La\in2\pi\mathbb Z^3$: for $SU(2)$ with the charged
modes of charge $\pm1$, $La=2\pi e_i$ corresponds to the fundamental
holonomy $\exp(2\pi iT^3)=-1$, a centre element, trivial on all adjoint
fields but a distinct state of the theory; the degenerate minima are
connected by tunnelling through the valley barrier of height $O(\hbar c/L)$,
which produces the splittings between the 't Hooft electric-flux
sectors of the small-volume spectrum (van Baal's programme; not derived
here).

Consequence for the small-volume expansion: the zero-mode ground state
has width $La\sim g^{2/3}$ and energy $g^{2/3}\hbar c/L$, far below the valley saturation scale $\hbar c/L$ and the tunnelling barrier, so the C133 picture
is exact at leading order and the corrections enter at relative order
$g^{2/3}$, as in the Feshbach reduction. The regime where the zero-mode
energy reaches $\hbar c/L$, $g(L)^{2/3}\sim1$, is where the holonomy
delocalizes over the whole compact valley, the flux sectors become
degenerate and the description changes character: the crossover
$z\simeq2$ of Lüscher--Münster in this language.

## 5. Consequence for STATE

(H3)'s one-loop input along the abelian valley is now explicit:
$U_\perp=\frac{C_M}{3\pi^2}\hbar cL|a|^2+O(\hbar cL^2|a|^3)$, bounded by $O(\hbar c/L)$
globally, periodic with centre-degenerate minima. By the symmetry argument of Section 3a the same quadratic term holds for every constant background, so (H3) at its leading correction is a relatively bounded perturbation of
$h_3$ by $-|C_M|g^{4/3}\sum_i|\xi_i|^2\,\hbar c/(3\pi^2L)$ inside the region $La\ll1$ and by a bounded potential outside it, which the confining bound of C133 controls; the Landau-level input enters only at the next order. The abelian theory has no valley potential at all, which is the small-volume form of the abelian/non-abelian distinction.
