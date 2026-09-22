# The record's distance is a path length

Three results that close STATE's next items 1 and 2 of 2026-09-23.

**The single-shot constant for every protocol.** Every protocol theorem
of the programme — the aperture bound of the
[probabilistic note](planck-gap-probabilistic.md), the recoil bound of the
[recoil note](record-costs-recoil.md), the disturbance bound of the
[disturbance note](record-costs-disturbance.md) — holds with
$\arcsin(1-2\epsilon)$ in place of $1-2\epsilon$ (Theorem P). Since
$\arcsin(1-2\epsilon)=\arccos(2\sqrt{\epsilon(1-\epsilon)})$, this is the
sharp single-shot constant of Theorem 1 of the probabilistic note, so the
gap between the single-shot and protocol forms is closed, and at certain
decision the recoil bound reads

$$s\sum_j\Delta_j\ \ge\ 4\pi\hbar=2h .$$

**The aperture bound in its kick form.** For every protocol of any
instruments, with the same preparation under both hypotheses,

$$\hbar\arcsin(1-2\epsilon)\ \le\ \int_0^\tau|f(t)|\,L(t)\,dt ,$$

with $L(t)$ the body's position spread at time $t$ (Theorem K). A force
is a succession of impulses, and an impulse is registered only through
the position spread it acts on. The $(L,P)$ form of the probabilistic
note follows because free motion spreads position at the rate $P/m$, and
the two-packet preparation saturates the kick form exactly as
$\epsilon\to0$.

**One accounting.** The aperture bound pays for the force at the body,
the disturbance bound pays for it at the marks. Any split of the force
between the two gives a valid bound (Theorem M), and for von Neumann marks
and a force of one sign the best split is pointwise:

$$\hbar\arcsin(1-2\epsilon)\ \le\ \int_0^\tau|f(u)|\,\min\bigl(L(u),R(u)\bigr)\,du,\qquad
R(u)=\frac1m\sum_j\Delta_j\,G_\tau(t_j,u),$$

with $G_\tau$ the Dirichlet Green's function of the interval. $R(u)$ is
the **recoil length**: the marks' recoil spreads weighted by the
displacement each one would produce at time $u$ relative to the chord
pinned at the ends, summed, which is a length (an upper bound on the
spread those recoils produce, since independent recoils add in
quadrature). So the force is paid in length, at every moment the smaller
of the body's spread and the marks' recoil length (Corollary M1).

*Prior art.* Lemma 1 is the mixed-state Mandelstam--Tamm bound in the
Bures angle (Uhlmann, [Phys. Lett. A **161**, 329, 1992](https://doi.org/10.1016/0375-9601(92)90555-Z);
Anandan and Aharonov, [PRL **65**, 1697, 1990](https://doi.org/10.1103/PhysRevLett.65.1697));
statistical distance as a path length is Wootters's
([PRD **23**, 357, 1981](https://doi.org/10.1103/PhysRevD.23.357)) and
Braunstein and Caves's
([PRL **72**, 3439, 1994](https://doi.org/10.1103/PhysRevLett.72.3439)); the
hybrid chain is the hybrid argument of Bennett, Bernstein, Brassard and
Vazirani ([SIAM J. Comput. **26**, 1510, 1997](https://doi.org/10.1137/S0097539796300933));
Bures-angle speed limits for general processes are those of Taddei and
coauthors ([PRL **110**, 050402, 2013](https://doi.org/10.1103/PhysRevLett.110.050402));
and the position-spread form of force sensitivity is the waveform
estimation limit of Tsang, Wiseman and Caves
([PRL **106**, 090401, 2011](https://doi.org/10.1103/PhysRevLett.106.090401));
all metadata. New here are the split accounting of Theorem M and the
recoil length of Corollary M1. Exploratory; no ledger promotion.

## 1. The Bures angle

For density operators $\rho,\sigma$ let
$F(\rho,\sigma)=\operatorname{Tr}|\sqrt\rho\sqrt\sigma|$ be the root
fidelity and $A(\rho,\sigma)=\arccos F(\rho,\sigma)\in[0,\pi/2]$ the
Bures angle. Four standard facts are used.

1. $A$ is a metric on states: it obeys the triangle inequality.
2. $A$ does not increase under any channel, measurements and classical
   post-processing included (monotonicity of the fidelity).
3. $F(\rho,\sigma)=\max|\langle\psi|\phi\rangle|$ over purifications
   (Uhlmann, [Rep. Math. Phys. **9**, 273, 1976](https://doi.org/10.1016/0034-4877(76)90060-4),
   metadata), so $A(\rho,\sigma)$ is at most the Fubini--Study angle
   between any two purifications.
4. $\tfrac12\|\rho-\sigma\|_1\le\sin A(\rho,\sigma)$ (Fuchs and van de
   Graaf, [IEEE Trans. Inf. Theory **45**, 1216, 1999](https://doi.org/10.1109/18.761271),
   metadata); for probability distributions this is the classical
   statement.

**Lemma 1 (one unitary step).** Let $\rho$ be a state of body, apparatus
and a classical record register $x$, $\rho=\sum_xp_x|x\rangle\langle x|\otimes\rho_x$,
and let $V=\sum_x|x\rangle\langle x|\otimes V_x$ with
$V_x=\mathcal T\exp(i\int_0^1K_x(u)\,du)$. Then
$A(\rho,V\rho V^\dagger)\le\sup_x\int_0^1\Delta K_x(u)\,du$, each spread
taken in the state $V_x(u)\rho_xV_x(u)^\dagger$ along the path.

*Proof.* Square roots of block-diagonal operators are block diagonal,
so $F(\rho,V\rho V^\dagger)=\sum_xp_xF(\rho_x,V_x\rho_xV_x^\dagger)$, and
$\sum_xp_x\cos A_x\ge\cos\sup_xA_x$. For each block, purify $\rho_x$ to
$\psi_x$; by fact 3 the angle is at most the Fubini--Study length of the
curve $V_x(u)\psi_x$, whose speed is the spread of $K_x(u)$ in the current
state, and that spread equals the spread in the mixed state it
purifies. $\square$

For a time-independent generator $G$ acting on the body, the bound is
$\sup_x\Delta_{\rho_x}G$, the spread in the body's marginal.

## 2. Theorem P: the single-shot constant for every protocol

**Theorem P.** In Theorem 2 of the probabilistic note, Theorem R and
Corollary R1 of the recoil note, Theorem U and Corollary U1 of the
disturbance note, and Theorems K and M below, the conclusion holds with
$\arcsin(1-2\epsilon)$ in place of $1-2\epsilon$.

*Proof.* Each proof builds a chain of hybrid processes $H_0,\dots,H_n$
joining the two hypotheses, in which consecutive hybrids apply the same
channel before and after one step where they differ by a unitary. Replace
the triangle inequality for total variation by fact 1, data processing
by fact 2, and the per-step trace-distance bound by Lemma 1. This gives
$A(P_{\mathrm I},P_{\mathrm F})\le\Sigma$, the same sum $\Sigma$ of spreads
over $\hbar$ that each proof obtains. A test with equal-prior error at
most $\epsilon$ has $\tfrac12\|P_{\mathrm I}-P_{\mathrm F}\|_1\ge1-2\epsilon$,
so by fact 4 $\sin A\ge1-2\epsilon$, hence
$\Sigma\ge A\ge\arcsin(1-2\epsilon)$. In the recoil theorem the two
probe families are products, and the chain replaces one factor at a
time. $\square$

The constant is sharp in the single-shot and aperture forms. For a
single shot it is Theorem 1 of the probabilistic note, the aperture
bound's protocol form is now the same inequality with the same constant,
and the two-packet preparation attains the kick form as $\epsilon\to0$
(§3). The recoil and disturbance bounds are not shown attained: the best
known recoil protocol sits a factor of about $2.1$ above the bound at five
per cent error. At $\epsilon\to0$ the constant is $\pi/2$ where it was $1$.

## 3. Theorem K: the aperture bound in its kick form

Write $f(t)$ for the force history, $F$-hypothesis against free motion,
with the same preparation $\sigma$ under both. Let $L(t)$ be the supremum
of the body's position spread $\Delta\hat y$ at time $t$, in the laboratory
frame, over the conditional states that can occur at time $t$ when the
force acts on any initial part of the interval.

**Theorem K.** Every protocol of instruments, of any kind, adaptive or
not, deciding at error $\epsilon$ satisfies
$\hbar\arcsin(1-2\epsilon)\le\int_0^\tau|f(t)|L(t)\,dt$.

*Proof.* Let hybrid $H_{t^*}$ apply the force on $[0,t^*]$ and none
afterwards, the marks unchanged; $H_\tau$ is $\mathrm F$ and $H_0$ is
$\mathrm I$. Take a partition containing the mark times. On a cell
$[t,t+\delta]$ free of marks, $H_{t+\delta}$ and $H_t$ agree up to $t$ and
after $t+\delta$, and differ by the forced evolution over the cell, which
for linear dynamics is the free evolution followed by the translation by
the displacement the force produces from rest,
$(\int_t^{t+\delta}(t+\delta-s)f\,ds/m,\ \int_t^{t+\delta}f\,ds)$. Its
generator has spread at most $|\int_t^{t+\delta}f|\,\Delta\hat y+O(\delta^2)\Delta\hat p$
in the state it acts on. Lemma 1 and Theorem P's chain give
$\hbar A\le\sum_{\rm cells}|\int f|\,L+O(\delta)\sup\Delta\hat p$, and refining the
partition gives the integral when the momentum spread of the chain's
states is bounded. If it is infinite for some conditional state on some
cell, free evolution makes that state's position spread infinite at every
later time of the cell, so $L=\infty$ on a set of positive measure and the
theorem holds vacuously. $\square$

**Corollary K1 (the aperture form).** If the conditional states after
each mark, and at $t=0$, have position spread at most $L$ and momentum
spread at most $P$, then between marks the spread grows at most linearly,
$L(t)\le L+P(t-t_j)/m$, because a c-number force translates and free
motion shears. For the constant force,

$$F\tau L+\frac{F\tau^2}{2m}P\ \ge\ \hbar\arcsin(1-2\epsilon),$$

and with marks every $\delta t$ the second term shrinks to at most
$F\tau\,\delta t\,P/2m$. $\square$

This is Theorem 2 of the probabilistic note with the sharp constant, and
it holds under either reading of that note's aperture. With spreads
bounded in the interaction picture,
$\Delta(\hat y-\hat pt/m)\le L$, the laboratory spread is at most
$L+Pt/m$, and the same integral results.

**Saturation.** The two-packet preparation of the probabilistic note,
separation $\pi\hbar/(F\tau)$, has position spread $\pi\hbar/(2F\tau)$ up to
a relative correction of order $\sqrt{\tau\Delta E/\hbar}$ from spreading.
So $\int_0^\tau F\,L\,dt\to\pi\hbar/2$ as $\tau\Delta E\to0$, while its error
probability tends to zero and $\arcsin(1-2\epsilon)\to\pi/2$. The kick form
is attained exactly in that limit.

## 4. Theorem M: one accounting

**Theorem M.** Split the force as $f=g+h$, and let $c$ be any function
on $[0,\tau]$ with $c''=g/m$. For every protocol of instruments deciding at
error $\epsilon$ whatever the body's initial state under each hypothesis
(the composite requirement of Theorem U; with the same initial state
assumed under both, the chain's mixed pair would only give
$\arcsin(1-4\epsilon)$),

$$\hbar\arcsin(1-2\epsilon)\ \le\ \int_0^\tau|h(t)|\,L(t)\,dt
+\sum_j\sup\Delta\bigl(c(t_j)\hat D_j-mc'(t_j)\hat X_j\bigr),$$

with $\hat D_j,\hat X_j$ the disturbances of mark $j$ as in the disturbance
note, and $L(t)$ taken over the states of the chain below.

*Proof.* Take the pair of initial states $\sigma$ under $\mathrm I$ and
$T_c(0)\sigma$ under $\mathrm F$, $T_c(t)$ the translation by
$(c(t),mc'(t))$. The chain has two legs. First, starting from the process
with force $f$ from $T_c(0)\sigma$, switch off $h$ cell by cell as in
Theorem K, paying $\int|h|L/\hbar$; this ends at the process with force $g$
from $T_c(0)\sigma$. Since $c''=g/m$, the process with force $g$ from
$T_c(0)\sigma$ is the free process from $\sigma$ translated by $T_c(t)$
between marks, which is the setting of Theorem U; its chain reaches the
free process from $\sigma$ and pays the second sum. Lemma 1 bounds every
step and fact 1 adds the legs. $\square$

With $h=f$ and $c=0$ it is Theorem K; with $h=0$ and $c=P-a-bt$ it is
Theorem U. The theorem reads as a transport of the offset between the
hypotheses. A free line of offset is absorbed in the initial state at no
cost, curvature carried through a mark costs that mark's disturbance
weighted by the offset it meets, and force removed at the body costs
impulse times position spread. The record's Bures distance is at most the
length of any such transport, and a protocol escapes the floor only if at
every moment the body is spread, or the marks disturb, enough to cover
the force acting then.

**Corollary M1 (the force is paid in length).** For von Neumann marks
with recoil spreads $\Delta_j$ and a force of one sign, take $g=\chi f$
with $0\le\chi\le1$ and $c$ the solution vanishing at $0$ and $\tau$,
$c(t)=-\frac1m\int_0^\tau G_\tau(t,u)g(u)\,du$,
$G_\tau(t,u)=\min(t,u)(\tau-\max(t,u))/\tau$. Then
$\sum_j\Delta_j|c(t_j)|=\int\chi|f|R$, and minimizing over $\chi$ pointwise,
which is legitimate because for von Neumann marks the chain's conditional
spreads do not depend on $\chi$,

$$\hbar\arcsin(1-2\epsilon)\ \le\ \int_0^\tau|f(u)|\min\bigl(L(u),R(u)\bigr)\,du,
\qquad R(u)=\frac1m\sum_j\Delta_jG_\tau(t_j,u). \qquad\square$$

A mark at $0$ or at $\tau$ contributes nothing to $R$, whatever its
recoil, since $G_\tau$ vanishes there; its reading still fixes the chord.
For the three marks of Proposition D of the
[mark-cost note](mark-cost-and-statistical-floor.md), outer marks sharp,
$R(u)=\Delta_2\min(u,\tau-u)/2m$, a tent of height $\Delta_2\tau/4m$. The
pure recoil bound is $F\int R=\Delta_2s/4$; the pure aperture bound is
$F\int L$. The recoil length vanishes at the ends and peaks in the middle,
so the mixed bound pays at the marks near the ends and at the body wherever
the body is more compact than $R$. Whenever $L$ and $R$ cross, $\int F\min(L,R)$
is strictly below both pure costs, and the necessary condition it states
is strictly stronger than either.

## 5. The numbers

| Bound | Old constant | Sharp constant | At $\epsilon=0.05$ | Certain decision |
| --- | --- | --- | --- | --- |
| Recoil, $s\sum_j\Delta_j/\hbar\ge$ | $8(1-2\epsilon)$ | $8\arcsin(1-2\epsilon)$ | $8.96$ | $4\pi$, i.e. $s\sum\Delta_j\ge2h$ |
| Disturbance, $\bigl(\frac s8\sum\Delta(\hat D_j)+\frac J2\sum\Delta(\hat X_j)\bigr)/\hbar\ge$ | $1-2\epsilon$ | $\arcsin(1-2\epsilon)$ | $1.12$ | $\pi/2$ |
| Aperture, $\bigl(F\tau L+\frac{F\tau^2}{2m}P\bigr)/\hbar\ge$ | $1-2\epsilon$ | $\arcsin(1-2\epsilon)$ | $1.12$ | $\pi/2$ |

The balanced aperture of minimal area now gives
$\tau\Delta E\ge\frac12\hbar\arcsin^2(1-2\epsilon)$, which is $\pi^2\hbar/8$ at
certain decision. The correlated three-mark protocol sits within
$\sqrt2z_{1-\epsilon}/\arcsin(1-2\epsilon)$ of the recoil bound, about $2.1$
at five per cent error, at every squeezing.

## 6. Consequence for STATE

Items 1 and 2 of STATE's queue are settled, apart from the worst-case
interval $[9,36]$ of the derivation note, which concerns a framework
without quantum instances. Every protocol theorem carries the sharp
single-shot constant; the aperture bound is the kick form
$\int|f|L\ge\hbar\arcsin(1-2\epsilon)$; and one accounting, Theorem M,
contains the aperture and disturbance bounds and interpolates between
them, with the pointwise form $\int|f|\min(L,R)$ for von Neumann marks.
The remaining modern item is whether the minimum over splits and lines in
Theorem M is attained by some protocol, which would make it the exact
floor.
