# The SU(2) bridge midpoint in closed form: the curvature term is exact

**Result, 2026-09-27.** Proposition 6 of the
[series/parallel note](series-parallel-gauge-refinement.md) described the
midpoint of the Brownian bridge on $SU(2)$, the building block of the
non-abelian parallel insertion, only to leading order in the heat time,
with the curvature factor $1/h$, $h=(d/4)\cot(d/4)$, derived by Laplace's
method and labelled as asymptotics. For the fundamental character the
midpoint expectation is computable exactly. For a bridge of duration $t$
from $e$ to a group element at geodesic distance $\theta\in[0,2\pi)$,

$$E\,\chi_{1/2}(m)=e^{-t/32}\Bigl[2\cos\frac\theta4-\frac t{2\theta}\,
\sin\frac\theta4\Bigr]\ \ \text{up to image terms of relative size}\
\Bigl(2+\frac{32\pi^2}t\Bigr)e^{-4\pi(2\pi-\theta)/t}$$

(Theorem 1). Expanded to first order it is exactly the prediction of
Proposition 6(b),
$2\cos\frac\theta4\,[1-\frac t{32}(1+\frac2{h(\theta)})]$, because
$\frac t{32}\cdot\frac2h=\frac t{4\theta}\tan\frac\theta4$. So the curvature
term N2, the side-flux-dependent softening of the mid-face weight, is
confirmed with no remainder of order $t^2$ in the $w=0$ sector: the only
correction to the displayed formula is the exponentially small winding
of the bridge around the group. This is the first exact non-abelian
statement about the parallel insertion in three dimensions, and it
settles the fundamental-representation part of the uniform Laplace
remainder that Proposition 7 of the series/parallel note assumes.

The ingredients are character orthogonality and Poisson summation; the
computation is elementary and no novelty is claimed for it.

## 1. Setting

Group metric as in the series/parallel note §1: $C_2(j)=j(j+1)$,
$SU(2)$ the three-sphere of radius 2, heat kernel
$k_t=\sum_j(2j+1)e^{-tj(j+1)/2}\chi_j$ with
$\chi_j(\theta)=\sin((2j+1)\theta/2)/\sin(\theta/2)$ at rotation angle
$\theta$ (the geodesic distance from $e$). The midpoint $m$ of the bridge of
duration $t$ from $e$ to $g$ has density
$k_{t/2}(m)\,k_{t/2}(m^{-1}g)/k_t(g)$ with respect to Haar measure. Its
geodesic midpoint $m_*=\exp(\frac12\log g)$ has rotation angle $\theta/2$,
so $\chi_{1/2}(m_*)=\sin(\theta/2)/\sin(\theta/4)=2\cos(\theta/4)$.

## 2. The exact formula

**Theorem 1.** Put
$\Theta_\pm(\theta)=\sum_{w\in\mathbb Z}(\pm1)^w e^{-(\theta-4\pi w)^2/(2t)}$ and
$\Xi_\pm(\theta)=\sum_{w\in\mathbb Z}(\pm1)^w(\theta-4\pi w)
e^{-(\theta-4\pi w)^2/(2t)}$. For $\theta\in(0,2\pi)$,

$$E\,\chi_{1/2}(m)=e^{-t/32}\,
\frac{2\cos(\theta/4)\,\Xi_-(\theta)-\frac t2\sin(\theta/4)\,\Theta_-(\theta)}
{\Xi_+(\theta)}. \tag{1}$$

Keeping only $w=0$ gives the displayed formula of the summary.

*Proof.* Expand both heat kernels in characters. Character
orthogonality in the form
$\int\chi_a(m)\chi_b(m^{-1}g)\,dm=\delta_{ab}\chi_a(g)/d_a$, together with
$\chi_{j_1}\chi_{1/2}=\chi_{j_1+1/2}+\chi_{j_1-1/2}$, gives

$$k_t(g)\,E\,\chi_{1/2}(m)=\sum_{j_1}\ \sum_{j_2=j_1\pm1/2}(2j_1+1)\,
e^{-t[C_2(j_1)+C_2(j_2)]/4}\,\chi_{j_2}(g).$$

Write $n=2j_1+1$. Then $C_2(j_1)+C_2(j_2)=\frac14[n^2+(n\pm1)^2-2]
=\frac12(n\pm\frac12)^2-\frac38$, so the exponential is
$e^{3t/32}e^{-t(n\pm1/2)^2/8}$. Multiply by $\sin(\theta/2)$, reindex the
$j_2=j_1-\frac12$ sum by $n\mapsto n+1$, and write $s=n+\frac12$ over
$s\in\frac12+\mathbb N$: the summand becomes
$(s-\frac12)\sin\frac{(s+\frac12)\theta}2+(s+\frac12)\sin\frac{(s-\frac12)\theta}2
=2s\cos\frac\theta4\sin\frac{s\theta}2-\sin\frac\theta4\cos\frac{s\theta}2$,
which is even in $s$. Hence

$$k_t(g)\sin\frac\theta2\;E\,\chi_{1/2}(m)=\frac{e^{3t/32}}2
\Bigl[2\cos\frac\theta4\,A-\sin\frac\theta4\,B\Bigr],$$

with $B=\sum_{s\in\frac12+\mathbb Z}e^{-ts^2/8}\cos\frac{s\theta}2$ and
$A=\sum_{s\in\frac12+\mathbb Z}s\,e^{-ts^2/8}\sin\frac{s\theta}2=-2\partial_\theta B$.
In the same way
$k_t(g)\sin\frac\theta2=\frac{e^{t/8}}2A_0$ with
$A_0=\sum_{n\in\mathbb Z}n\,e^{-tn^2/8}\sin\frac{n\theta}2$. Poisson summation
over the half-integers (which introduces the sign $(-1)^w$) and over the
integers gives
$B=\sqrt{8\pi/t}\,\Theta_-$, $A=(2/t)\sqrt{8\pi/t}\,\Xi_-$ and
$A_0=(2/t)\sqrt{8\pi/t}\,\Xi_+$. Divide. $\square$

**The image terms.** For $\theta\in(0,2\pi)$ the pair $w=\pm1$ in $\Xi_\pm$
has, relative to the $w=0$ term $\theta e^{-\theta^2/(2t)}$, the size
$e^{-8\pi^2/t}\,|2\theta\cosh(4\pi\theta/t)\mp8\pi\sinh(4\pi\theta/t)|/\theta
\le(2+32\pi^2/t)\,e^{-4\pi(2\pi-\theta)/t}$, using
$\sinh x\le x\cosh x$. In $\Theta_-$ the same pair has relative size at most
$2e^{-4\pi(2\pi-\theta)/t}$. The pairs $|w|\ge2$ are smaller by a further
factor $e^{-16\pi^2/t}$ up to polynomial factors. This is the large-field
term N4, the winding of the bridge around the group, and it is
negligible uniformly on $\theta\le\theta_0<2\pi$.

## 3. Comparison with Proposition 6

Proposition 6(b) predicts that $m=m_*e^\xi$ with $\xi$ Gaussian of mean zero
and covariance $\frac t4{\rm diag}(1,\frac1h,\frac1h)$ in the frame (axis,
transverse). In the spin-$\frac12$ representation $(\xi\cdot T)^2=-\frac14|\xi|^2$,
so $E\,D^{1/2}(e^\xi)=1-\frac18E|\xi|^2+O(t^2)=1-\frac t{32}(1+\frac2h)+O(t^2)$,
and $E\,\chi_{1/2}(m)=2\cos\frac\theta4\,[1-\frac t{32}(1+\frac2h)]+O(t^2)$.
The $w=0$ part of (1) equals
$2\cos\frac\theta4\,e^{-t/32}[1-\frac t{4\theta}\tan\frac\theta4]$, and
$\frac t{32}\cdot\frac2{h(\theta)}=\frac t{16}\cdot\frac{\tan(\theta/4)}{\theta/4}
=\frac t{4\theta}\tan\frac\theta4$. The two agree at first order, curvature
factor included. As $\theta\to0$ both give $2(1-\frac{3t}{32})$, the flat value
$E|\xi|^2=\frac{3t}4$.

Formula (1) says more than the asymptotics. In the $w=0$ sector the
fundamental character of the midpoint is the product of an isotropic
factor $e^{-t/32}$ and the exactly linear curvature correction
$1-\frac t{4\theta}\tan\frac\theta4$; there are no higher-order terms in $t$.
The correction grows as $\theta\to2\pi$, where $\tan(\theta/4)$ diverges and
the midpoint becomes bimodal, and there the image terms take over. This
is the non-abelian counterpart of the parity factor $\rho_t(\phi)$ of the
$U(1)$ cube (Proposition 3 of the series/parallel note).

## 4. Every spin

**Theorem 2.** For every spin $J$ and $\theta\in(0,2\pi)$, with $\sigma=0$ for
integer $J$ and $\sigma=\frac12$ for half-integer $J$,

$$E\,\chi_J(m)=\frac{\Xi_{(\sigma)}(\theta)}{\Xi_+(\theta)}
\sum_{k=-J}^{J}e^{-tk^2/8}\cos\frac{k\theta}2
-\frac t2\,\frac{\Theta_{(\sigma)}(\theta)}{\Xi_+(\theta)}
\sum_{k=-J}^{J}k\,e^{-tk^2/8}\sin\frac{k\theta}2,$$

where $\Xi_{(0)}=\Xi_+$, $\Theta_{(0)}=\Theta_+$, $\Xi_{(1/2)}=\Xi_-$,
$\Theta_{(1/2)}=\Theta_-$, and $k$ runs in unit steps. In the $w=0$ sector,

$$E\,\chi_J(m)=\sum_{k=-J}^{J}e^{-tk^2/8}\Bigl[\cos\frac{k\theta}2
-\frac t{2\theta}\,k\sin\frac{k\theta}2\Bigr]. \tag{2}$$

For integer $J$ the first ratio is exactly one, image terms included.

*Proof.* As for Theorem 1, now with $\chi_{j_1}\chi_J=\sum_{k=-J}^{J}\chi_{j_1+k}$.
This identity holds for every $j_1$ if $\chi_j$ is defined by
$\sin((2j+1)\theta/2)/\sin(\theta/2)$ also for $2j+1\le0$: it is the
product-to-sum formula for $\sin(n\theta/2)\sum_ke^{ik\theta}$. The
formal terms with $2j_2+1\le0$ cancel in pairs carrying the same weight,
so the sum may be taken over all $n=2j_1+1\in\mathbb Z$, halved; the
summand is even under $(n,k)\mapsto(-n,-k)$. With $n_2=n+2k$,
$C_2(j_1)+C_2(j_2)=\frac12(n+k)^2+\frac12(k^2-1)$, so the weight is
$e^{t/8}e^{-tk^2/8}e^{-ts^2/8}$ with $s=n+k\in\mathbb Z+\sigma$. Expanding
$(s-k)\sin\frac{(s+k)\theta}2$ and discarding the terms odd in $s$ leaves
$\cos\frac{k\theta}2\cdot s\sin\frac{s\theta}2-k\sin\frac{k\theta}2\cos\frac{s\theta}2$.
Summing over $s$ gives $A_\sigma$ and $B_\sigma$, Poisson summation gives
$\Xi_{(\sigma)}$ and $\Theta_{(\sigma)}$, and the factor $e^{t/8}$ cancels
against the denominator. For $J=\frac12$ this is Theorem 1. $\square$

**Agreement with Proposition 6 for every spin.** The leading term of (2)
is $\sum_k\cos(k\theta/2)=\chi_J(m_*)$, the character at the geodesic
midpoint (rotation angle $\theta/2$). The Gaussian prediction of
Proposition 6(b) at first order is
$\sum_k\cos\frac{k\theta}2\,[1-\frac t8k^2-\frac t8(J(J+1)-k^2)/h]$ with
$1/h=4\tan(\theta/4)/\theta$. The two agree iff, with $\varphi=\theta/2$,

$$\sum_kk\sin(k\varphi)=\tan\frac\varphi2\sum_k\bigl(J(J+1)-k^2\bigr)\cos(k\varphi).$$

The left side is $-\chi_J'(\varphi)$ and the sum on the right is
$J(J+1)\chi_J+\chi_J''$. The class-function Laplacian of $SU(2)$ in this
metric gives $\chi_J''+\cot(\varphi/2)\,\chi_J'=-J(J+1)\chi_J$, which is the
identity. (For $J=\frac12$ and $J=1$ it can be checked directly:
$\sin(\varphi/2)=\tan(\varphi/2)\cos(\varphi/2)$ and
$2\sin\varphi=\tan(\varphi/2)(2+2\cos\varphi)$.) So the curvature term of
Proposition 6 is exact at first order in every representation, and (2)
contains no terms of order $t^2$ beyond the Gaussian factors
$e^{-tk^2/8}$.

**What the trace does not give.** By Proposition 6(a),
$E\,D^J(m)=D^J(m_*)\Lambda^J$ with $\Lambda^J$ real diagonal in the axis basis,
and (2) fixes only $\sum_\mu e^{i\mu\theta/2}\Lambda^J_{\mu\mu}$, one equation
for $2J+1$ entries. The isolated cube needs the entries, because its four
cut faces have different axes.

## 5. The fundamental sector of the isolated cube is exact

**Theorem 3.** (a) In spin $\frac12$ the midpoint's matrix expectation is a
real multiple of a unitary: $E\,D^{1/2}(m)=\lambda(\theta,t)\,D^{1/2}(m_*)$ with

$$\lambda(\theta,t)=e^{-t/32}\,\frac{\Xi_-(\theta)-\frac t4\tan\frac\theta4\,\Theta_-(\theta)}{\Xi_+(\theta)}
\ \overset{w=0}{=}\ e^{-t/32}\Bigl[1-\frac t{4\theta}\tan\frac\theta4\Bigr],
\qquad\theta\in(0,2\pi).$$

(b) For one refined cube (series/parallel note, §4), whose four cut side
faces have heat times $t_j$ and side angles $\theta_j$, the spin-$\frac12$ term
of the character sum for $\Psi$ is exactly

$$d_{1/2}\,e^{-3t_m/8}\,{\rm tr}_{1/2}\prod_jE\,D^{1/2}(m_j^{\pm1})
=2\,e^{-3t_m/8}\Bigl(\prod_{j=1}^4\lambda(\theta_j,t_j)\Bigr)\chi_{1/2}(h_{\rm int}),$$

where $h_{\rm int}$ is the holonomy of the geodesic interpolation around the
mid-face. In this sector the interpolation term N1 is exact (it is
$h_{\rm int}$), the curvature term N2 is exact (it is $\prod\lambda$), and the
commutator term N3 vanishes.

*Proof.* (a) By Proposition 6(a) of the series/parallel note,
$E\,D^{1/2}(m)=D^{1/2}(m_*)\Lambda$ with $\Lambda={\rm diag}(\Lambda_+,\Lambda_-)$ real in
the axis basis, where $D^{1/2}(m_*)={\rm diag}(e^{i\theta/4},e^{-i\theta/4})$. Its
trace $e^{i\theta/4}\Lambda_++e^{-i\theta/4}\Lambda_-$ equals $E\,\chi_{1/2}(m)$, which is
real because the midpoint density and $\chi_{1/2}$ are real. The imaginary
part gives $\sin(\theta/4)(\Lambda_+-\Lambda_-)=0$, so $\Lambda_+=\Lambda_-=\lambda$, and
$\lambda=E\,\chi_{1/2}(m)/(2\cos(\theta/4))$ by Theorem 1. (b) The bridge for a cut
face runs from $Q_j^{-1}$ to $P_j$; left translation by $Q_j^{-1}$ maps it to a
bridge from $e$, so $E\,D^{1/2}(m_j)=\lambda_jD^{1/2}(m_{*j})$ with $m_{*j}$ the
geodesic midpoint, and $E\,D^{1/2}(m_j^{-1})=\lambda_jD^{1/2}(m_{*j})^{-1}$ because
$\lambda_j$ is real. The four midpoints are independent, since each is fixed by its own
cut face and an isolated cube has no shared mid-edges, so the trace of the product of expectations is
$\prod_j\lambda_j$ times the trace of the product of the unitaries, which is
$\chi_{1/2}(h_{\rm int})$. The prefactor is $d_{1/2}e^{-t_mC_2(1/2)/2}$ with
$C_2(\frac12)=\frac34$. $\square$

For $J\ge1$ the diagonal entries differ: the Gaussian prediction is
$\Lambda^J_{\mu\mu}\simeq1-\frac t8[\mu^2+(J(J+1)-\mu^2)/h]$, which depends on $\mu$
unless $h=1$. The reality argument gives only $\Lambda^J_{\mu\mu}=\Lambda^J_{-\mu,-\mu}$,
so for $J=1$ one equation remains for the two entries $\Lambda^1_{11}$ and
$\Lambda^1_{00}$. The matrix-element version of the orthogonality computation
of Theorem 1, with the Clebsch--Gordan coefficients of $j_1\otimes J$, is the
tool for them.

## 6. Consequence for STATE

The curvature term of the $SU(2)$ parallel insertion is now exact for
every character (Theorems 1 and 2), with only exponentially small winding
terms left, and the spin-$\frac12$ sector of the isolated cube is exact
(Theorem 3). One step remains before Proposition 7 becomes a theorem for
the isolated $SU(2)$ cube: the diagonal entries $\Lambda^J_{\mu\mu}$, $J\ge1$, of the
midpoint's matrix expectation, since the cube's character sum
$\sum_Jd_Je^{-t_mC_2(J)/2}{\rm tr}_J\prod_jE\,D^J(m_j^{\pm1})$ multiplies
matrices with different axes. They follow from the same orthogonality
method applied to matrix elements, or from the characters of the midpoint
translated along the centralizer of the side holonomy.
