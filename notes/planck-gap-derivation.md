# The Planck gap as a theorem: every marking protocol needs $F^2\tau^3>9m\kappa$

Let $\kappa$ be the smallest product of resolution and recoil width over
the marks a record model can make. Then for **every** finite protocol of
marks, of any number, at any times, the falling parabola can be told from
the inertial line over a duration $\tau$ in the worst case only if

$$\boxed{F^2\tau^3>9\,m\kappa,\qquad\text{equivalently}\qquad
\tau\Delta E=\frac{F^2\tau^3}{2m}>\frac92\,\kappa,\qquad
A_{\rm inertial,fall}=\frac{vF\tau^3}{6m}>\frac{3v\kappa}{F},}$$

and a two-mark protocol decides as soon as $F^2\tau^3>36m\kappa$ when
marks saturating $\kappa$ are available (Theorems 1--2). The threshold
duration is therefore pinned within a factor $4^{1/3}$ by $\kappa$ alone,
and the Planck gap of the recorded Galileo comparison is positive exactly
when $\kappa>0$ (Corollary 3). The same bound governs Democritus insertion:
the marks inside a window of duration $\tau'$, used by themselves, record
the force only if $F^2\tau'^3>9m\kappa$ (Corollary 4). Any record model in
which a probe's later position records fix its momentum to arbitrary
accuracy has $\kappa=0$ (Proposition 5); quantum kinematics has
$\kappa\ge2\hbar=h/\pi$ by the Busch--Lahti--Werner error--disturbance
theorem (Proposition 6), so the quantum Galileo comparison needs
$\tau\Delta E>9\hbar$; Newton's optics gives the heuristic value
$\kappa=\Lambda p=h/2$ of the [mark-floor note](newton-mark-floor.md).
The proof is a separation argument for the adversary's feasibility set,
an AM--GM step that turns $\delta\Delta\ge\kappa$ into a square root, and
one integration by parts that converts the certificate into a Dirichlet
energy. Constants are explicit throughout; nothing is fitted.

## 1. Setting and definitions

Transverse coordinate $y$, mass $m>0$, comparison on $[0,\tau]$ between the
inertial hypothesis $\mathrm I$ and the falling hypothesis $\mathrm F$,
which differ by the displacement

$$P(t)=\frac{Ft^2}{2m},\qquad P(0)=P'(0)=0,\qquad P''=\frac Fm .$$

A **mark** at time $t_j$ has a **resolution** $\delta_j>0$: the datum it
leaves is an interval of length $\delta_j$ containing $y(t_j)$; and a
**recoil width** $\Delta_j\ge0$: the transverse impulse it delivers to the
body lies, under either hypothesis, in an interval of length $\Delta_j$
that is fixed by the totality of records, so that two runs which agree in
every record can differ in that impulse by at most $\Delta_j$. Between
marks the body moves freely under $\mathrm I$ and with the force $F$ under
$\mathrm F$. A **protocol** is a finite set of marks at times
$0=t_0<t_1<\dots<t_k\le\tau$; the mark at $t_0=0$ is the preparation, whose
recoil width $\Delta_0$ is the width within which the records fix the
initial transverse momentum. A protocol **decides** the comparison in the
worst case when no pair of runs, one under $\mathrm I$ and one under
$\mathrm F$, with initial positions, initial momenta and recoils allowed
by the marks, produces the same data. Set

$$\kappa=\inf_j\delta_j\Delta_j$$

over the marks the model can make; a model satisfies the **mark
trade-off** with constant $\kappa$ when every available mark has
$\delta\Delta\ge\kappa$. For the corpuscular model of the mark-floor note
this is premise M3 with $\kappa=\Lambda p$.

**Feasibility system.** Write $y_{\rm F}-y_{\rm I}=P+d$. Then
$d(t)=x+vt+\sum_{j\ge1}\rho_j(t-t_j)_+/m$ with $x\in\mathbb R$ free (both
initial positions lie in the same datum interval, so their difference is
bounded only by the datum constraint at $t_0$), $|v|\le\Delta_0/m$ and
$|\rho_j|\le\Delta_j$. Two runs give the same data exactly when

$$|d(t_i)+P(t_i)|\le\delta_i\qquad(i=0,1,\dots,k). \tag{1}$$

The protocol decides if and only if (1) has no solution
$(x,v,\rho_1,\dots,\rho_{k-1})$ in the stated ranges. (The last mark's
recoil affects nothing that is recorded and is omitted.)

## 2. Certificate of decidability

**Lemma 1 (separation).** The protocol decides if and only if there are
multipliers $\mu_0,\dots,\mu_k\in\mathbb R$ with $\sum_i\mu_i=0$ and

$$\sum_i\mu_iP(t_i)>\sum_i|\mu_i|\delta_i+\frac{\Delta_0}{m}|S_0|
+\sum_{j\ge1}\frac{\Delta_j}{m}|S_j|,\qquad
S_j=\sum_{i>j}\mu_i(t_i-t_j). \tag{2}$$

*Proof.* Let $L:(x,v,\rho)\mapsto(d(t_i))_i\in\mathbb R^{k+1}$ be the linear
map of Section 1 and $B$ the box $|v|\le\Delta_0/m$, $|\rho_j|\le\Delta_j$.
The system (1) is feasible exactly when the closed convex set
$C=\{L(x,v,\rho):x\in\mathbb R,(v,\rho)\in B\}$ meets the compact box
$Q=\{q:|q_i+P(t_i)|\le\delta_i\}$. $C$ is the sum of a line and a compact
convex set, hence closed and convex. If $C\cap Q=\emptyset$, the separation
theorem for a closed and a compact convex set gives $\mu$ with
$\sup_{q\in Q}\mu\cdot q<\inf_{c\in C}\mu\cdot c$. Since $x$ is free the
infimum is $-\infty$ unless $\mu\cdot L(1,0,0)=\sum_i\mu_i=0$; with that,
$\inf_C\mu\cdot c=-\frac{\Delta_0}m|\sum_i\mu_it_i|-\sum_{j\ge1}\frac{\Delta_j}m|\sum_{i>j}\mu_i(t_i-t_j)|$
by choosing the signs of $v$ and $\rho_j$, and
$\sup_Q\mu\cdot q=-\sum_i\mu_iP(t_i)+\sum_i|\mu_i|\delta_i$. The strict
inequality between them is (2); if the separation comes with the
opposite orientation, replace $\mu$ by $-\mu$. Note $\sum_i\mu_it_i=S_0$
when $\sum_i\mu_i=0$.
Conversely, if (2) holds and $(x,v,\rho)$ solved (1), pairing (1) with
$\mu$ would give $\sum_i\mu_iP(t_i)\le\sum_i|\mu_i|\delta_i-\sum_i\mu_id(t_i)
\le\sum_i|\mu_i|\delta_i+\frac{\Delta_0}m|S_0|+\sum_{j\ge1}\frac{\Delta_j}m|S_j|$,
contradicting (2). $\square$

**Lemma 2 (trade-off to a square root).** If $\delta_j\Delta_j\ge\kappa$
for all $j$, then the right side of (2) is at least
$2\sqrt{\kappa/m}\,\sum_{j=0}^k\sqrt{|\mu_j||S_j|}$.

*Proof.* For each $j$, $|\mu_j|\delta_j+\frac{\Delta_j}m|S_j|
\ge2\sqrt{|\mu_j||S_j|\delta_j\Delta_j/m}\ge2\sqrt{\kappa|\mu_j||S_j|/m}$
by the arithmetic--geometric mean inequality; $S_k=0$. $\square$

## 3. The universal lower bound

**Lemma 3 (the certificate as a Dirichlet energy).** Let $\sum_i\mu_i=0$,
$N(u)=\sum_{i:\,t_i>u}\mu_i$ and $T(u)=\int_u^\tau N(w)\,dw$ for $u\in\mathbb R$.
Then $T$ is continuous and piecewise linear, $T\equiv T(0)$ on $(-\infty,0]$,
$T\equiv0$ on $[\tau,\infty)$, $T(t_j)=S_j$, the slope of $T$ jumps by
$\mu_j$ at $t_j$, and

$$\sum_i\mu_iP(t_i)=\frac Fm\int_0^\tau T(u)\,du,\qquad
\sum_j\mu_jT(t_j)=-\int_0^\tau T'(u)^2\,du. \tag{3}$$

*Proof.* $N$ is piecewise constant, vanishes for $u<0$ because
$\sum_i\mu_i=0$ and for $u\ge t_k$, and drops by $\mu_j$ as $u$ crosses
$t_j$; so $T'=-N$ has the stated jumps and support. Also
$T(t_j)=\sum_i\mu_i\,|\{u\in[t_j,\tau]:u<t_i\}|=\sum_{i>j}\mu_i(t_i-t_j)=S_j$.
For the first identity, $P(t_i)=\int_0^{t_i}P'(u)\,du$ and Fubini give
$\sum_i\mu_iP(t_i)=\int_0^\tau P'(u)N(u)\,du=-\int_0^\tau P'T'\,du
=-[P'T]_0^\tau+\int_0^\tau P''T\,du=\frac Fm\int_0^\tau T\,du$, using
$T(\tau)=0$ and $P'(0)=0$. For the second, $T'$ is of bounded variation
with jumps $\mu_j$ at $t_j$ and no other variation, so
$\sum_j\mu_jT(t_j)=\int_{\mathbb R}T\,dT'=[TT']_{-\infty}^{\infty}-\int T'^2
=-\int_0^\tau T'^2$, as $T'$ vanishes outside $[0,\tau]$. $\square$

**Theorem 1 (universal lower bound).** Suppose every mark of a protocol
satisfies $\delta_j\Delta_j\ge\kappa$. If the protocol decides the
Galileo comparison on $[0,\tau]$ in the worst case, then

$$F^2\tau^3>9\,m\kappa .$$

*Proof.* By Lemma 1 there is $\mu$ with $\sum_i\mu_i=0$ satisfying (2), and
by Lemma 2 and (3)

$$\frac Fm\int_0^\tau T\,du>2\sqrt{\frac\kappa m}\sum_j\sqrt{|\mu_j||S_j|}
\ge2\sqrt{\frac\kappa m}\sqrt{\sum_j|\mu_j||S_j|}
\ge2\sqrt{\frac\kappa m}\sqrt{E},\qquad E=\int_0^\tau T'^2\,du,$$

using $\sum_j\sqrt{a_j}\ge\sqrt{\sum_ja_j}$ for $a_j\ge0$ and
$\sum_j|\mu_j||S_j|\ge|\sum_j\mu_jT(t_j)|=E$. The right side is
nonnegative, so $\int_0^\tau T>0$. Since $T(\tau)=0$,
$|T(u)|=|\int_u^\tau T'|\le\sqrt{\tau-u}\sqrt E$ by Cauchy--Schwarz, hence
$\int_0^\tau T\le\int_0^\tau\sqrt{\tau-u}\,du\,\sqrt E=\tfrac23\tau^{3/2}\sqrt E$,
that is $\sqrt E\ge\tfrac32\tau^{-3/2}\int_0^\tau T$. Inserting,
$\frac Fm\int_0^\tau T>3\sqrt{\kappa/m}\,\tau^{-3/2}\int_0^\tau T$, and
dividing by the positive integral, $F\tau^{3/2}>3\sqrt{\kappa m}$. $\square$

The theorem uses nothing about the marks except the product bound: no
least length, no least impulse separately, no restriction on how many
marks are made or when, no assumption that the marks are of one kind, and
no probabilistic model. In the mark-floor note's two-mark protocol the
same inequality appeared with the constant $16$; Theorem 1 says that no
protocol whatever can push the constant below $9$.

## 4. The matching upper bound and the gap

**Theorem 2 (two marks suffice).** Suppose the model offers, for the
duration $\tau$ in question, a preparation mark with
$\delta_0=\sqrt{\kappa\tau/m}$ and $\Delta_0=\kappa/\delta_0$, and a
terminal mark with $\delta_1\le\sqrt{\kappa\tau/m}$. Then the two-mark
protocol decides the comparison whenever $F^2\tau^3>36\,m\kappa$.

*Proof.* Under $\mathrm I$ the terminal position lies in an interval of
length $w=\delta_0+\Delta_0\tau/m=2\sqrt{\kappa\tau/m}$; under $\mathrm F$
in its translate by $s(\tau)=F\tau^2/2m$. A datum of length $\delta_1$
cannot meet both when $s(\tau)>w+\delta_1$, which holds if
$F\tau^2/2m>3\sqrt{\kappa\tau/m}$, that is $F^2\tau^3>36m\kappa$.
$\square$

**Corollary 3 (the Planck gap of the recorded comparison).** Let
$\tau_*(F,m)$ be the infimum of durations over which some available
protocol decides the comparison. Under the hypotheses of Theorems 1--2,

$$9\,m\kappa\le F^2\tau_*^3\le36\,m\kappa,\qquad
\frac92\kappa\le\tau_*\Delta E(\tau_*)\le18\kappa,\qquad
\frac{3v\kappa}{F}\le A(\tau_*)\le\frac{12v\kappa}{F},$$

the lower bounds from Theorem 1 as infima and the upper bounds from
Theorem 2.

In particular the recorded comparison has a positive floor if and only if
$\kappa>0$, and the floor is a fixed multiple of $\kappa$, between
$\tfrac92$ and $18$ in the action-scaled variable $\tau\Delta E$. The
geometric area inherits the factor $v/F$ and has no floor of its own,
which is the [Q14](action-unit-dimensional-selection.md) gate: the only
action the record model contains is $\kappa$.

**Corollary 4 (Democritus insertion).** Let marks be inserted at
$t_a=t_{j}<t_{j+1}<\dots<t_{j+r}=t_b$ inside $[0,\tau]$, and let the
observer use these marks alone to decide whether the motion on $[t_a,t_b]$
was free or forced, with no information about the momentum at $t_a$
beyond what these marks give. Then the window records the force only if
$F^2(t_b-t_a)^3>9m\kappa$.

*Proof.* Shift the origin to $t_a$. With the momentum at $t_a$ unknown, $v$
is free as well as $x$, so the certificate of Lemma 1 acquires the extra
condition $S_0=\sum_i\mu_it_i=0$ and loses the term $\frac{\Delta_0}m|S_0|$,
which was zero under that condition anyway. Lemmas 2--3 and the proof of
Theorem 1 go through unchanged with $\tau$ replaced by $t_b-t_a$.
$\square$

So inserted points finer than $\tau_*=(9m\kappa/F^2)^{1/3}$ show, by
themselves, free motion only; the force reappears when enough of them are
pooled that the pooled window exceeds $\tau_*$, and it also reappears if
momentum information from before the window is carried in, in which case
the comparison is the whole-interval one and Theorem 1 applies to it.
This is the rigorous form of the mark-floor note's Theorem 2, and of
I003's remark 3: $\kappa$ controls the mesh at which the marked polygon
stops converging to Newton's curve.

## 5. What fixes $\kappa$

**Proposition 5 (deterministic probes give $\kappa=0$).** Suppose the
marks are made by probes that travel freely after the mark, that a probe's
transverse momentum after the mark equals its momentum before minus the
impulse delivered, and that a probe's position can be recorded at any
distance $D$ with a resolution $\delta_s$ bounded independently of $D$.
Then for every mark $\Delta\le p_\parallel(\delta+\delta_s)/D$ for all $D$,
where $p_\parallel$ is the probe's longitudinal momentum, so $\Delta=0$ and
$\kappa=0$.

*Proof.* The probe's transverse momentum after the mark is
$p_\parallel$ times the tangent of its direction, which the two recorded
positions fix to within $(\delta+\delta_s)/D$; momentum conservation
transfers the same width to the delivered impulse; let $D\to\infty$.
$\square$

This is the far-screen countermodel of the mark-floor note stated for any
deterministic probe, and it is the mechanism behind the classical closures
C068--C123 ([synthesis](action-scale-obstructions.md)): full-state records
fix the recoil, the trade-off constant is zero, and Corollary 3 gives floor
zero. A positive $\kappa$ therefore requires that the probe's later
position records **do not** fix its momentum, which is an indeterminacy of
the probe's own kinematics.

**Proposition 6 (quantum marks have $\kappa\ge2\hbar$).** Model a mark as
an instrument on the body's Hilbert space $L^2(\mathbb R)$ with a real
output, and define its resolution and recoil width in the worst-case
sense: for every input state whose position distribution is supported in
an interval of length $\ell$ centred at $x$, the output is supported in an
interval of length $\ell+\delta$ centred at $x$; and for every input state
whose momentum distribution is supported in an interval of length $\ell$,
the post-mark momentum distribution, shifted by the mark's nominal impulse,
is supported in an interval of length $\ell+\Delta$. Then $\delta\Delta\ge2\hbar$.

*Proof.* The calibration error of the output as an approximate position
measurement, in the sense of Busch, Lahti and Werner (the supremum over
sharply localized inputs of the Wasserstein-2 distance between output and
input position distributions, [PRL 111, 160405 (2013)](https://doi.org/10.1103/PhysRevLett.111.160405)
and [J. Math. Phys. 55, 042111 (2014)](https://doi.org/10.1063/1.4871444),
abstract and theorem statements), is at most $\delta/2$: a distribution
supported within $\delta/2+\ell/2$ of the input's support has Wasserstein
distance at most that from it, and $\ell\to0$. Likewise the calibration
disturbance of momentum is at most $\Delta/2$, since a momentum measurement
after the mark, corrected by the nominal impulse, is an approximate
momentum measurement whose output lies within $\Delta/2+\ell/2$ of the
input momentum support. Busch--Lahti--Werner prove that the product of the
position error and the momentum disturbance of any instrument is at least
$\hbar/2$. Hence $(\delta/2)(\Delta/2)\ge\hbar/2$. $\square$

With Corollary 3 this gives the quantum Galileo comparison the rigorous
floor

$$\tau_*\Delta E(\tau_*)\ge\frac92\cdot2\hbar=9\hbar\approx1.43\,h,$$

while the N01 closed-loop benchmark, an interferometric protocol outside
the class of marks considered here, needs $\tfrac43\tau\Delta E\ge\pi\hbar$
for perfect discrimination, $\tau\Delta E\ge3h/8$. The two numbers bracket
the same combination; the present one is a theorem for all mark
protocols under the stated worst-case definitions, the other an exact
optimum for one protocol and a probabilistic criterion.

**The Newton-age value.** The corpuscular premises M1--M3 of the
mark-floor note give $\kappa=\Lambda p$, with $\Lambda=1/89000$ inch
measured by Newton and $p$ unmeasured in his age; on the identification
$p=h/\lambda$, $\Lambda=\lambda/2$ this is $\kappa=h/2$, within a factor
$\pi/2$ of the proved quantum value $h/\pi$. Newton-age materials give
Corollary 3 in full, once M3 is granted; Proposition 5 shows that
Newton's own determinate fits deny M3 and give $\kappa=0$; Proposition 6
shows that quantum kinematics grants it with an explicit constant. The
logical structure of the Planck gap is therefore:

$$\text{Planck gap of the recorded Galileo comparison}\;>0
\quad\Longleftrightarrow\quad\kappa>0
\quad\Longleftarrow\quad\text{indeterminate probe kinematics},$$

with the first equivalence proved here for all finite mark protocols and
explicit constants, and the second implication supplied by the quantum
error--disturbance theorem. No step assumes a path-integral phase rule,
a fixed measurement budget, or a supplied action unit other than $\kappa$
itself; and $\kappa$ is not supplied but characterized: it is zero for
every deterministic probe with far-field position records and at least
$2\hbar$ for every quantum instrument.

## 6. Consequence for STATE

The Planck gap is now a theorem with a converse: Theorem 1 and Theorem 2
sandwich the threshold of the recorded Galileo comparison between
$9m\kappa$ and $36m\kappa$ in $F^2\tau^3$ for every finite protocol of
marks, Corollary 4 does the same for Democritus insertion, Proposition 5
shows $\kappa=0$ for every deterministic probe with far-field records, and
Proposition 6 gives $\kappa\ge2\hbar$ in quantum kinematics from an
established measurement-uncertainty theorem. The premise that carries
$h>0$ is thereby reduced from the corpuscular M3 to the single number
$\kappa$, and the question "why is $h>0$" is the question "why is
$\kappa>0$", answered negatively for deterministic probes and positively
for quantum ones.

Open: (a) a consistency derivation of $\kappa>0$ that does not start from
quantum kinematics, for which Proposition 5 now states exactly what must
fail, namely far-field position records fixing a probe's momentum;
(b) extension of Theorem 1 from the constant force to a general $P(t)$
with $P(0)=P'(0)=0$, where the proof gives
$\int_0^\tau P''T\le\|P''\|_{L^2}\,\|T\|_{L^2}$ and hence
$\|P''\|_{L^2(0,\tau)}\,\tau>\ldots$; the constant-force case is the
worst case for a given $\|P''\|_\infty$ and should be written out;
(c) the probabilistic version, replacing worst-case widths by
distributions, where the N01 phase threshold and C006 belong.
