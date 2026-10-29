# Bounded-force records: reachability, minimax recovery and composition

An unresolved bounded force produces an exact curved endpoint lens. Noisy
position histories instead produce three exact finite-horizon momentum-risk
regimes, saturating at $2\sqrt{mF\varepsilon}$. Both fit one symmetric-fibre
minimax principle. Independent composition adds scalar radii; shared record
budgets change the exponent because they change the admitted error set.
Every positive action-valued quantity here depends on specified delay, force
or precision. None selects a preparation-independent action.

This is a classical deterministic information model: $m,F>0$, known initial
$(q_0,p_0)$, $\dot q=p/m$, $\dot p=f$, every measurable $|f|\le F$, and
non-disturbing records with explicitly supplied precision/timing. There is
no stochastic force law, apparatus back-reaction or speed ceiling on the
whole class. Products multiply separate scalar minimax absolute errors;
they are not simultaneous error lower bounds on each individual motion.
Areas use $dq\,dp$, with action units and no $2\pi$ normalization.

This treatment consolidates C070–C087. Historical coordinator/model reviews
were internal written checks, not external peer review. The long-horizon
hidden pair and sharp finite difference match Seeber–Haimovich, Proposition
3.1 and Lemma 4.3/Theorem 4.1, as read in B41–B42. The remaining fixed-time,
cut and composition formulas are derived below; exact publication priority
is unassessed. Source capsules remain in B38–B46.

## The symmetric-fibre minimax principle

Let $U$ be a convex centrally symmetric input set, $A$ a linear record map,
$L$ one scalar linear target, and $E$ a closed symmetric convex record-error
set. Known offsets are subtracted. Define

$$K=\{u\in U:Au\in E\},\qquad r_L=\sup_{u\in K}|Lu|.$$

This is exactly the minimax worst-case scalar error for records $y=Au+e$,
$e\in E$. For two inputs compatible with one record, $(u-v)/2\in U$ and
$A(u-v)/2\in E$, so their scalar outputs differ by at most $2r_L$.
The midpoint of the compatible output interval attains error at most $r_L$.
Conversely opposite central-fibre inputs share record zero and force the
lower bound; approximating extremizers suffice if no maximum exists.
For bounded-force histories, the $L^\infty$ ball is weak-star compact and
position/momentum integrals are continuous, so maxima exist. Complete-history
bands impose a closed intersection of pointwise inequalities. The proof
applies equally to box errors and shared convex norm budgets. Coordinatewise
midpoints attain both coordinate risks, without claiming a single worst
motion realizes both errors for every estimator.

## Endpoint lens, causal delay and exact cut composition

With no new record after time zero, the endpoint increments at delay $t$ are

$$v=\int_0^t f(s)ds,\qquad
u=\frac1m\int_0^t(t-s)f(s)ds.$$

The exact set $K_t$ is

$$|d|\le1,\qquad |z-d/2|\le(1-d^2)/4,
\qquad d=v/(Ft),\quad z=mu/(Ft^2).$$

To prove the boundary, write $f=2Fh-F$, $0\le h\le1$, with fixed integral
$t(1+d)/2$. Its decreasing-weight position integral is largest when $h=1$
on the initial interval of that length and smallest when it is on the final
interval. Subtracting the threshold weight makes the exchange inequality
pointwise on both sides of that interval. Evaluating these one-switch forces
gives the displayed bounds; convex combinations fill each fixed-impulse
section. Constant opposite forces give coordinate half-ranges

$$r_q=Ft^2/(2m),\qquad r_p=Ft,\qquad r_qr_p=F^2t^3/(2m).$$

Inertial prediction attains both. Integrating the lens width gives its
canonical area $A(t)=2F^2t^3/(3m)$, a different normalization and observable
from the risk product. Individual admissible trajectories include zero force.

Let $S_b(q,p)=(q+bp/m,p)$ and $K_0=\{0\}$. For $T=a+b$,

$$K_T=S_bK_a+K_b.$$

Splitting each force integral proves one inclusion; concatenating arbitrary
admissible segment forces proves the reverse. This converse uses the
rectangular-in-time force class, without additional cross-time constraints.
Every finite unobserved refinement therefore leaves the endpoint lens
unchanged. Its segment areas cannot be added. Replacing the cut lens by its
marginal rectangle strictly enlarges the terminal set: the spurious corner
$(-Fa^2/(2m),Fa)$ followed by $+F$ has total impulse $FT$ but position differs
by $Fa^2/m$ from the only possible full-input trajectory with that impulse,
namely $f=F$ almost everywhere. The joint state or its compatible fibre is
necessary for exact propagation.

An exact full phase-state record at time $a$ leaves a translate of $K_b$.
An exact position record with normalized displacement
$\zeta=m(q_a-q_0-p_0a/m)/(Fa^2)\in[-1/2,1/2]$ leaves the momentum interval

$$I_\zeta=p_0+Fa[1-\sqrt{2-4\zeta},-1+\sqrt{2+4\zeta}],$$

of width $D=Fa[\sqrt{2-4\zeta}+\sqrt{2+4\zeta}-2]$.
The lens upper boundary is $1/2-(d-1)^2/4$ and the lower boundary
$(d+1)^2/4-1/2$, proving these endpoints directly. The exact terminal set is
$\{(q_a+bp/m,p):p\in I_\zeta\}+K_b$, with area

$$A(b)+Fb^2D/m.$$

Apply the determinant-one inverse shear: the added interval is vertical,
lengthening every lens section by $D$ over horizontal width $Fb^2/m$.
Central records leave $D=2(\sqrt2-1)Fa$; extreme records give $D=0$.
Concavity bounds $D$ by the central value. As $b\to0$ the area closes
uniformly, although central-record momentum width tends to
$2(\sqrt2-1)FT$. Area closure alone is not phase recovery.

## Finite-precision cuts and exact canonical area

Subtract inertial motion and let a record at $a$ specify
$|q-y|\le\varepsilon$. Put $Q=Fa^2/(2m)$,
$l=\max(-Q,y-\varepsilon)$, $r=\min(Q,y+\varepsilon)$; require $l\le r$.
For $q\in[-Q,Q]$ define

$$L(q)=Fa[1-\sqrt{2-4mq/(Fa^2)}],\qquad
U(q)=Fa[-1+\sqrt{2+4mq/(Fa^2)}].$$

The exact compatible and terminal sets are
$C=\{l\le q\le r,L(q)\le p\le U(q)\}$ and $E=S_bC+K_b$.
Writing $w=r-l$, $D_*=U(r)-L(l)$ and $A_C=\int_l^r(U-L)dq$ gives

$$|E|=A_C+\frac{2F^2b^3}{3m}+2Fbw+\frac{Fb^2}{m}D_*.$$

An explicit primitive is

$$A_C=\frac{F^2a^3}{m}[G(z_r)-G(z_l)],\quad z_q=mq/(Fa^2),$$
$$G(z)=\frac{(2+4z)^{3/2}-(2-4z)^{3/2}}6-2z.$$

For the area proof the inverse-sheared future lens is the integral sum of
segments in directions $g_s=(-s/m,1)$ of half-weight $Fds$, $0\le s\le b$.
Adding a segment $[-\alpha g,\alpha g]$ to a convex planar set increases
area by $2\alpha$ times the width of $\det(x,g)$ on that set. Section
integration proves this even for a degenerate set. Successively adding finite
segments separates their own area and the original-set width contributions.
Step approximations to $g_s$ have support-function error at most
$F\int\|g_s-g_s^{(n)}\|ds$, so Hausdorff and convex-area continuity give

$$|E|=|C|+|K_b|+2F\int_0^b\operatorname{width}_C(q+sp/m)ds.$$

Since $L,U$ increase, that width is $w+sD_*/m$. This proves the formula.
Differentiating $G$ verifies the primitive. Its degenerate case $l=r$ is
included. An unobserved full lens has $w=Fa^2/m$, $D_*=2Fa$,
$A_C=2F^2a^3/(3m)$; the four terms sum to $A(a+b)$.

As $w\le2\varepsilon$, $D_*\le2Fa$, $A_C\le2Faw$,

$$0\le|E|\le4FT\varepsilon+2F^2ab^2/m+2F^2b^3/(3m).$$

Thus every joint $(\varepsilon,b)\to(0,0)$ closes area uniformly at fixed
$F,m,T$. For central $y=0$, $b=0$, however,
$A_C=4(\sqrt2-1)Fa\varepsilon+o(\varepsilon)$ and momentum width tends
to $2(\sqrt2-1)FT$. A fixed tolerance also gives no record-uniform positive
area: a strip touching an extreme position at one point has zero area.

## Two records, complete histories and all finite horizons

Two position records at $t_1=T-b-\delta$, $t_2=T-b$, with errors
$\varepsilon_1,\varepsilon_2$, admit the causal estimator

$$\widehat p=m(y_2-y_1)/\delta,\qquad
\widehat q_T=y_2+b\widehat p/m.$$

Its exact worst-case errors are

$$B=m(\varepsilon_1+\varepsilon_2)/\delta+F\delta/2,
\qquad R_p=B+Fb,\quad R_q=\varepsilon_2+bB/m+Fb^2/(2m).$$

Indeed $p(t_2)-m(q(t_2)-q(t_1))/\delta
=\delta^{-1}\int_{t_1}^{t_2}(s-t_1)f(s)ds$. Integrate once more over
$[t_2,T]$ for position. Constant $+F$ on both final intervals and adverse
errors $e_1=+\varepsilon_1,e_2=-\varepsilon_2$ attain both bounds.
These are the stated estimator's exact errors; known initial data can improve
the minimax optimum at short horizons. Exact compatible sets can instead be
propagated by alternating $S_tC+K_t$ with the corresponding record strips.
They lie in a rectangle of area at most $4R_qR_p$, an outer area bound.

For equal tolerance $\varepsilon$, the unconstrained finite-difference optimum
is $\delta_*=2\sqrt{m\varepsilon/F}$, $B_*=2\sqrt{mF\varepsilon}$,
provided $\delta_*\le T-b$. Taking $b=\delta_*$ gives
$R_p=4\sqrt{mF\varepsilon}$, $R_q=7\varepsilon$, product
$28\sqrt{mF}\varepsilon^{3/2}$. Generally $\delta,b\to0$ and
$(\varepsilon_1+\varepsilon_2)/\delta\to0$ suffice to recover both
coordinates. A timing optimum outside the available horizon must be clipped.

The exact complete-history optimum includes the transient. Let $T$ now
mean the observed horizon, with records for every $t\in[0,T]$ of tolerance
$\varepsilon>0$. Put $\tau=\sqrt{m\varepsilon/F}$, $s=T/\tau$. Then

$$Q(T)=\varepsilon\min\{s^2/2,1\},\qquad
P(T)=\sqrt{mF\varepsilon}\,V(s),$$
$$V(s)=\begin{cases}
s,&0\le s\le\sqrt2,\\
\sqrt{2s^2+4}-s,&\sqrt2\le s\le4,\\
2,&s\ge4.
\end{cases}$$

Here is the full bounded-curvature proof. The central fibre consists of scaled
paths $x(0)=x'(0)=0$, $|x''|\le1$ and $|x|\le1$ on $[0,s]$. For
terminal velocity $v\ge0$, first $v\le s$. For fixed $v$, acceleration
$u=2w-1$ has $\int w=(s+v)/2$. Putting its positive part last minimizes
the decreasing-weight endpoint integral, giving

$$x(s)\ge(v^2+2sv-s^2)/4,\qquad v\le\sqrt{2s^2+4}-s.$$

Subtract the weight at the switching point to verify the minimizing
rearrangement pointwise, using the equal integrals. On the final $v$ time
units, $x'(t)\ge v-(s-t)$, so
$2\ge x(s)-x(s-v)\ge v^2/2$ and $v\le2$. The lower envelope of these
three bounds is $V$: junctions are $\sqrt2$ and $4$. Position has upper
bound $\min(s^2/2,1)$.

For $s\le\sqrt2$, $u=+1$ attains both endpoints. For
$\sqrt2\le s\le4$, put $h=s-\sqrt{s^2/2+1}=(s-V(s))/2$ and use
$u=-1$ for $h$ then $+1$ for $s-h$. The endpoint is $x=1$, $x'=V$;
its minimum at $2h$ is $-h^2\ge-1$ since $0\le h\le1$.
For $s\ge4$, wait $s-4$, use $-1$ for one unit then $+1$ for three units.
This reaches $-1$ with zero velocity after two active units and ends at
$+1$ with velocity $2$. Opposite paths hide behind the same inertial record.
The symmetric-fibre principle proves exact minimax attainment, including
both junctions and $T=0$.

A blind interval $b\ge0$ after the observed horizon has exact risks

$$P_b=P(T)+Fb,\qquad Q_b=Q(T)+bP(T)/m+Fb^2/(2m).$$

The same extremizer maximizes both observed endpoint coordinates; append
$+F$ to attain the bounds, while the triangle inequality supplies the upper
bounds on the central fibre. In saturation the hidden preparation can also
be described as $-F,+F$ for successive durations $\tau$, reaching
$-\varepsilon$ at rest, followed by $+F$ for $2\tau$ to reach
$+\varepsilon$ with momentum $2\sqrt{mF\varepsilon}$. Thus for
$T\ge4\tau$ two records separated by $2\tau$ already attain exactly the
complete-history coordinate risks, with the blind-delay extension above.
Densifying records at fixed tolerance cannot improve them. The time $4\tau$
is the earliest momentum saturation time for this known-initial-state model.
For this pair alone a speed ceiling holds if $F(2\tau+b)/m<c$ and $p_0=0$;
a ceiling imposed on the entire force class requires a new proof.

At short fixed-precision times $QP=F^2T^3/(2m)$. At fixed positive $T$,
improving tolerance eventually gives $QP=2\sqrt{mF}\varepsilon^{3/2}\to0$.
Neither complete-history access nor a force ceiling selects irreducible noise.

## Independent composition and discarded record labels

For independent input/error classes and retained constituent records, central
fibres are Cartesian products. For a scalar target $\sum_i a_iL_i$, symmetry
aligns constituent extremizers, so its exact minimax radius is
$\sum_i|a_i|r_i$. Compatible midpoint estimators and the common opposite
central pair prove both directions. For total mass $M=\sum m_i$, centre
position and total canonical momentum therefore have

$$Q_A=\sum_i m_iQ_i/M,\qquad P_A=\sum_iP_i.$$

For two bodies, relative position and its conjugate
$p_r=\mu(p_1/m_1-p_2/m_2)$ instead have
$Q_r=Q_1+Q_2$, $P_r=\mu(P_1/m_1+P_2/m_2)$.
Changing to centre/relative coordinates generally couples the admissible sets.
This is a radius law, distinct from independent-variance addition.

For force bounds $F_i$, tolerances $\varepsilon_i$ and common observed $T$,
retaining only the weighted centre record has exactly the one-body image

$$(M,F_\Sigma,E),\qquad F_\Sigma=\sum_iF_i,
\quad E=\sum_i m_i\varepsilon_i/M.$$

Every aggregate force $f$ and error $e$ lifts via
$f_i=F_if/F_\Sigma$, $e_i=\varepsilon_i e/E$, preserving prescribed initial
states and independence of forces/errors. Individual records in this lift
need not be inertial. Conversely sums obey those bounds. Hence its exact
risks $Q_B,P_B$ are the finite-horizon formulas above with these aggregate
parameters, and information inclusion gives $Q_B\ge Q_A$, $P_B\ge P_A$.

At $T\ge\max_i4\sqrt{m_i\varepsilon_i/F_i}$,

$$Q_A=Q_B=E,\quad P_A=2\sum_i\sqrt{m_iF_i\varepsilon_i},
\quad P_B=2\sqrt{MF_\Sigma E}.$$

The aggregate horizon condition follows because $ME/F_\Sigma$ is a
force-weighted average of $m_i\varepsilon_i/F_i$. Cauchy–Schwarz gives
equality of momentum risks exactly when $F_i/(m_i\varepsilon_i)$ is common.
Equal $m,\varepsilon$ with $F_2=4F_1=4F$ give
$P_A=6\sqrt{mF\varepsilon}$ and $P_B=2\sqrt{10mF\varepsilon}$.

At finite horizons put $A_i=F_iT^2/2$, $B_i=m_i\varepsilon_i$. Then
$MQ_A=\sum\min(A_i,B_i)$ and $MQ_B=\min(\sum A_i,\sum B_i)$.
Position loss is strict exactly when some $A_i<B_i$ and some $A_j>B_j$:
according to which sum is smaller the difference is respectively
$\sum(A_i-B_i)_+$ or $\sum(B_i-A_i)_+$. For equal masses/tolerances,
$F_1=F$, $F_2=16F$, $T=\sqrt{m\varepsilon/F}$ give

$$Q_A=3\varepsilon/4,\quad Q_B=\varepsilon,\quad
P_A=9\sqrt{mF\varepsilon},\quad
P_B=(\sqrt{714}-17)\sqrt{mF\varepsilon}>P_A.$$

Their products are $(27/4)\sqrt{mF}\varepsilon^{3/2}$ and
$(\sqrt{714}-17)\sqrt{mF}\varepsilon^{3/2}$; both coordinates can be lost
in this transient. Identical $n$-copy experiments instead give $H_A=H_B=nH_1(T)$
at every horizon, including $H_1^{\rm sat}=2\sqrt{mF}\varepsilon^{3/2}$.

If finite nonnegative radii depend only on mass and close separately under
all positive-mass product compositions, then $mQ(m)$ and $P(m)$ are additive.
Nonnegative additive functions are monotone and therefore linear, yielding
$Q(m)=q_*$, $P(m)=p_*m$, $H(m)=q_*p_*m$. A positive mass-independent
product is impossible under these premises, already by identical doubling.
Separate radius closure is an assumption, not inferred from product closure.
The class $F(m)=a m$ and common $\varepsilon$ realizes the extensive case at
$T\ge4\sqrt{\varepsilon/a}$, with $q_*=\varepsilon$,
$p_*=2\sqrt{a\varepsilon}$. It still supplies both scales.

## Shared error geometry and independently budgeted blocks

For $n$ identical constituents impose the pointwise budget
$\|e(t)\|_r\le\varepsilon$, $1\le r\le\infty$, independently of forces.
Set $E_n=\varepsilon n^{-1/r}$, $1/\infty=0$. Norm duality bounds the
average error by $E_n$. Equal errors attain it, and equal constituent forces
lift every aggregate force at mass $nm$, bound $nF$. The full-record central
fibre has displacements $z_i$ satisfying the same norm bound pointwise;
their average has $|z|\le E_n$, $|mz''|\le F$. Conversely every such scalar
central path lifts synchronously with $z_i=z$, errors $-z_i$. Thus retaining
all records or only the average gives exactly the same centre risks:

$$Q_n=E_n\min(s_n^2/2,1),\quad
P_n=n\sqrt{mFE_n}V(s_n),\quad s_n=T\sqrt{F/(mE_n)}.$$

The synchronous lift meets the budget at every time. At blind delay $b$,
$P_{n,b}=P_n+nFb$, $Q_{n,b}=Q_n+bP_n/(nm)+Fb^2/(2m)$.
In saturation,

$$H_n^{\rm sat}=n^{1-3/(2r)}H_1^{\rm sat},\qquad
T\ge4\sqrt{m\varepsilon/F}\,n^{-1/(2r)}.$$

$r=2$ gives $n^{1/4}$, $r=\infty$ gives $n$, $r=1$ gives $n^{-1/2}$;
$r=3/2$ gives copy-count invariance. For two quadratic-budget bodies this is
$2^{1/4}H_1^{\rm sat}$, with effective tolerance $\varepsilon/\sqrt2$.
At early times its product is $F^2T^3/m$. This is a selected apparatus norm,
not independent-preparation universality or a quantum phase constant.

Now partition $N$ identical constituents into independently budgeted blocks
of sizes $n_j$, each with $\|e^{(j)}\|_r\le\varepsilon_j$.
Let $E_j=\varepsilon_jn_j^{-1/r}$, $w_j=n_j/N$, and write
$q(T,E),p(T,E)$ for the one-constituent finite-horizon risks. The block lift
and Cartesian support law give, for all constituent records or all block
averages,

$$Q_A=\sum_jw_jq(T,E_j),\qquad P_A=\sum_jn_jp(T,E_j).$$

Keeping only the total centre record has exactly the single-body image with
precision $\bar E=\sum_jw_jE_j$, mass $Nm$, force bound $NF$.
Lift any centre error by $e_i=(E_j/\bar E)e$ within block $j$, and any total
force by equal constituent shares. Thus
$Q_B=q(T,\bar E)$, $P_B=Np(T,\bar E)$. At common saturation,

$$Q_A=Q_B=\bar E,\quad
P_A=2\sqrt{mF}\sum_jn_j\sqrt{E_j},\quad
P_B=2N\sqrt{mF\bar E}.$$

Strict concavity gives strict momentum loss unless all $E_j$ agree; at
arbitrary finite horizons the formulas govern, without a general strictness
claim. Equal blocks $n_j=a$, $\varepsilon_j=\varepsilon$ give

$$H_{\rm blocks}=k a^{1-3/(2r)}H_1^{\rm sat},\qquad
H_{\rm global}=(ka)^{1-3/(2r)}H_1^{\rm sat},\qquad
H_{\rm blocks}/H_{\rm global}=k^{3/(2r)}.$$

The block saturation horizon suffices for both. At $r=3/2$ independently
supplied identical blocks give $kH_1$, while one fixed global allowance gives
$H_1$. Regrouping unchanged constraints is associative; giving every child a
fresh allowance changes a sum constraint into a maximum constraint.

For finite $r$ the smallest centred unweighted global ball containing the
product of block balls has radius $B=(\sum_j\varepsilon_j^r)^{1/r}$,
attained by simultaneous saturation. For $k>1$ and positive budgets the
inclusion is strict: concentrate all $B$ in one block. No global ball equals
the product, since restrictions to each block subspace would require radius
$\varepsilon_j$, inconsistent with simultaneous saturation. Equal blocks
have $B=k^{1/r}\varepsilon$ and the same centre risks as the blocks at every
horizon, despite the strictly larger error set. To match the original global
$\varepsilon$ risks using separate equal blocks requires allowances
$\varepsilon k^{-1/r}$; their product is strictly contained in the matching
global ball. At $r=\infty$ the Cartesian sets coincide. A tolerance budget
is an admissible-error statement, not a derived energetic or monetary cost.

## Source scope and consequence for STATE

[B38](../references/batches/B38.md) reads Liberzon's bounded-input double
integrator and one-switch control passage; its arrival-time task differs from
the fixed-time lens proved here. [B39](../references/batches/B39.md) and
[B40](../references/batches/B40.md) record the cut and convex-area methods.
[B41](../references/batches/B41.md)–[B42](../references/batches/B42.md)
identify the exact Seeber–Haimovich differentiation/pair match.
[B43](../references/batches/B43.md)–[B46](../references/batches/B46.md)
record bounded coverage for product fibres, transient rearrangement, norm
budgets and block composition. These retain their original reading labels;
source capsules and internal checks do not establish publication priority.

For STATE, a physical apparatus restriction on attainable bands and delays
is still required. Known-flow delayed reconstruction is a different task,
proved in [the apparatus treatment](autonomous-finite-readout.md).
The exact lens area, coordinate-risk product and variance-based composition
law have different meanings. Refining delay or precision closes the scales
here; selecting one global error norm does not make it universal under
independent apparatus composition.
