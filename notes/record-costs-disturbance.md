# The record costs disturbance: a floor for every instrument

For every protocol of marks of any kind (any unitary coupling of the body
to an apparatus, any pointer, noise that depends on the body or not, any
apparatus state), deciding at error probability $\epsilon$ between free
motion and a constant force $F$ over a duration $\tau$, whatever the
body's initial state under each hypothesis, requires

$$\boxed{\;\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ \ge\ \hbar\arcsin(1-2\epsilon),
\qquad s=\frac{F\tau^2}{2m},\quad J=F\tau,\;}$$

where $\hat D_j$ and $\hat X_j$ are the impulse and the position jump that
mark $j$ gives the body, as Heisenberg operators on body and apparatus,
and $\Delta$ is their spread, the supremum over the states that enter the
mark in the interpolating processes of the proof; for disturbances that
are apparatus operators these are the apparatus's own states. The
reading error does not appear. The initial state may differ between the
two hypotheses, which is what an unknown initial state means for a test
between them, and the constants $1/8$ and $1/2$ are the price of that: a
test allowed to assume the same initial state under both faces the
coefficients $s$ and $J$ instead. The sagitta of Lemma X is paired with the
momentum disturbance and the impulse of Proposition I with the position
disturbance, the same pairing as in the aperture theorem of the
[probabilistic note](planck-gap-probabilistic.md),
$J\,L+s\,P\ge\hbar\arcsin(1-2\epsilon)$. The constant
$\arcsin(1-2\epsilon)$ comes from running the proof with the Bures angle
in place of total variation (Theorem P of the
[path-length note](record-distance-path-length.md), 2026-09-23); the
proof as written gives the weaker $1-2\epsilon$, and the path-length note
also joins this bound and the aperture bound in one accounting.

This is option 2 of the plan set on 2026-09-22 for extending Theorem A,
and it closes that plan. Ozawa's error--disturbance relation
([PRA **67**, 042105, 2003](https://doi.org/10.1103/PhysRevA.67.042105),
metadata), which was the expected tool for body-dependent noise, turns out
to be unnecessary, though $\hat D_j$ and $\hat X_j$ are his disturbance
operators. The ingredients are standard: Ozawa's disturbance operators,
Mandelstam--Tamm along a path, and a symmetry-based hybrid argument, the
reasoning behind information--disturbance bounds for covariant families
and behind Wigner--Araki--Yanase-type bounds (Marvian and Spekkens,
[Nat. Commun. **5**, 3821, 2014](https://doi.org/10.1038/ncomms4821);
Tajima, Shiraishi and Saito,
[PRL **121**, 110403, 2018](https://doi.org/10.1103/PhysRevLett.121.110403);
Kuramochi and Tajima,
[PRL **131**, 210201, 2023](https://doi.org/10.1103/PhysRevLett.131.210201);
metadata). What is claimed here is the combination and its reading in
Newton's quantities. The floor is a statement about disturbance alone,
because the offset between the two hypotheses has to be carried through
every mark, and what a mark does to that offset is fixed by what it does
to the body. For von Neumann marks, which disturb only momentum, the
theorem is the recoil theorem of the [recoil note](record-costs-recoil.md);
for marks that read momentum, which disturb position, it is new.
Exploratory; no ledger promotion.

## 1. Setting

Transverse coordinate $\hat y$, momentum $\hat p$, mass $m$, on $[0,\tau]$.
Mark $j$ acts impulsively at $t_j$ by a unitary $U_j$ on body $\otimes$
apparatus $j$, after which a pointer of apparatus $j$ is read; the
apparatus starts in any state, and couplings may depend on earlier
readings. Define the mark's disturbances

$$\hat D_j=U_j^\dagger\hat pU_j-\hat p,\qquad \hat X_j=U_j^\dagger\hat yU_j-\hat y,$$

operators on body and apparatus, with no restriction on how they depend
on either. Under $\mathrm F$ the body feels a force whose displacement
relative to free motion from rest is $P(t)$, $P(0)=P'(0)=0$. A test
decides at error $\epsilon$ when its equal-prior error is at most $\epsilon$
for every pair of initial states.

For a line $a+bt$ set $c(t)=P(t)-a-bt$ and $w(t)=(c(t),\,mc'(t))$, the
**offset**: if the initial state under $\mathrm F$ is the initial state
under $\mathrm I$ translated by $w(0)=(-a,-mb)$, then between marks the
state under $\mathrm F$ is the state under $\mathrm I$ translated by $w(t)$,
up to a phase, because free evolution carries a translation by $(c,mc')$
to one by $(c+c'\delta t,mc')$ and the force adds
$(P(t')-P(t)-P'(t)\delta t,\,m(P'(t')-P'(t)))$. Write $T(w)=e^{-iG_w}$,
$G_w=(c\hat p-mc'\hat y)/\hbar$, for the translation by $w$.

## 2. The theorem

**Theorem U.** For every line $a+bt$ and every initial state $\sigma$,

$$1-2\epsilon\ \le\ \frac1\hbar\sum_j\ \sup\ \Delta\bigl(c_j\hat D_j-mc_j'\hat X_j\bigr),$$

with $c_j=c(t_j)$, $c_j'=c'(t_j)$, and the supremum over the conditional
states that can enter mark $j$ when the protocol is run from $\sigma$ with
the offset carried through the earlier marks and then removed, translated
by $sw(t_j)$ for $s\in[0,1]$. For marks whose disturbances are apparatus
operators, these are the apparatus's own states and the body drops out.

*Proof.* Take the pair of initial states $\sigma$ under $\mathrm I$ and
$T(w(0))\sigma T(w(0))^\dagger$ under $\mathrm F$; a test deciding at error
$\epsilon$ has $\mathrm{TV}\ge1-2\epsilon$ between their record
distributions. Let hybrid $H_r$ run $\mathrm F$ with the offset through
mark $r$, remove the offset immediately after mark $r$, and run $\mathrm I$
afterwards. By §1, removing the offset at any time between marks gives the
same process, so $H_0$ is $\mathrm I$ from $\sigma$, $H_k$ is $\mathrm F$
from the translated state, and $H_{r-1}$ and $H_r$ agree up to mark $r$
and differ only there: with $\rho$ the state entering mark $r$ in
$H_{r-1}$ and $w=w(t_r)$, $H_{r-1}$ applies $U_r$ and $H_r$ applies
$T(w)^\dagger U_rT(w)=E\,U_r$ with $E=T(w)^\dagger U_rT(w)U_r^\dagger$. The
remainders are the same channel, so by data processing and the triangle
inequality

$$\mathrm{TV}\le\sum_r\tfrac12\bigl\|E\rho'E^\dagger-\rho'\bigr\|_1,\qquad\rho'=U_r\rho U_r^\dagger .$$

For $E(u)=e^{iuG}U_re^{-iuG}U_r^\dagger$, $u\in[0,1]$, $G=G_w$, one has
$\frac{d}{du}E(u)=iK(u)E(u)$ with $K(u)=e^{iuG}(G-U_rGU_r^\dagger)e^{-iuG}$.
The generators are unbounded; the step below assumes that $E(u)$ maps
the purification into the domain of $K(u)$ with $u\mapsto E(u)|\Psi\rangle$
differentiable, which holds on a dense set of states and extends to the
rest by continuity, and it allows $\Delta K=\infty$, in which case the bound
is vacuous (a sharp position mark pays that). The Mandelstam--Tamm bound
in the geometric form of Anandan and Aharonov bounds the Fubini--Study
angle between a purification of $\rho'$
and its image under $E=E(1)$ by $\int_0^1\Delta K(u)\,du$, each spread taken
in the state $E(u)\rho'E(u)^\dagger$, and the trace distance by the sine
of that angle, as in Theorem 2 of the probabilistic note. Conjugating
back, the spread of $K(u)$ in $E(u)\rho'E(u)^\dagger$ equals the spread of
$U_r^\dagger GU_r-G$ in $T(uw)\rho T(uw)^\dagger$, and

$$U_r^\dagger G_wU_r-G_w=\frac1\hbar\bigl(c\,\hat D_r-mc'\,\hat X_r\bigr).$$

Adaptive couplings replace each term by its supremum over the conditional
states, as in the hybrid argument of the probabilistic note. $\square$

**Corollary U1 (constant force).** Take the line of best uniform
approximation, $a+bt=\frac F{2m}(\tau t-\tau^2/8)$, a valid choice that is
optimal for the momentum term alone; with position disturbances present,
the minimum of the combined sum over lines can be smaller. Then $|c_j|\le s/8$ and
$m|c_j'|=F|t_j-\tau/2|\le J/2$, and the spread is a seminorm, so

$$(1-2\epsilon)\hbar\ \le\ \frac s8\sum_j\sup\Delta(\hat D_j)+\frac J2\sum_j\sup\Delta(\hat X_j). \qquad\square$$

For a general force the same step gives any line's $\max|c|$ and
$m\max|c'|$ in place of $s/8$ and $J/2$.

## 3. What the theorem covers

The marks are impulsive. A coupling that lasts a finite time is covered
by slicing it into short impulsive pieces, each charged with the offset
at its own time.

**Von Neumann marks.** $U=e^{-i\lambda\hat y\hat P_A/\hbar}$ gives
$\hat D=-\lambda\hat P_A$ and $\hat X=0$, so Theorem U is Theorem R of the
recoil note, $1-2\epsilon\le\hbar^{-1}\min_{a,b}\sum_j\Delta_j|c_j|$.

**Marks that read momentum.** $U=e^{-i\mu\hat p\hat Q_A/\hbar}$ shifts the
pointer momentum by $-\mu\hat p$ and gives $\hat D=0$,
$\hat X=\mu\hat Q_A$. A momentum mark therefore pays in position jumps,
and its term is paired with the impulse $J$: recording that the body has
gained momentum costs an undetermined displacement.

**Marks with body-independent noise that also displace position.** The
[additive-noise note](additive-noise-marks.md) shows that Theorem R holds
for them with the recoil spread alone, since the jump $\hat X_j$ then
commutes with the reading and the kick. Theorem U gives the weaker bound
with the extra $J$-term; the difference is that Theorem U removes the
offset after every mark, while the argument there carries it to the end.

**Body-dependent noise.** When $\hat D_j$ or $\hat X_j$ involves the body,
their spreads involve the body's state, and the bound must hold for every
initial state, including the most benign. A kick $\hat D=-\lambda\hat P_A+\kappa\hat y$
with a fresh probe uncorrelated with the body has
$\Delta(\hat D)^2=\lambda^2\Delta\hat P_A^2+\kappa^2\Delta\hat y^2\ge\lambda^2\Delta\hat P_A^2$,
so additive body dependence with a fresh probe adds to the cost. Other
forms can lower it for particular states: a kick
$-\lambda\hat P_Af(\hat y)$ with $f$ small where some initial state is
concentrated costs little on that state, and the theorem then says that
the protocol fails for that state unless other marks pay. An apparatus
already correlated with the body, which an earlier mark can create, is
accounted for through the conditional states.

**Why the error drops out.** Ozawa's relation bounds a product of error
and disturbance and includes the body's own spreads. Theorem U needs only
the second factor. The test can separate the hypotheses only if some mark
responds differently to the offset, and how a mark responds to a
translation of the body is fixed by the generator $U^\dagger G_wU-G_w$,
which is a combination of disturbances. The reading error enters the
sufficiency side, how close a given protocol comes to the bound.

## 4. The floors, now complete

| Statement | Holds for | Pays in |
| --- | --- | --- |
| Phase $\mathcal K_\tau/\hbar$ between the motion and its inscribed polygon ([polygon-lift note](polygon-lift-phase.md)) | Every body state | Nothing: a c-number |
| $J\,L+s\,P\ge\hbar\arcsin(1-2\epsilon)$ (probabilistic note) | Every instrument, bounded laboratory | The body's spreads $L$, $P$ |
| $\frac s8\sum\Delta(\hat D_j)+\frac J2\sum\Delta(\hat X_j)\ge\hbar\arcsin(1-2\epsilon)$ (Theorem U) | Every instrument, every pair of initial states; spreads over the proof's interpolating states | The marks' disturbances |
| $s\sum\Delta_j\ge8\hbar\arcsin(1-2\epsilon)$ (recoil note) | Body-independent noise, every probe state | Recoil |
| $\tau\Delta E\ge24z^2\hbar\sqrt{(1-\rho)/(1+\rho)}$, sharp (mark-cost note) | Gaussian probes with correlation at most $\rho$ | Resolution times recoil |

The two universal statements are the second and third rows. Both are
hybrid accountings of one offset: the aperture theorem removes it at the
body between marks and pays in the body's spreads; Theorem U carries it
through the marks and pays in their disturbances. Both are necessary, and
in both Newton's two quantities appear with the same partners: the
sagitta with momentum, the impulse with position.

**M3, final form.** The premise that carries $h>0$ into the recorded
Galileo comparison, for every instrument, is that a record costs
disturbance: a mark that registers the sagitta must leave the body's
impulse undetermined, and a mark that registers the impulse must leave its
position undetermined, with total exchange rate $\hbar$.

## 5. Consequence for STATE

Theorem A's extension is finished: option 3 (every probe state, the
recoil note), option 1 (body-independent noise, the additive-noise note)
and option 2 (every instrument, Theorem U). The universal floor for
arbitrary instruments is a disturbance bound paired with Newton's
sagitta and impulse, and it needs no error--disturbance relation. What
remains on the modern leg is to state the combined accounting, which
removes the offset at the body in some intervals and carries it through
the marks in others, as one optimization, and to decide whether its
minimum is attained.
