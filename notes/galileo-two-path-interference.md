# Galileo's comparison as two-path interference

A coherent, endpoint-matched comparison
of Newton's impulsive chord with Galileo's constant-force parabola has
action difference

$$
K_\tau:=\Delta S=\frac{F^2\tau^3}{24m}
=\frac{F}{4v}A_{\rm inertial,fall}=\frac{\tau\Delta E}{12}.
$$

At supplied reduced phase parameter $\hbar>0$, its optimal equal-prior
error against the zero-phase reference, using $n$ independent controlled
passes and an arbitrary joint measurement, is exactly

$$
p_{\rm err}^{(n)}=\frac12\left(1-
\sqrt{1-\cos^{2n}\!\left(\frac{K_\tau}{2\hbar}\right)}\right).
$$

For fixed $n,\hbar$, refinement sends this error to $1/2$.
At fixed $\tau>0$, the coherent error oscillates as
$\hbar\downarrow0$ and has no limit. A specified averaging of the
inverse phase parameter gives a genuine noncommutation theorem for coherence;
a specified tunable comparison gives one for distinguishability
(Theorem 3). These prescriptions make precise the extra operation needed
in the proposed classical-first limit.

The resulting action threshold is conditional on the phase rule, the
Born rule and the resources of the comparison. It re-expresses the
polygon-lift phase bound through the halved functional. Theorems C and E
of the fifth-postulate note constrain different records with the same
supplied quantum action constant. Positivity of that constant remains an
independent physical obligation. All results below are proved under
their displayed hypotheses; the scale-selection step remains open.

The symbol $\hbar$ is the supplied reduced quantum phase constant, with physical Planck action $h_P=2\pi\hbar$. The time mesh and instrument resolution remain separate. Varying or averaging inverse values in the limiting theorems below is a formal family-of-models prescription, not an experiment that varies nature's constant or an automatic record-resolution law.

The comparison uses controlled unitaries and product copies; Proposition 2
is not used in the limiting Theorem 3. Its relative averaging prescription
is part of the hypothesis. Model checks are internal, not independent review.

A second experiment records the electron's position after opening either
slit or both. Three calibrated count distributions can give an action
band. Moving a window of known width across the beam can determine a
single reduced action magnitude in the scalar model, even with unknown
illumination. The force the window exerts on the transmitted beam limits
what published fringes establish about zero action. A classical shutter
with one random-impulse scale reproduces the entire averaged pattern,
even when the electron and shutter positions are read together.
[Two slits and a position detector](#two-slits-and-a-position-detector).

## 1. The Galileo area and the two histories

Let $m,F,v,\tau>0$, with downward coordinate $y$ and common horizontal
motion $x=vt$. The initial tangent and falling curve are

$$
y_I(t)=0,\qquad y_F(t)=\frac{Ft^2}{2m},\qquad
A_{\rm inertial,fall}=\frac{vF\tau^3}{6m},\qquad
\Delta E=\frac{F^2\tau^2}{2m}.
\tag{1}
$$

Thus $(3F/v)A_{\rm inertial,fall}=\tau\Delta E$.
The common-endpoint chord is $y_C(t)=F\tau t/(2m)$.
For the transverse Lagrangian $L=m\dot y^2/2+Fy$, direct integration gives

$$
S[y_I]=0,\qquad S[y_F]=\frac{F^2\tau^3}{3m},\qquad
S[y_C]=\frac{3F^2\tau^3}{8m},\qquad S[y_C]-S[y_F]=K_\tau.
\tag{2}
$$

The horizontal action cancels in every difference. Equation (2) also
exposes the endpoint issue: the bare tangent and parabola finish at
different heights. Adding $d\chi(y,t)/dt$ to $L$ changes their action
difference by their unequal final $\chi$ values. Their measurable
relative phase therefore requires endpoint matching and specified
control phases. The conversion coefficient for $K_\tau$ is $F/(4v)$;
the area conversion $(F/v)A_{\rm inertial,fall}$ equals $4K_\tau$.

Here is the exact matching used throughout. Supply canonical quantum
kinematics $[y,p]=i\hbar$ in the Schrödinger representation, and set

$$
U_\tau=\exp\left[-\frac{i\tau}{\hbar}
\left(\frac{p^2}{2m}-Fy\right)\right],\qquad
Q_\tau=e^{iF\tau y/(2\hbar)}
e^{-i\tau p^2/(2m\hbar)}e^{iF\tau y/(2\hbar)}.
$$

**Lemma 1 (matched comparison).** With these scalar-potential
conventions,

$$Q_\tau=e^{iK_\tau/\hbar}U_\tau.\tag{3}$$

*Proof.* The kernel of $Q_\tau$ has the free normalization and phase
$L_\tau(x,y)=m(y-x)^2/(2\tau)+F\tau(x+y)/2$. The classical solution
joining $x$ to $y$ is
$q_*(t)=x+(y-x)t/\tau+F(t^2-\tau t)/(2m)$.
Substitution into the action gives $L_\tau-K_\tau$. The fluctuation
action about $q_*$ is exactly $\int m\dot\xi^2/2$, with zero endpoint
fluctuations, hence the same free Gaussian normalization. This proves
(3), equivalently the exact quadratic kernel identity in the
[insertion note, §§2--3](refinement-composition-and-limit.md)
(passage). $\square$

The impulses in $Q_\tau$ reproduce the chord and match the parabola's
final momentum after the last half-kick. Equation (3) holds for every
initial body state. A branch-dependent scalar potential would add its
own phase, so its absence or calibration is part of the experiment.
The [polygon-lift note, Theorem 1](cut-measure-newton.md#weyl-lifting-and-polygon-phases) (full-read)
proves the corresponding identity for every partition.

For a literal tangent arm, the explicit reunion in
[the Galileo note, §§3--4](newton-insertion-action.md) (full-read)
uses signal forces $F,-F,F$ over durations $\tau,2\tau,\tau$ against a
free reference. Its closed action difference is
$\Delta S_{\rm loop}=-2F^2\tau^3/(3m)=-16K_\tau$.
Every phase formula below applies with that signed difference when that
four-cell experiment is chosen. The coefficient belongs to the reunion
protocol; the original area (1) remains the geometric anchor.

For fixed endpoints the constant-force action has one stationary path.
The chord is an off-shell path for the continuous-force action and a
classical history for the impulsive control. Thus (3) compares two
controlled histories, each with an exact quadratic path integral.
Treating the tangent and parabola as two stationary points of one
fixed-endpoint constant-force functional would change the variational
problem.

## 2. What the halved functional measures

Use $\hbar$ for reduced phase parameter and $\eta\in[0,1/2)$ for a target
decision error. Identification with quantum mechanics means
$\hbar=|\hbar|$, with ordinary Planck constant $h_P=2\pi|\hbar|$.

**Proposition 2 (two contributions and their remainder).** Suppose a
halved functional, with its normalization and observable fixed, has
two retained contributions

$$
\mathcal A_\hbar
=a_0e^{iS_0/\hbar+i\mu_0}
+a_1e^{iS_1/\hbar+i\mu_1}+R_\hbar,
\quad a_j\ge0,\quad |R_\hbar|\le r.
$$

Put $\phi=(S_1-S_0)/\hbar$ and $\beta=\mu_1-\mu_0$. Then

$$
|\mathcal A_\hbar|^2
=a_0^2+a_1^2+2a_0a_1\cos(\phi+\beta)+E,
\qquad |E|\le2(a_0+a_1)r+r^2.\tag{4}
$$

*Proof.* Expand the square, bound the leading amplitude by $a_0+a_1$,
and bound its cross term with $R_\hbar$ by $2(a_0+a_1)r$.
$\square$

For two nondegenerate stationary points at a fixed partition,
$a_j=|O(z_j)|/\sqrt{|\det S''(z_j)|}$ and $\mu_j$ contains the
observable phase and Hessian signature. Stationary phase supplies
$r\le C_\pi\hbar$ for sufficiently small $\hbar$, with
cutoffs and smoothness as in
[round 1, §1](rivero-1998-conjecture-central-forces.md) (full-read).
Equation (4) retains that partition-dependent constant; uniform control
as the partition changes needs a separate estimate. For the exactly
matched quadratic propagators in (3), the relative phase has zero
remainder and zero relative Gaussian signature.

At a fixed phase, a large $|S_1-S_0|/\hbar$ still leaves the cross
term in (4) at full amplitude. Averaging, selecting a branch, or
retaining an orthogonal branch record supplies the missing
diagonalization. Equal-action contributions survive phase averaging,
as round 1's pair of quartic saddles demonstrates.

An operational record requires a preparation and measurement rule in
addition to (4). For example, tag the arms by normalized pointer states
$|r_0\rangle,|r_1\rangle$, and put
$\gamma=\langle r_0|r_1\rangle$. Recombining the arms gives the cross term
$2a_0a_1\operatorname{Re}(\gamma e^{i(\phi+\beta)})$ and visibility
$V=2a_0a_1|\gamma|/(a_0^2+a_1^2)$.
For balanced arms and pure tags, optimal inference of the arm from the
pointer has

$$
D_{\rm path}=\sqrt{1-|\gamma|^2},\qquad
p_{\rm path}=\frac{1-D_{\rm path}}2,\qquad
V^2+D_{\rm path}^2=1.\tag{5}
$$

The eigenvalues of the difference of the two rank-one tag states are
$\pm\sqrt{1-|\gamma|^2}$, proving (5) by the binary measurement
optimization used below. This is the pure balanced case of established
interferometric duality; see
[Schwindt, Kwiat and Englert 1999](https://arxiv.org/abs/quant-ph/9908072)
(abstract). Path identification depends on the tags, while phase
detection depends on coherent recombination. Orthogonal tags identify
the arm even at $\Delta S=0$ and remove its interference. A bare halved
functional supplies neither those tags nor their physical cost.

## 3. Exact phase record, error target and resources

Prepare a balanced control qubit and a common arbitrary body density
operator $\rho$. Under hypothesis $H_0$, apply $U_\tau$ in both arms;
under $H_1$, apply $U_\tau$ in arm 0 and $Q_\tau$ in arm 1. Supply
coherent control with calibrated relative scalar phases, no extra
environmental tags, the Born rule, and equal hypothesis priors.
Equation (3) factorizes the output into the same body state under both
hypotheses and the control states

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad
|+_\phi\rangle=\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt2},
\qquad \phi=K_\tau/\hbar.\tag{6}
$$

A recombiner of phase $\alpha$ has exact port probabilities
$P_\pm(\alpha|\phi)=[1\pm\cos(\phi-\alpha)]/2$.
Scanning $\alpha$ reveals the fringe shift; its visibility remains one
for every $\phi$. The optimal distinction of the two hypotheses is

$$
D_n=\sqrt{1-\cos^{2n}(\phi/2)},\qquad
p_{\rm err}^{(n)}=\frac{1-D_n}{2}.\tag{7}
$$

*Proof.* For normalized vectors with overlap $c$, the difference of
their rank-one density operators has eigenvalues
$\pm\sqrt{1-|c|^2}$. For any equal-prior binary test $0\le M\le I$,
the success probability is
$[1+\operatorname{tr}M(\rho_1-\rho_0)]/2$; the positive eigenspace
attains the maximum. Here
$|\langle+|+_\phi\rangle|=|\cos(\phi/2)|$ and $n$ independent copies
raise the overlap to its $n$th power. This proves (7) including
attainability. $\square$

Thus (7) detects a history-dependent phase against a reference.
The uncontrolled body channels of $Q_\tau$ and $U_\tau$ coincide for
every $\rho$, giving error $1/2$ even with arbitrarily many copies.
The coherence resource in (6) is essential to exposing the scalar.

For the original unclosed free/falling pair, the final displacement and
impulse themselves supply a further signal. A pure body's overlap then
contains the expectation of a Weyl displacement in its prepared state,
so its magnitude depends on that preparation. For each $\tau>0$ one
can choose a wavefunction with position support narrower than the
nonzero interaction-picture displacement $F\tau^2/(2m)$; its translated
support is disjoint and the two outputs are orthogonal. Shrinking that
support costs increasing momentum spread. Thus the phase-only theorem
applies to the matched, coherently controlled record (6), with its
specified resources; an unrestricted detector of the raw endpoint
separation requires a separate preparation or disturbance budget.

Write $\delta=\operatorname{dist}(\phi,2\pi\mathbb Z)\in[0,\pi]$.
For a fixed positive integer $n$, (7) reaches error at most $\eta$ iff

$$
\delta\ge d_{n,\eta},\qquad
d_{n,\eta}=2\arccos\left([4\eta(1-\eta)]^{1/(2n)}\right).
\tag{8}
$$

On the first lobe $0\le K_\tau/\hbar\le\pi$, this is equivalent to

$$
K_\tau\ge\hbar d_{n,\eta},\qquad
\tau\ge\left(\frac{24m\hbar d_{n,\eta}}{F^2}\right)^{1/3},
\qquad A_{\rm inertial,fall}\ge\frac{4v\hbar}{F}d_{n,\eta}.
\tag{9}
$$

For $n=1$, $d_{1,\eta}=2\arcsin(1-2\eta)$, exactly the
[polygon-lift record bound, §4](cut-measure-newton.md#weyl-lifting-and-polygon-phases) (passage).
For $0<\eta<1/2$, $d_{n,\eta}\to0$ as $n\to\infty$; for $\eta=0$
it equals $\pi$ at every finite $n$. With $k$ coherent passes replace
$\phi$ by $k\phi$. These resource choices change the threshold.

The dependence on errors is explicit. If actual hypothesis states
$\widetilde\rho_i$ satisfy
$\tfrac12\|\widetilde\rho_i-\rho_i\|_1\le e_i$, the optimum error
changes by at most $(e_0+e_1)/2$, by the triangle inequality in (7).
A common phase calibration error $u$ on each of $n$ independent signal
copies gives distance at most
$\sqrt{1-\cos^{2n}(u/2)}\le\sqrt n\,|u|/2$, and hence changes the
optimal error by at most $\sqrt n\,|u|/4$ when the reference is exact.
An action uncertainty $|\delta S|$ contributes $|u|=|\delta S|/\hbar$.
These bounds state how accurately the control must be known to use (9).

## 4. The two orders of limits

Put $C=F^2/(24m)>0$, so $K_\tau=C\tau^3$.

**Theorem 3 (refinement, classical resolution and the missing prescription).**

(a) For the fixed coherent protocol (6), with fixed finite $n$,

$$
D_n\le\min\left(1,\frac{\sqrt n\,C\tau^3}{2\hbar}\right),
\qquad \lim_{\tau\downarrow0}p_{\rm err}^{(n)}=\frac12
\quad(\hbar>0).\tag{10}
$$

At every fixed $\tau>0$, $\lim_{\hbar\downarrow0}D_n$ fails to
exist: its liminf is zero and limsup is one. Consequently the coherent
classical-first iterated limit is undefined.

(b) Fix $b\in(0,1)$ and average the inverse phase parameter by replacing
$\phi$ with $u\phi$, uniformly over $u\in[1-b,1+b]$, forgetting $u$.
For this explicitly averaged two-arm state, its normalized coherence is

$$
\Gamma_b(\tau,\hbar)
=\frac1{2b}\int_{1-b}^{1+b}e^{iuK_\tau/\hbar}\,du
=e^{i\phi}\operatorname{sinc}(b\phi),\qquad
|\Gamma_b|\le\min\left(1,\frac{\hbar}{bK_\tau}\right).
\tag{11}
$$

With $\operatorname{sinc}(0)=1$, the iterated limits are

$$
\lim_{\hbar\downarrow0}\lim_{\tau\downarrow0}\Gamma_b=1,
\qquad
\lim_{\tau\downarrow0}\lim_{\hbar\downarrow0}\Gamma_b=0.
\tag{12}
$$

(Refinement after a Fable review, 2026-09-27.) The non-commuting limits
(12) depend on averaging over a *relative* window of the inverse
resolution. With an absolute window of half-width $w_0$ in $1/\hbar$ the
average is $e^{i\phi}\operatorname{sinc}(K_\tau w_0)$, independent of $\hbar$, and both
iterated limits equal one. Theorem 3(b) therefore states a property of
the relative-averaging prescription, which is the prescription (12)
uses.

For fixed weights and signature difference in (4), this prescription
leaves a diagonal-intensity error bounded by
$2a_0a_1\min(1,\hbar/(b|\Delta S|))$ in addition to the averaged
remainder bound of (4), with bound $2a_0a_1$ when $\Delta S=0$.
If the stationary-phase remainder obeys
$r\le C_\pi\hbar$ uniformly for small resolution, averaging uses
resolutions $\hbar/u$ and one may take
$r\le C_\pi\hbar/(1-b)$.

(c) Alternatively, assume a calibrated comparison can be attenuated to
any action $rK_\tau$, $0\le r\le1$, under both hypotheses, with no
additional relative phase. For example, use duration
$r^{1/3}\tau$ in (6), keeping $F,m$ fixed. Let $D_{\rm tun}$ be the
best single-copy distance over these choices. Then

$$
D_{\rm tun}(\tau,\hbar)
=\sin\left(\min\left\{\frac{K_\tau}{2\hbar},\frac\pi2\right\}\right),
\tag{13}
$$
$$
\lim_{\hbar\downarrow0}\lim_{\tau\downarrow0}D_{\rm tun}=0,
\qquad
\lim_{\tau\downarrow0}\lim_{\hbar\downarrow0}D_{\rm tun}=1.
\tag{14}
$$

*Proof.* The inequality
$1-(1-x)^n\le nx$ for $x\in[0,1]$, with
$x=\sin^2(\phi/2)$, proves (10).
For fixed $K_\tau>0$, the sequences
$\hbar_j=K_\tau/(2\pi j)$ and
$\hbar'_j=K_\tau/((2j+1)\pi)$ give respectively $D_n=0$ and
$D_n=1$. Integration gives (11); dominated continuity at $\phi=0$
and the displayed reciprocal bound at $\phi\to\infty$ prove (12).
In (c), maximize $|\sin(r\phi/2)|$ over $[0,1]$. The first maximum
is reached at $r=\pi/\phi$ when $\phi\ge\pi$; otherwise $r=1$
maximizes it. This proves (13)--(14). $\square$

Part (b) formalizes the loss of off-diagonal terms needed to recover
the two selected critical-point weights. Its averaged balanced state
approaches $I/2$ classically first, and $|+\rangle\langle+|$ when
refined first. The trace distance between these two limiting states is
$1/2$; dephasing by itself supplies no accessible which-path tag.
Part (c) instead supplies an actual discrimination experiment with
errors tending respectively to $1/2$ and zero. Its extra tunable control
is a physical hypothesis; changing the output recombiner alone would
leave (7) unchanged. A classical branch-selection prescription can
also retain distinct histories at every positive cell length, but their
paths converge together as that length vanishes. A limiting Dirac
measure alone expresses no retained record of the shrinking difference.

These conclusions sharpen the proposed classical-first statement.
For any fixed $b$ the condition $b|\Delta S|/\hbar\gg1$
controls the averaged cross term, with the explicit error in (11).
For coherent discrimination the exact condition is (8), with its
phase aliases. The two conditions express different measurements.
Along a joint limit the dimensionless ratio $C\tau^3/\hbar$
governs both: tending to zero erases the phase signal; a finite ratio
gives the corresponding signal, including the aliases in (8); a
diverging ratio requires the prescription
in (b) or (c) for a definite limit.

For a partition of fixed total duration $T$, the matched polygon action
is $K_\pi=C\sum_j\tau_j^3\le CT|\pi|^2$. Its coherent distance from
the exact curve is at most $\sqrt n\,CT|\pi|^2/(2\hbar)$.
After $k$ uniform halvings a cell's action falls by $8^{-k}$ and the
whole polygon defect by $4^{-k}$. Hence the whole fixed-duration
comparison converges as well. Resolving ever smaller cells can require
increasing resources: for a fixed small-error target the small-phase
independent-copy scaling is $n$ of order $(\hbar/K_\tau)^2$,
whereas coherent repetition uses $k$ of order $\hbar/K_\tau$.
Such budgets were held fixed in (10).

## 5. Relation to the disturbance and concentration floors

The [fifth-postulate note, Theorems C, E and §7](principia-fifth-postulate.md)
(passage) separates observable algebra, states and records. With
$\hbar=|\hbar|$, the three bounds here have the following scopes.

| Bound | Quantity constrained | Extra hypotheses beyond Newtonian geometry |
| --- | --- | --- |
| Phase record (9), one copy | $K_\tau\ge2|\hbar|\arcsin(1-2\eta)$ on the first lobe | Coherent controlled comparison, calibrated reunion, Born rule and one pass |
| Theorem C(b) | $(s/8)\sum_j\Delta D_j+(J/2)\sum_j\Delta X_j\ge|\hbar|\arcsin(1-2\eta)$ | Regular quantum joint states, unitary instrument, test valid for every initial body state; the theorem's interpolating-state suprema |
| Theorem E | $\lambda_0(ab/|\hbar|)\ge(1-2\eta)^2$ | Quantum state concentrated in both position and momentum windows with probability at least $1-\eta$ each |

Here $s=F\tau^2/(2m)$, $J=F\tau$, $a,b$ are window half-widths,
and $\lambda_0$ is the largest eigenvalue of the time-and-band-limiting
operator with the fifth-postulate note's convention. For Theorem E's
finite threshold take $0<\eta<1/2$; at $\eta=0$ simultaneous compact
concentration is impossible for finite $a,b$. A phase difference of
$\pi$ already gives perfect discrimination in (7).

The geometry relates $sJ=12K_\tau$. Converting Theorem C into a bound
on $K_\tau$ additionally needs bounds on the allowed disturbances
$\Delta D_j,\Delta X_j$ relative to $J,s$. Converting Theorem E needs
a physical identification of the concentration widths $a,b$ with
trajectory resolution. Choosing, for example, $a=\alpha s$ and
$b=\beta J$ would give
$K_\tau\ge|\hbar|c_*(\eta)/(12\alpha\beta)$, with
$c_*(\eta)=\lambda_0^{-1}((1-2\eta)^2)$ and the positive dimensionless
apertures $\alpha,\beta$ supplied. Geometry alone fixes neither choice.

The phase experiment has a two-dimensional record space. Its
Fubini--Study distance from the reference is $\delta/2$, and the
equal-prior error target requires that distance to be at least
$\arcsin(1-2\eta)$. This is the same statistical-angle step used in
Theorem C's disturbance proof. Theorem E uses the overlap norm of two
spectral projections in an infinite-dimensional canonical state space.
Its concentration function and error dependence carry different
information. Their common right-hand scale comes from the supplied
canonical phase constant; the equality of the scale alone establishes
no equivalence of the three experimental tasks.

There is a stronger exact bridge within the restricted Gaussian mark
model. The [polygon-lift note, Theorem 7](cut-measure-newton.md#weyl-lifting-and-polygon-phases)
(passage) uses the same functional
$\mathcal K_\tau[f]=(2m)^{-1}\iint G_\tau(s,u)f(s)f(u)\,ds\,du$
for the polygon phase and the optimal mark deflection. For constant
force, $\mathcal K_\tau=K_\tau$; with mark trade-off
$\kappa=|\hbar|/2$, its supremal squared deflection is
$d_{\rm mark}^2=2K_\tau/|\hbar|$.
That equality retains the Gaussian, uncorrelated error/recoil and
dense-protocol hypotheses. It leaves the general C and E bounds with
their own quantities and quantifiers.

Thus the two-path calculation gives the polygon theorem's existing
phase bound in the halved-functional representation, plus its explicit
limit prescriptions. It adds no independent exclusion of the common
zero branch allowed by
[round 2, §4](rotation-composition-universality.md) (passage).
Every $\hbar>0$ supports (3)--(14); their thresholds scale with
that freely supplied value. At zero, the exponential representation
is singular, while classical mechanics still supplies ordinary
trajectories and, with state completeness, sharp pointer records as in
Theorem C(c). A singular coordinate for that classical theory creates
no inconsistency in the theory itself.

## Two slits and a position detector

*Historical experimental application before the 18 November scope reset.*

Newton's 1713 Corollary 4 to Lemma X makes displacement a measure of
force. Here the mechanical calibration is the displacement produced by a
known transverse impulse $J$. Denote it by $BJ$. For free flight from a
mask to a detector over time $T$, $B=T/m$, where $m$ is the inertial mass.
Fix the ruler, screen pixel pitch $b$, flight-time gate $T_0\pm\Delta T$
with $T_0>\Delta T$, and a nonzero screen frequency $k$ in radians per
unit length. The gain can also be calibrated with a reference impulse
and a ruler in a focusing apparatus. A mass referred to a mechanical
standard gives action in absolute units. Free flight with just a ruler
and clock gives action per unit mass. [Newton's revision, passages from
1687 and 1713](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force).

**What to count.** Randomize the setting on fresh trials from one source.
Pass both beams,
only the left, or only the right. For each setting $s$ let
$z_s(k)=\int e^{ikx}\,d\mu_s(x)$, with $\mu_s$ the screen count measure
*per incident trial*. A loss contributes zero. A separately recorded
common background cancels in $C=z_{LR}-z_L-z_R+z_{\varnothing}$.
Both quadratures are sums over the same observed positions. Fix an
error allowance $e(k)$ such that $\delta=(|C_{\rm obs}|-e(k))_+$ is a
lower bound on the ideal $|C|$. It includes counting error, any change
in incident flux, unmatched transmission and unobserved screen tails.
An upper bound on a missed count probability bounds its whole Fourier
contribution. Rounding to pixels introduces at most $|k|b/2$ per counted
particle. A common translation-invariant detector blur multiplies $C$ by
a characteristic function of modulus at most one. Three histograms
normalized to their own transmitted counts discard the relative weights.
This statistic uses only the counted positions. Phase retrieval from
propagated intensities is established. For example, Teague uses
irradiance and perimeter phase data under the wave propagation equation
(abstract).
[Teague, 1983](https://doi.org/10.1364/JOSA.73.001434).

**What a positive excess measures.** At the plane of selection let $Q,P$
be transverse position and mechanical momentum. First take two intervals
with widths $w_L,w_R$, centre separation $D$, projections $\Pi_L,\Pi_R$
and $d_\pm=D\pm(w_L+w_R)/2$, with $d_->0$. The both-open state $\rho$
is supported on their union and has trace at most one. It can include
arbitrary unobserved degrees of freedom. Each single-open operation must
preserve its corresponding block $\Pi_j\rho\Pi_j$ to the accuracy charged
to $e(k)$. For classical trajectories this just means passing the same
particles with the same downstream response on the open side. Any such
classical source, including one with memory, gives $C=0$ by additivity.

For operator models suppose the common detector coordinate is
$X=AQ+BP+c$, with $A$ dimensionless and $c$ a length. Take the real
linear combinations self-adjoint on closure on a common invariant core
permitting unitary commutator differentiation, and let
$K=\|[Q,P]\|<\infty$. This class includes commuting motion. With
$E=e^{ikX}$ the only contributions to $C$ are the two off-diagonal
blocks. The separated-spectrum Sylvester estimate gives
$d_-\|\Pi_L E\Pi_R\|\le\|\Pi_L[Q,E]\Pi_R\|$, and likewise in reverse.
Unitary commutator differentiation gives $\|[Q,E]\|\le|kB|K$.
With $p_j=\operatorname{tr}(\rho\Pi_j)$ the trace norm of each coherence
block is at most $\sqrt{p_Lp_R}$ by Hilbert–Schmidt Cauchy–Schwarz.
Consequently a measured $\delta>0$ requires

$$
 K\ \ge\ \frac{d_-\,\delta}{2\sqrt{p_Lp_R}\,|k|B_{\max}},
 \qquad B_{\max}=\sup |B|.
$$

The same bound holds for a common mixture of flight times in the gate,
using Cauchy–Schwarz on the trial probabilities. A positive excess
requires both arms to transmit. Using $2\sqrt{p_Lp_R}\le1$ gives a
conservative bound without measuring the arm weights separately. It
rules out wholly commuting motion in the stated apparatus. A lower
bound on the norm leaves open commuting sectors of other preparations.
No scalar commutator or calibrated
relative phase enters. The ordered-interval estimate uses Theorem 9.2
with the compressed position operators shifted by the midpoint of the
gap (passage). [Bhatia and Rosenthal](https://repository.ias.ac.in/2521/1/2521.pdf#page=10).
For the unitary integral under the stated domain hypotheses see §3.1
(passage). [Iserles and Kropielnicka](https://arxiv.org/pdf/2401.06635#page=5).

In a regular Weyl representation with trial reduced action $a$,
$e^{ikX}$ translates position support by a signed distance of magnitude
$|akB|$. Modular translations as probes of separated wave packets are
established (passage, §II). [Tollaksen et al.](https://arxiv.org/pdf/0910.4227).
An off-diagonal block can survive only if a translated interval meets
the other. Thus for $B_{\min}=\inf|B|>0$ a positive excess requires

$$
 \frac{d_-}{|k|B_{\max}}\ \le\ |a|\ \le\
 \frac{d_+}{|k|B_{\min}} .
$$

Under the [action dilation](groupoid-quantum-newton-states.md#7-interacting-kernels-under-tangent-scaling)
$x=sX',\,t=rT'$, the slit widths, centres, offset $c$ and screen pitch
divide by $s$. The gate times divide by $r$, momenta and impulses
multiply by $r/s$, and $k'=sk$, $B'=B/r$, $a'=ra/s^2$ at fixed mass.
Both the prepared slit labels and $kx$ at detection
are invariant with these transformed settings. Holding the physical
ruler and clock fixed makes the band independent of mathematical mesh.

**Two positive scales can give identical records.** Even with the same
mass, slits, clock and pixels the band need not pick a unique $a$.
Take free flight at fixed $T$ inside the gate, $a>0$, $\beta=aT/m$,
slits of width $D/4$ about $\pm D/2$, and a normalized coherent wave
$\psi$ with a nonzero packet within $D/64$ of each centre and zero
elsewhere. Put
$s=21/20$, $\tilde a=sa$ and choose the other incident wave by

$$
 \tilde\psi(sq)=s^{-1/2}
       \exp\!\big[i(1-s)q^2/(2\beta)\big]\,\psi(q).
$$

Both supports stay inside their original slits. In the free Fresnel
kernel for $\tilde a$, substituting $q'=sq$ cancels the change in the
input quadratic phase and leaves the same Fourier integral in $x$.
The output acquires only the factor $\exp[i(1/s-1)x^2/(2\beta)]$.
This works for each slit separately, their coherent sum and the rejected
outcome. The full screen laws thus agree even before binning. The
preparations obey the same measured slit transmissions while differing
in their unresolved illumination within each slit. The only length in
the chosen input envelope can be taken proportional to $D$.

**A mask displaced from the slits.** One way to use three settings is
to put complementary edges at
the same coordinate $q_*$ in the *actual mask plane* and a both-open
run. For a distance $d>0$ measure the incident probabilities $p_-(d)$
in $[q_*-d,q_*)$ and $p_+(d)$ in $[q_*,q_*+d]$. A translation of the
same edge to $q_*-d,q_*,q_*+d$ measures these by differences of total
transmission with full collection and calibrated position resolution
(for a continuous beam the endpoint convention has no effect).
When $|akB|\le d$, translation in one direction allows only one of the
two off-diagonal blocks to contribute. Its initial and final points
both belong to these strips. Cauchy–Schwarz on that matrix element,
and on any common time mixture, gives the observable implication

$$
 \delta>\sqrt{p_-^{\,\rm upper}(d)\,p_+^{\,\rm upper}(d)}
 \quad\Longrightarrow\quad |a|>\frac{d}{|k|B_{\max}} .
$$

This control includes diffraction before the selector.

**What a full mask scan adds.** Translate one opaque screen with a clear
window of fixed width $W$. In the actual selector plane its ideal
transmission at setting $y$ is $M_y=\mathbf{1}_{[y,y+W]}(Q)$, acting
as the identity on transmitted amplitudes. Let $z_o$ denote the mask-out
harmonic and $z_y$ the transmitted harmonic, background subtracted and
on the same incident count scale. Hold $B\ne0$ fixed for the moment.
For a trial scalar action set $u=akB$. The two factors in $M_y E M_y$
test membership of positions a distance $|u|$ apart. The set of $y$
that pass both has length $(W-|u|)_+$, independent of either position.
Integrating the matrix element gives

$$
 \int_{\mathbb R} z_y(k)\,dy=(W-|akB|)_+ z_o(k).
$$

This uses the familiar aperture autocorrelation (passage, Hopkins on
the pupil function and frequency response). [Hopkins, 1955](https://janrik.net/Papers/Hopkins-TheFrequencyResponseOfADefocusedOpticalSystem-withNotes.pdf).
A stable common detector blur multiplies both sides by the same factor.
Under the dilation above $y'=y/s$, $W'=W/s$. Thus integration over
the physical mask settings scales by the same factor as $W$.
If $z_o\ne0$ and the observed ratio $\int z_y\,dy/(Wz_o)$ is a real
number $R$ strictly between zero and one, the sole compatible magnitude
is $W(1-R)/|kB|$. An imaginary part outside the errors tests the model
itself. Thus this scan can distinguish the explicit pair above on the
same screen. A positive classical ensemble with a passive mask and
any fixed downstream response contributes for exactly $W$ of mask
travel per trajectory. It gives $R=1$, including for rays with an
unobserved history. This prediction assumes free passage through the
clear window.

A classical shutter can also transmit with a random transverse impulse.
At fixed $B$ choose a classical incident ensemble giving the measured
mask-out position law, then add an independent kick $J$ on transmission.
After integration over $y$, every incoming ray has weight $W$. For the
mechanical momentum scale $j_0>0$ choose the density and its
characteristic function

$$
 g(J)=\frac{1}{2\pi j_0}\operatorname{sinc}^2\!
          \left(\frac{J}{2j_0}\right),\qquad
 \mathbb E e^{ivJ}=(1-j_0|v|)_+ .
$$

Here $\operatorname{sinc}x=\sin(x)/x$ with value one at zero. This is the
same rectangular-aperture Fourier pair. Setting $j_0=|a|/W$ gives the
scalar model's full averaged screen measure at every $k$, including after
common detector blur. In the classical model $j_0$ is an apparatus
impulse. The ideal density has long tails. For the specified single
harmonic and $0\le R\le1$, two equally likely finite kicks
$J=\pm\arccos(R)/|kB|$ give exactly the same ratio. Even the location
of the integrated diffraction cutoff can therefore be reproduced by
a force distribution. Keeping the individual mask positions supplies
further observations. Classical random kicks as an explanation of
certain which-way measurements have prior art (abstract).
[Wiseman and colleagues, 1996](https://opg.optica.org/abstract.cfm?uri=iqec-1996-TuL115).

With the original finite time gate one can still use
$D_{\rm scan}=|W z_o-\int z_y\,dy|$. For each common delay the loss
of the overlap length is at most $|ak|B_{\max}$ and the absolute
harmonic is at most the incident probability at the mask. Averaging
gives $D_{\rm scan}\le p|ak|B_{\max}$, where $p$ is the total mask-plane
probability per incident trial. For measured value $D_{\rm obs}$ and
total error $e_D$ in units of length, this gives
$|a|\ge(D_{\rm obs}-e_D)_+/(p|k|B_{\max})$ without resolving the
two slits. For a finite range $I$ choose $y$ uniformly
there and multiply the trial mean by $|I|$. With full transmission
counting, the missing integral has modulus at most
$Wp-\int_I p_y\,dy$, since every position is passed for $W$ of travel
and $|z_y|\le p_y$. Finite position accuracy of the selector can be
included by calibrating its actual translation distribution. These
operations survive arbitrary mathematical subdivision of $T$.

**How a mechanical disturbance could imitate the signal.** In free
classical flight an extra transverse impulse $J_j$ at the selector
changes the Fourier record of arm $j$ by at most
$p_j |k|B_{\max}\mathbb E_j|J_j|$, since
$|e^{iku}-1|\le |ku|$. Here $J_j$ is the change between shutter settings
on a transmitted trajectory. For a distributed force difference use
the endpoint displacement bound $m^{-1}\int_0^T(T-t)|\Delta F_j(t)|\,dt$
in place of $B_{\max}|J_j|$. These are independent mechanical controls
on a systematic error. In an operator realization a common additive
self-adjoint error $R$ in $X$ with $\|R\|\le r_x$ changes each
Fourier effect by at most $|k|r_x$ by the bounded-perturbation formula.

Newtonian recoil gives one way to measure such a displacement independently
of the electron pattern. For an isolated free shutter of mass $M$, let
$D_M$ be its final displacement relative to the continuation of its
incoming inertial line. Conservation of the transverse centre of mass
gives the particle's extra displacement as $-(M/m)D_M$, even for two
opposite forces whose net impulse vanishes. Ruler readings on the shutter
at $-T_c,0,T$ with absolute error $\rho_M$ bound the extrapolation
error by $2(1+T/T_c)\rho_M$. A force on the support or momentum carried
away by another body or field belongs in this balance. An independent
recoil bound needs the absolute displacement on transmitted trials,
including readout disturbance. A signed mean can vanish for the two
opposite kicks above.

The scan allows a force test even if scattering directly at an edge is
strong. Suppose independent controls localize unrestricted deflection
to strips of width $\eta$ on the *inside* of each window edge, certify
an opaque exterior, and bound extra displacement elsewhere in the
transmitted beam by $r_x$. For each classical ray at most $2\eta$ of
window travel lies in the strips. There the Fourier readout can change
by at most two. The resulting classical allowance in $D_{\rm scan}$ is
at most $p(4\eta+W|k|r_x)$ in units of length. Edge transmission and
deflection require their own calibration before using this allowance.

There is an explicit classical $a=0$ alternative if the shutter can change
that force freely. Fix classical incoming momentum zero and a continuous
incoming position law on each slit with the measured slit weights. In
each transmitted arm let $u(q)$ be its conditional cumulative
probability, uniform on $[0,1]$. For shutter setting $s$ let $H_s$ be
the target cumulative distribution of the detected coordinate, conditional
on transmission. Apply the transverse impulse
$J_s(q)=[H_s^{-1}(u(q))-Aq-c]/B$. The same downstream flight now gives
the prescribed $H_s$ for every setting and leaves the position at the
selector unchanged. For a finite screen and $B\ne0$ the impulses are
bounded. With additive transmitted weights this reproduces all three
count measures, including a fringe pattern. Finite forces suffice even
with the same flight time. In free flight keep the incident ray label
$q$, exert the constant force $m[H_s^{-1}(u(q))-q]/[h(T-h/2)]$ for any
chosen duration $0<h<T$, then let the particle coast. Its endpoint is
exactly $H_s^{-1}(u(q))$. Newton's finite-force hypothesis alone permits
this change of apparatus. The same force works under arbitrarily fine
subdivision of the flight. Additional observations during the pulse, or
an independent bound on its deflection, can distinguish it.

**Can measuring both bodies remove the recoil alternative?** Let the
shutter move freely, with transverse position $Y$ and momentum $P_M$.
An offset $y$ within it selects the *relative* position $S=Q-Y$.
For fixed $T$ after the selection, read both endpoints
$X_e=Q+TP/m$ and $X_M=Y+TP_M/M$. Their joint harmonic has independent
screen frequencies $k_e,k_M$. In regular commuting constituent Weyl
algebras with trial actions $a_e,a_M$, its unitary translates the
support of $S$ by a distance of magnitude
$T|a_e k_e/m-a_M k_M/M|$. The same window overlap therefore gives

$$
 \frac1W\int_{\mathbb R}z_y(k_e,k_M)\,dy
 =\left(1-\frac{T}{W}
    \left|\frac{a_e k_e}{m}-\frac{a_M k_M}{M}\right|\right)_+
    z_o(k_e,k_M).
$$

For a common action $a$, the classical construction above now gives
the two bodies *opposite* impulses $(J,-J)$ with $j_0=|a|/W$. The
joint harmonic acquires the same factor for every $(k_e,k_M)$. A
classical incident ensemble can have any prescribed mask-plane position
marginal and any prescribed mask-out endpoint pair at this fixed time:
draw those two pairs and set each incoming momentum to its mass times
its sampled displacement divided by $T$. Thus both endpoint records
and any common subsequent binning agree for the full averaged scan.
Total transverse momentum is conserved in the classical construction.

An explicit pair uses the same source at *every* time in the clock gate.
Prepare independent centred Gaussian position and momentum marginals for
each body $i=e,M$, with zero cross covariances and independently fixed
rms widths $\ell_i$ and $\pi_i=m_i\sigma_{v,i}$. Set
$a_*=\min_i\ell_i\pi_i>0$. The product Gaussian is an admitted Wigner
state at $a_*$ since $\ell_i\pi_i\ge a_*/2$. Its free-flight marginals
equal those of classical Gaussian particles with those widths
(Gaussian characterization and linear canonical propagation, abstracts).
[Simon, Sudarshan and Mukunda](https://doi.org/10.1016/0375-9601(87)90625-6)
and [their Gaussian propagation paper](https://doi.org/10.1103/PhysRevA.36.3868).
Use the passive window at $a_e=a_M=a_*$ and the window with opposite
kicks of scale $a_*/W$ at $a_e=a_M=0$. Their averaged joint position
laws agree at each delay, hence with any common finite clock resolution.
This preparation specifies lengths, velocity widths, masses, window,
pixel pitches and clock gate. The positive trial scale is constructed
from those inputs. It is independent of a value for physical $\hbar$.

A finite version uses just three mask offsets and three bounded kicks.
Give the mask real amplitude transmission
$t(S-y)=[1+\cos(2\pi(S-y)/\Lambda)]/2$ with ruler-calibrated pitch
$\Lambda$. Choose $y=0,\Lambda/3,2\Lambda/3$ equally often. Retain
transmission, clock and both positions and average over the offset.
The three spatial Fourier coefficients of $t$ are $1/4,1/2,1/4$ for
orders $-1,0,1$. Averaging the three offsets cancels every product of
distinct orders. The pass probability is $3/8$. Conditional on passing,
the two-body output at $a_*$ is a mixture of opposite momentum shifts.
In the classical model use the same incident Gaussian law and the
measured acceptance $t(S-y)^2$. On transmission apply opposite kicks
$(J,-J)$ drawn independently from

$$
 \Pr(J=0)=\tfrac23,\qquad
 \Pr(J=+2\pi a_*/\Lambda)=\Pr(J=-2\pi a_*/\Lambda)=\tfrac16 .
$$

The averaged acceptance for *each* incoming relative position is $3/8$,
so the admitted classical Gaussian ensemble has the original weights.
This gives exactly the same rejection probability and joint endpoint
law at each delay in the gate with finite mask travel. Equal translation
errors with the same distribution at the three offsets still cancel the
cross terms. The mechanical parameter to check independently at this
finite grating is the impulse $2\pi a_*/\Lambda$.

**Retaining the offset separates this explicit pair.** Take
$\ell_e=\ell_M=\Lambda$ and $\pi_e=\pi_M=\pi_0$. Set
$\kappa=2\pi/\Lambda$, $\mu=mM/(m+M)$ and choose the clock centre
$T_0=\mu\Lambda/(a_*\kappa)$ using the specified preparation widths.
At offset zero count $\cos(\kappa(X_e-X_M))$ per incident particle.
Write $L^2=\ell_e^2+\ell_M^2$ and
$\sigma_V^2=\sigma_{v,e}^2+\sigma_{v,M}^2$.
At $T_0$ the relative Weyl translation spans one pitch. The centred
positions in the two mask factors differ by one pitch, so each is a
half-pitch from the midpoint. Their product changes the sign of the
first Fourier order of $t^2$. Every classical kick in the displayed
pair contributes phase one. The Gaussian characteristic function gives
the signed difference of the two predicted counts

$$
 z_{\rm quantum}-z_{\rm classical}
 =-\tfrac12 e^{-(\kappa T_0\sigma_V)^2/2}
             (1+e^{-2\kappa^2L^2}) .
$$

The difference stays observable with independently fixed resolutions.
For $s=T/T_0\in[0.95,1.05]$ the first and second cosine coefficients
of the mask-product difference are
$(\cos(\pi s)-c_s)/2$ and $(1-c_s)/8$, where
$c_s=(2+\cos(2\pi s))/3$. The constant coefficient cancels. The Gaussian
position averages of these cosines against the readout are at least
$1/2$ for the first and between zero and one for the second. Since
$\cos(\pi s)<-3/4$, $c_s>5/6$ and $\kappa T_0\sigma_V\le1$, the
negative difference has magnitude greater than $3/16$ throughout the
gate. Pixel pitches $b_e,b_M$ and an offset error $|\Delta y|$ change
the difference by at most $\kappa(b_e+b_M+2|\Delta y|)$, using
$|t'|\le\kappa/2$. Taking each at most $\Lambda/256$ leaves a gap
greater than $1/16$ per incident trial before counting error. The
prediction compares the two specified instruments. A force law allowed
to vary with the setting still needs independent control.

The long tails of $g$ are dispensable for any fixed finite detector.
For $n$ exhaustive joint pixel and clock outcomes, including overflow, let
$v(J)$ be the vector of their probabilities at fixed kick. Its
components are measurable, bounded and sum to one. Positive cubature
for these $n$ functions gives at most $n$ finite kicks and positive
weights reproducing $\int v(J)g(J)\,dJ$ exactly. The weights sum to
one because the pixels exhaust the outcomes (Corollary 2, passage).
[Bayer and Teichmann](https://www.wias-berlin.de/people/bayerc/files/tchakaloff.pdf).
For a fixed $h$ shorter than the earliest flight time, the opposite
forces $\pm(J/h)(4-6t/h)$ on $0<t<h$ deliver exactly $\pm J$.
Their first time moments vanish, so at every $T>h$ the endpoint shifts
are exactly $TJ/m$ and $-TJ/M$. The force remains finite under any
mathematical refinement of the pulse.
A *prescribed* independent ceiling $J_{\max}$ is a different condition.
Truncating $g$ at this ceiling and renormalizing changes any pixel-event
probability by at most the removed probability, bounded by
$4j_0/(\pi J_{\max})$ using the displayed density. Distinguishing the
alternatives requires a sufficiently small measured ceiling.

In particular $Z=X_e+(M/m)X_M$ cancels the displacement due to *every*
internal Newtonian impulse. Setting $k_M=(M/m)k_e$ shows that this
readout tests only $a_e-a_M$. At equal actions $S$ and $Z$ strongly
commute. Their joint spectral measure is a positive classical joint
law that reproduces every individual slit setting and every $Z$ bin,
even without averaging. This uses the established commutation of
relative position with total momentum (EPR, §2, passage) and the
corresponding unequal-scale formula in the composition argument
(passage). A measured incoming inertial line of the shutter, or
separate endpoints *conditioned on the mask setting*, supplies
information lost in these two readouts.
[Einstein, Podolsky and Rosen, 1935](https://doi.org/10.1103/PhysRev.47.777)
and [centre and relative variables](rotation-composition-universality.md#relation-to-fluctuation-composition-and-dimensional-selection).

**What was independently measured.** Bach et al. measured both slits
by electron microscopy. Their Table S1 gives width $64.6$ nm and
separation $282.7$ nm, hence nominal $d_-=218.1$ nm and $d_+=347.3$ nm.
A $5\,\mu{\rm m}$ detection slit sampled the unmagnified pattern at
$L=240\pm5$ mm. Displacing it calibrated the deflection-plate scan.
The fitted modulation period was about $44\,\mu{\rm m}$. The fit
uses $\pi d_{\rm fit}/(\lambda L)$, so $\lambda L/d_{\rm fit}$ recovers
the period on this calibrated screen. Taking their diffraction-fitted
slit spacing as a second independent length would reuse their assumed
de Broglie wavelength. [Bach et al., supplement, Fig. S2 and Table S1](https://www.tezu.ernet.in/rctp2015/2%20supp_double_slit.pdf) (passages).

The nominal 600 eV flight gives $T\simeq16.5$ ns in the nonrelativistic
approximation, from $T=L/\sqrt{2E_z/m}$. A flight-time gate or an
accelerating voltage and independently calibrated charge-to-mass ratio
are needed to establish this gain. At the quoted period, a differential
signal from selectors *in the slit plane* would place $|a|/m$ nominally
between $9.3\times10^{-5}$ and $1.5\times10^{-4}\ {\rm m^2/s}$.
These numbers describe the scale of the proposed test. The fitted
visibility $0.819\pm0.032$ is from one pattern. The authors report
limited scan range, possible beam-current drift, and a selection mask
$240\,\mu{\rm m}$ from the slits. They see weak two-slit diffraction
even at a nominal single-open setting. Their visibility and slit
dimensions therefore do not supply $\delta$ and the two strip probabilities
in the same plane. Table S1 gives the movable window's SEM width as
$4.680\,\mu{\rm m}$. A translation $|akB|=0.283\,\mu{\rm m}$ would
reduce its integrated harmonic by about six percent. The published
mask scan uses a saturating intensity display. The supplement includes
an image-charge potential at the mask in its wave simulation. Neither
the displayed contrast nor that simulation bounds the classical
shutter-dependent displacement in the scan statistic.
[Bach et al., §3 and Fig. 2](https://doi.org/10.1088/1367-2630/15/3/033018)
and [supplement, Fig. S2, Tables S1–S2](https://www.tezu.ernet.in/rctp2015/2%20supp_double_slit.pdf) (passages).

Tavabi et al. placed a wire in a plane conjugate to the slits and
recorded focused slit images before and after diffraction exposures to
check drift. Their Fig. 4 shows progressive covering of the *right*
slit and Fig. 5 gives intensity scans in arbitrary units. This
demonstrates the practical near-plane control. The published comparison
does not give both complementary count weights, strip bounds and a
bound on shutter-dependent deflection for one common ensemble.
[Tavabi et al., Figs. 3–5](https://doi.org/10.1038/s41598-019-43323-2)
(passages).

## 6. Consequence for STATE

Item 2 gains an exact two-path error law on the Galileo cubic action,
with the endpoint conversion, phase aliases, resources and limiting
prescriptions explicit. Fixed-resolution refinement erases this phase
record; classical-first averaging or calibrated attenuation gives the
precise contrasting limits. The result locates a conditional record
threshold at $K_\tau=\tau\Delta E/12$ for the matched polygon protocol,
and at the corresponding calibrated action for a literal inertial
reunion. Position counts after complementary apertures offer a different
test. Three settings admit an explicit pair of positive action scales.
The integrated movable-window harmonic distinguishes their magnitudes
under calibrated passive transmission. Its outstanding physical input
is an observed deviation from the classical sum larger than independently
bounded shutter and detector effects. Opposite classical impulses reproduce
the averaged electron and shutter positions jointly. The record that
cancels internal force exactly also cancels a common quantum action.
The necessity of such a common scale remains open.
