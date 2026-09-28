# The SU(2) mid-plane on its small-field set: bounds and the missing comparison

**After refereeing (GPT-6 Astra, 2026-09-28).** Claim-by-claim review of
Claude's derivation: **A1 ACCEPT** (with the inverse notation corrected);
**A2 REFINE** (complete image pairing, explicit constants, endpoint range,
and the distinction between a bridge and the interacting measure);
**A3 REFINE** (local convexity survives with corrected midpoint curvature
and defined derivative constants); **A4 REJECT** (Proposition 4 is false
under Hypothesis I, already along a flat-holonomy path; its covariance,
gauge comparison and Taylor estimates also have missing premises);
**A5 REFINE** (the Peierls arithmetic survives with corrected curvature
constant; the logarithmic size condition remains conditional). The
accepted results are Lemmas 1--2 and the corrected local Lemma 3 below.
The normalized small-field comparison remains open. The original proof
and its attribution are preserved in git history.

Take one halving of direction 1 in $1+2$ dimensions, with gauge group
$SU(2)$, heat time $t=\lambda_3a=\hbar g_{\rm cl}^2a$, and

$$\varepsilon=t^{1/2-\delta},\qquad \eta=2\varepsilon,
\qquad 0<\delta<1/6.$$

All operator norms below use the Euclidean norm on the three real colour
components, $[T_a,T_b]=\epsilon_{abc}T_c$, $|T_a|=1$. Distances on $SU(2)$
use the three-sphere of radius 2; Haar measure has total mass one.
Inputs read at passage level: [series/parallel](series-parallel-gauge-refinement.md),
Proposition 1, Hypothesis P($\alpha$), Proposition 7;
[mid-plane order $t$](su2-midplane-order-t.md), §§1 and 7, especially
(16)--(18); [exact midpoint](su2-midpoint-exact.md), Theorem 1 and its
image formula. This note concerns one finite mid-plane and bounds
uniform in its area where explicitly stated.

## 1. Setting and the restriction

There are $N$ sites, $2N$ edges and $N$ faces on the periodic mid-plane.
Use periods at least three to avoid repeated boundary incidences. In the
mid-vertex gauge of Proposition 1 set $m_e=m_{*e}\exp\xi_e$, with $m_{*e}$
the shortest-geodesic midpoint between $P_e$ and $Q_e^{-1}$. Their distance
is $|X_e|\le\varepsilon$. Up to constants independent of $\xi$, the exponent is

$$S(\xi;U)=\frac1t\sum_e\left[d(P_e,m_e)^2+d(m_e,Q_e^{-1})^2
-\frac12|X_e|^2\right]
+\frac1{4t}\sum_g|\log m_{\partial g}|^2+J(\xi;U).\tag{1}$$

Here $J$ contains the full heat-kernel and Haar amplitudes. Its local
$\xi$ derivatives are bounded uniformly on a fixed chart away from the
cut locus. Constants in $J$, including its bridge value at $\xi=0$,
can be transferred to the external normalization; only the bridge's
squared-distance term necessarily vanishes there. Count each bridge
denominator once, either in $S$ or outside the integral. Include the
old-face ratios in the external normalization $B(U)$.

Keep Claude's soft-barrier definition explicit:

$$W_\eta(\xi)=\sum_e w_\eta(|\xi_e|),\qquad
\mu_U(d\xi)=Z_s(U)^{-1}e^{-S(\xi;U)-W_\eta(\xi)}d\xi,
\qquad \mathcal D_s=-\log Z_s+B(U).\tag{2}$$

The domain is $\prod_e B(0,c_0)$; $w_\eta$ is $C^2$, convex and radial,
vanishes for $r\le\eta$, and diverges at $c_0$. Choose its boundary decay
so that the integrations by parts used below have vanishing boundary
terms and finite Fisher information. It is fixed independently of $U$
in these midpoint coordinates. Its support extends beyond
$\Omega_\eta=\{\max_e|\xi_e|\le\eta\}$. A hard restriction to
$\Omega_\eta$ defines a different partition function. Both choices are
convex restrictions, but their covariance lower bounds need different
boundary arguments.

The interacting law includes every mid-face weight. Lemma 2 bounds the
single-edge bridge before these weights are inserted. Transferring that
tail bound to (2), bounding the probability that any of $2N$ edges is
large, and comparing the two partition functions are additional tasks.
Even for independent bridges the union bound carries a factor $2N$.

## 2. Lemma 1: covariant inverse decay (A1 ACCEPT)

Let $C_A$ be the oriented face-edge incidence operator with each entry
an adjoint rotation of the background connection. Set
$H_A=4I+\frac12C_A^*C_A$. For every background,

$$4I\le H_A\le8I.\tag{3}$$

If $K=H_A+E$, $E=E^*$ has range one in the graph of edges sharing a
face, and $\|E\|\le\kappa<4$, then, writing $d=d(e,e')$,

$$\|(K^{-1})_{ee'}\|\le\frac1{4-\kappa}
\left(\frac{2+\kappa}{6}\right)^d.\tag{4}$$

In particular the original range $\kappa<2$ is valid, and at $\kappa=0$
the bound is $\frac14 3^{-d}$. Here $K$ denotes the perturbed Hessian;
$K^{-1}$ denotes its inverse.

*Proof.* For each face,
$|(C_A\xi)_g|^2\le4\sum_{e\in\partial g}|\xi_e|^2$. Each edge belongs
to two faces, so $\|C_A\xi\|^2\le8\|\xi\|^2$. Thus
$\|K-6I\|\le2+\kappa<6$. The $n$th power of $K-6I$ has zero
$(e,e')$ block for $n<d$, and each remaining block has norm at most
$(2+\kappa)^n$. Sum the Neumann series about $6I$ to obtain (4).
The count of faces per edge makes every constant independent of $N$.
$\square$

This is a bound on the sum of operator products at a given order.
It supplies no bound of $3^{-L}$ for each individual path with the same
constant after absolute path counting.

## 3. Lemma 2: heat kernel and bridge tail (A2 REFINE)

For $0<t\le1$ and $0\le\theta\le2\pi$,

$$k_t(\theta)\le C_+t^{-5/2}e^{-\theta^2/(2t)};\qquad
k_t(\theta)\ge c_-t^{-3/2}e^{-\theta^2/(2t)}
\quad(0\le\theta\le1).\tag{5}$$

Here are explicit, deliberately loose constants. Put $a_n=4\pi n$,
$b_n=(4n+2)\pi$, and

$$\begin{aligned}
A_0&=\pi\left[1+2\sum_{n\ge1}(1+(a_n+\pi)^2)
 e^{-(a_n^2-2\pi a_n)/2}\right],\\
A_1&=2\pi\sum_{n\ge0}(1+(b_n+\pi)^2)
 e^{-b_n(b_n-2\pi)/2},\\
C_+&=e^{1/8}\sqrt{8\pi}\max(A_0,A_1),\qquad c_-=\sqrt{8\pi}.
\end{aligned}\tag{6}$$

*Written image check.* Write $f_t(u)=u e^{-u^2/(2t)}$. The exact image
formula is

$$k_t(\theta)=e^{t/8}\sqrt{8\pi}\,t^{-3/2}
\frac{\sum_{w\in\mathbb Z}f_t(\theta-4\pi w)}{\sin(\theta/2)}.$$

On $[0,\pi]$, pair $w=\pm n$. Their sum is
$f_t(a_n+\theta)-f_t(a_n-\theta)$, which vanishes at zero. Since
$|f'_t(u)|\le(1+u^2/t)e^{-u^2/(2t)}$, its absolute value is at most

$$2\theta(1+(a_n+\pi)^2/t)e^{-(a_n-\theta)^2/(2t)}.$$

Use $\theta/\sin(\theta/2)\le\pi$ and
$a_n^2-2a_n\theta\ge a_n^2-2\pi a_n$ to obtain the $A_0/t$ bound
on the image quotient after extracting $e^{-\theta^2/(2t)}$.

On $[\pi,2\pi]$, set $\psi=2\pi-\theta\in[0,\pi]$. Pair **all**
images as $w=-n$ and $w=n+1$, $n\ge0$. Each pair is
$f_t(b_n-\psi)-f_t(b_n+\psi)$ and has magnitude at most

$$2\psi(1+(b_n+\pi)^2/t)e^{-(b_n-\psi)^2/(2t)}.$$

Divide by $\sin(\psi/2)\ge\psi/\pi$ and use
$(b_n-\psi)^2-(2\pi-\psi)^2\ge b_n(b_n-2\pi)$.
This gives $A_1/t$, including the antipodal limit $\psi=0$.
In particular the leading pair is

$$e^{-(4\pi^2+\psi^2)/(2t)}
[(2\pi-\psi)e^{2\pi\psi/t}-(2\pi+\psi)e^{-2\pi\psi/t}],$$

as in Claude's calculation. Pairing the remaining images too removes
the apparent singularity from division by $\sin(\psi/2)$.

For $\theta\le1$, the absolute remainder relative to
$\theta e^{-\theta^2/(2t)}$ is bounded by

$$2\sum_{n\ge1}(1+(a_n+1)^2/t)e^{-(a_n^2-2a_n)/(2t)}<\frac12.$$

For completeness, $3<\pi<4$ bounds this sum by
$2\sum_{n\ge1}(1+289n^2)e^{-56n^2}<1/2$; use
$t^{-1}e^{-b/t}\le e^{-b}$ for $b\ge1$, $t\le1$, followed by
$n^2\le4^n$, $e^{56}>2^{56}$ and a geometric series.
Together with $\theta/\sin(\theta/2)\ge2$ this proves the lower bound
with (6), also at zero by continuity. $\square$

**Bridge conclusion.** Assume $|X|\le1$, $r\ge|X|/2$, and $0<t\le1$.
For the normalized bridge of duration $t$,

$$\beta\{d(m,m_*)\ge r\}
\le \min\left(1,C_2t^{-7/2}e^{-2r(r-|X|)/t}\right),
\qquad C_2=32C_+^2/c_-.\tag{7}$$

Indeed at distance $\rho\ge r$ both endpoint distances are at least
$\rho-|X|/2\ge0$. The two upper bounds at time $t/2$ divided by the
lower bound at time $t$ give the density bound with exponent
$-[2(\rho-|X|/2)^2-|X|^2/2]/t=-2\rho(\rho-|X|)/t$.
This exponent decreases with $\rho$ for $\rho\ge|X|/2$; integrate
against Haar measure of mass one. At $r=\eta=2\varepsilon$ and
$|X|\le\varepsilon\le1$ the gain is $e^{-4\varepsilon^2/t}$.
This proof uses the two endpoint triangle inequalities through $m_*$.

## 4. Lemma 3: a corrected local convexity theorem (A3 REFINE)

The midpoint background face logarithm $Y_g=\log(m_{*\partial g})$
obeys $|Y_g|\le3\varepsilon$. To see this, compare its four edges to
those of the transported lower layer. Each midpoint changes its edge
by distance at most $\varepsilon/2$, and the lower-layer plaquette has
distance at most $\varepsilon$. Bi-invariance and the product triangle
inequality give $\varepsilon+4\varepsilon/2=3\varepsilon$.
The bound $\varepsilon$ in the original sketch needs an extra premise.
Individual background links can be large; transport them out of each
local product before taking logarithms.

Here is a precise version of the local estimate, with constants defined
by fixed-dimensional derivatives rather than unquantified BCH symbols.
Fix $r_0=1/16$. On $|b|,|z|\le r_0$ define

$$B(b,z)=d(e,e^{-b/2}e^z)^2+d(e,e^{b/2}e^z)^2-|b|^2/2,$$

and on $|y|,|z_i|\le r_0$ define

$$F(y,z_1,\ldots,z_4)=\frac14
\left|\log(e^ye^{z_1}\cdots e^{z_4})\right|^2.$$

All these products lie in a fixed injectivity chart. Let $L_B$ be the
supremum of the derivative of $D_z^2B$ with respect to $(b,z)$, using
the sum norm on the input blocks and operator norm on the output.
Let $L_F$ be the analogous supremum of the derivative of
$D_{(z_1,\ldots,z_4)}^2F$. These are finite constants on the indicated
compact sets. At the origin these Hessians are $4I$ and the block
matrix with every block $I/2$, respectively.

Let $J_B,J_F$ be supremum norms of the edge and face Hessians of the
corresponding local heat-kernel/Haar log amplitudes for $0<t\le1/2$
on the same charts; omit terms independent of $\xi$. They are finite:
the zero-image Jacobian factors are analytic on these compact sets,
and each differentiated nonzero image has a polynomial in $1/t$
times $e^{-c/t}$ with $c>0$. The positive zero-image quotient bounds
the logarithm's denominator away from zero for small $t$; positivity
and compactness handle the remaining closed time interval. Define

$$J_* = J_B+2J_F,\qquad C_3=L_B+8L_F+J_* .\tag{8}$$

These supremum definitions fix the constants independently of the plane;
a numerical value is unnecessary for the following explicit condition.
For $3\varepsilon\le r_0$, $\rho=|\xi|_\infty\le r_0$,
$0<t\le\min(1/2,\varepsilon)$, the **unbarriered** action satisfies

$$\|t\,\nabla_\xi^2S-H_A\|
\le L_B(\varepsilon+\rho)+2L_F(3\varepsilon+4\rho)+tJ_*
\le C_3(\varepsilon+\rho).\tag{9}$$

Here $C_A$ uses the signed adjoint transports in the ordered background
face products. At each face the four rotations are isometries. Applying
the mean value theorem to the two Hessians just defined gives the local
bounds; summing face quadratic forms costs a factor two because every
edge belongs to two faces. This proves (9) directly and supplies the
derivative control missing from the BCH sketch.

Choose $c_0\le r_0$ with $C_3(\varepsilon+c_0)<4$, and $2\varepsilon<c_0$.
Then $S$ is uniformly convex on the product of balls of radius $c_0$;
$S+W_\eta$ has the same lower Hessian bound. On $\Omega_\eta$ the
unbarriered error is at most $3C_3\varepsilon$.
The soft measure (2) has the weaker pointwise error
$C_3(\varepsilon+c_0)$ on its full support. Its barrier Hessian can be
arbitrarily large. These distinctions matter in §5.

## 5. Proposition 4: verdicts and the corrected conditional implication

The original Hypothesis I asked for a $C^2$ path $U(s)$ from $1$ to $U$
with $|X_p(s)|\le2\varepsilon$,

$$\sum_p|\dot X_p(s)|^2\le C_I\sum_p|X_p(1)|^2,\qquad
|\ddot X_p(s)|\le C_I\sum_{p'\sim p}|X_{p'}(1)|^2.\tag{10}$$

**A4 overall: REJECT, with a counterexample.** On a fixed periodic plane
choose identical adjacent flat layers with commuting holonomies
$e^{s\theta_2T_3},e^{s\theta_3T_3}$. Constant links
$e^{s\theta_jT_3/N_j}$ realize the path. Every plaquette flux, flux
velocity and flux acceleration is zero, so (10) holds. Nevertheless,
the fixed-volume Laplace calculation in (16)--(17) of the
[mid-plane note](su2-midplane-order-t.md) gives

$$\mathcal D_s(U_\theta,t)-\mathcal D_s(1,t)
=\Omega_N(\theta)+o_N(1),\qquad
\Omega_N(\theta)>0\quad\hbox{for a nontrivial adjoint holonomy}.\tag{11}$$

The same leading term holds for (2): the barrier equals zero in a ball
of radius $\eta$, and $\eta/\sqrt t=2t^{-\delta}\to\infty$; rescaling
by $\sqrt t$ recovers the full Gaussian determinant at fixed $N$.
Uniform convexity about this zero-flux saddle controls the discarded
tail at fixed $N$. The proposed right-hand side
$C\varepsilon\sum_p|X_p|^2/t$ is exactly zero. Hypothesis I therefore
allows data contradicting the claimed theorem. A winding term or an
additive volume remainder must be included, with its own estimate.
The actual P($\alpha$) allows $Ct^\alpha\sum_p1$ and a size clause;
those features distinguish it from the rejected stronger assertion.

**A4(a), linear term: ACCEPT in a smooth local chart at $1$.** Global
conjugation rotates every Lie-algebra link tangent by the adjoint
representation. Its invariant covectors vanish, so the first derivative
of the gauge-invariant partition function at $1$ is zero. The same
argument works for independent flux coordinates if such a chart has
been supplied. Plaquette logarithms alone omit torus holonomies and
satisfy compatibility constraints; writing a global $\nabla_X$ requires
additional coordinates. Gauge invariance permits the quadratic flat
holonomy response (11).

**A4(b), differentiation: ACCEPT with its domain hypotheses.** For a
fixed coordinate domain and a $U$-independent barrier, differentiating
under the finite integral gives, for any boundary coordinates $u_i$,

$$\partial_i\partial_j\mathcal D_s
=E[S_{ij}]-\operatorname{Cov}(S_i,S_j)+B_{ij}.\tag{12}$$

Uniform local domination justifies differentiation. A moving hard
boundary needs boundary terms, unless it is first represented in a
fixed domain. Equation (12) alone provides no local, independent flux
coordinates with plane-uniform derivative bounds.

**A4(b), covariance upper bound: REFINE.** Put $V=S+W_\eta$ and let
$\kappa$ bound the unbarriered Hessian error on the **whole support**.
The Brascamp--Lieb inequality gives

$$\operatorname{Cov}_\mu(\xi)
\le E[(\nabla^2 V)^{-1}]\le t(H_A-\kappa I)^{-1}.\tag{13}$$

Convex barriers preserve this upper bound. For a hard convex restriction
one can obtain it by convex approximation. In (2) the available choice
is $\kappa=C_3(\varepsilon+c_0)$; replacing it by
$3C_3\varepsilon$ requires controlling the exterior region.

**A4(b), covariance lower bound: REJECT as used.** With the stated
integration-by-parts hypotheses, the score identity and matrix
Cauchy--Schwarz give

$$\operatorname{Cov}_\mu(\xi)\ge
\bigl(E[\nabla^2 V]\bigr)^{-1},\qquad
E[\nabla V\nabla V^T]=E[\nabla^2 V].\tag{14}$$

The right-hand side contains $E[\nabla^2W_\eta]$. Its sign increases the
Fisher information and decreases this lower bound. Discarding it has
the wrong direction for the asserted lower estimate. A tail probability
alone bounds neither an unbounded barrier Hessian nor the Fisher
information. Hard truncation produces boundary terms; already a
one-dimensional centred Gaussian truncated to a finite symmetric
interval has variance strictly smaller than its untruncated variance.
To recover a two-sided comparison one needs, for example,

$$\|tE[\nabla^2S]-H_A\|\le\kappa,\qquad
 t\|E[\nabla^2W_\eta]\|\le b,\tag{15}$$

in addition to the pointwise lower bound in (13). These give the
conditional estimate

$$\|\operatorname{Cov}_\mu(\xi)-tH_A^{-1}\|
\le\max\left\{\frac{t\kappa}{4(4-\kappa)},
\frac{t(\kappa+b)}{4(4+\kappa+b)}\right\}.\tag{16}$$

It follows by inversion of the Loewner bounds and $H_A\ge4I$.
The original proof established neither (15) with $b=O(\varepsilon)$
nor the required interacting tail estimate. The displayed
Brascamp--Lieb inequality is the standard input
([Brascamp--Lieb 1976](https://doi.org/10.1016/0022-1236(76)90004-5),
metadata); (14)--(16) follow by the written score calculation above.

**A4(b), covariant-to-abelian comparison: REJECT as justified.** The
kernel $M_AH_A^{-1}M_A^T$ carries adjoint transport between distinct
face frames. Gauge transformations act independently at these frames;
comparison with a fixed abelian matrix needs specified identifications.
Only traced closed products are gauge invariant by themselves.
Even for a closed product, curvature bounds control contractible loops;
a winding loop can have nontrivial holonomy with every $X_p=0$.
Finally (4) controls the total operator power, whereas taking absolute
values path by path loses its cancellations and introduces path
multiplicity. The proposed $\sum_L L^2 3^{-L}$ argument omitted all
three issues. Needed: a gauge-covariant bulk kernel comparison with
summable spatial moments, and a separate winding remainder.

**A4(b), nonlinear score remainder: REFINE.** If local derivatives
actually satisfy
$E|\nabla_\xi\langle v,R\rangle|^2\le
C(\varepsilon+\eta)^2\|v\|^2/t^2$ on a support with curvature error
$\kappa$, then (13) implies
$\operatorname{Var}\langle v,R\rangle\le
C(\varepsilon+\eta)^2\|v\|^2/[t(4-\kappa)]$.
Cauchy--Schwarz bounds the cross covariance. The Taylor bound on $R$
requires its derivative version and a controlled boundary chart; its
value bound alone supplies neither.

**A4(c), Taylor step: REFINE.** A precise surviving implication is as
follows. Suppose that winding has been separated, a genuine $C^2$
coordinate path $X(s)$ satisfies (10), and
$h=\mathcal D_s-\mathcal D_0-W_N$ is a function of those coordinates.
Assume $X(0)=0$, $\nabla h(0)=0$, and along the path

$$\|\nabla^2h\|\le A\varepsilon/t,\qquad
\sup_p|\nabla_ph|\le B\varepsilon/t.\tag{17}$$

Let $q_I$ bound the number of $p$ for which a fixed $p'$ appears in
$p'\sim p$. The exact chain rule and Taylor's integral formula give

$$|h(X(1))-h(0)|\le
\frac{C_I}{2}(A+Bq_I)\frac{\varepsilon}{t}
\sum_p|X_p(1)|^2.\tag{18}$$

Indeed the Hessian term integrates to at most
$AC_I\varepsilon\|X(1)\|^2/(2t)$ and the gradient-acceleration term
to at most $BC_Iq_I\varepsilon\|X(1)\|^2/(2t)$.
An operator norm estimate alone gives an $\ell^2$ gradient bound;
it does not imply the per-plaquette bound in (17). A uniformly summable
kernel estimate would supply that missing norm. For abelian data the
linear flux path is available only in a compatible coordinate sector
with the harmonic data fixed. All constants in (18) are explicit in
the supplied hypotheses; proving them uniformly in the plane is still
part of the problem.

## 6. What stays open for the weak (18) of the mid-plane note (A5 REFINE)

(a) **Small-field comparison.** The tasks include barrier moment control,
a background-covariant local response estimate, independent admissible
coordinates or a replacement for the global path, and winding control.
The original list of only Hypothesis I and large fields was incomplete.
The formal order-$t$ coefficients retain their status as formal
coefficients; this review supplies no normalized remainder for them.

(b) **Large fields: the failed naive Peierls arithmetic is accepted.**
Using the extra premise $|Y_g|\le\varepsilon$, the face loss at
$|\xi_e|\le2\varepsilon$ is
$\exp[-(\varepsilon+8\varepsilon)^2/(4t)]
=e^{-81\varepsilon^2/(4t)}$ per affected face, against bridge gain
$e^{-4\varepsilon^2/t}$ per large edge. Since an edge touches two faces,
the crude worst-case loss is $81\varepsilon^2/(2t)$ per edge and the
net exponent is $+(73/2)\varepsilon^2/t$. The comparison grows rather
than decays. With only the coarse small-field assumption, §4 gives
$|Y_g|\le3\varepsilon$; replace 81 by 121 and $73/2$ by $113/2$.
These are bounds on the exponential part; heat-kernel prefactors add
powers of $t$, which cannot repair the wrong sign as
$\varepsilon^2/t=t^{-2\delta}\to\infty$. Shared faces can reduce the
loss for particular sets; the crude bound suffices to expose failure
of the proposed uniform argument. A normalized connected-set or
other large-field estimate is still required. The soft barrier also
needs comparison with a genuine small-field partition function.

(c) **Logarithmic size: conditional, with the rate corrected.** For
flat Gaussian backgrounds the explicit walk count (17) in the
[mid-plane note](su2-midplane-order-t.md) proves
$0\le\Omega_N\le(3N/n_*)3^{-n_*}$, $n_*=\min(N_2,N_3)$.
More generally, if a winding estimate

$$|W_N|\le C e^{-\gamma n_*}\sum_p(1+|X_p|^2/t)\tag{19}$$

has been proved with $\gamma>0$ independent of $N,t$, then
$n_*\ge(\alpha/\gamma)\log(1/t)+C_0$ suffices for P($\alpha$),
with the constant multiplied by $e^{-\gamma C_0}$. A decay factor
$q=(2+\kappa)/6$ would give $\gamma=\log(6/(2+\kappa))$;
$\log3$ is the value at $\kappa=0$. With fixed positive $\kappa$
one must use the smaller rate. If $\kappa=O(\varepsilon)$, the
$\log3$ leading coefficient can be recovered with a bounded correction
because $\varepsilon\log(1/t)\to0$. Polynomial prefactors in $n_*$
need absorption into a slightly smaller rate or a $\log\log(1/t)$
correction. Lemma 1 alone proves (4); a winding estimate for the
normalized interacting free energy still requires a separate argument.

## 7. Consequence for STATE

Atlas cell 2 keeps its formal order-$t$ calculation. Round 8 Part A
accepts the covariant decay and corrected bridge/convexity bounds,
rejects Proposition 4 as stated, and replaces its Taylor step by the
explicit conditional implication (17)--(18). The next small-field task
is the normalized, gauge-covariant response estimate with barrier and
winding control; the large-field and iteration obligations remain.
