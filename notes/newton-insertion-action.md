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

For the short-time force measurement in Lemma X, two bounded, increasing
forces can differ at release yet give the same final motion and even the
same forced-particle propagator at the first reading. A bound on how
fast the force changes restores uniform recovery with sufficient
differential position accuracy. A separate test using three position
probabilities gives a conditional lower bound on the trial action,
with an explicit allowance for a recoiling source.

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

## Lemma X and the measurement of initial force

In Book I, Lemma X, Newton changes *vi regulari* in the London 1687
edition to *Vi finita* in the Cambridge 1713 edition, specifying a force
that is constant, continually increasing or continually decreasing. In
the new Corollary 4 he infers force from initial displacement divided by
time squared, as a proportion. The following measurement is a modern
realization for a body of independently calibrated inertial mass $m$.
[1687, Lemma X](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00077#par27)
and [1713, Lemma X and Corollaries 3–5](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082#par28)
(diplomatic transcriptions, passages).

**What the marks have to resolve.** Read positions $y$ against an
inertial ruler at the calibrated times $0,\tau/2,\tau$. Let
$D_\tau y=y(0)-2y(\tau/2)+y(\tau)$. This cancels an unknown initial
position and velocity, including a common affine ruler drift. For
$m q''=f(t)$ with continuous $f$, the normalized second divided
difference averages $f$ with weight $4\min(t,\tau-t)/\tau^2$ on the
window. This weight integrates to one and has mean time $\tau/2$.
[De Boor, §9, Eqs. (47)–(48)](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf#page=17)
(passage, Peano kernel). Thus a single fixed force gives its initial
value in the limit. For a class with an independently calibrated bound
$|f(t)-f(0)|\le Lt$ and differential record error
$|D_\tau y-D_\tau q|\le\rho_\tau$,

$$
\left|\frac{4m}{\tau^2}D_\tau y-f(0)\right|
\le \frac{L\tau}{2}+\frac{4m\rho_\tau}{\tau^2}.
$$

Here $L$ has units force/time and $\rho_\tau$ is a length. Calibration of
the gate times or their contribution to $\rho_\tau$ is part of the
protocol. Uniform recovery follows if $m\rho_\tau/\tau^2\to0$. For a
specified force accuracy it suffices to keep the right side below that
accuracy. The equations of classical mechanics allow all these conditions.
For linear three-meter measurements of a free mass under a prescribed
force, the same difference removes the initial test-body variables.
Measuring a suitable combination of the middle pointer's position and
momentum also cancels its recoil from the output, at a cost in meter
preparation. This prevents inferring an irreducible record error from
the test mass's initial spread alone.
[Braginsky et al., §II B, Eqs. (2.21)–(2.24), (2.29)–(2.33)](https://arxiv.org/pdf/gr-qc/0109003#page=7)
(passage).

**Two forces hidden before the first reading.** Fix a force unit $F_*>0$
and any interval of duration $s>0$ between release and the first
positive observation. Write $u=t/s$ and define on $[0,1]$

$$
\begin{gathered}
H(u)=u^4(1-u)^6/24,\qquad h=H^{(4)},\\
\eta=\frac{1}{2(1+\|h\|_\infty+\|h'\|_\infty)},\qquad
f_\pm(t)=F_*[1+u\pm\eta h(u)].
\end{gathered}
$$

Both forces are positive and strictly increasing. Their slopes are at
least $F_*/(2s)$, and $h(0)=1$, $h(1)=h'(1)=0$. Continue both by
$F_*(3-\exp(1-u))$ for $u\ge1$. They are continuously differentiable,
bounded by $3F_*$, and differ at release by $2\eta F_*$ independently
of $s$. Four integrations by parts give $\int_0^1u^j h(u)\,du=0$ for
$0\le j\le3$, since $H$ and its first three derivatives vanish at both
ends. The first two moments match the endpoint impulse and displacement
for every common initial state. Within the window the position difference
is $2\eta F_*s^2 H''(u)/m$ and afterwards it is zero. Thus even a
continuous position record with fixed positive error can be shared by
choosing $s$ small enough and taking the midpoint of the two records.

The pair also tests phase-sensitive readout. For the prescribed
Hamiltonians $p^2/(2m)-f_\pm(t)q$ with a common scalar-potential zero,
the [general force propagator identity](cut-measure-newton.md#general-force-histories-one-dirichlet-functional)
(Theorem G7(a), passage) reduces endpoint evolution to two kicks and
the scalar action $\langle f,G_s f\rangle/(2m)$, where $G_s$ is the
Dirichlet inverse of $-d^2/dt^2$ on $[0,s]$. The kicks agree by the
first two moments. With $b(t)=1+t/s$, the difference of the two scalar
actions is $(2\eta F_*^2/m)\int_0^s h(t/s)(G_s b)(t)\,dt$. Since
$G_s b$ is a cubic polynomial in $t$, the remaining moments make this
integral zero.
The two body propagators are identical, including their phase, for every
supplied reduced action $a>0$. This covers endpoint interference against
a common reference. A record of the drive or an intervention within
the interval is additional data. At each smaller first gate the
construction chooses a different pair. It proves failure of a uniform
force measurement over Newton's finite monotone class and preserves the
pointwise limit for each fixed force.

**A reciprocal classical source.** Give the source a finite mass $M$,
put $\mu=mM/(m+M)$, and choose a common initial separation
$r_0$ and relative speed $v>0$. Solve $\mu\ddot r_\pm=f_\pm(t)$ from
these data. Since $\dot r_\pm\ge v$, define a time-independent pair
potential along each path by $V_\pm'(r_\pm(t))=-f_\pm(t)$. It exerts
opposite forces on the two masses. At $s$ the separations and relative
speeds agree by the matched moments. Free centre-of-mass motion then
gives identical endpoint positions and momenta of **both** masses. With
equal initial potential zeros, the work identity
$V_\pm(r_0)-V_\pm(r_\pm(s))=\mu(\dot r_\pm(s)^2-v^2)/2$
also matches their terminal energies and allows a common continuation.
During the window $\dot r_\pm\le v+2F_*s/\mu$ and
$r_\pm(s)-r_0\le vs+F_*s^2/\mu$. The interaction changes over a
shrinking length. Its force gradient at the join has magnitude
$F_*/(s\dot r_\pm(s))$. Fixed masses, initial speed and bounded exchanged work
allow these potentials in classical mechanics. Their fabrication and
independent inspection would require a source model of their own.
The propagator equality above applies to the prescribed uniform fields.
This reciprocal realization establishes classical endpoint equality for
the stated initial preparation.

## A three-time test with a calibrated position resolution

A candidate physical premise can be stated entirely in observed
frequencies. Prepare the same ensemble of bodies and independently choose
one final reading per run at $t_j=0,\tau/2,\tau$, with no earlier
measurement. For a spatially uniform calibrated acceleration $g$,
subtract $g(t_j-\tau/2)^2/2$ from each position. Write $p_j$ for the
probability that this corrected position, after the calibrated blur
below, falls in the same bounded interval $I$ of the ruler. Count all
preselected runs, with missing outcomes included in the error bounds.
The proposed observation is a positive excess

$$V=p_0+p_2-p_1-1>0.$$

The corresponding classical bound $V\le0$ is the particle reentry inequality of
[Paterek and Goussev, Eqs. (2) and (4)](https://arxiv.org/pdf/2511.10155#page=2)
(passage), in the freely falling coordinates of the parabola. A classical
trajectory is a straight line in these coordinates. Membership of both
endpoints in $I$ implies membership of the midpoint, for every initial
place and velocity and hence for every positive distribution over them.
This also allows arbitrary extra preparation labels when the choice of
gate is independent and the calibrated detector reads the body's position.

**How a violation would exclude small actions.** Fix a ruler width
$\ell>0$ and a calibration time $T_c>0$ independently of the gate spacing.
Set $w=\ell/T_c$. Require that the total position response at each gate
be a centred Gaussian of variance $\sigma_j^2=\ell^2+w^2(t_j-\tau/2)^2$.
This is a specification for the calibrated detector response including
any blur deliberately applied to its records. It makes the three noise
marginals exactly those of adding one random affine function
$X+U(t-\tau/2)$ with independent centred Gaussian offsets of standard
deviations $\ell,w$. Thus the blurred records still obey $V\le0$ for
every classical ensemble. Measurements on different runs require no
joint draw of these offsets.

Compare also every canonical Schrödinger model with trial reduced
action $a>0$, the same mass $m$, uniform force $mg$, and Born position
readout. Its Wigner distribution at the middle time propagates by the
exact affine Newtonian flow, so blurring the three marginals is equivalent
to convolving that distribution at the middle time with a Gaussian of
covariance $\operatorname{diag}(\ell^2,m^2w^2)$ in position and momentum.
The Gaussian smoothing theorem gives a positive probability density for
every state when $\ell m w\ge a/2$. The classical interval argument then
applies to that density.
[Quadratic transport, Theorem A(b)](principia-fifth-postulate.md)
(passage) and [Cartwright, Gaussian smoothing](https://doi.org/10.1016/0378-4371(76)90145-X)
(abstract). If simultaneous error bounds $e_j$ cover the three reported
probabilities at the stated joint confidence level, then

$$
\widehat p_0+\widehat p_2-\widehat p_1-1>e_0+e_1+e_2
\quad\Longrightarrow\quad
a>2m\ell w=\frac{2m\ell^2}{T_c}
$$

for every such candidate model. The observation also excludes the
classical zero member under the stated trajectory and readout laws.
The bound uses a mass, a length and a time supplied without quantum
calibration. The other dimensional inputs are the gate times, the
interval endpoints and the acceleration. For a spatially uniform force
with acceleration miscalibration bounded by $\delta g$, the residual
shift at gate $j$ is at most $\delta g(t_j-\tau/2)^2/2$ relative to
the middle-time tangent. A shift $d$ changes the blurred interval
probability by at most $|d|/(\sqrt{2\pi}\sigma_j)$, from the derivative
of the Gaussian interval probability. Other errors in the force law,
clock, detector or gate selection need their own probability bounds.

**Allowing an unobserved source to recoil.** Suppose the source remains
coupled throughout the gate. In a canonical model, add a source
Hamiltonian and a bounded self-adjoint
potential $W_t(Q)$ acting on the source at each body coordinate.
Assume the source alone has a unitary propagator, the perturbation is
norm-continuous in time, and a force calibration supplies
$\sup_q\|W_t(q+d)-W_t(q)\|\le m\delta g|d|$ for every $d,t$.
This includes bounded reciprocal pair potentials $W(q-R)$ with the
stated slope. For any joint state at the middle time $t_m=\tau/2$,
the error in gate probability caused by dropping this coupling is at most

$$b_j=\frac{\delta g(t_j-t_m)^2}{\sqrt{2\pi}\,\sigma_j}.$$

Indeed, under the reference uniform force, the terminal mode $e^{ikQ}$
transported back to an intermediate time $r$ translates the argument
of $W_r$ by a distance of magnitude $a|k(t_j-r)|/m$. Its commutator
with $W_r$, divided by $a$, has norm at most $\delta g|k(t_j-r)|$.
The bounded-perturbation Duhamel formula in either time direction gives
a mode error at most $\delta g|k|(t_j-t_m)^2/2$.
For the Gaussian-blurred interval effect $B_j$,
$|k\widehat B_j(k)|\le2\exp(-\sigma_j^2 k^2/2)$ in the Fourier
convention with inverse factor $1/(2\pi)$. Integrating the mode error
gives $b_j$. The deterministic correction for $g$ translates the
interval and leaves this bound unchanged. Starting both evolutions
at the same middle-time joint state allows arbitrary body–source
correlations. The comparison probabilities are those of one common
reduced body state. For a classical source with $|\ddot q-g|\le\delta g$
on each unobserved path, the tangent displacement bound above gives
at most $b_j/2$ per gate even if the residual depends on that path.
Thus adding $\sum_j b_j$ to the required excess covers both classes.
The calibration has to bound the interaction on the admitted domain.
A mean acceleration measurement alone supplies no such bound.

Subdividing the mathematical propagation between these fixed gates
changes neither side of the test. Physically sending $\tau$ to zero
at fixed $\ell,T_c$ and fixed release preparation is different. All
three blurred probabilities then converge to the same $p<1$ by
continuity of the motion and readout, so $V\to p-1<0$. The positive
width and bounded $I$ give the strict inequality. Conversely, a strict
ideal reentry violation on a half-line persists for some finite interval
and sufficiently small positive blur by continuity of the three marginal
probabilities. Paterek and Goussev exhibit such states in the supplied
quantum theory. The missing physical input is a violation in corrected
gate counts with the response and errors independently calibrated.
[Brown et al., Fig. 3 and supplement IV B](https://arxiv.org/pdf/2203.03053#page=4)
(passages) reconstruct a trapped atom's state from quadratures by a
quantum maximum-likelihood fit. Their reported Wigner negativity does
not supply these three counts. A verified violation would constrain
the calibrated motional models above. Extending that constraint to all
preparations requires a further physical argument.

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
For Lemma X, a bound on the force gradient and relative speed of a
reciprocal source gives a testable $L$. The three-time experiment instead
tests a common distribution of trajectories directly. Independent
evidence for the calibrated probability excess remains open.
