# Newton's comparison: areas, action defects and controlled reunion

For horizontal speed $v>0$ and downward force $F>0$, Galileo's inertial line
and falling parabola enclose area $A=vF\tau^3/(6m)$, with the exact conversion

$$\boxed{(3F/v)A=\tau\Delta E,\qquad\Delta E=F^2\tau^2/(2m).}$$

The matched-endpoint chord lens is half that area and has action defect
$F^2\tau^3/(24m)=\tau\Delta E/12$. A genuine receding-centre limit preserves
this chord defect but cancels the apparent tangent-sector remainder. A
specified $F,-F,F$ force loop reunites both position and velocity and gives
an exact scalar quantum phase for every common motional preparation, once
quantum kinematics and coherent control are supplied. None of these geometric
or phase statements establishes independent positive-action necessity.

This treatment integrates the constant-force derivation and its receding-centre
correction with the controlled reunion. Written model/coordinator checks are
internal; the mechanics and phase ingredients are established and no
literature-priority claim is made.

## The source geometry and three different areas

Take $m,F,v,\tau>0$, downward $y$, and

$$q_I(t)=(vt,0),\qquad q_F(t)=(vt,Ft^2/(2m)),\quad0\le t\le\tau.$$

The inertial–fall region is closed by the vertical segment at $x=v\tau$.
Direct integration gives $A=vF\tau^3/(6m)$, sagitta
$s=F\tau^2/(2m)$ and deterministic transverse kinetic gain
$\Delta E=Fs=F^2\tau^2/(2m)$. Total mechanical energy is conserved;
the potential loses that amount. This $\Delta E$ is not a quantum energy
standard deviation.

| Region | Positive ordinary area |
| --- | --- |
| Inertial horizontal line to falling parabola | $vF\tau^3/(6m)$ |
| Matched-endpoint chord to falling parabola | $vF\tau^3/(12m)$ |
| Inertial line to endpoint chord | $vF\tau^3/(4m)$ |

The first is twice the second; the third is their sum. Kepler sectors about
a force centre are another construction. A horizontal Galilean boost to
speed $v$ removes the plotted spatial area, while a matched-endpoint action
difference remains: the common horizontal action cancels. The conversion
therefore specifies a frame with $v\ne0$.

[Diagram of constant-force regions](../out/constant-force-areas.svg)

The read witnesses are [Motte/Chittenden 1846](../docs/Newton_Principia_Motte1846.md),
Definitions I–VIII and Scholium, Laws/corollaries, Book I Section I and
Section II Propositions I–II, and the
[Motte 1729/Wilkins excerpt](../docs/Newton_Principia_BookI_SectionI_Motte1729_Wilkins2002.md).
Reading level: the named English passages, not every edition or full historical
literature. Their relevant paragraph map is:

| Passage, 1846 printed pages | Use |
| --- | --- |
| Definitions II, IV, VII–VIII, 73–77 | Momentum and impressed, accelerative and motive force |
| Definition Scholium, 77–82 | Mathematical time/space versus sensible measures |
| Laws Corollaries V–VI, 89 | Relative motion under common translations/accelerations |
| Laws Scholium, 89–90 | Projectile parallelogram and Galileo's parabola |
| Lemmas I–III, 95–96 | Limits of inscribed/circumscribed figures |
| Lemma X, 99–100 | Initial force displacement quadratic in duration |
| Lemma XI Cor. 4–5, 101 | Cubic tangent triangles and one-third curved segment |
| Section I closing Scholium, 102–103 | Evanescent divisible quantities and limiting ratios |
| Proposition I, 103–105; II, 105–106 | Central impulse polygon and converse area-direction law |

The common parallel force belongs to the projectile Scholium and Lemmas X–XI;
Proposition I assumes a fixed centre. Some source equations are images;
Wilkins's PDF and the [projectile](../docs/images/i_090a.jpg) and
[central polygon](../docs/images/i_104.jpg) figures supplied the recorded
passage checks. The historical limits are not evidence for an established
fluxional-time interpretation or a physical $\hbar\to0$ theorem.

## Matched endpoints, arbitrary partitions and action normalization

For $L=m|\dot q|^2/2+Fy$, the same-endpoint chord has
$y_C(t)=F\tau t/(2m)$. If $y=y_F+\eta$ and both endpoint variations
vanish, integration by parts using $m\ddot y_F=F$ gives

$$S[y_F+\eta]-S[y_F]=\frac m2\int_0^\tau\dot\eta^2dt.$$

For $\eta=Ft(\tau-t)/(2m)$ this is

$$D_{C,F}=\frac{F^2\tau^3}{24m}
 =\frac{F}{2v}A_{\rm chord,fall}
 =\frac{F}{4v}A_{\rm inertial,fall}=\frac{\tau\Delta E}{12}.$$

A common ordinary point-function term $dG(q,t)/dt$ added to $L$ cancels
because the endpoints and times agree. A velocity-dependent $G$ changes
the endpoint data required by that statement: adding
$d(\kappa\dot y)/dt$ changes this chord-minus-parabola action by
$-\kappa F\tau/m$, since their endpoint velocities differ. That is a
higher-derivative Lagrangian, outside this point-mechanics convention.
The bare inertial and falling paths have different vertical
endpoints; an observable phase comparison needs endpoint/control phases.

For a partition $0=t_0<\cdots<t_N=T$ with steps $\tau_j$, the polygon
interpolating exact trajectory values has

$$D_\pi=\frac{F^2}{24m}\sum_j\tau_j^3
 \le\frac{F^2T}{24m}|\pi|^2\longrightarrow0,\qquad
A_\pi=\frac{vF}{12m}\sum_j\tau_j^3.$$

The local tangent slope cancels in each chord lens. At fixed $N$ convexity
minimizes the sum at equal steps, $\sum\tau_j^3=T^3/N^2$. Splitting a cell
into $a,b>0$ decreases its defect by $F^2ab(a+b)/(8m)$. These are sampled
chords; an executed force-impulse polygon has its own dynamical error estimate.
The unmarked vertex impulse $F\tau_j$, sagitta and area can all vanish while
$2ms(\tau_j)/\tau_j^2=F$ stays exact.

Neighbouring off-shell variations $\eta=\alpha t(\tau-t)$ have defect
$m\alpha^2\tau^3/6\to0$. Positive Dirichlet curvature does not make a
smallest positive defect. Likewise the deterministic work $\Delta E$ is
not the $\sigma_H$ in Mandelstam–Tamm:

$$\sigma_H\sigma_B\ge\tfrac12|\langle[H,B]\rangle|,\qquad
\tau_B=\frac{\sigma_B}{|d\langle B\rangle/dt|},\qquad
\sigma_H\tau_B\ge\hbar/2,$$

under the proper domains and a nonzero denominator. With $v<c$, the
Newtonian constant-force segment stays below $c$ if
$\tau<(m/F)\sqrt{c^2-v^2}$; arbitrarily small intervals remain possible.
The [foundations manuscript](../papers/action-gap-foundations.tex) retains
its distinct relativistic variation calculation. Feynman's
[least-action discussion](../docs/Feynman_LeastAction_II19.md), passage,
uses contributions with action differences within $\hbar$, not a prohibition
on such paths. A supplied phase rule $e^{iS/\hbar}$ gives period
$h=2\pi\hbar$ and an order-one comparison duration
$(24m\hbar/F^2)^{1/3}$ for this pair; it does not select $\hbar$.

## A genuine receding centre: subtract before taking the limit

For $C_R=(0,R)$ define signed sector area

$$A_R[\gamma]=\frac12\int_\gamma[x\,dy-(y-R)\,dx]
 =\frac R2\Delta x+\frac12\int_\gamma(x\,dy-y\,dx).$$

The $R$ term cancels exactly for paths sharing endpoints, giving their closed
loop area. For a fixed limiting parabola its finite part is
$Fv\tau^3/(12m)$. A varying family must also retain its endpoint correction.
Use the actual central-force solutions

$$m\ddot q_R=(F/R)(C_R-q_R),\quad q_R(0)=0,\quad\dot q_R(0)=(v,0),
\quad\omega_R^2=F/(mR),$$
$$x_R(t)=\frac v{\omega_R}\sin(\omega_Rt),\qquad
y_R(t)=R[1-\cos(\omega_Rt)].$$

They converge on compact time intervals to the parabola, but
$x_R(\tau)=v\tau-Fv\tau^3/(6mR)+O(R^{-2})$.
Angular momentum about $C_R$ is $mRv$, so the arc and inertial tangent
both have sector area $Rv\tau/2$, with difference zero at every $R$.
The endpoint term

$$\frac R2[x_R(\tau)-v\tau]\longrightarrow-\frac{Fv\tau^3}{12m}$$

cancels the apparent finite part. Replacing the path by its limiting parabola
before subtracting the divergent reference changes this comparison.
For the chord joining the **actual** arc endpoints instead,

$$A_R[q_R]-A_R[\operatorname{ch}_R]
 =\frac{Rv}2\left[\tau-\frac{\sin(\omega_R\tau)}{\omega_R}\right]
 \longrightarrow\frac{Fv\tau^3}{12m}.$$

This preserves precisely the matched-endpoint lens and its normalization,
not the inertial tangent sector. Source/proof context:
The named source passages above support the geometric comparison. Its
written calculation is internal; no independent historical or proof review
is claimed.

## Controlled reunion of the inertial and falling arms

Keep a reference arm at zero transverse force and apply to the signal arm

$$f(t)=\begin{cases}F,&0<t<\tau,\\-F,&\tau<t<3\tau,\\
F,&3\tau<t<4\tau.\end{cases}$$

Both begin at $y=\dot y=0$. This is branch-controlled motion; gravity needs
compensation on the reference and return stages. Define
$P(t)=\int_0^tf$, $Y(t)=m^{-1}\int_0^tP$. Then $P(4\tau)=Y(4\tau)=0$;
$P/F$ is respectively $t$, $2\tau-t$ and $t-4\tau$. Direct integration gives

$$\int_0^{4\tau}P^2dt=\tfrac43F^2\tau^3,\qquad
\int_0^{4\tau}Ydt=2F\tau^3/m,\qquad
A_{\rm loop}=2vF\tau^3/m=12A_{\rm inertial,fall}.$$

$Y\ge0$ peaks at $F\tau^2/m$ at $2\tau$. Using $m\ddot Y=f$ and the
vanishing boundary term $mY\dot Y$,

$$\Delta S_{\rm loop}=-\frac1{2m}\int P^2dt
 =-\frac{2F^2\tau^3}{3m}=-\frac F{3v}A_{\rm loop}
 =-\frac43\tau\Delta E.$$

The sign and coefficient differ from the off-shell chord defect because
return forces are part of this experiment. Its exact comparison with the
original falling lens is $|\Delta S_{\rm loop}|=4FA_{\rm inertial,fall}/v$.

Supply canonical quantum kinematics, a coherent two-arm label and
$H_I=p^2/(2m)$, $H_F(t)=H_I-f(t)y$, with no additional arm-dependent
scalar potentials or uncontrolled phases. In the interaction picture,
$B(t)=if(t)(y+tp/m)/\hbar$ has scalar commutator

$$[B(t),B(s)]=\frac{if(t)f(s)(t-s)}{m\hbar}.$$

Higher nested commutators vanish and $\int f=\int tf=0$ kills the first
integrated term. The second yields exactly

$$U_I(4\tau)^\dagger U_F(4\tau)
 =\exp\left[-\frac{i}{2m\hbar}\int_0^{4\tau}P^2dt\right]I
 =e^{i\Delta S_{\rm loop}/\hbar}I.$$

The sign follows by integrating
$\int f(t)\int_0^tf(s)(t-s)ds\,dt=-\int P^2dt$.
The algebra on Schwartz states extends by the forced free-particle unitaries
to the motional Hilbert space. Position and momentum reunite exactly for
every common initial motional preparation, not just classical centroids.

## A conditional finite-copy phase threshold is not an action lattice

A balanced coherent arm label has relative phase
$\phi=\Delta S_{\rm loop}/\hbar$. Against the zero-phase reference,
$n$ independent copies and arbitrary joint binary measurement give

$$p_{\rm opt}=\tfrac12\left(1+\sqrt{1-\cos^{2n}(\phi/2)}\right).$$

On the first lobe $|\phi|\le\pi$, success at least $p_*>1/2$ requires

$$d_{n,p_*}=2\hbar\arccos([4p_*(1-p_*)]^{1/(2n)}),\qquad
\tau\ge\left(\frac{3m d_{n,p_*}}{2F^2}\right)^{1/3},\qquad
A_{\rm inertial,fall}\ge\frac{v d_{n,p_*}}{4F}.$$

For $n=1,p_*=3/4$, $d=\pi\hbar/3$. At fixed $p_*<1$ it tends to zero
as $n\to\infty$, whereas perfect discrimination requires $\pi\hbar$ for
every finite $n$. Periodicity prevents a monotone extension beyond that lobe.
The loop remains defined below the threshold; only its distinguishability
at those resources decreases. The [matched two-path experiment](galileo-two-path-interference.md)
uses a different control history and retains its own noncommuting-limit tests.

Similarly, with $h_P=2\pi\hbar$, $J\Delta\phi\ge h_P$ for $N$ equal angular cells gives
$J\ge N\hbar$, not exact quantization: $J=(N+1/2)\hbar$ satisfies all
cell bounds. Exact tiling is additional. In the conditional Kepler model
$E_N=-A/N^2$, if $\omega_N=\hbar^{-1}dE_N/dN$ and
$T_N=2\pi/\omega_N$, then

$$\frac{(E_{N+1}-E_N)T_N}{h_P}
 =\frac{N(2N+1)}{2(N+1)^2}\longrightarrow1.$$

The derivative rule is exact while finite differences approach it. No step
transfers a comparison-path threshold to orbital cells without a physical map.

Uniform mean anomaly and a single whole-orbit action are Kepler
specializations. Generic bound central motion has radial and angular
actions, need not close and can have incommensurate frequencies. Reduced
actions $(2\pi)^{-1}\oint p\,dq$ must be distinguished from the unreduced
integrals. EBK offsets and quantum angular-momentum spectra require their
own quantum or semiclassical premises; none follows from a cell inequality.
Large $J/\hbar$ describes a changing large-action family or a specified
formal limit. Holding $J$, physical $\hbar$ and $J=N\hbar$ fixed while
taking $N\to\infty$ is inconsistent.

## Consequence for STATE

The inertial–parabola area, matched chord defect, receding-centre sectors and
controlled reunion retain different endpoints and coefficients. Mesh size,
record resolution and $\epsilon=\hbar/S_0$ are separate limits. A consistent
classical geometric refinement and a supplied quantum phase benchmark are
both constructed here; independent exclusion of zero action remains open.
