# Finite position precision and the reachable action area

A bounded-error position record gives an exact terminal canonical area with
separate precision and residual-delay terms. At fixed force ceiling, mass and
total horizon, that area closes uniformly as both errors vanish.

R09, 2026-09-10. C074–C075 accepted by
[written review](../reviews/finite-precision-B40.md);
[B40](../references/batches/B40.md) records the bounded prior-art audit.
The model and lens come from
[R08](reachable-cut-composition.md). Areas use $dq\,dp$, with action units
$ML^2/T$ and no $2\pi$ factor. Records are non-disturbing information;
their achievable precision and latency are supplied protocol parameters.

## 1. Compatible set

Fix $m,F,T>0$, exact initial state $(q_0,p_0)$, and every measurable force
$|f|\le F$. Observe at $a\in(0,T)$, with residual delay $b=T-a$.
Subtract the known inertial motion. A reported position increment $y$ means
the true increment lies in $[y-\varepsilon,y+\varepsilon]$, where
$\varepsilon\ge0$ is a deterministic error bound. No probability law is used.

Put $Q=Fa^2/(2m)$ and clip the record to the reachable position range:

$$l=\max(-Q,y-\varepsilon),\qquad r=\min(Q,y+\varepsilon).$$

Assume $l\le r$; otherwise the record is inconsistent. Define the momentum
fibre endpoints for $q\in[-Q,Q]$:

$$L(q)=Fa\left[1-\sqrt{2-4mq/(Fa^2)}\right],\qquad
U(q)=Fa\left[-1+\sqrt{2+4mq/(Fa^2)}\right].$$

The compatible cut set and terminal increment set are exactly

$$C=\{(q,p):l\le q\le r,\ L(q)\le p\le U(q)\},\qquad
E=S_bC+K_b,$$

where $S_b(q,p)=(q+bp/m,p)$ and $K_b$ is R08's future lens.
Intersection implements the error record; concatenation of any compatible
past with any allowed future proves equality. A translation restores the
known inertial terminal state without changing area.

## 2. Exact area

Write $w=r-l$, $D_*=U(r)-L(l)$, and $A_C=\int_l^r[U(q)-L(q)]dq$.
Then

$$\boxed{|E|=A_C+\frac{2F^2b^3}{3m}+2Fbw+\frac{Fb^2}{m}D_*.}$$

The clipped area itself has the elementary expression

$$A_C=\frac{F^2a^3}{m}[G(z_r)-G(z_l)],\quad
z_q=\frac{mq}{Fa^2},\quad
G(z)=\frac{(2+4z)^{3/2}-(2-4z)^{3/2}}6-2z.$$

**Proof.** Apply the determinant-one shear $S_{-b}$. The future lens becomes
the integral sum of symmetric segments in directions $g_s=(-s/m,1)$,
$0\le s\le b$, each with force weight $F\,ds$. For a convex planar set
$C$ and a segment $[-\alpha g,\alpha g]$, section integration gives

$$|C+[-\alpha g,\alpha g]|-|C|
=2\alpha\,\operatorname{width}\{\det(x,g):x\in C\}.$$

Successively adding finitely many segments and using additivity of widths
under Minkowski sums splits the area into the original area, the area of
their segment sum, and the sum of these original-set width terms. Approximating
the continuous directions $g_s$ by step functions gives Hausdorff convergence
of the integral sets: the support-function error is bounded by
$F\int\|g_s-g_s^{(n)}\|ds$. Continuity of convex planar area gives

$$|C+S_{-b}K_b|=|C|+|K_b|
+2F\int_0^b\operatorname{width}_C(q+sp/m)\,ds.$$

Both $L(q)$ and $U(q)$ increase with $q$. For $s\ge0$, the maximum of
$q+sp/m$ on $C$ is $r+sU(r)/m$ and its minimum is $l+sL(l)/m$.
The width is therefore $w+sD_*/m$. Integration proves the formula, including
the degenerate strip $l=r$ by the same segment argument or continuity.
Differentiating $G$ gives the displayed integral for $A_C$.

## 3. Joint limit and endpoint checks

Since $w\le2\varepsilon$, $D_*\le2Fa$, and
$A_C\le2Fa\,w$, the exact expression yields the uniform estimate

$$0\le|E|\le4FT\varepsilon
+\frac{2F^2ab^2}{m}+\frac{2F^2b^3}{3m}.$$

Thus $|E|\to0$ for every joint approach $(\varepsilon,b)\to(0,0)$,
uniformly over compatible reported values, with fixed $F,m,T$ and $a=T-b$.
There is no needed relation between the rates of improving precision and delay.

The formula passes three independent limiting checks:

- Exact position: $w=A_C=0$, recovering R08's $A(b)+Fb^2D_*/m$.
- Entire lens retained: $w=Fa^2/m$, $D_*=2Fa$, $A_C=2F^2a^3/(3m)$;
  the four terms sum to $2F^2(a+b)^3/(3m)$, as unobserved composition requires.
- Zero residual delay: the terminal area is just the clipped area $A_C$.

For a central record $y=0$ at $b=0$ and small positive $\varepsilon$,

$$A_C=4(\sqrt2-1)Fa\,\varepsilon+o(\varepsilon).$$

Here continuity of the fibre width suffices. The momentum width tends to
$2(\sqrt2-1)FT>0$ in the joint limit: the information region becomes thin,
rather than shrinking to a point. A fixed error tolerance alone also supplies
no record-uniform positive area: a strip touching the extreme reachable
position at one point has $A_C=0$.

## 4. Next premise test

Precision and latency now enter a single exact action-valued formula. A
mechanical obstruction must constrain attainable records or their joint
precision/latency, rather than follow from area geometry alone. The next
bounded task should test two finite-precision position records: unlike one
record, they may also shrink momentum uncertainty. Keep the total experiment
fixed and derive the competing force and difference-quotient errors before
introducing an apparatus resource premise.
