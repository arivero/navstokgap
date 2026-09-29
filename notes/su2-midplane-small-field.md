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

## 7. Part B: quasi-local response and the obstruction to plaquette telescoping

**Result, GPT-6 Astra, 2026-09-28.** A covariance version of Lemma 1
gives a plane-uniform locality theorem for local perturbations of the
potential, under the explicit analytic hypotheses below. Converting
this to independent plaquette perturbations needs a further gauge
estimate. The natural uniformly bounded local right inverse of curl
already fails at the abelian linearization, as (26) proves. Thus this
step leaves Hypothesis I unreplaced; it isolates the cancellation a
successful replacement must establish.

### 7.1 Source check and scope

[Helffer--Sjöstrand (1994)](https://doi.org/10.1007/BF02186817),
*On the correlation for Kac-like models in the convex case*,
J. Stat. Phys. **74**, 349--409, treats dimension-dependent Gibbs
measures that are controlled perturbations of harmonic potentials
(reading label: **publisher metadata and abstract**; the full journal
text was behind subscription access in this check).
Helffer's [1993 author report](https://www.numdam.org/item/SEDP_1992-1993____A12_0/)
explicitly presents their joint work (reading label: **passage**, §4,
Theorem 4.2, and §5, printed pp. XII-13--17). It states exponential
correlation decay for sufficiently small coupling in a nearest-neighbour
harmonic model with a $C^3$ interaction having bounded derivatives
through order three. Section 5 explains the elliptic vector equation
and the additional weighted estimates needed for spatial decay. This
checks a concrete source scope; the general finite-range statement
needed here is proved below with its own hypotheses. The author report
also addresses thermodynamic limits. No source passage checked here
supplies gauge charts, barrier comparison or plaquette telescoping.
Bibliography entries: `HelfferSjostrand1994`, `Helffer1993Kac`.

### 7.2 A covariance theorem with the same decay constants

**After refereeing Theorem 5 (Claude, 2026-09-28).** ACCEPT. The
representation (22) is the Helffer--Sjöstrand formula; $\mathcal B\ge6I$ holds because
$L\ge0$ and the on-site Hessians are nonnegative, and $\mathcal B^{-1}$ keeps the edge
index; $\mathcal R$ is multiplication by a range-one matrix function of norm at
most $2+\kappa$; the Neumann tail gives $\frac16\sum_{n\ge d}q^n=q^d/(4-\kappa)$, and
Cauchy--Schwarz in $L^2(\mu)$ gives (21). The application to the barrier
measure is correctly left as a stated approximation condition.

**Theorem 5 (local-potential response).** Let $E$ be the finite edge
graph and $\mu\propto e^{-V}d\xi$ on $\mathbb R^{3E}$, with
$V=S+\sum_e w_e(\xi_e)$ smooth and confining, $w_e$ convex. Assume
the usual closed weighted-gradient realization, so integration by
parts and the differentiated Poisson equation hold; smooth potentials
with bounded Hessians and a uniform positive lower bound suffice.
Allow limits of such measures only when covariances and the gradient
norms appearing below converge. Suppose, everywhere on the domain,

$$\|t\nabla^2S-6I\|\le2+\kappa,
\qquad 0\le\kappa<4,\qquad
(\nabla^2S)_{ee'}=0\quad\hbox{if }d(e,e')>1.\tag{20}$$

For smooth $f,g$ with gradients supported in edge sets $R,T$, define
$a_f=\|\nabla f\|_{L^2(\mu)}$ and $a_g=\|\nabla g\|_{L^2(\mu)}$.
Then, uniformly in the graph size,

$$|\operatorname{Cov}_\mu(f,g)|
\le\frac{t}{4-\kappa}
q^{d(R,T)}a_fa_g,
\qquad q=\frac{2+\kappa}{6}<1.\tag{21}$$

The on-site convex Hessians can be large; the bound uses their sign,
without treating them as a small perturbation.

*Proof.* Write $L=-\Delta+\nabla V\cdot\nabla$, nonnegative in
$L^2(\mu)$. Uniform convexity gives a gap at least $(4-\kappa)/t$
for this auxiliary diffusion. Solve $Lu=g-Eg$ on the orthogonal
complement of constants. Differentiating gives

$$(LI+\nabla^2V)\nabla u=\nabla g,\qquad
\operatorname{Cov}(f,g)=
\langle\nabla f,(LI+\nabla^2V)^{-1}\nabla g\rangle_{L^2(\mu)}.\tag{22}$$

The first equality is the commutator identity
$\nabla Lu=(LI+\nabla^2V)\nabla u$; the second follows by integration
by parts in $\langle f-Ef,Lu\rangle$. This is the covariance
representation motivating the Helffer--Sjöstrand method.

On the vector Hilbert space set

$$\mathcal B=tLI+6I+t\operatorname{diag}_e\nabla^2w_e,
\qquad \mathcal R=t\nabla^2S-6I.$$

The operator $\mathcal B$ is block diagonal in the edge **index**,
although each scalar diffusion acts on all configuration variables.
It satisfies $\mathcal B\ge6I$; $\mathcal R$ has range one and norm
at most $2+\kappa$. Therefore

$$t(LI+\nabla^2V)=\mathcal B+\mathcal R,
\qquad
(\mathcal B+\mathcal R)^{-1}
=\sum_{n\ge0}(-\mathcal B^{-1}\mathcal R)^n\mathcal B^{-1}.$$

Its block from $T$ to $R$ has zero contributions for $n<d(R,T)$.
The remaining operator norm is bounded by
$\frac16\sum_{n\ge d}q^n=q^d/(4-\kappa)$.
Insert this in (22), with the factor $t$ from the inverse scaling,
to prove (21). Smooth approximation and convergence extend the
inequality to the stated limits. $\square$

For the local action in §4, (20) holds on its chart with
$\kappa=C_3(\varepsilon+c_0)$, independently of the background
connection. Application to the singular soft-barrier measure (2)
additionally needs a realization or approximation satisfying the
analytic hypotheses of Theorem 5 with the same finite-range bounds.
Lemma 3 is a chart estimate; constructing that approximation remains
an explicit condition here. This avoids importing a whole-space
theorem into a bounded chart without specifying its boundary domain.
Taking $\kappa\le1$ gives the concrete constants $t/3$ and decay
$2^{-d}$ as looser bounds in (21). These rates concern mid-plane
fluctuations and their auxiliary diffusion.

### 7.3 What locality of a free-energy increment means

Suppose $V_{u,v}=V_0+u h_R+v k_T$, $(u,v)\in[0,1]^2$, satisfies
Theorem 5 uniformly with the same $t,\kappa$. Here the gradients of
$h_R,k_T$ have supports $R,T$, and let
$a=\sup_{u,v}\|\nabla h_R\|_{L^2(\mu_{u,v})}$,
$b=\sup_{u,v}\|\nabla k_T\|_{L^2(\mu_{u,v})}$.
For $F(u,v)=-\log\int e^{-V_{u,v}}$, differentiating twice yields
$F_{uv}=-\operatorname{Cov}(h_R,k_T)$. Consequently

$$\begin{aligned}
|F(1,1)-F(0,1)-F(1,0)+F(0,0)|
&\le\frac{tab}{4-\kappa}\,q^{d(R,T)}.
\end{aligned}\tag{23}$$

Thus the increment caused in $R$ depends exponentially weakly on
a remote change in $T$. For a local observable $f_T$ independent of
$u$, the same argument gives

$$|E_1f_T-E_0f_T|\le
\frac{t}{4-\kappa}q^{d(R,T)}
\sup_u\|\nabla f_T\|_{L^2(\mu_u)}
\sup_u\|\nabla h_R\|_{L^2(\mu_u)}.\tag{24}$$

These statements also hold for nonlinear parameter paths if the mixed
potential derivative vanishes for disjoint supports, with $h_R,k_T$
replaced by the parameter scores. Local external normalizations have
zero mixed derivative for disjoint supports. In a fixed local link
chart, changing coarse links in a region changes only incident bridge
and face potentials, after enlarging the region by a fixed number of
cells. Subject to the analytic condition after Theorem 5, (23) is
therefore the precise localized-increment statement for $\mathcal D_s$.

Tails are summable uniformly on these two-dimensional edge graphs.
A crude bound on the number of edges at graph distance $\ell$ from
one edge is $2(4\ell+3)^2$. Thus

$$\sum_{\ell\ge r}2(4\ell+3)^2q^\ell
\le C(q)q^{r/2},\qquad
C(q)=2\sum_{\ell\ge0}(4\ell+3)^2q^{\ell/2}<\infty.\tag{25}$$

Summing (23) over remote local scores with bounded gradient norms gives
this tail, with their support-size and support-radius constants made
explicit in $a,b$ and the distance. The unlocalized increment itself
may have size proportional to the changed region; (23) controls its
dependence on the distant environment.

### 7.4 The estimate that fails in the proposed telescoping

Plaquette variables obey compatibility relations. A single plaquette
update at fixed surrounding data generally fails those relations.
Even in the linearized embedded $U(1)$ sector on an $n\times n$ torus,
with harmonic data fixed, infinitesimal link changes $a$ and flux
changes $x$ satisfy $Ca=x$ and $\sum_p x_p=0$. At momentum
$k=(2\pi/n,0)$ the curl symbol of the mid-plane note is
$c(k)=(0,e^{2\pi i/n}-1)$. For a flux mode supported at this momentum,
every solution satisfies

$$\|a\|_2\ge\frac{\|x\|_2}{2\sin(\pi/n)}
\ge\frac{n}{2\pi}\|x\|_2.\tag{26}$$

Real sine/cosine modes give the same bound. Hence a right inverse
$a=\mathcal R x$ on admissible zero-mean fluxes cannot have norm
bounded independently of $n$. An exponentially local kernel
$\|\mathcal R_{ep}\|\le C e^{-\gamma d(e,p)}$ with $C,\gamma$
independent of $n$ would have bounded row and column sums by (25),
and bounded $\ell^2$ norm by the Schur test, contradicting (26).
Changing two separated opposite plaquette fluxes can instead use a
long string of changed links or a spatially spread representative.
The supports and score norms in (23) then track that representative.

The precise missing step is a **curvature response estimate after gauge
cancellations**, rather than a local right inverse. For example, in
specified admissible flux coordinates with harmonic data retained and
winding subtracted, one would need the normalized remainder
$h=\mathcal D_s-\mathcal D_0-W_N$ to have a Hessian kernel $K_{pq}$
satisfying

$$\sup_p\sum_q e^{\gamma d(p,q)}\|K_{pq}\|
\le C\varepsilon/t,\tag{27}$$

together with compatible paths or local replacements whose total
quadratic cost is bounded by $C\sum_p|X_p|^2$, and the required
zero-flux/winding remainder. Equation (21) controls the link-score
covariance. The cancellation of the large inverse-curl factors in
the combined expression $E[S_{ij}]-\operatorname{Cov}(S_i,S_j)+B_{ij}$
remains to be proved. The Gaussian case exhibits such cancellations;
(26) therefore diagnoses failure of the naive coordinate conversion,
without ruling out (27).

With those extra estimates, (18), or a compatible telescoping version
of it, and (19) would give the weak P($\alpha$) bound on the selected
large-plane regime. Theorem 5 and locality alone supply neither the
$O(\varepsilon)$ comparison to the Gaussian response nor the winding
bound, and Part A's barrier and large-field issues remain. This is the
precise obstruction reached in Part B. All claims of P($\alpha$) and
the normalized expansion (18) of the mid-plane note remain conditional.

## 8. Round 9: cancellation in flux response

**After refereeing (Claude, 2026-09-28).** §8.1 ACCEPT, checked in full:
Woodbury gives $G=\frac14(I-C^*PC)$, hence (28); the slab form (29) vanishes at
constant flux and gives $-|x|^2/(4t)$ for opposite layers, both as in
Proposition 2; $8I+L=12I-\mathsf A$ and the walk series give the weighted row
sum $1/(12-4e^\gamma)=\frac16$ at $\gamma=\log(3/2)$, so (30) reads $\frac1t(\frac5{12}+\frac14)=\frac2{3t}$. §8.2
ACCEPT as a formal statement: the equal-layer symbol $M(p)=-\lambda/(2(8+\lambda))$
follows from (29), a flat neutral connection shifts it to $M(p+H)$, and the
Coulomb lift $X^3(k)/(e^{i\kappa}-1)$ of a soft flux produces the $1/\kappa$ residue in
(32). The pole is a property of the fixed-frame chart (parallel transport
of charged curvature), consistent with the gauge-invariant expectation of
§6; it fixes that (27) must be posed covariantly. §8.3 ACCEPT.

### 8.1 Exact Gaussian reference (GPT-6 Astra, 2026-09-28)

Use the unrestricted abelian Gaussian in one slab with boundary links
$a_0,a_1$. Retain their harmonic components
$h_0,h_1$ and impose the linear compatibility relations on all cut and
transverse fluxes. Put $x=Ca_0$, $y=Ca_1$, so $\sum x=\sum y=0$.
Independent zero-mean Fourier components and harmonic data give actual
coordinates. The spatial kernels below represent bilinear forms on this
constrained space, by restriction of an ambient kernel; eliminating one
face or inserting a nonlocal orthogonal projector would change its row sums.
The three colour copies in the linearization are identical.
Set $L=CC^*$, $P=(8I+L)^{-1}$ and $G=H_0^{-1}$. The mean bridge link
is $b=(a_0+a_1)/2$ up to a gradient from direction-1 links. In uncentred
mid-links $m$ the normalized exponent and external old-face term are

$$S_0=\frac{2}{t}\|m-b\|^2+\frac1{4t}\|Cm\|^2,
\qquad B_0=-\frac{\|x\|^2+\|y\|^2}{8t}.$$

Assign half of each old-face ratio to each slab. Since
$\operatorname{Cov}_0(m)=tG$, differentiation in $b$ gives

$$E_0[S_{0,bb}]-\operatorname{Cov}_0(S_{0,b},S_{0,b})
=\frac1t(4I-16G)=\frac4t C^*PC,
\qquad G=\frac14(I-C^*PC).\tag{28}$$

For any lift $\mathcal R$ with $C\mathcal R=I$ on admissible fluxes,
$(C\mathcal R)^*P(C\mathcal R)=P$ as a restricted bilinear form.
The large factors in (26) disappear. Gaussian integration consequently gives

$$\begin{aligned}
\mathcal D_{0,\mathrm{slab}}
&=\frac1{2t}\langle x+y,P(x+y)\rangle
 -\frac{\|x\|^2+\|y\|^2}{8t}+\mathrm{const},\\
K^0_{\sigma p,\tau q}
&=\frac1t\left(P_{pq}-\frac14\delta_{\sigma\tau}\delta_{pq}\right)I_3,
\qquad \sigma,\tau\in\{0,1\}.
\end{aligned}\tag{29}$$

Cut-flux directions at fixed $x,y$ and all harmonic directions have
zero response. Summing slabs reproduces Proposition 2 of the
[series/parallel note](series-parallel-gauge-refinement.md) (passage).
On the square torus $8I+L=12I-\mathsf A$, where $\mathsf A$ is
nearest-neighbour adjacency. Its positive walk series yields
$\sup_p\sum_q e^{\gamma d(p,q)}P_{pq}\le(12-4e^\gamma)^{-1}$.
For $\gamma=\log(3/2)$ and the pair distance
$d((\sigma,p),(\tau,q))=d(p,q)+|\sigma-\tau|$, (29) therefore gives

$$\sup_{\sigma,p}\sum_{\tau,q}e^{\gamma d}
 \|K^0_{\sigma p,\tau q}\|
\le\frac1t\left(\frac{1+e^\gamma}{12-4e^\gamma}+\frac14\right)
=\frac{2}{3t}.\tag{30}$$

Assembly gives $4/(3t)$, independently of the periods. The Gaussian
remainder $h$ has zero kernel, hence satisfies
(27) with $C=0$; (30) bounds the reference response itself.

**Mechanism.** The Gaussian score identity produces the Schur complement
(28), equivalently the Woodbury identity for $4I+C^*C/2$. Its two exterior
curls annihilate gradients and harmonic shifts and turn every flux lift
into the identity. Combining the direct Hessian and covariance before
taking absolute values leaves a massive face resolvent. Normalized bridge
denominators remove the cut-face response; the old-face normalization
adds only the diagonal term in (29). This calculation uses the full
Gaussian domain; a barrier requires its own correction.

### 8.2 Formal non-abelian response: a surviving soft transport term

Specify a chart before testing (27). Use face logarithms in fixed site
frames, with the formal Coulomb lift $a=\mathcal R X+H+O(X^2)$,
$\mathcal R=C^*L^{-1}$ on zero-mean modes; retain $H$ and all nonlinear
compatibility relations. This is a finite-volume formal chart about zero.
Its cubic response already contains an inverse-curl pole. The following
test concerns equal adjacent layers, zero cut flux, and $H=0$.

Use the unrestricted zero-image expansion; barrier and image errors
remain outside it. Write the normalized action as
$S_0+V_3+V_4+J+\cdots$, with $V_j=\mathcal S_j/t$, and expand the BCH
logarithm as $Z_1+Z_2+Z_3+\cdots$. Each squared mid-face contributes
$\langle Z_1,Z_2\rangle/(2t)$ and
$(|Z_2|^2+2\langle Z_1,Z_3\rangle)/(4t)$ to $V_3,V_4$ respectively.
The bridge curvature contributes
$-\sum_e|[X_e,\xi_e]|^2/(24t)$ to $V_4$; $J$ includes the normalized
Haar and heat-kernel amplitudes. With $E_0$ at the shifted Gaussian saddle,
the first insertions and the required connected cubic pair are

$$\Delta\mathcal D=E_0V_3+E_0V_4
-\tfrac12\operatorname{Cov}_0(V_3,V_3)+E_0J+\cdots.\tag{31}$$

One vertex is first order in an insertion parameter; under
$[\ ,\ ]\mapsto g[\ ,\ ]$, the cubic is order $g$, while quartic and
the connected pair are both order $g^2$. Gaussian Wick contraction gives
the classical terms $F_3/t,F_4/t$ in (15) of the
[order-$t$ note](su2-midplane-order-t.md) (passage), including
$-\langle\partial_\xi\mathcal S_3,G\partial_\xi\mathcal S_3\rangle/(2t)$.
Thus a one-vertex quartic truncation alone would miss a necessary term.
The complete classical cubic can be tested without listing its vertices.
For equal layers, (29) has flux Hessian $M(p)/t$, where
$M(p)=-\lambda(p)/(2(8+\lambda(p)))$ and
$\lambda(p)=4-2\cos p_2-2\cos p_3$.
At a constant flat neutral connection $a_j=H_jT_3$, the charged
components have the exact classical quadratic symbol $M(p+H)/t$.
Indeed replace $C$ by the flat covariant curl in (28); its face
Laplacian has symbol $\lambda(p+H)$. This also fixes the sum of **all**
cubic transport vertices at zero incoming connection momentum.
Massive Gaussian elimination makes these link vertices analytic near
that momentum. For a neutral soft flux at $k=(\kappa,0)$, the Coulomb
lift has $a_3^3(k)=X^3(k)/(e^{i\kappa}-1)$ and $a_2^3(k)=0$;
here $X(z)=\sum_k X(k)e^{ikz}$ defines the Fourier amplitudes.
The resulting first-order charged flux Hessian of $h$, with outgoing
momenta $p+k,p$, consequently contains

$$\begin{aligned}
K^{(1)}_{+}(p+k,p)
&=\frac{X^3(k)}t
 \left[\frac{\partial_{p_3}M(p)}{e^{i\kappa}-1}+O(1)\right],\\
\partial_{p_3}M(p)&=-\frac{8\sin p_3}{(8+\lambda(p))^2}.
\end{aligned}\tag{32}$$

Choose $p_3\notin\{0,\pi\}$ and fixed nonzero $p$. The bounded term
includes the other placements of the neutral leg; their inverse curls
have momenta near $p$, and remain bounded. Reality pairs $k$ with $-k$.
Equation (32) has size $|X^3(k)|/(t|\kappa|)$ with a nonzero residue.
A plane-uniform row-sum bound $C\sup|X|/t$ would bound every such Fourier
matrix element and is incompatible with this coefficient as
$\kappa\to0$. This is a formal failure of (27) in this fixed-frame chart.
It occurs in the classical cubic, before quartic terms: the latter and
the cubic pair have classical boundary degree four, and bridge curvature
vanishes on this equal-layer test. Loop contractions have higher powers
of $t$ than the displayed $1/t$ residue. Winding subtraction removes
wrapping paths; the nonwrapping massive resolvent has the same bulk
momentum shift and residue. A flat-holonomy subtraction cannot remove it.

The mechanism is parallel transport of charged curvature between distinct
faces. The Gaussian Schur complement cancels the inverse curls on its two
external legs; differentiating its transport introduces a third leg
$\mathcal R X$, retained by (32). Covariantly transported derivatives or
another specified flux chart could change this conclusion. Such a
replacement needs its own definition and bound; (32) identifies the
term that prevents promoting the Gaussian proof in fixed site frames.

### 8.3 Beyond first order

To pursue (27), first replace the fixed-frame Hessian by a specified
covariant response that absorbs (32), and prove the corresponding
compatible-path estimate. Then control all connected insertions with
plane-uniform weighted sums, the normalized interacting barrier moments,
the full winding remainder and the large-field comparison. The Gaussian
identity and formal expansion supply no such all-order remainder bound.

## 9. Round 11: a tree-transported flux response

**Part 1, GPT-6 Astra, 2026-09-28; definition, unrefereed.** A fixed
tree gives a gauge-covariant finite-volume chart. Its response retains
the path dependence of comparisons between different faces.

### 9.1 Chart and response on the periodic plane

Write the vertices as $(i,j)\in\mathbb Z_{n_2}\times\mathbb Z_{n_3}$,
$n_2,n_3\ge3$, with root $o=(0,0)$. Choose the comb tree: all
nonseam direction-2 edges in every row, and the nonseam direction-3
edges in column zero. The path $\tau_v$ goes up column zero and then
along row $j$ to $v$. Let $T_v=U(\tau_v)$, using the convention
$U_{vw}\mapsto g_vU_{vw}g_w^{-1}$. For a face based at $v(p)$ put

$$\widehat U_{vw}=T_vU_{vw}T_w^{-1},\qquad
z_p=\operatorname{Ad}_{T_{v(p)}}\log U_{\partial p},\qquad
\Omega_j=U(\ell_j),\quad j=2,3.\tag{33}$$

Here $\ell_2,\ell_3$ are the two oriented coordinate cycles through
$o$. Tree links become identity; every displayed variable transforms
by the single rotation $\operatorname{Ad}_{g_o}$. Keep both $\Omega_j$
as variables. Near identity use $H_j=\log\Omega_j$; together with the
fluxes these determine the linear harmonic components (equal to
$H_j/n_j$ on flat data). Larger holonomies need
separate patches. Winding subtraction is performed after this retention.

The admissible set $\mathcal M$ consists of $(z,H)$ produced by the
$N+1$ non-tree links. This explicitly retains the nonabelian surface
relation between the based face products and the cycle commutator.
Locally it is a smooth embedded manifold: at identity its tangent is
$\sum_p z_p=0$ with two arbitrary harmonic variables; curl plus the
two periods is injective on tree-gauge links and has dimension
$3(N+1)$. The inverse function theorem supplies local reconstruction
$U(z,H)$. Use separate copies on the two slab boundaries, join their
roots by the fixed direction-1 path, and retain the cut-face data and
their compatibility relations when extending to the full slab.

To specify the second derivative as well as the frames, equip each
fixed-$H$ admissible slice with the metric induced by $\sum_p|dz_p|^2$.
Use (29) in $z$ as the Gaussian subtraction, summed over slabs, and
express $W_N$ through the same reconstruction, keeping its holonomy data.
Define $K^T=\nabla_{\mathcal M,H}^2(h\circ U)$, the intrinsic Hessian
for this metric, restricting to compatible slab variations. This is
an explicit covariant response; its definition includes the derivative
of the frames and the curvature of the constraint surface. Kernels
are ambient face-block representatives of this bilinear form, as in
§8.1, restricted to admissible tangent vectors. A weighted bound means
existence of such a representative; eliminating a face changes the
matrix norm being asked for. At nonzero fields all expansions below
are finite-volume formal jets about $(z,H)=0$.

### 9.2 Gaussian persistence and the strip term (Part 2)

**Exact Gaussian statement; formal interacting interpretation, unrefereed.**
At zero field the tree frames are identity, the constraint linearizes
to zero total flux, and (28)--(30) apply unchanged as ambient restricted
forms: $\gamma=\log(3/2)$, constant $2/(3t)$ per slab, $4/(3t)$
after assembly, and zero Gaussian remainder. A fixed change of face
frames conjugates every kernel block by orthogonal matrices and preserves
these bounds. Differentiating field-dependent frames needs another step.

For an explicit diagnostic let $Q_{pq}=\operatorname{Ad}_{U_{pq}}$
transport between neighbouring face basepoints along the single edge,
and put $\widehat Q_{pq}=\operatorname{Ad}_{T_p}Q_{pq}
\operatorname{Ad}_{T_q}^{-1}$. Subscripts on $T$ denote basepoints.
Define $\mathsf A_T$ by these four neighbour blocks and
$P_T=(12I-\mathsf A_T)^{-1}$. Its orthogonal walk weights give exactly
the majorant in (30), for every connection, even when $P_T-P_0$ is large.
It is the transported massive-resolvent sector suggested by the flat
test in §8.2; identifying the full interacting Hessian requires the
other cubic terms as well.

At $U(s)=\exp(sa)$ write $\theta_v=\sum_{e\in\tau_v}a_e$ with oriented
signs. Then

$$\left.\partial_s\widehat Q_{pq}\right|_0
=\operatorname{ad}_{b_{pq}},\qquad
b_{pq}=\theta_p+a_{pq}-\theta_q,
\qquad \dot P_T=P_0\dot{\mathsf A}_T P_0.\tag{34}$$

For a contractible comparison loop, discrete Stokes gives
$b_{pq}=\sum_{f\in\Sigma_{pq}}\pm z_f^{(1)}$; a wrapping loop also
retains its period. Formula (34) absorbs a pure-gauge connection,
since $a_{pq}=\theta_q-\theta_p$ then gives zero. In the comb chart,
the vertical comparison at $(i,j)$ instead encloses a strip:
$b_3(i,j)=\sum_{r=0}^{i-1}z_{rj}^{(1)}$ for nonseam rows.
Thus the soft connection leg of (32) becomes a strip-flux sum.

Here is a written size test with both based cycle holonomies fixed.
Let $n_2=n$ be even, $n_3\ge3$, and set
$f_i=\varepsilon$ for $0\le i<n/2$, $f_i=-\varepsilon$ otherwise.
Take $a_2=0$, $a_3(i,j)=b_iT_3$, $b_i=\sum_{r<i}f_r$.
All tree transports and both based cycles are identity, and the exact
commuting face logs are $sf_iT_3$, with zero total flux.
A vertical neighbour block of $\dot{\mathsf A}_T$ has norm
$|b_{n/2}|=n\varepsilon/2$, since $\|\operatorname{ad}_{T_3}\|=1$.
The identities $\|P_0^{-1}\|\le16$ and (34) imply

$$\|\dot P_T\|\ge\frac{\|\dot{\mathsf A}_T\|}{16^2}
\ge\frac{n\varepsilon}{512}.\tag{35}$$

This lower bound also applies to its maximal unweighted ambient row sum,
by self-adjointness and the Schur bound. Conversely, writing
$\|K\|_\gamma=\sup_p\sum_q e^{\gamma d(p,q)}\|K_{pq}\|$,
the same example has
$\|\dot{\mathsf A}_T\|_\gamma\le n\varepsilon e^\gamma$ and
$\|\dot P_T\|_\gamma\le n\varepsilon/24$ at the stated $\gamma$.
Only the two vertical neighbours contribute. The coefficient is a
finite-volume derivative at $s=0$; its growth persists however small
the allowed interval in $s$ becomes.

**New obstruction term:** $t^{-1}P_0\dot{\mathsf A}_T P_0$ carries
strip area although its two outer resolvents have uniform exponential
decay. The strips above are contractible and $H=0$; a subtraction of
wrapping paths alone leaves such comparisons. Equation (35) tests this
ambient sector, while (27) concerns the full restricted Hessian of $h$.
Cancellation with the remaining cubic vertices and the admissible
response, or a different response using short pairwise paths, remains
to be established. Consequently this tree chart supplies the Gaussian
constants and an explicit new term obstructing the proposed proof of
$C\varepsilon/t$; a plane-uniform first-order constant for $h$ remains
open. The calculation asserts no failure theorem for every covariant chart.

### 9.3 Higher orders (Part 3)

After resolving the strip term, (27) still requires summable connected
BCH insertions, including the cubic pair in (31), with derivatives of
the tree frames and the admissibility constraints included. Short
pairwise transports would require their own compatible Hessian and
path-cost construction. Uniform barrier moments, holonomy-dependent
winding control and the large-field comparison must then transfer the
formal coefficients to the normalized $h$; iteration remains a further step.

## 10. Round 12: the complete classical cubic on the strip

**After refereeing §10 (Claude, 2026-09-28).** ACCEPT as a formal
classical statement. Checked: $D_n\in[1/98,1/50]$ (numerator mean 2,
$10\le12-2\cos k\le14$); (41) from $M=-\lambda/(2(8+\lambda))$, $dM/d\lambda=-4/(8+\lambda)^2$,
$\partial_p\lambda=2\sin p$; the leading value $-4D_nH/t$ per layer and $H=n\varepsilon/2$.
Two remarks for the next round. (i) The surviving term is carried by a
delocalized tangent: $V$ occupies a whole row and wraps the $j$-cycle,
and $H=n\varepsilon/2$ is the Aharonov--Bohm phase of that cycle's holonomy at the
middle row, a gauge-invariant non-local datum (a non-based cycle). The
obstruction therefore belongs to the same family as the winding
functional, now for cycles that the fixed-cycle slice leaves free.
(ii) The exact dependence on $H$ enters through $\cos(p+H)$ and saturates, so
the value change along $V$ is at most $O(\min(n\varepsilon,1))|u|^2/t$ with pointwise
amplitude $|u|/\sqrt n\le\varepsilon$: of order $\varepsilon^2n/t$, against P($\alpha$)'s additive
term $t^\alpha N\simeq\varepsilon n^2$. Under the size clause this crude count gives no value
counterexample, consistent with §10.2's caution.

**GPT-6 Astra, 2026-09-28; formal, unrefereed.** Work on the equal-layer,
zero-cut-flux slice containing §9.2's strip, with both based cycles fixed
at identity. The calculation below includes every classical cubic term
on this slice, hence tests the full Hessian on compatible equal-layer
vectors. The classical coefficient means the stationary-action term
of order $t^{-1}$ in the unrestricted zero-image expansion. Barrier,
image and loop estimates remain separate from this formal coefficient.

### 10.1 Elimination, frames and the intrinsic derivative

Use the comb-tree gauge itself, so its transports are identically one
throughout the coordinate family. Let $a$ be the boundary link logarithms
and $u$ the uncentred mid-link logarithms. For the four oriented link
logs $l_1,l_2,l_3,l_4$ around a face define

$$Q(a)_p=\frac12\sum_{r<s}[l_r(a),l_s(a)],\qquad
q(c,d)=\frac{Q(c+d)-Q(c)-Q(d)}2,\qquad
R=I-C^*PC=4G.\tag{36}$$

Thus $\log U_{\partial p}=(Ca)_p+Q(a)_p+O(a^3)$.
Ad-invariance gives
$\langle u-a,[a,u]\rangle=0$: the bridge squared distance has
zero cubic term. Gaussian elimination gives $u_0=Ra$; stationarity
annihilates the quadratic action's pairing with the second-order
correction to $u_0$. Including the old-face ratio, the quadratic and
cubic stationary actions, with their common factor $t^{-1}$ removed, are

$$F_2=2\langle Ca,PCa\rangle-\tfrac14\|Ca\|^2,\qquad
F_3^{\rm link}=\tfrac12\langle CRa,Q(Ra)\rangle
-\tfrac12\langle Ca,Q(a)\rangle.\tag{37}$$

The bridge denominator is constant at zero cut flux. Its classical
contribution therefore vanishes; Haar and heat-kernel amplitudes start
at order $t^0$. Expressing the Gaussian subtraction in the actual
tree flux $z=Ca+Q(a)+O(a^3)$ contributes
$4\langle Ca,PQ(a)\rangle-\tfrac12\langle Ca,Q(a)\rangle$.
Consequently, for the linear tree lift $A$ with $CAz=z$ on $\sum z=0$,

$$\boxed{h^{\rm cl}_3(z)=\frac4t
\langle Pz,Q(RAz)-Q(Az)\rangle.}\tag{38}$$

This subtraction includes the second-order reconstruction of links:
its contribution to $F_2$ cancels the corresponding Gaussian chain-rule
term. In another gauge the same cancellation includes derivatives of
the tree frames; working in tree gauge makes their value exactly zero.
Equation (38) is the full cubic, including the old-face normalization.

At the origin the normal space of the fixed-cycle admissible manifold
consists of constant face fields. The equal-layer Gaussian Hessian
$M/t=(4P-I/2)/t$ annihilates this space. Thus its second-fundamental-form
term and its first-order change under intrinsic parallel transport
vanish. The remainder has zero quadratic jet, so its Christoffel term
starts at second order in the background. For $z=sf$, $a=Af$ and
compatible $v,w$ with $c=Av,d=Aw$, the complete linear-in-$s$ classical
Hessian correction is therefore $K_1=D^2h^{\rm cl}_3(f)$:

$$\begin{aligned}
tK_1(v,w)=8\{&\langle Pf,q(Rc,Rd)-q(c,d)\rangle\\
&+\langle Pv,q(Ra,Rd)-q(a,d)\rangle\\
&+\langle Pw,q(Ra,Rc)-q(a,c)\rangle\}.
\end{aligned}\tag{39}$$

The same coefficient belongs to $\nabla^2\mathcal D_s$ after its
Gaussian Hessian is removed, using intrinsic parallel identification
of tangent spaces. This specifies the derivative independently of a
chosen acceleration of a compatible path.

### 10.2 Proposition 6: a surviving compatible strip coefficient

**Formal classical verdict.** On the square strip family of §9.2 take
$n\in4\mathbb N$, $n\ge8$, and $m=n/2$. There are compatible charged
tangents $V$ of unit norm in the two-boundary metric for which

$$K_1(V,V)=-\frac{n\varepsilon}{t}D_n+\mathcal E_n,\qquad
D_n=\frac1n\sum_{r=0}^{n-1}
\frac{2-2\cos(2\pi r/n)}{(12-2\cos(2\pi r/n))^2},\qquad
|\mathcal E_n|\le C_*\varepsilon/t,\tag{40}$$

where $1/98\le D_n\le1/50$ and, as one deliberately loose explicit choice,
$C_*=10^6[\sum_{\ell\ge0}(\ell+1)^4 3^{-\ell}]^3$.
Thus a term of order $n\varepsilon/t$ survives in the complete intrinsic
Hessian. The coefficient refers to differentiation at $s=0$ for each
finite $n$; the small logarithm chart may shrink with $n$.

*Written proof.* Put $e_j=T_1\cos(\pi j/2)+T_2\sin(\pi j/2)$ and choose
$c_2=0$, $c_3(i,j)=\delta_{i,m}e_j/\sqrt{2n}$, $v=Cc$.
Then $\|c\|^2=1/2$, $\|v\|^2=1$, and each row of $v$ sums to zero.
Its tree lift is exactly $c$. Varying the vertical boundary links by
$U_3(i,j;s,u)=\exp(uc_3(i,j))\exp(sb_iT_3)$ and keeping horizontal
links equal to one fixes the tree and both based cycles exactly.
The induced face logs supply the nonlinear compatibility corrections.
At zero, take $V=(v,v)/\sqrt2$; intrinsic parallel continuation gives
the coefficient (39), independently of the displayed path's acceleration.

Split the neutral link field into $a=h+r$, with
$h_3=(n\varepsilon/2)T_3$, $h_2=0$ and
$r_3(i,j)=-\varepsilon d_{\mathbb Z_n}(i,m)T_3$.
This is an algebraic splitting of the cubic (39); the comparison field
$h$ supplies a flat symbol while the actual strip retains zero cycles.
For a constant neutral link $HT_3$, the full quadratic elimination in
charged face variables replaces $M(k,p)$ by $M(k,p+H)$, exactly as in
§8.2: the covariant curl has face Laplacian symbol
$2-2\cos k+2-2\cos(p+H)$. Consequently

$$\partial_H M(k,p+H)|_{H=0}
=-\frac{8\sin p}{(12-2\cos k-2\cos p)^2}.\tag{41}$$

For $p=\pi/2$, the normalized $v$ has horizontal spectral weights
$(2-2\cos k)/(2n)$. Equation (41) gives $-4D_nH/t$ per common-layer
unit vector $v$, and hence $-2D_nH/t$ on $V$. Substituting
$H=n\varepsilon/2$ proves the leading term in (40), including its sign.

The remainder comes from inserting $r$ in (39). Its curl is $f$, with
$\|Pf\|_\infty\le\varepsilon/8$. The other two terms contain one
localized factor $c$ or $Rc$ and one factor growing at most as
$\varepsilon d(i,m)$. For an explicit summation bound use
$\|R_{ee'}\|\le3^{-d(e,e')}$, $|P_{pq}|\le3^{-d(p,q)}/8$,
at most $2(4\ell+3)^2$ edges in a shell, and
$|q(c,d)_p|\le\frac14\sum_{r<s}(|l_r(c)||l_s(d)|+|l_r(d)||l_s(c)|)$.
Move the distance weight across each kernel using the triangle
inequality, then apply Cauchy--Schwarz to the two localized factors.
The resulting three kernel moments, four face incidences and the
coefficients in (39) are bounded by $C_*$ above, uniformly in $n$.
Finally $10\le12-2\cos k\le14$ and the mean numerator is 2,
which prove the stated bounds on $D_n$. $\square$

The contractible-walk part has the same limiting coefficient: wrapping
terms have length at least $n$ and their differentiated massive walk
tails are a polynomial in $n$ times $3^{-n}$. Thus winding subtraction
leaves this obstruction. Equation (40) rules out a plane-uniform
$C\varepsilon/t$ bound for the formal first-order comb-tree Hessian,
even on admissible vectors. Weak P($\alpha$) remains a value estimate;
its truth on large planes requires another argument, since a growing
Taylor coefficient alone gives neither a uniform finite-field remainder
nor a counterexample to that value inequality.

### 10.3 Next step and consequence for STATE

Cell 2 now calls for a value comparison using short pairwise transports:
retain the covariant massive kernel, bound each contractible loop by
its enclosed curvature, and construct compatible increments with a
uniform total quadratic cost. This targets weak P($\alpha$) directly;
barrier moments, winding, large fields and iteration remain the
subsequent obligations of §9.3. Proposition 4's rejection stands.

## 11. Round 13: short-path classical value comparison

**GPT-6 Astra, 2026-09-28; unrefereed.** Short transports give compatible
local increments and a uniform covariant classical comparison. Comparing
that value to the fixed-frame Gaussian subtraction leaves the explicit
transport term (46). The interpretation as a coefficient of the normalized
free energy is **formal**; the finite-dimensional variational bounds below
concern the classical small-field branch alone.

**After refereeing §11 (Claude, 2026-09-28).** Proposition 7 ACCEPT at
the level of structure: the contraction for the stationary equation in
the ball $\|\xi\|_\infty\le\varepsilon$, with Hessian error $K\varepsilon$ in operator and block
row-sum norm and $\nabla^2E\ge3I$, yields a unique interior minimum and the
plane-uniform bound (43) on an actual finite-dimensional minimum. The
open part is exactly the transport term $\mathcal T_T$ of (46), currently bounded
by $\frac12\|z\|^2$; by the remark on §10, it is expected to carry the
Aharonov--Bohm phases of cycles left free by the slice. Part 3 of the
round was cut by the usage limit (reset 2026-09-29 01:33).

**Proposal (Claude, 2026-09-28).** Proposition 7 bounds the classical
value uniformly against the covariant short-path reference; what resists
is only the comparison (46) with the abelian fixed-frame reference, which
carries the holonomy phases of §10. This suggests stating weak P($\alpha$) with
a covariant background-field reference $\mathcal D_0^{\rm cov}(U)$, the Gaussian defect of the
mid-plane fluctuations in the background connection of $U$, gauge-invariant
and holonomy-dependent, in place of the abelian $\mathcal D_0$. Two questions
decide whether this is the right formulation: whether $\mathcal D_0^{\rm cov}$ reduces to
$\mathcal D_0$ plus terms admissible in P($\alpha$) on smooth fields (so that the coupling
bookkeeping of the iteration survives), and whether the one-loop and
barrier parts obey the same covariant comparison.

### 11.1 Compatible increments (Part 1)

Keep equal boundary layers $U$, zero cut flux and the two based cycles
fixed. Write $z_p=\log U_{\partial p}$ in its own face frame,
$\|z\|_\infty\le\varepsilon$. A dual path of length $\ell$ avoiding the
edges of the fixed cycles gives an exact boundary family: multiply its
crossed links by $\exp(sv_e)$, with the signed $v_e$ transported successively
along the path. Choose these transports so that the left-trivialized face
holonomy velocities cancel at each interior face. The endpoints then have
velocities $v$ and $-Q_\gamma^{-1}v$. Differentiating logarithms applies
$d\log$ at each endpoint; its norm is at most 2 for $|z|\le1/16$.
Thus the link cost is $\ell|v|^2$, and the flux-velocity cost is at most
$8|v|^2$. Both layers use the same family. The untouched cycle links fix
both cycles exactly; the actual link products enforce all nonlinear
surface relations. Shortest paths are taken in this cut dual graph.
Their lengths can grow across the cut. This constructs local transfers;
a uniform decomposition of an arbitrary boundary contraction remains a
separate requirement.

For the value comparison use compatible **midpoint** increments instead:
$m_e=U_e\exp\xi_e$, keeping all boundary links fixed. These increments
have unconstrained midpoint cycles, as required by the original integral.
Let $C_U$ be the signed rotated incidence obtained by moving each inserted
$\xi_e$ to the basepoint of its face product. Then
$C_UC_U^*=4I-\mathsf A_U$, with four orthogonal neighbour blocks, and

$$P_U=(8I+C_UC_U^*)^{-1}=(12I-\mathsf A_U)^{-1},\qquad
\xi_0=-C_U^*P_Uz,\qquad
\|\xi_0\|_\infty\le\varepsilon/4,\quad
\|\xi_0\|_2^2\le\|z\|_2^2/8.\tag{42}$$

Indeed $P_U=\sum_{\ell\ge0}12^{-\ell-1}\mathsf A_U^\ell$:
the absolute row sum is at most $1/8$, each edge meets two faces, and
$\|C_U\|\le\sqrt8$. Every term transports between successive neighbouring
faces; its weight includes the full multiplicity $4^\ell$. The actual
links $U_e\exp(s\xi_{0e})$ realize the increment and all its induced face
relations, with integrated link cost at most $\|z\|_2^2/8$.
The quadratic action $2\|\xi\|^2+\|z+C_U\xi\|^2/4-\|z\|^2/4$
is minimized at (42), with value
$F_U^{\rm cov}=2\langle z,P_Uz\rangle-\|z\|^2/4$.

### 11.2 Proposition 7: value bound and the surviving transport (Part 2)

Put $K=40(1+L_F)$, with $L_F$ defined in §4, and assume
$\varepsilon\le\min(1/16,1/(4K))$. Let $F^{\rm cl}(U)$ be the minimum,
on $\|\xi\|_\infty\le\varepsilon$, of the classical action
$t(S-J)-\|z\|^2/4$ on this equal-layer slice. Then

$$|F^{\rm cl}(U)-F_U^{\rm cov}|\le
K\varepsilon\|z\|_2^2.\tag{43}$$

This is a plane-uniform bound for an actual finite-dimensional minimum.
Its $t^{-1}$ contribution to $\mathcal D_s$ remains a formal classical
identification, with barrier and amplitude estimates separate.

*Proof.* The bridge term is exactly $2\sum_e|\xi_e|^2$.
Ad-invariance makes the face gradient at zero exactly $C_U^*z/2$.
The local Hessian bound defining $L_F$, summed over the two faces at
each edge, bounds the Hessian error from $4I+C_U^*C_U/2$ by
$K\varepsilon$, both in operator norm and in block row-sum norm,
throughout this ball. Indeed each face costs at most
$L_F(\varepsilon+4\varepsilon)$ in operator norm; conversion to a
four-block row sum costs at most 2, and each edge meets two faces.
Also $H_U^{-1}=(I-C_U^*P_UC_U)/4$ has block row sum at most $1/2$.
The stationary equation is a contraction
$\xi=\xi_0-H_U^{-1}(\nabla E(\xi)-\nabla E(0)-H_U\xi)$,
where $E=t(S-J)-\|z\|^2/4$. It maps the ball into radius
$\varepsilon/4+K\varepsilon^2/2<\varepsilon$, with Lipschitz constant
at most $1/8$. Convexity gives the unique interior minimum $\xi_*$.
Since $\nabla^2E\ge3I$ and $\|\nabla E(0)\|\le\sqrt2\|z\|$,
$\|\xi_*\|\le\sqrt2\|z\|/3$. Taylor's formula bounds the value error
at either minimizer by $K\varepsilon\|\xi\|^2/2$; evaluating each
functional at the other's minimizer proves (43). $\square$

For each unordered face pair choose a shortest dual path $\sigma_{pq}$,
with $\sigma_{qp}=\sigma_{pq}^{-1}$, and its transport $Q_{pq}$ from
$C_U$. Retain walks $\gamma:p\to q$ with the same lifted displacement
as $\sigma_{pq}$; their comparison loops are contractible. Denote their
resolvent sums by $P_U^c$ and, with every rotation replaced by 1,
$p^c_{pq}$. All remaining walks define $P_U^w=P_U-P_U^c$.
Each incidence transport uses at most three physical edges, so a loop
$\gamma\sigma_{pq}^{-1}$ for a length-$\ell$ walk has length at most
$16\ell$. Cancelling backtracks and commuting perpendicular steps fills
its lift with at most $256\ell^2$ plaquettes, counted with multiplicity.
The exact ordered plaquette product and telescoping orthogonal matrices
therefore give

$$\|Q_\gamma-Q_{pq}\|\le256\ell^2\varepsilon,\qquad
\sup_p\sum_q\|(P_U^c)_{pq}-p^c_{pq}Q_{pq}\|
\le\frac{256\varepsilon}{12}\sum_{\ell\ge0}\ell^2 3^{-\ell}
=32\varepsilon.\tag{44}$$

This uses enclosed curvature, permits self-intersections, and includes
walk multiplicity. Reverse paths give the same column bound. Consequently
$F_{\rm short}=2\sum_{pq}p^c_{pq}\langle z_p,Q_{pq}z_q\rangle-\|z\|^2/4$
satisfies the explicit quadratic-cost estimate

$$|F^{\rm cl}-2\langle z,P_U^wz\rangle-F_{\rm short}|
\le(K+64)\varepsilon\|z\|^2.\tag{45}$$

To compare with §§9--10's Gaussian value, set
$I^T_{pq}=\operatorname{Ad}_{T_p}^{-1}\operatorname{Ad}_{T_q}$ and define
$$F_{0,T}^c=2\sum_{pq}p^c_{pq}\langle z_p,I^T_{pq}z_q\rangle-\|z\|^2/4.$$
The precise surviving term is

$$\begin{aligned}
F^{\rm cl}-2\langle z,P_U^wz\rangle-F_{0,T}^c
 &=\mathcal T_T+\mathcal R,\\
\mathcal T_T&=2\sum_{pq}p^c_{pq}
 \langle z_p,(Q_{pq}-I^T_{pq})z_q\rangle,\\
|\mathcal R|&\le(K+64)\varepsilon\|z\|^2,\qquad
|\mathcal T_T|\le\tfrac12\|z\|^2.
\end{aligned}\tag{46}$$

The last bound uses $\|Q-I\|\le2$ and row sum $\le1/8$.
Short-path loops in (44) have area controlled by walk length; the tree
comparison in (46) can enclose §9's long strips even for neighbours.
Equation (46), divided by $t$, is the verdict for the classical value:
the covariant short-path reference has a uniform $O(\varepsilon)$ cost,
while the prescribed Gaussian reference retains $\mathcal T_T/t$.
The subtraction here removes the explicitly defined quadratic winding
walks; identifying it with the full normalized $W_N$ requires its separate
estimate. An $O(\varepsilon\|z\|^2)$ bound on $\mathcal T_T$ for admissible
fields, or a value counterexample, remains open; (40) alone decides neither.

### 11.3 Implication for weak P($\alpha$) (Part 3)

Proposition 7 gives the classical value estimate
$|F^{\rm cl}/t-F_U^{\rm cov}/t|\le Kt^{1/2-\delta}\|z\|^2/t$
on the equal-layer, zero-cut-flux slice, hence the weak P($\alpha$)
error budget with $\alpha=1/2-\delta>2\delta$ for $0<\delta<1/6$
against this covariant reference, with classical coupling shifts zero.
Equation (46) leaves $\mathcal T_T/t$ against the prescribed fixed-frame
reference after the displayed quadratic winding subtraction; its current
bound $\|z\|^2/(2t)$ lacks the required small factor. Claude's referee
remarks correctly distinguish this unresolved value comparison from the
strip Hessian coefficient: that coefficient alone decides neither the
value inequality nor its failure. The consequence for STATE is to assess
the covariant reference and its iteration bookkeeping next; normalized
one-loop, barrier, full winding and large-field estimates, general boundary
layers and stability under perturbed actions remain separate obligations.

## 12. Round 14: a covariant reference and its flux sectors

**GPT-6 Astra, 2026-09-29; unrefereed.** Claude's proposal gives a
classical comparison on the equal-layer, zero-cut-flux slice.

**After refereeing §12 (Claude, 2026-09-29).** ACCEPT, with one constant
corrected in place. The old-face subtraction in the quadratic action of
§11.1, in $E$ of Proposition 7 and in (47) was printed as
$-\frac12\|z\|^2$. The old-face ratio of (29) and (37) at $x=y=z$ is
$-\frac14\|z\|^2$, and only that value gives the stated minimum
$F_U^{\rm cov}=2\langle z,P_Uz\rangle-\frac14\|z\|^2$, since the
regularized least-squares minimum of $2\|\xi\|^2+\frac14\|z+C_U\xi\|^2$
is $2\langle z,P_Uz\rangle$. With $-\frac12$, (43) would fail by
$\frac14\|z\|^2$. The four places now read $-\frac14$; the proofs use only
gradients and Hessians and stand as written. Checked: (47) by completing
the square with Hessian $H_U=\frac12(8+C_U^*C_U)$; (48) from Sylvester's
identity $\det(8+C_U^*C_U)=8^{3N}\det(8+L_U)$ with $8+L_U=12-\mathsf A_U$,
the trace series with $\|\mathsf A_U\|/12\le\frac13$,
$3-\operatorname{tr}R=\frac12\|R-I\|_F^2$ for a rotation, at most $N4^\ell$
rooted walks and $\sum_\ell\ell^33^{-\ell}=\frac{33}8$, so $B=202\,752$;
(49) from the row bound $\frac18$ and $a=t/\lambda_3$; (50) from
$I-P_UL_U=8P_U$; (51), where the twisted sector $m=1$ has no adjoint zero
mode; the electric projection, normalized by $|\mathbb Z_2^2|^{-1}=\frac14$
and applied to partition functions; (52) from (43) with
$\varepsilon=t^{1/2-\delta}$ and $d_U\le Bt^{1-2\delta}N$, admissible since
$\frac12-\delta\le1-2\delta$. Two readings for STATE. (i) On the smooth
family, any quadratic reference with a bounded kernel obeys a bound of the
form (49): $\|z\|^2/t\le M^2Nt^3/\lambda_3^4$ is the classical action of
the slab, which lies below the additive term $t^\alpha N$ for $\alpha\le3$.
Smooth-field admissibility thus protects the coupling bookkeeping without
selecting $\mathcal D_0^{\rm cov}$. The selection comes from (52), which
holds on the whole small-field slice for $\mathcal D_0^{\rm cov}$ and is
open for $\mathcal D_0$ through $\mathcal T_T$. (ii) By (50) the classical
defect is $-\frac1{32}\|C_U^*z\|^2/t$ at leading order, of dimension six,
so the classical step carries no $F^2$ term, as in the exact tree-level
statement of [G1](gaussian-blocking-coupling.md); the $O(t)$ coupling
shift comes from the determinant $d_U$, the superrenormalizable pattern of
$D=3$. Correction to my §10 remark: $H$ is the rotation per link, and the
row cycle's Aharonov--Bohm phase is $n_3H$ modulo $2\pi$, as §12.3 states.

### 12.1 Finite-plane definition

Keep all midpoint links, including their cycles, free as in §11.1.
For each background $U$ with principal face logs $z$, define
$L_U=C_UC_U^*$, $H_U=4I+C_U^*C_U/2$ and $P_U=(8I+L_U)^{-1}$.
Normalize the Gaussian integral by its value at the identity background:

$$\begin{aligned}
\mathcal D_0^{\rm cov}(U)&=-\log
\frac{\int_{\mathbb R^{6N}}e^{-E_U^{(2)}(\xi)/t}\,d\xi}
{\int_{\mathbb R^{6N}}e^{-E_1^{(2)}(\xi)/t}\,d\xi}
=\mathcal D_{0,\rm cl}^{\rm cov}(U)+d_U,\\
E_U^{(2)}(\xi)&=2\|\xi\|^2+\tfrac14\|z+C_U\xi\|^2-\tfrac14\|z\|^2,\\
\mathcal D_{0,\rm cl}^{\rm cov}&=F_U^{\rm cov}/t,
\qquad d_U=\tfrac12\log\frac{\det H_U}{\det H_1}.
\end{aligned}\tag{47}$$

Completing the square proves (47) exactly for this finite Gaussian model.
Gauge changes rotate the edge and face spaces orthogonally, preserving
both terms. The bound $H_U\ge4I$ includes harmonic modes and makes the
integral finite without a zero-mode deletion. The walk series retains
all holonomies, including winding paths. This is a frozen-background
quadratic model; the exact classical Hessian, heat-kernel/Haar amplitudes
and the barrier supply corrections. The fixed-frame $\mathcal D_0$ on
this slice means (29) with $x=y=z$ transported to the tree frame and its
field-independent constant removed. At identity background the kernels
coincide; expanding $U$ and $z$ together recovers its classical quadratic
jet. The term $d_U$ is explicitly a Gaussian one-loop contribution.

### 12.2 Smooth fields and the coupling budget

**Finite bounds; continuum derivative interpretation formal.** Set
$n=\min(n_2,n_3)$ and compare to the full periodic fixed-frame kernel.
For a smooth family assume explicitly $\max_p|z_p|\le Ma^2$, with $M$
independent of $a,N$, and $t=\lambda_3a\le1$. The row bound $1/8$ gives
$|\mathcal D_{0,\rm cl}^{\rm cov}-\mathcal D_0|
\le\|z\|^2/(2t)\le M^2Nt^3/(2\lambda_3^4)$, including tree seams.
The determinant lemma and its absolutely convergent trace series give

$$d_U=-\frac12\sum_{\ell\ge1}
\frac{\operatorname{Tr}(\mathsf A_U^\ell-\mathsf A_1^\ell)}{\ell12^\ell},
\qquad |d_U|\le B\varepsilon^2N+\tfrac92N3^{-n},\quad
B=\frac{3\cdot256^2}{4}\sum_{\ell\ge1}\ell^3 3^{-\ell}.\tag{48}$$

Indeed a contractible closed walk has adjoint holonomy $R$ with
$\|R-I\|\le256\ell^2\varepsilon$ by (44), and
$3-\operatorname{tr}R=\|R-I\|_F^2/2\le3\|R-I\|^2/2$.
There are at most $N4^\ell$ rooted walks. Wrapping walks have $\ell\ge n$;
using $|\operatorname{tr}(R-I)|\le6$ gives the last term in (48).
For the smooth family replace $\varepsilon$ by $Ma^2$. Hence

$$|\mathcal D_0^{\rm cov}-\mathcal D_0|
\le\frac{M^2}{\lambda_3^4}(t^3/2+Bt^4)N+\tfrac92N3^{-n}.
\tag{49}$$

Under P($\alpha$)'s $n\ge c_0/t$, (49) is an admissible additive
$C_{M,\lambda_3,c_0,\alpha}t^\alpha N$ for $0<\alpha\le3$;
$3^{-n}\le[\alpha/(e c_0\log3)]^\alpha t^\alpha$ makes the constant explicit.
This proves smooth-family admissibility with its stated $M$ dependence.
For coupling bookkeeping, spectral calculus also gives exactly

$$F_U^{\rm cov}=-\tfrac14\langle z,L_U(8+L_U)^{-1}z\rangle
=-\tfrac1{32}\|C_U^*z\|^2+r_U,\qquad
0\le r_U\le\tfrac1{256}\|L_Uz\|^2.\tag{50}$$

For a fixed smooth connection $z=a^2F_{23}+O(a^3)$ and
$C_U^*z=a^3(D_3F_{23},-D_2F_{23})+O(a^4)$ up to orientations.
Thus the classical bulk starts at dimension six, $O(a^2)$ relative to
$F^2/t$; (48)'s contractible determinant starts at curvature squared,
allowing $O(t)$ relative coupling shifts. These formal local orders and
$\sum_jt_j^\alpha<\infty$ for $t_j=2^{-j}t_0$ preserve the proposed
smooth ultraviolet bookkeeping. The full small-field class still leaves
$\mathcal T_T/t$ in (46) outside the established remainder bound: (49)
uses $Ma^2$, while that class allows $t^{1/2-\delta}$. Holonomy-dependent
transport is the unresolved value term; a value counterexample remains
unproved. Stability for perturbed actions remains an extra theorem.

### 12.3 't Hooft sectors and the free-cycle phases (Part 2b)

**Source reading and its finite-plane application.** 't Hooft,
[*A property of electric and magnetic flux in non-Abelian gauge theories*](https://doi.org/10.1016/0550-3213(79)90595-9),
Nucl. Phys. B **153** (1979), 141--160 (`tHooft1979Flux`):
**Crossref metadata verified 2026-09-29; passage**, §§2--5, pp. 143--148,
[original-paper text transcription](https://studyres.com/doc/2086823/a-property-of-electric-and-magnetic-flux-in-non).
His transition functions close up to centre elements; spatial twists
label magnetic flux, while electric flux labels characters of the
centre-periodic gauge transformations. Temporal twists select those
characters by a finite Fourier transform of partition functions.

Here is the resulting $1+2$ formulation, with direction 1 interpreted
as Euclidean time for this sector discussion. Write $m=n_{23}\in\mathbb Z_2$,
$k=(n_{12},n_{13})\in\mathbb Z_2^2$. Spatial transition functions obey
$\Omega_2(x+L_3)\Omega_3(x)=(-1)^m\Omega_3(x+L_2)\Omega_2(x)$.
For each fixed $m$, construct $C_{U,m}$ using the adjoint transition
functions at seams, and use (47) with $H_U$ replaced by $H_{U,m}$.
Take $z$ from near-identity plaquette lifts after removing the prescribed
seam-centre factors. Keep the common denominator $\det H_1$:
sector-dependent constants then remain in relative sector weights.
Ordinary periodic SU(2) backgrounds here have $m=0$; $m=1$ requires
an explicitly twisted boundary problem, or an external centre-flux
insertion. Summing magnetic sectors would be a further choice of theory.

For an explicit flat representative choose constant transitions
$\Gamma_2\Gamma_3=(-1)^m\Gamma_3\Gamma_2$. Their commuting adjoint
rotations have joint phases $(\phi_2,\phi_3)$, and the eigenvalues are

$$L_m(r,s;\phi)=4-2\cos\frac{2\pi r+\phi_2}{n_2}
-2\cos\frac{2\pi s+\phi_3}{n_3},\qquad P_m=(8+L_m)^{-1}.\tag{51}$$

For $m=0$, commuting $\Gamma_j=\exp(\theta_jT_3)$ give phases
$(0,0)$ and $\pm(\theta_2,\theta_3)$. For $m=1$, take
$\Gamma_2=i\sigma_1$, $\Gamma_3=i\sigma_2$ (Pauli matrices): conjugation
fixes its own axis and reverses the other two, giving phase pairs
$(0,\pi),(\pi,0),(\pi,\pi)$. Formula (51) follows by translating a
plane wave once around each cycle. Curved backgrounds use $C_{U,m}$
directly and retain their continuous Wilson-loop data within the sector.
In §10's strip, $H$ in $\cos(p+H)$ is the rotation **per link**;
the free row cycle is $\exp(n_3HT_3)$, with adjoint phase $n_3H$ modulo
$2\pi$. Fixing two based cycles, or fixing $m=0$, leaves those row
holonomies curvature-dependent. Discrete flux labels alone therefore
leave the transport term of (46) present.

With a temporal closure the electric-sector prescription is
$Z_{e,m}=\frac14\sum_{k\in\mathbb Z_2^2}(-1)^{e\cdot k}Z_{k,m}$,
$e\in\mathbb Z_2^2$. Apply it to the assembled reference weights with
their temporal seam data retained, before taking a logarithm. Electric
flux is a quantum sector of the assembled kernel; a single classical
background $U$ specifies neither $e$ nor a Fourier transform of log
references. The adjoint local bounds survive either spatial twist;
relative electric-sector estimates additionally require control of
cancellation in this signed projection.

### 12.4 Classical verdict and consequence for STATE

Proposition 7 gives, for $\alpha=1/2-\delta>2\delta$, $0<\delta<1/6$,
$$|F^{\rm cl}/t-\mathcal D_{0,\rm cl}^{\rm cov}|
\le Kt^\alpha\|z\|^2/t.\tag{52}$$
This proves classical weak P($\alpha$) on the stated equal-layer slice,
uniformly in plane size; (48) also permits the full reference (47) in
(52) after adding $Bt^{1-2\delta}N+\frac92N3^{-n}$, admissible under the
size clause. Classical coupling shifts may be zero. Identification with
the normalized free energy remains **formal**. The Gaussian determinant
bound settles only that frozen model's one-loop term; the actual saddle
Hessian, Haar/heat-kernel amplitudes, normalized loop remainder, barrier
moments, image/large-field comparison and general boundary layers remain.
**Consequence for STATE:** retain this covariant reference and its sector
weights; next prove the normalized covariant comparison, then stability
under perturbed actions. Equivalence to the original fixed-frame
P($\alpha$) on the full small-field set still requires the transport-value
estimate, and electric-sector projection requires its own relative bound.

## 13. Round 15: the normalized covariant comparison

**GPT-6 Astra, 2026-09-29; written bounds, unrefereed.** Throughout this
section the layers are equal, cut flux is zero, and all free-cycle
holonomies remain in $C_U$. Put $\alpha=1/2-\delta$, $0<\delta<1/6$,
$\varepsilon=t^\alpha$, and impose Proposition 7's smallness conditions.

**After refereeing §13 (Claude, 2026-09-29).** ACCEPT (53)--(58) as
finite-plane written proofs under the stated chart and time conditions.
Checked: (53) from the block-$\ell^1$ contraction with
$\|H_U^{-1}\|_{1\to1}\le\frac12$ and $\|\xi_0\|_{1,b}\le\sum_p|z_p|$; (54) from
rank 12 per face, $\sum_p\sum_{e\in\partial p}|\xi_{*e}|=2\|\xi_*\|_{1,b}$ and
$\frac12\cdot\frac13\cdot12L_F(1+\frac{16}7)=\frac{46}7L_F$; the moment bound (55) by
integration by parts against $|y_e|^{k-2}y_e$, whose divergence in
$\mathbb R^3$ is $(k+1)|y_e|^{k-2}$, with the barrier term nonnegative because
$|\xi_{*e}|\le2\varepsilon/7<\eta$, and diagonal dominance
$(5-\kappa_r)-(3+\kappa_r)=2-2\kappa_r\ge\frac32$ at the maximizing edge; the
cubic Taylor bound with 16 products per face; Šidák's rectangle, which
stays in $|\xi_e|\le9\varepsilon/7<\eta=2\varepsilon$, with coordinate variances at most
$t/3.75$; the assembly of $C_0$ from (43), (54), (56) and
$e^{-t^{-2\delta}/2}\le B_\delta t^\alpha$; (57) with the counts $2$ and $3$ and $\frac{38}7$;
and the $k=2$ bound $M_2^2\le3t+3D_JtM_2$ with net dominance at least 1
when $\kappa_r,9tD_J\le\frac14$. The condition $\kappa_r\le\frac14$ shrinks the chart
to $c_0\lesssim1/(32L_F)$, which moves more of the integral into the
large-field comparison that §13 leaves open. One remark for the
iteration: the remainder $2A_LN\sqrt t$ in (56) is additive and depends on
the whole field through the interpolated measure, including flat
holonomies. The stated form of P($\alpha$) admits it. A multi-step argument
will need it as a sum of quasi-local terms; the uniform moments (55) and
Lemma 1's covariant decay are the ingredients for that rewriting.

### 13.1 Actual saddle determinant (Part 1)

Write $A_U=\nabla^2E_U(\xi_*)$, $\Delta_U=A_U-H_U$ and
$\|\xi\|_{1,b}=\sum_e|\xi_e|$. The contraction proof of Proposition 7
also works in block $\ell^1$: symmetry gives the column bounds from
its row bounds, and $\|C_U^*z/2\|_{1,b}\le2\sum_p|z_p|$. Hence

$$\|\xi_*\|_{1,b}\le\frac{\sum_p|z_p|}{1-K\varepsilon/2}
\le\frac87\sum_p|z_p|.\tag{53}$$

Each face Hessian difference has rank at most 12 and operator norm
at most $L_F(|z_p|+\sum_{e\in\partial p}|\xi_{*e}|)$, by §4's
mean-value bound with the orthogonal incidence maps held fixed.
The bridge Hessian is exactly $4I$. Thus the trace norm satisfies
$\|\Delta_U\|_{\rm tr}\le12L_F(\sum_p|z_p|+2\|\xi_*\|_{1,b})$.
Every $H_U+s\Delta_U\ge3I$, $0\le s\le1$, so integrating
$\frac12\operatorname{Tr}[(H_U+s\Delta_U)^{-1}\Delta_U]$ proves

$$\left|\frac12\log\frac{\det A_U}{\det A_1}-d_U\right|
\le C_D\sum_p|z_p|,\qquad C_D=\frac{46}{7}L_F.\tag{54}$$

Here $A_1=H_1$ exactly. More generally $z=0$ gives $\xi_*=0$ and
$A_U=H_U$, even with nontrivial flat holonomies. This is a local
field-dependent bound; the trace norm replaces any need to discard
transports in the resolvent. Both (53) and (54) are uniform in $N$.
For $t\le1$ and $\alpha\le1/2$,
$|z_p|\le(t^\alpha+|z_p|^2/t^\alpha)/2
\le t^\alpha(1+|z_p|^2/t)/2$, giving weak P($\alpha$) with
constant $C_D/2$. The coarser bound $6NK\varepsilon/4$ also follows
from $\|\Delta_U\|\le K\varepsilon\le1/4$ and
$|\log(1+x)|\le|x|/(1-|x|)$; it is admissible in the additive budget,
while (54) additionally vanishes at zero curvature.

### 13.2 Laplace remainder and the soft barrier (Part 2)

Choose $2\varepsilon<c_0\le1/16$ still smaller if necessary so that
$\kappa_r=8L_F(\varepsilon+4c_0)\le1/4$. Define $y=\xi-\xi_*$,
$S_2=(E_U(\xi_*)+y^TA_Uy/2)/t$, $R=E_U/t-S_2$, and
$V_\lambda=S_2+\lambda R+W_\eta$, $0\le\lambda\le1$.
The partition function $Z_E=\int e^{-E_U/t-W_\eta}$ equals
$e^{\|z\|^2/(4t)}Z_s^0$, where $Z_s^0$ is (2) with $J$ removed.
Thus its normalization includes precisely the classical old-face ratio.
On the whole chart, the unbarriered Hessians have diagonal blocks
$\ge(5-\kappa_r)I/t$, off-diagonal block majorants summing to
$(3+\kappa_r)/t$, and lower operator bound $(4-\kappa_r)I/t$.
Indeed $H_U$ has diagonal $5I$ and six off-diagonal incidences of norm
$1/2$; the eight local Hessian blocks per row give the stated error
majorant. Convex interpolation preserves these bounds. The fixed convex
barrier preserves the lower bound, hence (13), along the entire path.

Here is the additional saddle-centering argument. Proposition 7 gives
$|\xi_*|_\infty\le2\varepsilon/7<\eta$, so
$y_e\cdot\nabla w_\eta(\xi_e)\ge0$. Integration by parts against
$|y_e|^{k-2}y_e$, followed by Hölder at an edge maximizing
$M_k=(\langle|y_e|^k\rangle_\lambda)^{1/k}$, gives
$(2-2\kappa_r)M_k^k\le t(k+1)M_k^{k-2}$. Thus, for $k\ge2$,

$$\sup_{\lambda,e}\langle|y_e|^k\rangle_\lambda
\le M_k^{\rm bd}t^{k/2},\qquad M_k^{\rm bd}=[2(k+1)/3]^{k/2}.\tag{55}$$

The barrier's boundary decay in (2) justifies these integrations;
regularizing $|y_e|^{k-2}y_e$ at zero gives the same inequality.
In particular the probability of $|\xi_e|\ge r>\varepsilon$ is at most
$M_k^{\rm bd}t^{k/2}/(r-\varepsilon)^k$, including layers near $c_0$.
This controls ordinary local moments; expectations of the unbounded
barrier Hessian require separate hypotheses, and are unused here.

Taylor's integral remainder gives
$|R|\le L_F\sum_p(\sum_{e\in\partial p}|y_e|)
(\sum_{e\in\partial p}|y_e|^2)/(6t)$.
There are 16 products per face, each bounded in expectation by
$M_3^{\rm bd}t^{3/2}$ from (55), with $M_3^{\rm bd}=(8/3)^{3/2}$.
Put $A_L=(8/3)L_F(8/3)^{3/2}$.
Integrating $\partial_\lambda\log Z_\lambda=-\langle R\rangle_\lambda$
yields $|\log Z_E-\log Z_{2,W}|\le A_LN\sqrt t$.
Expansion about the actual Hessian absorbs the $\varepsilon$-quadratic
term into (54); the remaining Taylor error starts cubically.

Let $G_U=\int_{\mathbb R^{6N}}e^{-S_2}$ and
$q=2e^{-\varepsilon^2/(2t)}\le1/2$.
The centered Gaussian has scalar variances at most $t/3$.
The rectangle $|y_{e,a}|\le\varepsilon/\sqrt3$ lies inside $W_\eta=0$.
Šidák's Gaussian rectangle inequality gives
$Z_{2,W}/G_U\ge(1-q)^{6N}$, while $Z_{2,W}/G_U\le1$.
Input: [Šidák 1967](https://doi.org/10.1080/01621459.1967.10482935),
Corollary 1, p. 628 (**passage**, original paper; Crossref metadata
verified 2026-09-29). Consequently the identity-normalized remainder obeys

$$\left|\log\frac{Z_E(U)}{G_U}-\log\frac{Z_E(1)}{G_1}\right|
\le2A_LN\sqrt t+48Ne^{-t^{-2\delta}/2}.\tag{56}$$

This includes the barrier cost for every barrier satisfying (2), regardless
of its growth near $c_0$. Put $B_\delta=(\alpha/(\delta e))^{\alpha/(2\delta)}$;
maximizing $x^{\alpha/(2\delta)}e^{-x/2}$ gives
$e^{-t^{-2\delta}/2}\le B_\delta t^\alpha$.
Combining (43), (54) and (56) proves the normalized, amplitude-free bound
$| -\log[Z_E(U)/Z_E(1)]-\mathcal D_0^{\rm cov}(U)|
\le C_0t^\alpha\sum_p(1+|z_p|^2/t)$, with
$C_0=K+C_D/2+2A_L+48B_\delta$.
The normalized field dependence is controlled by the allowed additive
term; (56) permits a flat-holonomy remainder as well as curvature.

### 13.3 Haar/heat-kernel amplitudes (Part 3)

Include the external old-face amplitude once: write $\mathcal J=J+B_{\rm amp}$
as one local edge term, one mid-face term and one old-face term per cell,
with background-independent constants removed. Define $D_J\ge1$ as the
maximum of their first block derivatives (in $z,\xi_i$) and second
$\xi$-block derivatives on §4's compact charts, uniformly for $0<t\le1/2$.
Section 4's analytic amplitude/image argument makes this supremum finite.
At $z=\xi=0$ all local values equal their identity-background values,
regardless of the transports. Incidence counting and (53) give

$$|\mathcal J(U,\xi_*)-\mathcal J(1,0)|
\le D_J(2\sum_p|z_p|+3\|\xi_*\|_{1,b})
\le\frac{38D_J}{7}\sum_p|z_p|.\tag{57}$$

For interpolation by $s\mathcal J$, impose also $9tD_J\le1/4$.
Its Hessian block row majorant is $9D_J$, and its saddle score is at
most $3D_J$ per edge. The proof of (55), now with $k=2$, gives
$M_2^2\le3t+3D_JtM_2$, hence
$M_2\le(\sqrt3+3D_J)\sqrt t$ for $t\le1$.
Thus the interpolated potential stays convex, and
$|\langle\mathcal J-\mathcal J(U,\xi_*)\rangle_s|
\le6D_J(\sqrt3+3D_J)N\sqrt t$.
Integrating in $s$, identity-normalizing, and using (57) proves, with
$Z_E^J=\int e^{-E_U/t-W_\eta-\mathcal J}$,

$$\left|-\log\frac{Z_E^J(U)}{Z_E^J(1)}-\mathcal D_0^{\rm cov}(U)\right|
\le C t^\alpha\sum_p(1+|z_p|^2/t),\qquad
C=C_0+\frac{19D_J}{7}+12D_J(\sqrt3+3D_J).\tag{58}$$

### Consequence for STATE

Equation (58) proves normalized weak P($1/2-\delta$) **against (47)**
for one barriered step on the equal-layer, zero-cut-flux slice, uniformly
in plane size, with free-cycle holonomies retained and explicit chart
smallness conditions. The bound allows zero additional coupling shifts.
The next cell-2 task is general boundary layers; comparison to the full
integral outside this chart (images/large fields), fixed-frame equivalence,
electric projection, iteration and stability under perturbed actions remain.
The present amplitude bound already includes images inside the compact chart.

## 14. Round 16: unequal layers and a quasi-local remainder

**GPT-6 Astra, 2026-09-29; written bounds, unrefereed.** The cut-face
identity is $P_eQ_e=U_{f_e}$ (series/parallel, Proposition 1, **passage**).
Consequently zero cut flux means $P_e=Q_e^{-1}$: after transporting both
layers to the mid-vertex frames, they coincide. Unequal layers in those
frames require cut flux. We treat $|X_e|\le\varepsilon$ below, and recover
the requested zero-cut-flux case by setting $X=0$.

**After refereeing §14 (Claude, 2026-09-29).** ACCEPT (59)--(62) and
(63); ACCEPT (64) as the conditional statement it is. The opening
observation corrects the round's prompt: in mid-vertex frames the
equal-layer slice *is* the zero-cut-flux slice, so unequal layers carry
temporal plaquettes, and (62) rightly budgets them with
$\sum_e(1+|X_e|^2/t)$. Checked: (59) against (29), with minimum
$2\langle w,Pw\rangle-S/8$ and value $2\langle z,Pz\rangle-\frac14\|z\|^2$ at $x=y=z$; the bridge
Hessian $4\Pi_b+4h_b\Pi_b^\perp$ from $SU(2)\cong S^3$ of radius 2, with deficit
$4(1-h_b)\approx|b|^2/12$; $|a_p|\le c_M\sum|b_e|^2$ from the second difference of the
face-log map and Cauchy--Schwarz over four edges; $\|a\|^2\le8c_M^2\varepsilon^2T$ with
each edge in two faces; (60) from $2\langle a,P(2w+a)\rangle$ and
$\|a\|\|w\|\le c_M\varepsilon(S+T)$; (61) with bridge trace norm $3\beta T$ against the
lower bound $3I$; the rectangle inside $|\xi_e|\le13\varepsilon/7<2\varepsilon$; the $31/7$ count
in the amplitude bound; and in (64) the constants of (21) at $\kappa=\frac12$,
$t/(4-\kappa)=2t/7$, $q=5/12$, with (20) satisfied because the spectrum of $H$
lies in $[4,8]$. One condition is missing from the list: $|Y_p|\le3\varepsilon$
uses $|a_p|\le4c_M\varepsilon^2\le2\varepsilon$, so add $2c_M\varepsilon\le1$. On Part 2:
(63) already makes the remainder face-local in size, $|\ell_p|\le2A_ut^\alpha$
within each face's budget; what stays open is the locality of its
*dependence* on $U$, which an effective action for the next step needs.
The three premises named at the end of §14.2 are the precise gap, and
the Gaussian barrier cost $b(U)$, of size $O(Ne^{-t^{-2\delta}/2})$, looks the
easiest of the three: the same interpolation applied to $sW_\eta$ with
(21)'s decay should localize it.

### 14.1 Unequal layers: reference and comparison (Part 1)

Write the endpoints as $m_{*e}\exp(\pm b_e/2)$, $|b_e|=|X_e|$, and
put $Y_p=\log m_{*\partial p}$, $w=(x+y)/2$, $a=Y-w$.
Here $x,y$ are the two transverse face logs in their common basepoint
frames; assume $|x_p|,|y_p|,|b_e|\le\varepsilon$. Keep all midpoint
cycles free. With $C=C_{m_*}$, $P=(8+CC^*)^{-1}$, $H=4+C^*C/2$,
the covariantization of (29), including its determinant, is

$$\begin{aligned}
E_w^{(2)}(\xi)&=2\|\xi\|^2+\tfrac14\|w+C\xi\|^2
 -\tfrac18(\|x\|^2+\|y\|^2),\\
\mathcal D_{xy}^{\rm cov}&=\tfrac1{2t}\langle x+y,P(x+y)\rangle
 -\tfrac1{8t}(\|x\|^2+\|y\|^2)+\tfrac12\log(\det H/\det H_1).
\end{aligned}\tag{59}$$

The actual energy is $E=\sum_e B(b_e,\xi_e)+\sum_p F(Y_p,O_{pe}\xi_e)
-(\|x\|^2+\|y\|^2)/8$, with the four signed rotations of §4.
Define $\beta$ as half the maximum of the suprema of
$\|D_b^2D_\xi^2B\|,\|D_b^2D_\xi^3B\|$ on §4's compact chart.
Evenness in $b$ and $B(0,\xi)=2|\xi|^2$ give
$\|D_\xi^2B-4I\|,\|D_\xi^3B\|\le\beta|b|^2$ there.
At zero the exact Hessian is $4\Pi_b+4h_b\Pi_b^\perp$,
$h_b=(|b|/4)\cot(|b|/4)$, with the continuous value at $b=0$;
the bridge gradient vanishes. Thus $\nabla E(0)=C^*Y/2$ exactly.

Let $M$ be the supremum of the second derivative of the local face-log
map in its four insertion blocks, using their sum norm, on the same
chart; set $c_M=M/2$. Taylor expansion of the two endpoint products
at insertion $\pm b/2$ cancels the linear terms and gives
$|a_p|\le c_M\sum_{e\in\partial p}|b_e|^2$.
Consequently, writing $S=\|x\|^2+\|y\|^2$ and $T=\sum_e|b_e|^2$,
$\|a\|^2\le8c_M^2\varepsilon^2T$ and
$\|Y\|^2\le S+16c_M^2\varepsilon^2T$; also $|Y_p|\le3\varepsilon$.

Put $K_u=\beta+56L_F+1$ and impose $3\varepsilon\le1/16$,
$K_u\varepsilon\le1/4$, $2\varepsilon<c_0\le1/16$ and
$\kappa_u=\beta\varepsilon^2+8L_F(3\varepsilon+4c_0)\le1/4$.
The proof of (43), with $Y$ replacing $z$, has Hessian row error
$\le K_u\varepsilon$ on the radius-$\varepsilon$ ball and initial
iterate $\|\xi_0\|_\infty\le3\varepsilon/4$. Its contraction gives
$\|\xi_*\|_\infty\le6\varepsilon/7$,
$\|\xi_*\|_{1,b}\le(8/7)\sum_p|Y_p|$ and
$\|\xi_*\|_2\le\sqrt2\|Y\|_2/3$. The classical comparison is

$$|\min E-\min E_w^{(2)}|\le C_{\rm cl}\varepsilon(S+T),\qquad
C_{\rm cl}=K_u(1+16c_M^2)+c_M+2c_M^2.\tag{60}$$

Indeed comparison first to $E_Y^{(2)}$ costs $K_u\varepsilon\|Y\|^2$;
the remaining difference is $2\langle Y,PY\rangle-2\langle w,Pw\rangle$,
bounded by $\|w\|\|a\|/2+\|a\|^2/4$ since $\|P\|\le1/8$.
For $A=\nabla^2E(\xi_*)$, (54)'s trace proof now gives

$$\left|\tfrac12\log\frac{\det A}{\det A_1}
-\tfrac12\log\frac{\det H}{\det H_1}\right|
\le C_D\sum_p|Y_p|+\tfrac\beta2 T,\qquad C_D=46L_F/7.\tag{61}$$

The bridge contributes trace norm $3\beta T$; all interpolating
Hessians exceed $3I$. The moments (55) survive with $\kappa_u$.
The Gaussian rectangle still lies in the barrier-free region because
$6\varepsilon/7+\varepsilon<2\varepsilon$. Equation (56) holds with
$A_L$ replaced by $A_u=A_L+(\beta/3)(8/3)^{3/2}$, accounting for
the cubic bridge remainder on $2N$ edges.
Enlarge $D_J\ge1$ to include the first derivatives in $b,Y,x,y$ and
the same second insertion derivatives of the local amplitudes. Then
(57)'s right side becomes
$D_J[\sum_e|b_e|+\sum_p(|x_p|+|y_p|)+(31/7)\sum_p|Y_p|]$.
With $9tD_J\le1/4$ the centered amplitude cost remains
$12D_J(\sqrt3+3D_J)N\sqrt t$ after identity normalization.

Thus, for $\alpha=1/2-\delta$, $0<\delta<1/6$, $t\le1/2$ and
$2e^{-t^{-2\delta}/2}\le1/2$, the full barriered normalized bound is

$$\left|-\log\frac{Z_E^J(U)}{Z_E^J(1)}-\mathcal D_{xy}^{\rm cov}\right|
\le C_u t^\alpha\left[\sum_p\left(1+\frac{|x_p|^2+|y_p|^2}{t}\right)
+\sum_e\left(1+\frac{|X_e|^2}{t}\right)\right],\tag{62}$$

where an explicit loose choice is
$C_u=1000(1+C_{\rm cl}+C_D+\beta+c_M+c_M^2+A_u+B_\delta+D_J+D_J^2)(1+c_M)$.
Use $\sum|Y|\le\frac12\sum(|x|+|y|)+2c_MT$ and §13's scalar
Young bound to assemble it. This is weak P($\alpha$) including the cut
faces, with zero extra coupling shifts. Setting $X=0$ gives $x=y=Y$
and (58) (the extra $2N$ is absorbed in its constant). For genuinely
unequal layers, the transverse-only target additionally needs control
of the explicit midpoint term $[2\langle Y,PY\rangle-2\langle w,Pw\rangle]/t$
and the cut contributions in (60)--(61) by that smaller budget.

### 14.2 Local densities and the remaining decay hypothesis (Part 2)

**Exact decomposition; spatial response conditional.** Taylor-expand each
face and bridge term at the actual saddle, assigning half of each edge
remainder to each adjacent face. This gives $R=\sum_pR_p$ exactly.
With $\mu_{\lambda,U}$ from §13.2 define

$$\ell_p(U)=-\int_0^1[\langle R_p\rangle_{\lambda,U}
-\langle R_p\rangle_{\lambda,1}]\,d\lambda,\qquad
|\ell_p(U)|\le2A_u\sqrt t\le2A_ut^\alpha.\tag{63}$$

Equation (55) proves this face by face with the same 16 cubic products
as before; half-edge assignment adds $\beta(8/3)^{3/2}/3$ to the constant.
Consequently $\sum_p\ell_p$ is precisely the identity-normalized
$\log(Z_E/Z_{2,W})$. Assign amplitudes to faces in the same way and put
$Q_p=\mathcal J_p(\xi)-\mathcal J_p(\xi_*)$. Integrating their expectations
along the $s\mathcal J$ interpolation gives densities $a_p$ for the
centered amplitude log-ratio, with
$|a_p|\le12D_J(\sqrt3+3D_J)\sqrt t$. These bounds imply the requested
value bound with $1+|z_p|^2/t$ on the equal-layer slice, even at $z_p=0$.
Their dependence on $U$ still comes through the full measure and saddle.

Here is the precise decay supplied by Theorem 5 **if its soft-barrier
realization condition holds uniformly along these interpolations**.
For a potential perturbation $\theta k_T$ supported in $T$, hold the
local Taylor coefficients and saddle fixed, and retain the convexity
bounds and, for $R$, (55)'s fourth moments throughout the perturbation. Set
$b_T=\sup\|\nabla k_T\|_{L^2}$ and $d=d(\partial p,T)$.
The derivative Taylor bound and (55) with $k=4$ give
$\|\nabla R_p\|_{L^2}\le A_R=(320/3)(L_F+\beta)$;
incidence counting gives $\|\nabla Q_p\|_{L^2}\le A_J=6D_J$.
Using $\kappa\le1/2$ (including amplitudes), (21) proves

$$|\partial_\theta\langle f_p\rangle|
=|\operatorname{Cov}(f_p,k_T)|
\le\tfrac{2t}{7}A_f b_T e^{-\gamma d},\qquad
\gamma=\log(12/5),\quad(f,A_f)=(R,A_R)\text{ or }(Q,A_J).\tag{64}$$

The uniformity in $\lambda,s$ permits integration; (25) sums remote
scores. For actual boundary changes the exact response also contains
$\langle\partial_\theta f_p\rangle$ and the score $\partial_\theta V$.
Their quasi-local bounds require compatible boundary coordinates:
$\partial_\theta\xi_*=-A^{-1}\partial_\theta\nabla E(\xi_*)$ has
Lemma 1 decay for a local link score, whereas independent face-log
variations require the additional transport control identified in §7.4.
Finally (56) also contains $b(U)-b(1)$, where $b(U)=\log(Z_{2,W}/G_U)$.
Its rectangle bound controls only the total cost. Completing the requested
quasi-local remainder requires a uniform soft-barrier realization of (22),
the boundary-score bounds just specified, and local densities for this
Gaussian barrier cost with summable decay and size $O(t^\alpha)$.
Equations (63)--(64) establish the local small densities and the conditional
response estimate; the full quasi-local assertion retains these premises.

### Consequence for STATE

Round 16 extends the barriered covariant value comparison to unequal
layers with their cut-face budget (62); zero cut flux recovers equal
layers in common frames. The cubic and centered amplitude remainders
have uniformly small face densities (63), with conditional decay (64).
Cell 2 next needs the soft-barrier realization, boundary-score and local
barrier-cost estimates specified in §14.2, followed by full-integral
comparison and perturbed-action stability; iteration remains open.

## 15. Round 17 (Claude): the barrier realization and local barrier cost

**Claude, 2026-09-29; written proofs, unrefereed.** Astra's round 17 was
stopped by the usage limit before writing (reset 06:35); Claude supplies
§14.2's premises (i) and (iii) here. With (i), the localized-increment
bounds (23)--(24) of §7.3 hold for the barriered measures themselves, which
reduces the quasi-local remainder to one kernel comparison (§15.3).
Notation and conditions are those of §§13--14; $\Lambda=L_F+\beta$.

**After refereeing §15 (GPT-6 Astra, 2026-09-29).** **REFINE** the
extension: block-row counting gives the sufficient constant 14000 in
(65), replacing 13000; the amplitude constant 770 survives. **REFINE**
the approximation: mollification preserves convexity and convergence,
with equality to the barrier required only in the limit. **ACCEPT**
(66), (55) for partially barriered Gaussians, and (67) with $k_t\ge2$.
**REFINE** the decay claim after (67): it requires boundary-score
control for the saddle Gaussian and a specified barrier profile.
**REFINE** §15.3: use enlarged score supports and the Gaussian of (59),
whose parameter scores can be quadratic. Corrections are made below;
premise (iii)'s small densities are proved, their full spatial response
remains conditional.

### 15.1 Premise (i): Theorem 5 for the barriered measures

**Assumption (E1).** §4's local bounds, with the constants
$L_F,\beta,D_J$, hold on the enlarged chart $|\xi_e|\le2c_0$. Since
$c_0\le1/16$, this chart stays far from the cut locus.

*Extension.* Split the potential of §§13--14 into face densities,
$S_{\lambda,s}=S_2+\sum_p(\lambda R_p+sQ_p)$, with half of each edge term
assigned to each adjacent face as in §14.2 and
$Q_p=\mathcal J_p(\xi)-\mathcal J_p(\xi_*)$. Fix a smooth radial
$\chi$ with $\chi=1$ for $|\xi|\le c_0$, $\chi=0$ for $|\xi|\ge2c_0$,
$|\chi'|\le2/c_0$, $|\chi''|\le8/c_0^2$, put
$\chi_p=\prod_{e\in\partial p}\chi(|\xi_e|)$ and
$\tilde S=S_2+\sum_p\chi_p(\lambda R_p+sQ_p)$ on $\mathbb R^{6N}$.
On the chart $D=\prod_eB(0,c_0)$, $\tilde S=S_{\lambda,s}$ up to a
constant. On ${\rm supp}\,\chi_p$, $|y_e|\le2c_0+6\varepsilon/7\le3c_0$, so
$\sigma_p=\sum_{e\in\partial p}|y_e|\le12c_0$ and the cubic remainder obeys
$t|R_p|\le\Lambda\sigma_p^3/6\le288\Lambda c_0^3$,
$t|\nabla_eR_p|\le72\Lambda c_0^2$ and
$t\sum_{e'}\|(\nabla^2R_p)_{ee'}\|\le48\Lambda c_0$.
The cutoff has $\|\nabla\chi_p\|\le8/c_0$ and block row sum
$\|\nabla^2\chi_p\|\le20/c_0^2$ (a radial Hessian is
$\chi''\Pi_r+(\chi'/r)\Pi_\perp$ with $r\ge c_0$ where $\chi'\ne0$). The product
rule gives the block row sum $t\|\nabla^2(\chi_pR_p)\|\le
(48+1152+5760)\Lambda c_0\le7000\Lambda c_0$. Here the two cross
terms cost $2\cdot288+8\cdot72=1152$.
For amplitudes, $|\nabla_eQ_p|\le3D_J/2$, $|Q_p|\le18D_Jc_0$ and
Hessian row sum at most $4.5D_J$: one face plus half an edge amplitude
per incident edge. Thus the product rule gives
$(4.5c_0+24+360)tD_J/c_0\le385tD_J/c_0$ for $c_0\le1/16$.
Each edge meets two faces. Hence, if

$$K_u\varepsilon+14000\,\Lambda c_0+770\,tD_J/c_0\le\tfrac12.\tag{65}$$

then $\|t\nabla^2\tilde S-6I\|\le\frac52$ on all of $\mathbb R^{6N}$, uniformly in
$\lambda,s\in[0,1]$, with range one because $S_2$ and each $\chi_pR_p,\chi_pQ_p$
couple only edges of one face. This is (20) with $\kappa=\frac12$. Since
$c_0>2\varepsilon=2t^\alpha$, the last term of (65) is at most $385D_Jt^{1/2+\delta}$.

*Approximation.* For integers $k$ with $c_0-1/k>\eta$, continue $w_\eta$
from $r_k=c_0-1/k$ by its tangent plus $k(r-r_k)^2/2$.
This is nonnegative, radial, convex and $C^1$, with bounded Hessian
for each $k$. Convolve in $\mathbb R^3$ with a nonnegative radial smooth
mollifier of radius $o(1/k)$, chosen to give local $C^1$ convergence
inside $D$; call the result $w_k$. Convexity and nonnegativity survive.
Then $\mu_k\propto e^{-\tilde S-\sum_ew_k(\xi_e)}$ satisfies Theorem 5's smooth
hypotheses and (20) with $\kappa=\frac12$, for every $k,\lambda,s$. As $k\to\infty$,
$e^{-w_k(\xi)}\to e^{-w_\eta(\xi)}1_{|\xi|<c_0}$ off the sphere $|\xi|=c_0$ (where
$w_\eta$ diverges), with domination by $e^{-\tilde S}$, integrable by uniform
convexity. So $\mu_k\to\mu$ in total variation (Scheffé). The functions
needed here for (21), (23), (24), (64), namely $\chi_pR_p$, $\chi_pQ_p$, and
cut-off local scores, are bounded with bounded gradients and agree with
the original ones on $D$. Their covariances and gradient norms therefore
converge: apply total variation to $f,g,fg$ and $|\nabla f|^2$,
then take square roots for the gradient norms. Finite sums at fixed $N$
are allowed; general unbounded observables need uniform integrability.
The bounds pass to the limit with the constants
$t/(4-\kappa)=2t/7$ and $q=5/12$.

**Consequence.** Under (E1) and (65), (21), (23), (24) and (64) hold
for every barriered interpolated measure of §§13--14. Premise (i) of
§14.2 is proved.

### 15.2 Premise (iii): local densities of the barrier cost

Order the edges $e_1,\dots,e_{2N}$ and let $\mu_{<j}$ be the Gaussian of §13.2
at the saddle, restricted by the barriers of $e_1,\dots,e_{j-1}$. Then exactly

$$b(U)=\log\frac{Z_{2,W}}{G_U}=-\sum_{j=1}^{2N}\tau_j(U),\qquad
\tau_j=-\log E_{\mu_{<j}}\bigl[e^{-w_\eta(\xi_{e_j})}\bigr]\ge0.\tag{66}$$

The proof of (55) applies to each $\mu_{<j}$: $S_2$ has the diagonal
dominance of $A$, and edges carrying a barrier contribute the
nonnegative term $y_e\cdot\nabla w_\eta(\xi_e)$. Since $w_\eta=0$ for
$|\xi|\le\eta=2\varepsilon$ and $|\xi_*|\le6\varepsilon/7$,
$E_{\mu_{<j}}[e^{-w_\eta}]\ge1-p_j$ with
$p_j\le P(|y_{e_j}|>8\varepsilon/7)\le M_k^{\rm bd}t^{k/2}(7/8\varepsilon)^k$.
With $\varepsilon=t^{1/2-\delta}$ this is $M_k^{\rm bd}(7/8)^kt^{k\delta}$. Take
$k+1=\lfloor3t^{-2\delta}/8\rfloor$; then $2(k+1)/3\le t^{-2\delta}/4$, so
$M_k^{\rm bd}\le2^{-k}t^{-k\delta}$ and

$$0\le\tau_j\le2p_j\le2(7/16)^{k_t},\qquad
k_t=\lfloor3t^{-2\delta}/8\rfloor-1,\tag{67}$$

provided $k_t\ge2$ (equivalently $t^{-2\delta}\ge8$), which also gives
$p_j\le(7/16)^2<1/2$. Thus the barrier cost splits into edge densities that
are super-polynomially small, below $t^\alpha$ for small $t$, and the
identity-normalized $b(U)-b(1)$ has densities $\tau_j(1)-\tau_j(U)$ of the
same size (both costs lie in $[0,2p_j^{\rm bd}]$). For a local
potential perturbation $h_R$, (24) bounds the derivative of $\tau_j$
by $(4t/7)q^{d(R,e_j)}\omega_\eta p_j^{1/2}\|\nabla h_R\|_2$;
the factor two uses $E e^{-w_\eta}\ge1/2$. Here
$\omega_\eta=\sup_r w_\eta'(r)e^{-w_\eta(r)}$ must be finite with
controlled $t$ dependence; a fixed polynomial-divergence profile supplies
this. For actual boundary changes, $A(U)$ and $\xi_*(U)$ in $S_2$
depend on the entire field. Their score needs a separate quasi-local
bound. Equation (66) establishes small densities independently of that bound.

### 15.3 What remains for the quasi-local remainder

With §15.1, §7.3's (23) applies to the barriered, amplitude-weighted
measure of $\mathcal D_s$ itself. In link coordinates a boundary change
alters only incident bridge and face potentials, so its score is local
(distance below is between these enlarged supports),
and the mixed second difference of $\mathcal D_s$ for changes in regions
$R,T$ is at most $(2t/7)\,ab\,(5/12)^{d(R,T)}$. The Gaussian reference
$\mathcal D^{\rm cov}_{xy}$ obeys (21) as a Gaussian measure with Hessian
$H/t$; differentiating its $C(U)$ gives quadratic as well as linear scores.
Lemma 1 alone handles the linear-score part. Each bound
separately is of order $\varepsilon^2(5/12)^d/t=t^{-2\delta}(5/12)^d$ for
changes of size $\varepsilon$, with no small factor. A quasi-local
remainder needs the difference $\mathcal D_s-\mathcal D^{\rm cov}_{xy}$ to gain
$t^\alpha$ there: this is the kernel estimate (27) of §7, now against the
covariant reference. Premise (ii) of §14.2 is used in the interpolation
form only; the direct route through (23) needs it for the actual
measure, where scores are local.

### Consequence for STATE

Premise (i) and the small-density part of (iii) hold under (E1) and (65), so the
Helffer--Sjöstrand bounds hold for the barriered measures and the barrier
cost is a sum of small edge densities. The remaining cell-2 step toward
iteration is the covariant kernel estimate: (27) for
$\mathcal D_s-\mathcal D^{\rm cov}_{xy}$ with the factor $t^\alpha$;
the saddle-Gaussian barrier densities retain their boundary-score obligation.

## 16. Transcription of §§12--15 to $SU(3)$ (Claude)

**Claude, 2026-09-29; written check, unrefereed.** The project's gap goal
is $SU(3)$, and the one-step bounds of §§12--15 use the group only through
the items below. With the normalization of this note,
$\langle X,Y\rangle=-2\operatorname{tr}XY$ (for $SU(2)$ the norm of $X$ is its
rotation angle, and $SU(2)\cong S^3$ has radius 2), every root obeys
$|\alpha(X)|\le|X|$ on $\mathfrak{su}(3)$: for $X=i\,{\rm diag}(\lambda_1,\lambda_2,\lambda_3)$,
$(\lambda_i-\lambda_j)^2\le2(\lambda_i^2+\lambda_j^2)\le|X|^2$. Hence $\|{\rm Ad}_{e^X}-I\|\le\|{\rm ad}_X\|\le|X|$, as for
$SU(2)$, and the curvature-to-holonomy bounds of (44), the $d\log$ bound
of §11.1 and Lemma 1 (orthogonal adjoint blocks) hold verbatim. Write
$n=\dim G$: $n=3$ for $SU(2)$, $n=8$ for $SU(3)$.

**After refereeing §16 (GPT-6 Astra, 2026-09-29).** **ACCEPT** the root
bound and the table's dimension, Sylvester, $B$, wrapping, $C_D$, moment,
$M_2$, bridge-Hessian (with the spectral convention below), bridge-trace
and $k_t$ rows. **REFINE** the Šidák row: the exponent is $3/16$ for
eight components. **REFINE** the flux row by fixing the Fourier sign.
**ACCEPT** the clock-and-shift spectrum and its lower bound, using the
complexified adjoint basis. **REJECT** the identification of this
two-dimensional magnetic twist with a four-dimensional fractional charge.
**REFINE** the bridge-tail arithmetic to $43/15$ and propagate dimension
changes into the remainder constants. Corrections are made in place.

| Item | $SU(2)$ | $SU(3)$ | Reason |
|---|---|---|---|
| mid-plane coordinates | $\mathbb R^{6N}$ | $\mathbb R^{16N}$ | $2N$ edges $\times\,n$ |
| Sylvester factor in (48) | $8^{3N}$ | $8^{8N}$ | edge minus face dimension, $nN$ |
| $B$ in (48) | $\frac34256^2\cdot\frac{33}8$ | $2\cdot256^2\cdot\frac{33}8=540\,672$ | $n-\operatorname{tr}R=\frac12\|R-I\|_F^2\le\frac n2\|R-I\|^2$ for $R\in SO(n)$ |
| wrapping term in (48) | $\frac92N3^{-n_{\min}}$ | $12N3^{-n_{\min}}$ | $|\operatorname{tr}(R-I)|\le2n$ |
| $C_D$ in (54) | $\frac{46}7L_F$ | $\frac{368}{21}L_F$ | face rank $4n$; $C_D=\frac{4n}6\cdot\frac{23}7L_F$ |
| moment bound (55) | $[2(k+1)/3]^{k/2}$ | $[2(k+6)/3]^{k/2}$ | ${\rm div}(|y|^{k-2}y)=(k+n-2)|y|^{k-2}$ in $\mathbb R^n$ |
| Šidák term in (56) | $48Ne^{-t^{-2\delta}/2}$ | $128Ne^{-3t^{-2\delta}/16}$ | rectangle radius $\varepsilon/\sqrt n$, variance $\le t/3$ |
| $k=2$ bound in §13.3 | $M_2\le(\sqrt3+3D_J)\sqrt t$ | $M_2\le(2\sqrt2+3D_J)\sqrt t$ | $\langle y\cdot\nabla V\rangle=n$ |
| bridge Hessian (§14) | $4\Pi_b+4h_b\Pi_b^\perp$ | $4f({\rm ad}_{b/2})$ | $f(\theta)=\frac\theta2\cot\frac\theta2$ on the pairs $\pm i\theta$ of ${\rm ad}_{b/2}$, $f=1$ on its kernel |
| bridge trace in (61) | $\frac\beta2T$ | $\frac43\beta T$ | rank $n$ per edge: $\frac n6\beta T$ |
| $k_t$ in (67) | $\lfloor3t^{-2\delta}/8\rfloor-1$ | $\lfloor3t^{-2\delta}/8\rfloor-6$ | same choice with $k+n-2$ |
| centre and fluxes (§12.3) | $\mathbb Z_2$; $\frac14\sum_k(-1)^{e\cdot k}Z_{k,m}$ | $\mathbb Z_3$; $\frac19\sum_k\omega^{-e\cdot k}Z_{k,m}$ | convention $Z_{k,m}=\sum_e\omega^{e\cdot k}Z_{e,m}$ |

The constants $L_F,\beta,M,D_J$ of §4 and §14 are finite on the $SU(3)$
chart by the same analyticity; their values change and are left symbolic.
The bridge function means $f(i\theta)=(\theta/2)\cot(\theta/2)$.
Use $k_t\ge2$, $2e^{-3t^{-2\delta}/16}\le1/2$ for $SU(3)$;
replace $(8/3)^{3/2}$ by $6^{3/2}$ in $A_L,A_u$, and $\sqrt3$ by
$\sqrt8$ in amplitude costs. In $B_\delta$ replace it by
$[\alpha/(2\delta c e)]^{\alpha/(2\delta)}$, $c=3/16$.
These substitutions and the table apply when assembling $C_0,C,C_u$.

**Twisted flat sector.** For $m=1\in\mathbb Z_3$ take the clock and shift
matrices $\Gamma_2=P={\rm diag}(1,\omega,\omega^2)$ and $\Gamma_3=Q$, $Qe_j=e_{j+1}$. Both lie in
$SU(3)$ (a 3-cycle is even), and $PQ=\omega QP$. The eight traceless
matrices $Q^aP^b$, $(a,b)\in\mathbb Z_3^2\setminus\{0\}$, span $\mathfrak{sl}_3$, and
${\rm Ad}_P(Q^aP^b)=\omega^aQ^aP^b$, ${\rm Ad}_Q(Q^aP^b)=\omega^{-b}Q^aP^b$. The joint phases in (51) are
therefore $(\phi_2,\phi_3)=(2\pi a/3,-2\pi b/3)$ over all eight nonzero pairs:
as for $SU(2)$ at $m=1$, the twisted sector has no adjoint zero mode, and
$L_m\ge2-2\cos(2\pi/(3n_{\max}))>0$ there, since each mode has a phase
$\pm2\pi/3$ in at least one direction. For $m=0$, commuting Cartan
transitions give phases $0$ (twice) and $\pm\alpha(\theta)$ for the three
positive roots. The [centre note](sun-midpoint-centre.md) separately
identifies central images at trisections. A four-dimensional fractional
topological charge requires four-dimensional twist data; this magnetic
two-torus calculation supplies its adjoint spectrum only.

**Lemma 2 for any compact group.** Lemma 2's explicit tail,
$k_t\le C_+t^{-5/2}e^{-\theta^2/(2t)}$, comes from the $SU(2)$ image formula. §§13--15
do not use it; the large-field step and the bridge tail (7) do. A
bi-invariant metric has ${\rm Ric}(X,X)=\frac14\sum_i|[X,e_i]|^2\ge0$, so the Li--Yau
bounds for ${\rm Ric}\ge0$ apply
([Li and Yau 1986](https://doi.org/10.1007/BF02399203), Acta Math. 156,
153--201; Crossref metadata verified 2026-09-29; **passage**, Theorems
3.2 and 4.2 in the [original-paper transcription](https://paperzz.com/doc/6929746/on-the-parabolic-kernel-of-the-schrodinger-operator---shing),
checked 2026-09-29): for
every $\epsilon'\in(0,1)$ and $0<t\le1$, in this note's normalization
($e^{t\Delta/2}$, small balls of volume comparable to $t^{n/2}$),
$$c_{\epsilon'}t^{-n/2}e^{-d^2/((2-\epsilon')t)}\le k_t(g)\le C_{\epsilon'}t^{-n/2}e^{-d^2/((2+\epsilon')t)},\qquad d=d(g,1).$$
The proof of (7) then gives, for the bridge midpoint at distance
$\rho\ge r$ from $m_*$,
$\beta\{d(m,m_*)\ge r\}\le C'_{\epsilon'}t^{-n/2}\exp\{-[4(r-|X|/2)^2/(2+\epsilon')-|X|^2/(2-\epsilon')]/t\}$,
which at $\epsilon'=0$ is (7)'s exponent $2r(r-|X|)/t$. At $r=2\varepsilon$, $|X|\le\varepsilon$,
$\epsilon'=\frac12$, the gain is $e^{-43\varepsilon^2/(15t)}$ since
$9/(5/2)-1/(3/2)=43/15$, for each fixed compact simple group,
with group-dependent non-explicit constants. The
exact image formula of the [centre note](sun-midpoint-centre.md) would
give explicit constants and the sharper prefactor $t^{-n/2-|\Delta_+|}$ ($t^{-7}$
for $SU(3)$, $t^{-5/2}$ for $SU(2)$ as in (5)); that refinement is conjectural
here. The bulk order-$t$ coefficients of
the [order-$t$ note](su2-midplane-order-t.md) scale by the adjoint-Casimir
ratio, $\frac32$ for $SU(3)$ (§7b there).

**Consequence for STATE.** The one-step normalized small-field bounds of
§§13--15 hold for $SU(3)$ in the same $1+2$ mid-plane setting with the
constants tabulated above, and the bridge tail needed for the large-field
step holds for $SU(3)$ by Li--Yau with non-explicit constants; the $\mathbb Z_3$
flux sectors follow 't Hooft's projection with the clock-and-shift
representative.

## 17. Round 17b: shrinking chart and the remaining resolvent term

**GPT-6 Astra, 2026-09-29; written reduction.** The proposed chart
$c_0=3\varepsilon$ makes the smooth Hessian error small. 

**After refereeing §17 (Claude, 2026-09-29).** ACCEPT as a reduction.
The identity (68)--(69) checks: with $f_a=\nabla\partial_aS$, $g_a=\nabla\partial_aV_2$ and
(22), the covariance difference splits as the two score-difference terms,
$t\langle g_a,(R_\mu-R_0)g_b\rangle_\mu$ with $R_\mu-R_0=-R_\mu(\Delta+tW_k'')R_0$, and the
change of Hilbert space $\mathcal M$; the smooth insertion carries
$C_*\varepsilon$. I also accept the corrections to §§15--16 made in round 17b:
the Šidák exponent $3t^{-2\delta}/16$ for eight components, the constant 14000,
the gain $43/15$, and the rejection of my identification of the
two-dimensional $\mathbb Z_3$ twist with a four-dimensional fractional charge.
Two routes for (69), offered for the next round. (a) For $\mathcal B$, use the
barrier's own square root: since $tL_\mu+tS''\ge0$,
$\|(tW_k'')^{1/2}R_\mu^{1/2}\|\le1$, so
$|\mathcal B_{ab}|\le t\,\|R_\mu^{1/2}g_a\|_\mu\,\|(tW_k'')^{1/2}R_0g_b\|_\mu$. The last factor is an
expectation of $tW''$ against $|R_0g_b|^2$, supported where some $|\xi_e|>\eta=2\varepsilon$,
which (55) makes rare at rate $(7/16)^{k_t}$; integration by parts against
$e^{-W}$ trades $w''$ for $w'^2$ and boundary decay, and $R_0g_b$ decays from $b$ by
Theorem 5's Neumann bound, so a weighted estimate of size
$q^{d(a,b)}(7/16)^{k_t/2}$ times score norms looks within reach, uniformly in
$k$. (b) For $\mathcal M$, interpolate $G\to\mu$ as in §13.2 (same barrier added at
both ends through the approximants): the constant parts of the scores
cancel exactly, as noted, and the linear parts give second moments whose
change along the path is a third cumulant against $V-V_2$, bounded by (55)
and the $C_*\varepsilon$ Hessian deviation. The direct
resolvent proof still requires the barrier insertion (69) below.
Write $V=S+W_\eta$, with $S$ the extension in §15.1, and $H$ from (59).
For $6\varepsilon\le1/16$, (E1) and the earlier smallness conditions,
(65) becomes $(K_u+42000\Lambda)\varepsilon+(770/3)D_Jt/\varepsilon\le1/2$.
Since $t/\varepsilon\le\varepsilon$, set
$C_* =K_u+42000\Lambda+(770/3)D_J$. Then globally
$\|tS''-H\|_{\infty,b}\le C_*\varepsilon$; the norm is
$\sup_e\sum_{e'}\|M_{ee'}\|$. This includes $A-H$ and the amplitudes.
The full Hessian is $tV''=tS''+tW_\eta''$, whose last term is unbounded.

**Normalization and identity.** A unit parameter changes one boundary
link at velocity $\varepsilon UT$, $|T|=1$ in the $-2\operatorname{tr}$
metric. Let $V_2=E_w^{(2)}/t$, $G\propto e^{-V_2}$, and
$f_a=\nabla_\xi\partial_a S$, $g_a=\nabla_\xi\partial_a V_2$.
For $d(a,b)\ge2$ in the link graph, the local mixed potential derivative
vanishes; thus $K_{ab}=\partial_a\partial_b(\mathcal D_s-\mathcal D^{\rm cov})$
is minus the difference of score covariances. Scores have support radius
one. The requested remote bound is
$\sup_a\sum_{b:d(a,b)\ge2}e^{\gamma d(a,b)}|K_{ab}|\le C\varepsilon^3/t$;
unscaled link derivatives divide this by $\varepsilon^2$.

Work first with the smooth barrier approximants, and write
$R_\mu=[tL_\mu+tS''+tW_k'']^{-1}$,
$R_0=[tL_\mu+H]^{-1}$, $R_G=[tL_G+H]^{-1}$ and $\Delta=tS''-H$.
Both $R_\mu,R_0$ act in the **same** $L^2(\mu_k)$; Theorem 5's
Neumann argument bounds each edge block by $(2/7)(5/12)^d$.
With $\gamma=\frac12\log(12/5)$ their weighted block-row norms are at
most $R_\gamma=(2/7)C(5/12)$, with the explicit series (25).
The resolvent identity, followed by (22), gives exactly
$$\begin{aligned}
-K_{ab}={}&t\langle f_a-g_a,R_\mu f_b\rangle_\mu
+t\langle g_a,R_\mu(f_b-g_b)\rangle_\mu\\
&-t\langle g_a,R_\mu\Delta R_0g_b\rangle_\mu
+\mathcal B_{ab}+\mathcal M_{ab}.\end{aligned}\tag{68}$$
$$\begin{aligned}
\mathcal B_{ab}&=-t^2\langle g_a,R_\mu W_k''R_0g_b\rangle_\mu,\\
\mathcal M_{ab}&=t\langle g_a,R_0g_b\rangle_\mu
-t\langle g_a,R_Gg_b\rangle_G.\end{aligned}\tag{69}$$
Here at finite $k$, $-K$ denotes the score-covariance difference;
bounded local score extensions recover the physical kernel in the limit.
The smooth insertion has operator bound
$\|R_\mu\Delta R_0\|_{\infty,b,\gamma}\le
R_\gamma^2 e^\gamma C_*\varepsilon$, since $\Delta$ has range one.
This supplies the desired small factor in that term. Even granting the
score-gradient estimates from Taylor expansion and (55), (69) remains.
Theorem 5 controls $R_\mu$ by the **sign** of $W_k''$; it supplies
no vanishing bound on its sandwiched insertion, uniformly in $k$.
The multiplication norm of $tW_\eta''$ is infinite at every $t>0$.
The term $\mathcal M$ retains the change of measure and diffusion:
$L_\mu-L_G=\nabla(V-V_2)\cdot\nabla$. For constant $g_a,g_b$ it
vanishes because $R_0g_b=H^{-1}g_b$; actual link scores also have
linear gradients from $\partial_aH$, so this simplification covers only
their constant parts. A uniform weighted bound of size $\varepsilon^3/t$
on $\mathcal B+\mathcal M$ is the precise missing estimate in this route.
Equation (68) records a proof obligation, rather than a counterexample
to the requested kernel bound; changing Hilbert spaces silently would omit it.

**Tail cost of the smaller chart.** For the partially barriered saddle
Gaussian with the tested edge still free, (55) and §15.2's $k_t\ge2$
give $P(|\xi_e|\ge2\varepsilon)\le(7/16)^{k_t}$ and
$P(|\xi_e|\ge3\varepsilon)\le(7/30)^{k_t}$, using
$|\xi_*|\le6\varepsilon/7$. A union bound costs $2N$.
Thus the annulus above $3\varepsilon$ joins the large-field problem;
these reference tails leave comparison with the full group integral open.

### Consequence for STATE

Round 17b refines §§15--16 and isolates (69) as the next cell-2 estimate:
control the barrier insertion and change of measure with weighted size
$C\varepsilon^3/t$, uniformly in plane size and barrier approximation.
Full-integral comparison and perturbed-action stability follow that task;
the covariant kernel bound and iteration remain open.

## 18. Round 18: the barrier insertion and the change of measure

**GPT-6 Astra, 2026-09-29; written route tests, unrefereed.** The
square-root route gives (70), with the remaining weighted moment
specified in (72). The interpolation route is tested separately below.

**After refereeing §18 (Claude, 2026-09-29).** ACCEPT as route tests
with correctly identified residuals. Checked: (70) from $T_k\le R_\mu^{-1}$ and
$R_\mu\le\frac27$ (the smooth part of $tV''$ is at least $\frac72$); (74) for a constant
score paired with an affine one; (75) from the Lyapunov equation
$HD_b+D_bH=B_b$ and $tL_\nu(D_by)=D_bHy+tD_b(\lambda\nabla T+\nabla W_k)$. Both residuals, the
barrier-weighted fourth moment (72) and the moving-diffusion term $J_{ab}$ of
(73), are higher-moment and derivative bounds on Helffer--Sjöstrand
resolvent solutions. That problem has a literature for uniformly convex
gradient models: [Naddaf and Spencer 1997](https://doi.org/10.1007/BF02509796)
introduced the random-walk representation, and
[Delmotte and Deuschel 2005](https://doi.org/10.1007/s00440-005-0430-y)
estimate derivatives of the corresponding kernels in stationary random
environments with applications to the $\nabla\phi$ interface model (Crossref
metadata verified 2026-09-29; results recalled, not read here). Their
hypotheses are uniform ellipticity of the edge couplings; here the
couplings are uniformly elliptic ($\frac72\le$ smooth part $\le\frac{17}2$ in block norm)
and the barrier enters only on the diagonal of the edge index. (Round 19,
§19.1, corrects the next step of this remark: in $R_0$ the barrier enters
the drift, and it acts as killing only in $R_\mu$ and in the differentiated
equation; positivity of the block Hessian alone supplies no scalar
random-walk conductances.)
The next round should test whether their annealed estimates, with this
killing term, give (72) and $J_{ab}$ uniformly in $k$.
All operators and score normalizations are those of §17; $c_0=3\varepsilon$,
$\eta=2\varepsilon$, $q=5/12$ and $p_t=(7/16)^{k_t}$.

### 18.1 Part 1: the barrier's square root

Put $u_a=R_\mu g_a$, $v_b=R_0g_b$ and $T_k=tW_k''\ge0$.
The form inequality $T_k\le R_\mu^{-1}$ gives exactly
$$|\mathcal B_{ab}|\le t\|R_\mu^{1/2}g_a\|_\mu Q_b^{1/2},\qquad
Q_b=t\sum_e E_\mu[v_{b,e}^{T}w_k''v_{b,e}],\qquad
\|R_\mu^{1/2}g_a\|_\mu\le\sqrt{2/7}\|g_a\|_\mu.\tag{70}$$
This estimate retains the small-tail question in $Q_b$ and loses the
separation from $a$; recovering spatial decay requires an edge-local
version before the final Cauchy--Schwarz step.

Here is the proposed integration by parts, including its derivative
terms. Write $v=v_{b,e}$, $h=\nabla_e w_k$, $A=\nabla_eS$, and let
$D_ev$ and $\operatorname{div}_ev$ differentiate only $\xi_e$.
Integrating $\sum_{ij}\partial_j(v_iv_j\partial_iw_k)e^{-S-W_k}$ gives
$$E_\mu[v^Tw_k''v]=E_\mu[(v\cdot h)^2+(v\cdot h)(v\cdot A)
-h\cdot((D_ev)v+v\operatorname{div}_ev)].\tag{71}$$
One may first cut off $v$ and then pass to the limit when these terms
are integrable. Equation (71) exhibits the positive Fisher term
$E[(v\cdot h)^2]$, together with barrier-weighted derivatives of $v$.
Boundary decay removes the surface integral; bounding the surviving
terms still requires weighted integrability of the resolvent solution.

For a concrete profile choose $w_\eta(r)=x^4$, $x=(r-\eta)_+/(c_0-r)$
inside the ball. This is convex and $C^2$, and has polynomial divergence.
With $a_j=(j/(2\mathrm e))^{j/4}$, direct differentiation gives
$\sup w_\eta'e^{-w_\eta/2}\le\Omega_0/\varepsilon$ and
$\sup\|w_\eta''\|e^{-w_\eta/2}\le K_0/\varepsilon^2$, where
$\Omega_0=4(a_3+2a_4+a_5)$ and
$K_0=12a_2+58a_3+100a_4+74a_5+20a_6$.
In particular $\omega_\eta\le\Omega_0/\varepsilon$.
For approximants the needed additional profile hypothesis is the same
weighted-Hessian bound, uniformly in $k$, with a specified constant
$K_{\rm app}$ replacing $K_0$; local $C^1$ convergence alone supplies less.
Mollification enlarges the active set to $r>\eta-\rho_k$, where $\rho_k$
is its radius. Tail estimates must use this threshold before taking limits.

The precise missing moment can also be seen without differentiating $v$.
Let $\nu_{e,k}$ remove only the barrier on edge $e$ from $\mu_k$, and put
$A_{e,k}=\{|\xi_e|>\eta-\rho_k\}$, $p_{e,k}=\nu_{e,k}(A_{e,k})$.
Local reweighting and Cauchy--Schwarz give, under the profile hypothesis,
$$E_{\mu_k}[v_{b,e}^Tw_k''v_{b,e}]
\le {K_{\rm app}\over\varepsilon^2(1-p_{e,k})}
 p_{e,k}^{1/2}\bigl(E_{\nu_{e,k}}|v_{b,e}|^4\bigr)^{1/2}.\tag{72}$$
Even granting $p_{e,k}\le2p_t$ and $1-p_{e,k}\ge1/2$, this needs an
$L^4(\nu_{e,k})$ bound on $v_{b,e}$, uniform in $e,k,N$, with spatial decay.
For the partially barriered saddle Gaussian the tail follows from (55),
with sufficiently small $\rho_k$; transferring it to the extended,
amplitude-weighted $\nu_{e,k}$ also needs its moment argument.
Theorem 5 bounds $\|v_{b,e}\|_{L^2(\mu_k)}\le(2/7)q^{d(e,T_b)}\|g_b\|_\mu$,
where $T_b$ is the enlarged score support. Its norm and measure differ
from the fourth moment in (72). The removal density is proportional to
$e^{w_k}$, so this change of norm has no uniform bounded-density shortcut.
Thus (71)--(72) identify the failing term of this route: the local
barrier-weighted resolvent moment. Finite Fisher information for each
fixed barrier and total-variation convergence in §15.1 leave its uniform
$k\to\infty$ bound, and the weighted estimate for $\mathcal B$, open.

### 18.2 Part 2: interpolate the measure and the diffusion

Fix the boundary parameters and $k$. Set $T=S-V_2$,
$\nu_\lambda\propto e^{-V_2-\lambda T-W_k}$,
$A_\lambda=tL_{\nu_\lambda}+H$, $u_{\lambda,b}=A_\lambda^{-1}g_b$ and
$F_{ab}(\lambda)=tE_{\nu_\lambda}[g_a\cdot u_{\lambda,b}]$.
Differentiating the density and $A_\lambda u_{\lambda,b}=g_b$, with
$A_\lambda'=t\nabla T\cdot\nabla$, gives the exact finite-$k$ identity
$$F_{ab}'=-t\operatorname{Cov}_{\nu_\lambda}(g_a\cdot u_{\lambda,b},T)
-t^2E_{\nu_\lambda}[u_{\lambda,a}\cdot(\nabla T\cdot\nabla)u_{\lambda,b}].\tag{73}$$
Smooth cutoffs justify differentiation first; passage to the polynomial
scores requires the displayed integrability. The second term records
how the inverse changes with the drift, even though $H$ is fixed.
Adding the same barrier at both ends leaves the endpoint correction
$F_{ab}(0)-t\langle g_a,R_Gg_b\rangle_G$ in $\mathcal M$.

Write $y=\xi-m_0$, where $m_0=E_G\xi$, and $g_b=c_b+B_by$;
$B_b=(\partial_bH)/t$ for the quadratic parameter score. For two
constant gradients, $u_b=H^{-1}c_b$ pointwise and both terms in (73)
vanish. For a constant $c_a$ paired with an affine $g_b$, integrating
$A_\lambda u_b=g_b$ gives instead
$$F_{ab}(\lambda)=t c_a^TH^{-1}(c_b+B_bE_{\nu_\lambda}y),\qquad
F_{ab}'=-t c_a^TH^{-1}B_b\operatorname{Cov}_{\nu_\lambda}(y,T).\tag{74}$$
Thus cancellation covers the constant--constant part exactly; the mixed
parts require control of the moving mean. The centered second moment
$\Sigma_{ij}=\operatorname{Cov}_{\nu_\lambda}(y_i,y_j)$ does satisfy
$\Sigma_{ij}'=-\operatorname{cum}_{\nu_\lambda}(y_i,y_j,T)$, where the
cumulant is $E[(y_i-Ey_i)(y_j-Ey_j)(T-ET)]$.

A direct affine calculation locates the additional resolvent term.
Let $HD_b+D_bH=B_b$, so
$D_b=\int_0^\infty e^{-rH}B_be^{-rH}\,dr$ and
$\|D_b\|\le\|B_b\|/7$ using $H\ge7I/2$.
Then $v_b=H^{-1}c_b+D_by=R_Gg_b$ and, exactly,
$$u_{\lambda,b}=v_b-tA_\lambda^{-1}D_b(\lambda\nabla T+\nabla W_k).
\tag{75}$$
Indeed $tL_{\nu_\lambda}(D_by)=D_bHy+
 tD_b(\lambda\nabla T+\nabla W_k)$, which proves (75).
Consequently a moment-only interpolation would omit the last term of
(75). At $\lambda=0$ it already contains the barrier endpoint correction.
The small edge costs (67) bound partition-function values; their second
boundary derivatives require the response estimates sought here.

For the smooth path, the precise extra term in (73) is
$J_{ab}=t^2\sum_{ij}E[u_{\lambda,a,i}(\partial_jT)
\partial_j u_{\lambda,b,i}]$, with scalar coordinate indices $i,j$.
Hölder gives
$$|J_{ab}|\le t^2\sum_{ij}\|u_{\lambda,a,i}\|_4\|\partial_jT\|_4
\|\partial_j u_{\lambda,b,i}\|_2.$$
The bounds (55) control local polynomial moments, and
$\|tT''\|_{\infty,b}\le C_*\varepsilon$ controls smooth local coefficients.
Theorem 5 supplies edge-index $L^2$ decay for $u$; closing this estimate
requires spatially summable bounds also in its differentiation index $j$,
with the displayed higher norms uniform in $k$. The first term of (73)
likewise involves $u_b$, rather than just a quadratic polynomial.
Equations (73)--(75) identify the failing terms of the proposed
third-cumulant shortcut and retain the barrier endpoint explicitly.
A bound $C\varepsilon^3/t$ on the weighted norm of $\mathcal M$ therefore
remains an obligation, alongside the weighted moment (72).

### 18.3 Part 3: consequence for STATE

The round closes the two route tests with explicit residual terms:
(72) for the barrier insertion, and (73)--(75) for the measure and
diffusion change, including the barrier endpoint. Cell 2 next needs
weighted resolvent moment and derivative estimates uniform in the plane
and $k$, or a direct covariance comparison that controls these terms
together. The covariant kernel estimate (27), its constant, and the
quasi-local remainder required by §§14.2 and 15.3 remain open;
full-integral comparison and perturbed-action stability follow that step.

## 19. Round 19: semigroup representation and the applicability test

**GPT-6 Astra, 2026-09-29; written proofs, unrefereed.** The finite-$k$
representation gives uniform pointwise bounds for bounded local scores.

**After refereeing §19 (Claude, 2026-09-29).** ACCEPT (76)--(78) and the
replacement lemma (80) as a conditional result. Checked: (76) because $H$
is configuration-independent and commutes with the diffusion generator;
the pointwise bound (77) from $\int_0^\infty e^{-5s}e^{sC}ds=(5-C)^{-1}$, which removes
the fourth-moment question of (72) for bounded scores; (78) by
differentiating $\nabla V\cdot\nabla u$, so only $V''$ enters, with the two-index base
$tL+10I$ plus a nonnegative right multiplication; (81) by removing one
edge's barrier; the scale bookkeeping in (80). Most of (79) is already in
hand. The deterministic majorant $C^S$ with sums at most $\frac72$ follows from
§17's $\|tS''-H\|_{\infty,b}\le C_*\varepsilon\le\frac12$. The proof of (55) uses only diagonal
dominance and the sign of the barrier terms on the edges that carry
barriers, so it applies verbatim to the removed-edge measures $\nu_{e,k}$ and
to the interpolated $\nu_\lambda$; it gives $p_{e,k}\le2(7/16)^{k_t}$ for small $\rho_k$, hence
$p/(1-p)\le P\varepsilon^3/t$ for small $t$, and
$E|\nabla_eT|\lesssim\Lambda(1+\varepsilon/\sqrt t)$, far inside $L\varepsilon/t$. The profile constants
$K_{\rm app},\Omega_{\rm app}$ are a choice of approximants (the $x^4$ profile of §18 and its
mollifications). What remains is the score-extension step: extended
scores with the stated marginal constants and a Gaussian covariance error
$E_0\varepsilon^3/t$ against the original ones. With it, (80) gives the covariant
kernel estimate (27) at decay exponent $\frac12\log(10/7)$.
A concrete replacement lemma below uses local drift moments and score
extensions to close the comparison conditionally, including its barrier
endpoint. These additional inputs remain to be established for §17.

### 19.1 Part 1: the representation and its test

Fix $k,N,t>0$, write $V=S+W_k$, and let
$dX_s=-t\nabla V(X_s)\,ds+\sqrt{2t}\,dB_s$.
Its generator is $-tL_\mu$. Since $H$ is configuration-independent,
$$R_0g(x)=\int_0^\infty e^{-sH}E_x[g(X_s)]\,ds.\tag{76}$$
Indeed the two generators commute; integrating their semigroup gives
$(tL_\mu+H)^{-1}$. For a variable matrix potential $K(x)$ replace
$e^{-sH}$ by the ordered multiplicative functional $U_s$, with
$U_0=I$, $\dot U_s=-U_sK(X_s)$, inside the expectation.
This is the matrix Feynman--Kac representation; bounded-Hessian finite-$k$
approximants justify it by the product formula and differentiation.

For plane side lengths at least three, (59) gives $H_{ii}=5I$ and
off-diagonal block-row sum at most $3$ (six incidences of size $1/2$).
Thus $C_{ij}=\|(H-5I)_{ij}\|$ has row and column sums at most $3$.
The spectral $5/2$ bound about $6I$ in Theorem 5 concerns sums of
signed products; absolute path counting requires this different bound.
The series for $e^{-sH}$ is dominated blockwise by $e^{-5s}e^{sC}$.
It can be read as a continuous-time walk with nonnegative jump weights,
including holding weights, and killing at least $2$. The original
colour matrices carry signs and rotations; their spectral bounds alone
supply no positive random-walk transition rates. In particular the
barrier occurs in the **drift** of (76); the extra barrier killing belongs
to $R_\mu$ and to the differentiated equation. The literature analogy
in Claude's §18 paragraph therefore requires this distinction.

For this section set $\gamma=\frac12\log(10/7)$ and
$m=5-(7/2)e^\gamma>0$, a weaker weight than §17's.
For $K^H=(5I-C)^{-1}$, range one and the geometric series give
$$\sup_i\sum_j e^{\gamma d(i,j)}K^H_{ij}\le m^{-1},\qquad
\|(R_0g)_i\|_\infty\le\sum_jK^H_{ij}\|g_j\|_\infty.\tag{77}$$
The second inequality bounds every $L^4(\nu_{e,k})$ norm as well,
independently of its density relative to $\mu_k$. All $t$-dependence
here is in the score size; the resolvent constants are dimensionless.

For $u=(tL_\nu+H)^{-1}g$, let $Z_{ij}=\partial_j u_i$ in edge blocks.
Differentiation gives the closed equation
$$tL_\nu Z+HZ+Z(tV'')=Dg.\tag{78}$$
Thus first configuration derivatives require $V''$, rather than $V'''$.
If $tS''-5I$ has a deterministic range-one block majorant $C^S$ with
row and column sums at most $7/2$, the two-index Neumann series has
base $tL+10I+tW_k''$ on the differentiation index, and perturbation
weighted norm at most $7e^\gamma$. Its inverse has weighted row and
column sums at most $(2m)^{-1}$ on the product graph. The positive
on-site matrices $t w_k''$ are contractions in each colour block.
This proves summable derivative bounds from bounded, summable $Dg$,
uniformly in $k,N$. A spectral norm bound alone would lose this block
majorant information. The affine scores of (74) have bounded $Dg$ but
unbounded $g$ on the approximating whole space. Hence (77) directly
settles the bounded-score case; its application to those affine scores
needs a score extension or a moment argument. Part 2 states the former
as a precise replacement, rather than assuming an annealed theorem.

### 19.2 Part 2: a replacement lemma with local inputs

**Replacement lemma (conditional).** Use smooth local score potentials
with bounded gradients $g_a$, agreeing with the quadratic scores on
$D$. For arrays $A_{ai}=\|g_{a,i}\|_\infty$ and
$D_{aij}=\|\partial_jg_{a,i}\|_\infty$ (Euclidean and Frobenius norms),
assume every one-index marginal sum is bounded by $G=G_0\varepsilon/t$
and $D_*=D_0\varepsilon/t$, respectively, after weighting $A$ by
$e^{\gamma d(a,i)}$ and $D$ by $e^{\gamma[d(a,i)+d(a,j)]}$.
Here a marginal fixes any one index and sums all the others.
Assume the deterministic Hessian majorants of §19.1 for every
$V_2+\lambda T+W_k$, and the following local measure hypotheses:
$$\begin{gathered}
\sup_{e,k,\lambda}E_{\nu_\lambda}|\nabla_eT|
 +\sup_{e,k}E_{\mu_k}|\nabla_ew_k|\le L\varepsilon/t,\\
\sup_{e,k}p_{e,k}\le p<1,\qquad
\sup_k\|w_k''\|e^{-w_k/2}\le K_{\rm app}/\varepsilon^2,
\qquad {p\over1-p}\le P\varepsilon^3/t.\tag{79}
\end{gathered}$$
All constants $G_0,D_0,L,K_{\rm app},P$ are fixed, independent of $k,N,t$;
the last inequality specifies the allowed small-$t$ range explicitly.
For $\|Q\|_\gamma=\sup_a\sum_b e^{\gamma d(a,b)}|Q_{ab}|$, the
residuals (69), formed with these scores, obey
$$\|\mathcal B+\mathcal M\|_\gamma
\le {K_{\rm app}G_0^2P+2G_0D_0L\over m^2}
 {\varepsilon^3\over t}.\tag{80}$$

*Proof.* The Neumann bounds (77)--(78) propagate all the stated
marginal norms: $u$ has norm at most $G/m$, and $Du$ at most
$D_* /(2m)$. For $R_\mu g$ the same $G/m$ bound uses $C^S$ and
positive on-site killing. In particular (77) supplies (72)'s fourth
moment under the removed-edge measure, with spatially summable decay.
Using the pointwise bound directly improves the tail power in (72):
$$E_\mu\|w_k''(\xi_e)\|
 \le {K_{\rm app}p\over\varepsilon^2(1-p)},\qquad
\|\mathcal B\|_\gamma
 \le {t^2G^2K_{\rm app}p\over m^2\varepsilon^2(1-p)}.\tag{81}$$
Both inequalities follow by removing that edge barrier; its
normalizing denominator is at least $1-p$. The weighted row bound
then follows by inserting the two score envelopes on either side.
Also (78) inserted into (73) gives, uniformly along its smooth path,
$$\|J\|_\gamma\le {t^2GD_*\over2m^2}
 \sup_eE_{\nu_\lambda}|\nabla_eT|.\tag{82}$$
Thus its configuration-index sum is controlled before summing boundary
labels. The block norms already include the three colour components.

To include the barrier endpoint in $\mathcal M$, couple a stationary
$X$ of potential $S+W_k$ to the stationary Gaussian diffusion $Y$ of
potential $V_2$ with the same Brownian noise. Strong convexity gives
this joint stationary coupling by starting in the remote past.
Their difference satisfies $\dot Z=-HZ-tF(X)$, where
$F=\nabla(T+W_k)$. Variation of constants and the block majorant give
$\sup_eE|Z_e|\le th/m$, with $h=\sup_eE_\mu|F_e|\le L\varepsilon/t$.
By (76), each resolvent pairing is the time integral of
$tE[g_a(X_0)\cdot e^{-sH}g_b(X_s)]$ (and likewise for $Y$).
Subtract the two products, use the mean-value formula for each score,
and integrate $e^{-5s}e^{sC}$. The two terms each cost
$tGD_*\sup_eE|Z_e|/m$ in weighted row norm. Therefore
$\|\mathcal M\|_\gamma\le2t^2GD_*h/m^2$. This compares directly to
$G$, including the entire barrier endpoint. Combining with (81) proves
(80). All steps hold at finite $k,N$ with the displayed constants.
$\square$

**Applicability and cost.** This is outcome **(b)**: its inputs concern
local scores, tails and first drift moments, rather than a resolvent
residual. A local quadratic score can retain its linear part globally
and smoothly truncate its quadratic part outside $D$; on the shrinking
chart this plausibly gives $G_0,D_0$ independent of $t$. Applying (80)
to §17 requires constructing these extensions as gradients, checking
their marginal constants and bounding their Gaussian covariance error
by $E_0\varepsilon^3/t$ in weighted row norm. That explicit additional
score-extension hypothesis adds $E_0$ to (80)'s constant when comparing
to the original Gaussian scores; fixed-$N$ barrier limits also require
convergence of the extended score covariances. The Gaussian extension
error is a local polynomial-tail calculation. For (79), the cubic
remainder suggests $E|\nabla_eT|=O(\varepsilon^2/t)$; a uniform profile
bound $|w_k'|e^{-w_k/2}\le\Omega_{\rm app}/\varepsilon$ gives
$E_\mu|\nabla_ew_k|\le\Omega_{\rm app}p/[\varepsilon(1-p)]$.
The work still owed is the interacting removed-edge tail, this profile
bound, and deterministic Hessian envelopes. The Gaussian tail (55)
makes the scales plausible, while its transfer to the extended measure
is an additional proof. The stop rule is met by this conditional lemma;
(80) becomes applicable only after those local hypotheses are proved.

### 19.3 Consequence for STATE

Cell 2 advances to testing the local hypotheses (79) and the score-extension
conditions of §19.2. The conditional comparison (80) includes the barrier
endpoint, with decay exponent $\frac12\log(10/7)$; its application to the
original scores, the full-integral comparison and iteration remain open.

## 20. Round 20: the score extensions and the kernel estimate

**GPT-6 Astra, 2026-09-29; written derivation, unrefereed.**

**After refereeing §§20.1--20.2 (Claude, 2026-09-29).** ACCEPT. §20.1:
centring (85) at the saddle $s_\lambda$ of the extended potential, displaced from
$\xi_*$ by at most $h$, keeps the barrier sign ($|s_{\lambda,e}|<\eta-\rho_k$); the profile
family has the weighted bounds (84), with the convolution costing at most
a factor $\mathrm e$ because the oscillation across a mollifier ball stays below
2; $p\le2(7/16)^n$ and (83) give $P=1$; $L$ collects the drift terms. §20.2:
the extended potentials (86) are gradients agreeing with the scores on
$D$; the tail $G(A_a)\le42e^{-25\varepsilon^2/(6t)}$ from the Gaussian mean $\le\varepsilon/2$ and
variance $\le t/4$ per component; $E_G|\xi_i|^4\le8\varepsilon^4$; Hölder gives the $p_G^{1/4}$
factor, and (88) follows from splitting the difference of covariances.
The constants $G_0,D_0,A_0$ are loose and explicit.

### 20.1 Moment transfer and a fixed profile family

The transfer of (55) uses the saddle of the **extended smooth potential**.
Put $B=4c_M+6K_u/7$, $h=2B\varepsilon^2/3+2tD_J$ and
$n=k_t=\lfloor3t^{-2\delta}/8\rfloor-1$. In addition to §17 impose
$$C_*\varepsilon\le\tfrac12,\quad n\ge2,\quad
h\le {2\varepsilon\log2\over7n},\quad
4(7/16)^n\le\varepsilon^3/t.\tag{83}$$
These hold for sufficiently small $t$ at each fixed $0<\delta<1/6$.
Indeed $nh/\varepsilon=O(t^{1/2-3\delta}+t^{1/2-\delta})$.
For $S_\lambda=V_2+\lambda(S-V_2)$, let $s_\lambda$ be its unique
whole-space saddle. At $\xi_*$, the energy gradient vanishes,
$t|\nabla_eV_2(\xi_*)|\le B\varepsilon^2$ and
$t|\nabla_eS(\xi_*)|\le3tD_J$: use $|Y-w|\le4c_M\varepsilon^2$,
$\|C^*\|_{\infty,b}\le2$, and the radius-$\varepsilon$ Hessian error
$K_u\varepsilon$. Global diagonal dominance at least $3/2$ therefore gives
$\|s_\lambda-\xi_*\|_\infty\le h$, by the maximum-block argument on
$\int_0^1tS_\lambda''(\xi_*+u(s_\lambda-\xi_*))\,du$.
The majorants here are deterministic: apply §15.1's product-rule bounds
block by block, add $\|(H-5I)_{ij}\|$, and use their row and column
sums $3+C_*\varepsilon\le7/2$.

Here is one concrete family, indexed by integers $k\ge1$. At
$r_k=3\varepsilon-\varepsilon/(k+1)$ continue $w=x^4$ by
$w(r_k)+w'(r_k)(r-r_k)+w''(r_k)(r-r_k)^2/2$; denote the radial
whole-space continuation by $v_k$. Convolve it in three dimensions with
the probability density proportional to
$\exp[-1/(1-|z|^2)]1_{|z|<1}$, rescaled to radius
$$\rho_k=\min\left\{{\varepsilon\over1000(k+1)^6},
 {2\varepsilon\log2\over7n}\right\}.$$
The resulting $w_k$ is smooth, nonnegative and convex, vanishes on
$r\le\eta-\rho_k$, and has bounded Hessian for each $k$.
It converges locally in $C^1$ to $w$ inside $D$ and diverges outside.
With §18's constants one may take
$$K_{\rm app}=\mathrm eK_0,\qquad
\Omega_{\rm app}=\mathrm e(\Omega_0+\sqrt{2K_0/\mathrm e}).\tag{84}$$
For verification, beyond $r_k$ the radial Hessian is at most $w''(r_k)$,
and $w'\exp(-w/2)\le w'(r_k)e^{-k^4/2}
+\sqrt{2w''(r_k)/\mathrm e}\,e^{-k^4/2}$.
Inside $r_k+2\rho_k$, $\sup|v_k'|\le32(k+1)^5/\varepsilon$,
so the oscillation across a mollifier ball is less than $2$.
Convolving the weighted bounds thus costs at most $\mathrm e$.
For $r\ge r_k+\rho_k$, use $v_k\ge k^4$ on the convolution ball;
the same quadratic bound controls the gradient there. This proves (84)
for both $\|w_k''\|e^{-w_k/2}$ and $|w_k'|e^{-w_k/2}$.

For any subset of the edge barriers, integration by parts about
$s_\lambda$ gives, for every real $q\ge2$,
$$\sup_e E|\xi_e-s_{\lambda,e}|^q
 \le[2(q+1)t/3]^{q/2}.\tag{85}$$
The barrier term has the required sign since
$|s_{\lambda,e}|\le6\varepsilon/7+h<\eta-\rho_k$.
Whole-space Gaussian domination and bounded finite-$k$ Hessians justify
integration by parts, including on the removed edge. Thus (85) applies
to $\nu_{e,k}$, $\nu_\lambda$ and $\mu_k$.
The active threshold is at distance at least
$8\varepsilon/7-h-\rho_k$ from this saddle. Markov with $q=n$,
and $-\log(1-u)\le2u$ for $u\le1/2$, gives
$p_{e,k}\le2(7/16)^n=:p<1/2$. Equations (83) give
$p/(1-p)\le\varepsilon^3/t$, so choose $P=1$.
Finally the Hessian bound on $T=S-V_2$ and (85) with $q=2$ give
$E|\nabla_eT|\le B\varepsilon^2/t+3D_J+
C_*\varepsilon(h+\sqrt{2t})/t$.
Removing one barrier gives
$E_{\mu_k}|\nabla_ew_k|\le\Omega_{\rm app}p/[\varepsilon(1-p)]$.
Consequently (79) holds with
$L=B+3D_J+3C_*+\Omega_{\rm app}$, uniformly in $N,k,\lambda$.

### 20.2 Gradient extensions and their Gaussian error

Use one scalar direction per boundary link (three directions and two layers
cost a factor six in the incidence counts). A score has insertion support
$T_a$ of at most seven edges, each at distance at most one from $a$;
each insertion edge belongs to at most 42 such supports. Write
$\sigma_a=\partial_aV_2=\mathrm{const}+l_a\cdot\xi+q_a(\xi)$,
$q_a=\xi^TQ_a\xi/2$. Fix $b\ge1$ as the supremum of
$(t/\varepsilon)|l_{a,i}|$ and
$(t/\varepsilon)\|(Q_a)_{ij}\|_F$ over these local coefficients,
all allowed backgrounds and $t$; equivalently take the corresponding
unit-link derivatives of $E_w^{(2)}$. This is a fixed finite-dimensional
compact-chart supremum, independent of $N,t$. With §15.1's cutoff set
$$\widehat\sigma_a=l_a\cdot\xi+\chi_a q_a,\qquad
\chi_a=\prod_{i\in T_a}\chi(|\xi_i|),\qquad
\widehat g_a=\nabla\widehat\sigma_a.\tag{86}$$
These smooth potentials retain the entire linear part globally and agree
with $\sigma_a$ up to a constant on $D$. On the cutoff support,
$|q_a|\le98b\varepsilon c_0^2/t$ and
$|\nabla_iq_a|\le14b\varepsilon c_0/t$.
The product rule, including the radial Hessian's Frobenius norm, gives
$|\widehat g_{a,i}|\le1000b\varepsilon/t$ and
$\|\partial_j\widehat g_{a,i}\|_F\le2000b\varepsilon/t$.
Counting at most $7^2$ pairs per score and $42\cdot7$ per fixed insertion
index proves every marginal in §19.2 with the explicit choices
$$G_0=50000b e^\gamma,\qquad D_0=600000b e^{2\gamma}.\tag{87}$$

Here is the local polynomial-tail check against the Gaussian (59).
Its mean has block norm at most $\varepsilon/2$, and each scalar
variance is at most $t/4$. Thus $E_G|\xi_i|^4\le8\varepsilon^4$.
For $A_a=\{\max_{i\in T_a}|\xi_i|>3\varepsilon\}$, a union over seven
edges and three components gives
$G(A_a)\le p_G:=\min\{1,42\exp[-25\varepsilon^2/(6t)]\}$.
The error gradient vanishes off $A_a$; on it the product rule gives
$|\nabla_i(\widehat\sigma_a-\sigma_a)|
\le2000b\varepsilon t^{-1}\sum_{j\in T_a}|\xi_j|$.
Hölder and the fourth moment give its $L^2(G)$ bound
$24000b\varepsilon^2p_G^{1/4}/t$. Its weighted marginal sums are
therefore at most $A_0\varepsilon^2p_G^{1/4}/t$ with
$A_0=1100000b e^\gamma$. The original gradient's $L^2$ marginals
are at most $(G_0+A_0)\varepsilon/t$.
Apply the Gaussian covariance representation to the two differences of
products, using the weighted inverse bound $m^{-1}$. This proves
$$\|\operatorname{Cov}_G(\widehat\sigma,\widehat\sigma)
-\operatorname{Cov}_G(\sigma,\sigma)\|_\gamma
\le E_0p_G^{1/4}\varepsilon^3/t,\qquad
E_0=A_0(2G_0+A_0)/m.\tag{88}$$
At fixed $N,t$, these extended potentials grow at most linearly.
The densities are bounded by a fixed multiple of $e^{-S}$ for all
sufficiently large $k$, since their partition functions converge to a
positive limit. Strong convexity of $S$ supplies an integrable Gaussian
dominator for their products. Dominated convergence therefore proves
convergence of their means and covariances to the barriered covariances;
on $D$ these are exactly the original quadratic-score covariances.

### 20.3 Assembly of the kernel estimate (Claude, after the quota stop)

**Claude, 2026-09-29; assembly corrected by the referee below.** Use §19's weight,
$\gamma=\frac12\log(10/7)$, $m=5-\frac72e^\gamma$, the unit-link normalization of §17, and the
extended scores of (86) on the Gaussian side; on the barriered measure
$\mu$ the extended quadratic scores agree with $\sigma_a$ up to constants,
and their insertion gradients agree exactly, since $\mu$ lives on $D$.
The actual scores $\partial_aS$ remain distinct from $\sigma_a$.
Define $h_{ai}=\sup_D|\nabla_i\partial_a(S-V_2)|$ and
$$C_T=\sup_{N,t,U}{t\over\varepsilon^2}
\max\left\{\sup_a\sum_i e^{\gamma d(a,i)}h_{ai},
\sup_i\sum_a e^{\gamma d(a,i)}h_{ai}\right\}.$$
Uniform finiteness of this supremum is an additional hypothesis.
For radius-one supports with the counts of (87), the sufficient local
estimate $h_{ai}\le M_T\varepsilon^2/t$ gives $C_T\le42e^\gamma M_T$.
Establishing $M_T$ requires mixed boundary--insertion Taylor bounds for
the energy and amplitudes, including derivatives of the moving saddle
and Hessian used in the extension. The insertion-only bounds
$\Lambda,c_M,K_u,B$ supply no such mixed-jet estimate by themselves.
Compactness at fixed $t,N$ leaves the scaled supremum as $t\downarrow0$
unsettled; the shift estimate in §20.1 bounds a value, rather than its
boundary derivative. Amplitude mixed derivatives also need a specified
bound extending $D_J$.

**After refereeing §20.3 (GPT-6 Astra, 2026-09-29).** **REFINE** the first
term of $C_{27}$: (68) pairs $f_a-g_a$ with $f_b$, adding
$C_T^2\varepsilon/m$ to its coefficient. **ACCEPT**, conditionally on
the displayed score hypothesis, the smooth-insertion, barrier/measure,
and Gaussian-extension terms. **REFINE** score coincidence as above:
it holds modulo constants for quadratic potentials, exactly for their
gradients, and after the barrier limit. **ACCEPT** the conversion from
$\varepsilon$-velocity to unscaled link derivatives and its relative
$t^\alpha$ gain. **REJECT** the asserted derivation of uniform $C_T$
from the listed constants; the explicit missing estimate is above.
**REFINE** the identification with (27): (89) is a link-coordinate
analogue; §7.4's curvature-coordinate conversion remains an obligation.

**Conditional covariant link-kernel estimate.** Under (83), $C_T<\infty$
and the hypotheses of §§17--20,
for boundary links at link distance $d(a,b)\ge2$,
$$\sup_a\sum_{b:\,d(a,b)\ge2}e^{\gamma d(a,b)}\bigl|\partial_a\partial_b(\mathcal D_s-\mathcal D^{\rm cov})\bigr|
\le C_{27}\,{\varepsilon^3\over t},$$
$$C_{27}={2C_TG_0+C_T^2\over m}+{e^\gamma C_*G_0^2\over m^2}
+{\mathrm eK_0G_0^2+2G_0D_0L\over m^2}+E_0p_G^{1/4}.\tag{89}$$

*Proof.* Use (68) on the limiting barriered measure, with the extended
quadratic scores. Their covariance comparisons follow by §20.2's
dominated limit. Since $f=g+(f-g)$, the two score-difference terms cost
$(2C_TG_0+C_T^2\varepsilon)\varepsilon^3/(mt)$ by (77) and its
$R_\mu$ version; use $\varepsilon\le1$ for the constant in (89). The
smooth insertion costs $t(G_0\varepsilon/t)^2e^\gamma C_*\varepsilon/m^2$, since $\Delta$ has range one and
block row sum at most $C_*\varepsilon$, and each resolvent has weighted norm at most
$m^{-1}$. The residuals (69) obey (80) with $P=1$ and $K_{\rm app}=\mathrm eK_0$ from
§20.1. Returning from extended to original scores on the Gaussian side
costs (88). Collect the four terms. $\square$

In unscaled link derivatives the bound reads $C_{27}\varepsilon/t$, so the difference
kernel is smaller than the Gaussian kernel scale $1/t$ of (29) by the
factor $\varepsilon=t^\alpha$. This proves the conditional link-coordinate
estimate with decay rate $\frac12\log(10/7)$, uniformly in plane size.
Finite-$k$ quadratic-score comparisons converge to this estimate;
equality with the original scores is asserted on the limiting measure.

**Pair response and the next estimate.** Together with the
face-local sizes (63), (89) controls the pair dependence of the remainder
$r=\mathcal D_s-\mathcal D^{\rm cov}$ on boundary data: a change at distance $d$ from a region
moves the link derivative of $r$ by at most
$C_{27}\varepsilon^3e^{-\gamma d}/t$ per unit change. Polymer activities
require all-order connected response estimates, an admissible family
of link interpolation paths and control of their order-dependent
constants. The scale $\varepsilon^3/t=t^{\alpha-2\delta}$ also retains
the energy budget of (62); bare $O(t^\alpha)$ activities need a stronger
estimate or a specified normalization.

## 21. Round 21: third response and an all-order polymer criterion

**GPT-6 Astra, 2026-09-29; exact identities and conditional bounds,
unrefereed.** The third response reduces to a differentiated vector
resolvent. Its additional source is the third insertion derivative of
the potential, including the barrier. This specifies the next estimate.

**After refereeing §21 and the §20.3 corrections (Claude, 2026-09-29).**
I accept the corrections to my assembly: the added $C_T^2/m$, score
coincidence modulo constants, the rejection of my claim that $C_T$ follows
from the insertion-only constants (the mixed boundary--insertion jets need
their own bound), and (89) as the link-coordinate analogue of (27). §21:
ACCEPT (90); (91) by applying (22) twice to $\operatorname{Cov}(A_a^\circ A_b^\circ,A_c)$ with
$\nabla(A_a^\circ A_b^\circ)=A_a^\circ f_b+A_b^\circ f_a$; (92) by differentiating
$(tL_\mu+tV'')u_c=f_c$, whose drift term contributes $Z_ctV''$ and whose matrix
potential contributes $tV''Z_c+Y_c$; (93) as a conditional bound; and
(94)--(95) as the standard anchored Möbius conversion. The source $Y$ looks
closable with the tools at hand: $u_c$ is pointwise bounded by (77), so
$Y$ needs only $E_\mu\|w_k'''\|^4$, which the edge-removal argument of (81)
controls once the profile gives $\|w_k'''\|e^{-w_k/4}\le K_3/\varepsilon^3$; the $x^4$ profile has
this property with an explicit $K_3$.

### 21.1 Third mixed derivative

Work at finite $k,N$, in fixed insertion coordinates, with
$V=S+W_k$, $A_a=\partial_aS$, $f_a=\nabla A_a$,
$R=[tL_\mu+tV'']^{-1}$ and $u_a=Rf_a$.
Take three distinct boundary directions whose local potential supports
are pairwise separated, so $S_{ab}=S_{ac}=S_{bc}=0$ identically;
use the same condition for $V_2$. Separation here means disjoint
interaction terms, as in §17's link-graph convention. Differentiating
$E F$ gives $E\partial_cF-\operatorname{Cov}(F,A_c)$, hence
$$\partial_a\partial_b\partial_c r
=\operatorname{cum}_\mu(A_a,A_b,A_c)
-\operatorname{cum}_G(\sigma_a,\sigma_b,\sigma_c).\tag{90}$$
For overlapping supports the additional terms are
$E S_{abc}-\operatorname{Cov}(S_{ab},A_c)
-\operatorname{Cov}(S_{ac},A_b)-\operatorname{Cov}(S_{bc},A_a)$,
and their Gaussian counterparts. These terms matter at higher orders.

The covariance formula (22), applied twice, gives the exact identity
$$\operatorname{cum}_\mu(A_a,A_b,A_c)
=t^2E_\mu[f_a\cdot R\nabla(f_b\cdot u_c)
                 +f_b\cdot R\nabla(f_a\cdot u_c)].\tag{91}$$
Indeed apply it first to $\operatorname{Cov}(A_a^\circ A_b^\circ,A_c)$;
the product rule leaves $t\operatorname{Cov}(A_a,f_b\cdot u_c)$
and $t\operatorname{Cov}(A_b,f_a\cdot u_c)$. This proves (91)
without differentiating a parameter-dependent Hilbert-space pairing.
Differentiating the equation for $u_c$, with $Z_{c,ij}=\partial_j u_{c,i}$,
gives, in colour components,
$$tL_\mu Z_c+(tV'')Z_c+Z_c(tV'')=Df_c-Y_c,\qquad
(Y_c)_{ij}=t\sum_l(\partial_j V''_{il})u_{c,l}.\tag{92}$$
Thus the second derivative of the scalar Poisson solution introduces
$W_k'''$ as a source; the positive $W_k''$ still supplies killing.

Here are sufficient quantitative inputs for a weighted third bound.
Let $\ell(I)$ be the minimum number of graph edges in a tree joining
the labels $I$. For each tensor take the maximum of its one-index
marginal sums of $e^{\gamma\ell(I)}$ times its block $L^4(\mu_k)$ norm.
Assume these norms for $f,Df,Y$ are at most
$F\varepsilon/t,D_F\varepsilon/t,Y_0\varepsilon/t$, respectively,
uniformly in $k,N,t,U$. Smooth approximation and integrability of (91)
are included; the resulting cumulants must converge to the barrier limit.
The block semigroup bounds give $\|u\|\le F\varepsilon/(mt)$ and
$\|Z\|\le(D_F+Y_0)\varepsilon/(2mt)$: (92) has two Hessian indices,
base $10I$ and perturbation norm at most $7e^\gamma$.
Minkowski and stationarity give the same bounds in $L^4$ as in $L^\infty$.
Tree weights multiply under contraction since joining the constituent
trees joins their external labels. Hölder in (91) therefore proves
$$\sup_a\sum_{b,c\ {\rm separated}}e^{\gamma\ell(a,b,c)}
|\partial_a\partial_b\partial_c r|
\le C_3\varepsilon^3/t.$$
$$
C_3={F^2(3D_F+Y_0)+3(G_0+A_0)^2D_G\over m^2},
\quad D_G=294b e^{2\gamma}.\tag{93}$$
For the Gaussian term, $g$ is affine, its $L^2$ marginal bound is
$(G_0+A_0)\varepsilon/t$ by §20.2, and $Dg$ is constant with marginal
bound $D_G\varepsilon/t$ (at most $42\cdot7$ blocks).
Here $Y=0$, $Du$ is constant with bound $D_G\varepsilon/(2mt)$,
so Cauchy--Schwarz alone gives the second summand in $C_3$.
For the interacting term the two product-rule contributions in (91)
cost $2F^2D_F/m^2+F^2(D_F+Y_0)/m^2$.

Equation (93) is a precise reduction. The new work is the uniform
$Df$ and especially $Y$ bounds in (92), including the barrier limit.
The profile estimates (84) control $w_k'$ and $w_k''$ with a density
weight; a bound on $w_k'''u_c$ in the stated $L^4$ tensor norm remains
to be proved. Differentiating (78) as if its matrix potential stayed
constant would omit this term. The scale in unscaled derivatives is
$C_3/t$; the scaled third response retains the cubic size of (89).

### 21.2 All orders and anchored Möbius inversion

Fix admissible independent link paths $U_a(z_a)$, $0\le z_a\le1$,
of speed at most $\varepsilon$, with every mixed corner and intermediate
point in the chart. Assume $r(0)=0$. A sufficient all-order estimate is,
for every $n\ge1$, with fixed $A,q,\eta>0$,
$$\sup_a\sum_{\substack{X\ni a\\|X|=n}}
 e^{\eta\ell(X)}\sup_{z\in[0,1]^{\mathcal E}}
 |\partial_X r(U(z))|\le A t^\alpha q^n.\tag{94}$$
It includes adjacent links and all mixed potential derivatives. Repeated
differentiation uses $\partial_a E F=E\partial_aF-\operatorname{Cov}(F,A_a)$;
each new score adds a cumulant, with contact terms from differentiated
scores. Resolvent differentiation adds the higher jets of (92).
Uniform control of their growth in $n$ is part of (94).

Define $r_X=\sum_{Y\subseteq X}(-1)^{|X|-|Y|}r(U_Y,0_{Y^c})$.
Finite Boolean inversion gives $r(U)=\sum_Xr_X$; repeated fundamental
theorems of calculus give $|r_X|\le At^\alpha q^{|X|}e^{-\eta\ell(X)}$.
Assign each $X$ to a deterministic minimum connecting tree with vertex
set $H(X)$, and collect $\rho_H=\sum_{H(X)=H}r_X$.
Since $X\subseteq H$ and $\ell(X)=|H|-1$, summing over its subsets proves
$$|\rho_H|\le Ae^\eta t^\alpha
 e^{-[\eta-\log(1+q)]|H|}.\tag{95}$$
Thus (94) with $\eta>\log(1+q)$ gives the requested connected activities,
$C=Ae^\eta$, $\gamma'=\eta-\log(1+q)$, at finite volume.
An infinite-volume polymer norm additionally needs summability over
connected sets. Pairwise-separated third derivatives alone leave the
contact terms, admissible paths and order growth in (94) open.
Also (93) supplies $t^\alpha$ for $(t/\varepsilon^2)r$; bare $r$ needs
the stronger scale in (94), or activities carrying (62)'s energy budget.

### Consequence for STATE

Round 21 corrects the conditional link-kernel constant (89) and reduces
the third response to the explicit tensor source (92), yielding (93)
under its stated uniform norms. Cell 2 next needs the mixed score bound
$C_T<\infty$ and the barrier-weighted $Y$ estimate, then the all-order
growth and admissible paths of (94). Equation (95) proves the resulting
conditional polymer conversion; its bare-activity scale, curvature
conversion, large-field comparison and perturbed-action stability
remain explicit obligations.

## 22. Round 22: the mixed score jets and the barrier source

**GPT-6 Astra, 2026-09-29; written derivation, unrefereed.** The barrier
source closes with an explicit third-profile constant and a strengthened
small-time condition. All tensor norms below include colour Frobenius norms.

### 22.1 The source $Y$

Use scalar score extensions before taking the barrier limit. For a local
score $A_c$ set $a_c=A_c(0)$, $l_c=\nabla A_c(0)$ and
$\widehat A_c=a_c+l_c\cdot\xi+\chi_c(A_c-a_c-l_c\cdot\xi)$,
with the product cutoff of (86). This agrees with $A_c$ on $D$ and has
bounded gradient; the original finite-$k$ score can have an unbounded
affine gradient outside $D$. Equations (91)--(92) hold for these scalar
observables, with $f_c=\nabla\widehat A_c$. Write $F\varepsilon/t$ for
their pointwise weighted gradient marginals; §22.2 supplies $F$.
The $R_\mu$ version of (77) gives pointwise marginals $F\varepsilon/(mt)$.

Put $b_j=(j/\mathrm e)^{j/4}$ and
$$K_3=\mathrm e(24b_1+324b_2+1257b_3+2178b_4
                    +1881b_5+780b_6+120b_7).\tag{96}$$
Then the precise family of §20.1 satisfies
$\|D^3w_k\|_F e^{-w_k/4}\le K_3/\varepsilon^3$ uniformly in $k$.
Here is a direct check. On the active interval, $dx/dr=(1+x)^2/\varepsilon$,
$\varepsilon w'=4x^3(1+x)^2$ and
$\varepsilon^2w''=12x^2+56x^3+96x^4+72x^5+20x^6$.
A further derivative gives coefficients $24,216,744,1296,1224,600,120$
in degrees 1 through 7. The radial tensor formula bounds its Frobenius
norm by $|w'''|+9(w''/r+w'/r^2)$. Since $r\ge2\varepsilon$, the larger
polynomial $\varepsilon^3w'''+9\varepsilon^2w''+(9/4)\varepsilon w'$
has exactly the coefficients in (96). Beyond $r_k$, write
$A=w''(r_k)$ and $B=w'(r_k)$: the quadratic continuation has
$D_r^3v_k=0$ and $v_k'/r^2\le B/(4\varepsilon^2)+A/(2\varepsilon)$.
Its radial tensor is bounded by $9A/\varepsilon+9B/(4\varepsilon^2)$,
while $v_k\ge k^4$. The bound follows from
$\sup_{x\ge0}x^je^{-x^4/4}=b_j$. The continuation is $C^2$, so its
weak third derivative has no interface measure. Near the interface
§20.1's oscillation bound costs at most $\mathrm e^{1/2}$ under
convolution; beyond $r_k+\rho_k$ use $v_k\ge k^4$ on the entire ball.
The factor $\mathrm e$ in (96) covers both regions.

For completeness fix the smooth cutoff once, and let $K_\chi\ge1$
bound $c_0^r$ times the sum of all colour-block norms of $D^r\chi_p$
for $0\le r\le3$. Enlarge $\Lambda_3\ge\Lambda$ to bound the local
third insertion jets in these norms, and enlarge $D_J$ to bound all
first through third insertion derivatives of each local amplitude.
These constants are finite on the enlarged compact chart. The product
rule in §15.1 gives the global third-jet marginal bound
$$\|tS'''\|_{\gamma,\mathrm{marg},\infty}\le
J_S:=e^{2\gamma}K_\chi(4000\Lambda_3+100D_J).\tag{97}$$
Indeed the four differentiated cubic-remainder terms per face cost
$(64+576+864+288)K_\chi\Lambda_3=1792K_\chi\Lambda_3$;
each edge meets two faces. The amplitude terms cost at most
$19K_\chi D_Jt/c_0^2$ per face, and $t/c_0^2\le1/9$.
The quadratic extension has zero third insertion derivative.

Removing edge $i$ exactly as in (81) gives
$$\|D^3w_k(\xi_i)\|_{L^4(\mu_k)}
\le {K_3\over\varepsilon^3}\left({p\over1-p}\right)^{1/4}.$$
In addition to (83), impose
$$4(7/16)^n\le(\varepsilon^3/t)^4.\tag{98}$$
This holds for sufficiently small $t$ at each fixed $0<\delta<1/6$.
The barrier tensor is diagonal in its three edge indices. Contracting
its bound and (97) with the pointwise envelope of $u_c$, using the
joining-tree inequality of §21, proves
$$\|Y\|_{\gamma,\mathrm{marg},4}\le Y_0\varepsilon/t,
\qquad Y_0={F\over m}(J_S+K_3).\tag{99}$$

### Consequence for STATE

Part 1 supplies the explicit barrier source (99) for bounded-gradient
score extensions, with $F$ to be fixed in Part 2 and smallness (98).
The mixed score jets and final chart theorem are the remaining parts.
