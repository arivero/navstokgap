# The one-loop potential along abelian torus valleys is periodic, reproduces C133 at the origin, and saturates at order $1/L$

**Scope — one-loop, constant Cartan backgrounds only.**  For $SU(2)$
Yang--Mills on $T^3_L$ with a constant abelian background
$a=a_i^{\,3}T^3$, the zero-point energy of all modes, relative to $a=0$,
is the exact periodic function
$$U(a)=\frac{2\hbar c}{\pi^2L}\,\Phi(La),\qquad \Phi(b)=\sum_{m\in\mathbb Z^3\setminus\{0\}}\frac{1-\cos(m\cdot b)}{|m|^4}\ \ge0,$$ with $a$ of dimension inverse length ($[A]=L^{-1}$ in the convention of G07 Proposition 7), obtained by Poisson summation of the charged frequencies $\hbar c|k\pm a|$ over $k\in(2\pi/L)\mathbb Z^3$; the divergent part
of the sum is $a$-independent under any periodic regularization and
drops out. Near the origin $\Phi(b)=\pi^2|b|+\tfrac16C_M|b|^2+O(|b|^3)$
with $C_M=\lim_{b\to0}[\sum'_me^{im\cdot b}|m|^{-2}-2\pi^2/|b|]$, so $U(a)=2\hbar c|a|+\tfrac{C_M}{3\pi^2}\hbar cL|a|^2+\cdots$. The linear term $2\hbar c|a|$ is exactly the $k=0$ contribution, four oscillators of angular frequency $c|a|$ with zero-point energy $\tfrac12\hbar c|a|$ each, which are the transverse
oscillators of C133 along its abelian valley: the field-theory
computation reproduces the mechanism of [G07](low-dimensional-mass-gap.md)
and [G08](action-floor-yang-mills-gap.md) term by term.

The same root-plane calculation gives an explicit $SU(3)$ result.  If
$a_i$ lie in one Cartan subalgebra and $\alpha_{pq}(a)=(\lambda_{p,i}-\lambda_{q,i})_{i=1}^3$ are its three positive-root momentum shifts,
then
$$U_{SU(3)}(a)=\frac{2\hbar c}{\pi^2L}\sum_{1\le p<q\le3}\Phi\big(L\alpha_{pq}(a)\big).$$
Thus its $k=0$ part is $2\hbar c\sum_{p<q}|\alpha_{pq}(a)|$, exactly the
transverse zero-point term of the compact-semisimple C133 theorem, while
the nonzero modes give a quadratic correction of order
$g^{4/3}\hbar c/L$ in the C133 rescaling.  The derivation and precise
normalization are in Section 3c.

Globally the potential is bounded by $O(\hbar c/L)$ and has
degenerate centre-valued holonomy minima: confinement of the constant
modes along a valley is linear only for $La\ll1$, and saturates at order
$\hbar c/L$.  Since a weak-coupling zero-mode gap is
$g^{2/3}\hbar c/L\ll\hbar c/L$, the ground state is localized at
$La\sim g^{2/3}$ and never reaches the saturation; the crossover
$z\simeq2$ is where it does.  Sources: this is the spatial-torus form of
Weiss's finite-temperature potential (Phys. Rev. D 24 (1981) 475,
metadata), and it appears in the small-volume literature (Lüscher 1983,
abstract); the derivation below is self-contained.  This one-loop
calculation does **not** prove a fibrewise Feshbach estimate, uniform
lattice blocking, or a continuum $SU(3)$ gap.  Nothing here is promoted.

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

## 3c. The $SU(3)$ Cartan valley: an exact root-sum extension

This subsection is the promised $SU(3)$ version; it is still only a
constant Cartan-background, one-loop calculation.  Use the normalization
of [C133](low-dimensional-mass-gap.md), $\|X\|^2=2\operatorname{Tr}X^2$,
and write commuting Hermitian Cartan backgrounds as
\[
 a_i=\operatorname{diag}(\lambda_{1i},\lambda_{2i},\lambda_{3i}),
 \qquad\sum_{p=1}^3\lambda_{pi}=0,
 \qquad\alpha_{pq}(a)=(\lambda_{p i}-\lambda_{q i})_{i=1}^3 . \tag{10}
\]
The real adjoint root plane for the pair $p,q$ has covariant momenta
$k\pm\alpha_{pq}(a)$.  It is therefore precisely one copy of the charged
$SU(2)$ calculation in Sections 1--3.  Summing its two physical
polarizations and then the three positive roots gives
\[
 \boxed{\quad U_{SU(3)}(a)=\frac{2\hbar c}{\pi^2L}
 \sum_{p<q}\Phi\big(L\alpha_{pq}(a)\big).\quad}            \tag{11}
\]
There is no additional Cartan contribution: it is neutral and cancels on
subtracting the value at $a=0$.  Equation (11) is regulator-independent in
the same restricted sense as the $SU(2)$ derivation: a periodic
gauge-invariant regulator removes an $a$-independent divergence, while the
nonzero Poisson images produce the displayed holonomy-dependent term.

The $k=0$ term and the small-background expansion are consequently
\[
 \begin{split}
 U_{SU(3)}(a)
 &=2\hbar c\sum_{p<q}|\alpha_{pq}(a)|
 +\frac{C_M}{3\pi^2}\hbar cL\sum_{p<q}|\alpha_{pq}(a)|^2
 +O(\hbar cL^2|a|^3),                                      \tag{12}\\
 &=2\hbar c\sum_{p<q}|\alpha_{pq}(a)|
 +\frac{C_M}{2\pi^2}\hbar cL\sum_{i=1}^3\|a_i\|^2
 +O(\hbar cL^2|a|^3).                                      \tag{13}
 \end{split}
\]
For the second equality, at each spatial index
\[
 \sum_{p<q}(\lambda_p-\lambda_q)^2
 =3\sum_p\lambda_p^2=\frac32\|a_i\|^2.                    \tag{14}
\]
The first term in (12) has a direct C133 interpretation.  Choose, for
example, only $a_1$ nonzero.  For every positive root there are two real
root-plane components in each of $A_2,A_3$, hence four real transverse
oscillators of frequency $c|\alpha_{pq}(a)|$ and zero-point energy
$2\hbar c|\alpha_{pq}(a)|$.  Their sum is the first term in (12), agreeing
with the root-trace transverse zero-point mechanism in the completed
compact-semisimple matrix-model proof.  This checks the normalization but
does not identify the full field-theory Hamiltonian with its zero-mode
restriction.

Set $U_{\perp,SU(3)}=U_{SU(3)}-2\hbar c\sum_{p<q}|\alpha_{pq}(a)|$.  In
C133-scaled variables $a_i=g^{2/3}\xi_i/L$, (13) gives
\[
 U_{\perp,SU(3)}=
 \frac{C_M}{2\pi^2}\,g^{4/3}\frac{\hbar c}{L}
 \sum_i\|\xi_i\|^2+O\!\left(g^2\frac{\hbar c}{L}|\xi|^3\right). \tag{15}
\]
It is thus smaller by $g^{2/3}$ than a $g^{2/3}\hbar c/L$ zero-mode
energy in the region $L|a|\ll1$.  This is the exact one-loop **size** and
root structure which an $SU(3)$ fibrewise Schur estimate would have to
use.  It is not such an estimate: the expansion is local, while the
negative $C_M$ quadratic correction cannot by itself control the global
periodic potential or off-diagonal Feshbach terms.

Since every summand in (11) is nonnegative, $U_{SU(3)}\ge0$.  Its zeros
are exactly the Cartan holonomies satisfying
$L\alpha_{pq}(a)\in2\pi\mathbb Z^3$ for every $p<q$; equivalently,
$\exp(iLa_i)$ is in the centre $Z_3$ for each spatial direction.  The
potential has three centre choices per direction in the fundamental
holonomy description.  Its global bound is
\[
 0\le U_{SU(3)}(a)\le
 \frac{6\hbar c}{\pi^2L}\max\Phi=O(\hbar c/L).             \tag{16}
\]

## 4. Saturation and the centre-degenerate minima

For $SU(2)$, $U(a)\le2\hbar c\max\Phi/(\pi^2L)=O(\hbar c/L)$ for all $a$,
while the $k=0$ term $2\hbar c|a|$ alone grows without bound.  Equation
(16) gives the corresponding statement for $SU(3)$.  The linear
confinement of the constant modes along an abelian valley, which in C133
holds for all $|a|$, is in the torus theory only the small-$La$ regime of a
bounded periodic function.  The $SU(2)$ minima lie at
$La\in2\pi\mathbb Z^3$: $La=2\pi e_i$ corresponds to the fundamental
holonomy $\exp(2\pi iT^3)=-1$, a centre element, trivial on adjoint fields
but a distinct state.  The $SU(3)$ statement is the $Z_3$ version after
(16).  Such degenerate minima are connected by tunnelling through a
valley barrier of height $O(\hbar c/L)$, producing the splittings between
small-volume 't Hooft electric-flux sectors (van Baal's programme; not
derived here).

Consequence for a weak-coupling small-volume expansion: the zero-mode
ground state has width $La\sim g^{2/3}$ and energy
$g^{2/3}\hbar c/L$, far below the valley saturation scale $\hbar c/L$ and
the tunnelling barrier.  The C133 picture therefore gives the leading
local mechanism and the one-loop corrections enter at relative order
$g^{2/3}$.  It does not follow that a full Feshbach reduction is exact:
the relative Schur estimate and the control of backgrounds away from the
Cartan patch remain additional hypotheses.  The regime where the
zero-mode energy reaches $\hbar c/L$, $g(L)^{2/3}\sim1$, is where the
holonomy delocalizes over the whole compact valley, the flux sectors
become degenerate and the description changes character: the crossover
$z\simeq2$ of Lüscher--Münster in this language.

## 5. Consequence for STATE

The one-loop input along a Cartan valley is now explicit for both groups:
for $SU(2)$,
$U_\perp=\frac{C_M}{3\pi^2}\hbar cL|a|^2+O(\hbar cL^2|a|^3)$; for $SU(3)$,
(15) gives
$U_{\perp,SU(3)}=\frac{C_M}{2\pi^2}g^{4/3}(\hbar c/L)\sum_i\|\xi_i\|^2+O(g^2\hbar c|\xi|^3/L)$.
Both full potentials are periodic, bounded by $O(\hbar c/L)$, and have
centre-degenerate minima.  The $SU(3)$ formula is a genuine extension of
the Cartan one-loop calculation and matches C133's root-trace linear
term exactly.

It is **not** the relative form/Schur estimate (H3) in the
[weak-coupling Feshbach programme](weak-coupling-feshbach-reduction.md).
A local negative quadratic Taylor coefficient is not a global relative
bound on the fibre Hamiltonian; one must still control the fibrewise
projection, off-diagonal Schur term, non-Cartan backgrounds, and a
periodic gauge-invariant regulator.  Compact $U(1)$ has no valley
potential at all, which remains the small-volume form of the
abelian/non-abelian distinction.
