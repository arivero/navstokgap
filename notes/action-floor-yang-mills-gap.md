# An action floor on transverse phase-space area produces the Yang--Mills quantum-mechanical gap, and a gap forces an action unit

In the Yang--Mills quantum-mechanical model of [G07](low-dimensional-mass-gap.md)
the two directions of the analogy between a positive action floor $h>0$ and a
mass gap can both be stated and proved inside one solved system. Forward:
classical mechanics plus the single postulate that no transverse oscillation
has phase-space area below $h/2$ confines the escaping valley motion to
$|x|\le2\sqrt m\,E/(\hbar g)$ at energy $E$, makes the accessible phase-space
volume finite with the growth $E^{3/2}\ln E$ that Simon records for the true
eigenvalue counting function, and reproduces through Bohr--Sommerfeld
quantization the energy unit $\varepsilon=\hbar^{4/3}g^{2/3}m^{-2/3}$ of the
exact spectrum; the operator inequality behind G07's Theorem 5 is this
postulate made rigorous by the uncertainty inequality. The abelian model has
no transverse oscillation, so the same floor constrains nothing and its
spectrum stays continuous: with $h>0$ assumed, a commutative field still
has no gap. Backward: in the classical model with constants $m$ and $g$,
any positive finite gap $\Delta$, whatever extra constant produces it,
supplies the action unit $\Delta^{3/4}m^{1/2}g^{-1/2}$, so within the model
"gap" and "action unit" are dimensionally equivalent. The same equivalence
holds for Yang--Mills in $d=2$ and $d=3$, where the classical coupling is
dimensionful, and fails exactly in $d=4$, the action-critical dimension,
where a mass gap together with $c$ admits no action unit. The floor
postulate is a phase-space area statement; the necessity theorem sought in
STATE item 1 is the derivation of such a floor. This is G08, exploratory,
with no ledger promotion.

## 1. The transverse phase-space area and the floor postulate

Take the scalar model of G07, Theorem 5, with classical Hamiltonian
$$H_{\rm cl}=\frac{p_x^2+p_y^2}{2m}+\frac{g^2}{2}x^2y^2 .$$
At fixed $x\neq0$ the transverse motion is the oscillator
$E_y=p_y^2/2m+\tfrac12m\omega_x^2y^2$ with $\omega_x=g|x|/\sqrt m$.

**Proposition 1.** The transverse orbit at fixed $x$ and transverse energy
$E_y$ is the ellipse $\{p_y^2/2m+\tfrac12m\omega_x^2y^2=E_y\}$, and its
enclosed phase-space area is
$$J_y=\oint p_y\,dy=\frac{2\pi E_y}{\omega_x}=\frac{2\pi\sqrt m\,E_y}{g|x|}.$$

*Proof.* The ellipse has semi-axes $\sqrt{2mE_y}$ in $p_y$ and
$\sqrt{2E_y/(m\omega_x^2)}$ in $y$; the product times $\pi$ gives
$2\pi E_y/\omega_x$. $\square$

$J_y$ is the adiabatic invariant of the transverse oscillation: along the
valley it is conserved to leading order when $\omega_x$ changes slowly on
the oscillation's time scale, $|\dot x/x|\ll\omega_x$, that is
$|x|\gg x_{\rm ad}(E)=(2E)^{1/4}g^{-1/2}$ at energy $E$ (Landau--Lifshitz,
*Mechanics* §49; the note uses only Proposition 1 and the inequality
below, which need no adiabatic limit).

**Floor postulate $\mathsf F(h)$.** No admitted state has a transverse
oscillation of phase-space area below $h/2=\pi\hbar$:
$J_y\ge h/2$ whenever $x\ne0$, and $J_x\ge h/2$ whenever $y\ne0$.

The value $h/2$ is the Bohr--Sommerfeld ground-state area $(n+\tfrac12)h$
at $n=0$; any positive multiple of $h$ gives the same conclusions with a
different pure number.

## 2. Forward: the floor confines the valley and produces the gap

**Theorem 2.** Under $\mathsf F(h)$, every admitted classical state of
energy $E$ satisfies
$$|x|\le X(E)=\frac{2\sqrt m\,E}{\hbar g},\qquad |y|\le X(E),$$
and the transverse energy obeys $E_y\ge\hbar\omega_x/2=\hbar g|x|/(2\sqrt m)$.
In particular the admitted region of the energy shell is bounded, whereas
without the floor the shell contains the unbounded valley motions
$y=p_y=0$, $x(t)=x_0+p_xt/m$ of every energy $p_x^2/2m>0$.

*Proof.* For $x\ne0$, Proposition 1 and $E_y\le E$ give
$J_y=2\pi\sqrt m\,E_y/(g|x|)\le2\pi\sqrt m\,E/(g|x|)$; the floor
$J_y\ge\pi\hbar$ then forces $|x|\le2\sqrt mE/(\hbar g)$. Reading the same
inequality as a bound on $E_y$ gives $E_y\ge\hbar g|x|/(2\sqrt m)$. The
$y$ bound is symmetric. $\square$

**Remarks.**

1. *The floor is the quantum bound.* The inequality
   $E_y\ge\hbar g|x|/(2\sqrt m)$ is word for word the oscillator bound of
   G07, Theorem 5 (Lemma 0 there): $-\frac{\hbar^2}{2m}\partial_y^2
   +\frac{g^2}{2}x^2y^2\ge\hbar g|x|/(2\sqrt m)$. The quantum theorem is
   the floor postulate enforced by the uncertainty inequality
   $\int(\mu|\phi'|^2+\nu y^2|\phi|^2)\ge\sqrt{\mu\nu}\int|\phi|^2$, which
   is the statement that no normalizable state occupies a transverse
   phase-space area below $h/2$. So in this model the implication
   "$h>0$ gives the gap" is exact, with $h$ entering only through the area
   floor, and the rest of quantum kinematics is not used.
2. *Self-consistency of the adiabatic reading.* The cutoff $X(E)$ lies in
   the adiabatic region: $X(E)/x_{\rm ad}(E)=2^{3/4}(E/\varepsilon)^{3/4}$
   with $\varepsilon=\hbar^{4/3}g^{2/3}m^{-2/3}$, so for $E\gg\varepsilon$
   the floor acts where $J_y$ is conserved, and near the ground state,
   $E\sim\varepsilon$, the classical reading is only an estimate.
3. *Counting.* Without the floor the phase-space volume
   $|\{H_{\rm cl}\le E\}|$ is infinite for every $E>0$ (G07, Theorem 5,
   proof of (iv)). With the floor, the transverse area at fixed $x$ and
   fixed $p_x$ is $2\pi(E-p_x^2/2m)/\omega_x$; integrating over
   $|p_x|\le\sqrt{2mE}$ gives $(8\pi/3)\sqrt{2m}\,E^{3/2}\sqrt m/(g|x|)$
   per unit $x$, and integrating $|x|$ from a fixed inner scale to $X(E)$
   gives
   $$|\{H_{\rm cl}\le E\}\cap\mathsf F(h)|
   =\frac{16\sqrt2\,\pi m}{3g}\,E^{3/2}\ln\frac{X(E)}{x_0}+O(E^{3/2}),$$
   which grows like $E^{3/2}\ln E$. Simon states (Ann. Phys. 146 (1983)
   209, p. 3, passage read) that the true counting function $N(E)$ of
   $-\Delta+x^2y^2$ grows like $E^{3/2}\ln E$, while the classical volume
   is infinite. The floor therefore reproduces the growth law of the exact
   spectrum; the identification $N(E)\approx|\{\cdot\}|/h^2$ is the Weyl
   heuristic, stated here as a consistency check and not as a theorem.
4. *Semiclassical levels.* With $J_y=(n+\tfrac12)h$ conserved, the valley
   motion has effective Hamiltonian $p_x^2/2m+\kappa_n|x|$,
   $\kappa_n=(n+\tfrac12)\hbar g/\sqrt m$, and Bohr--Sommerfeld
   quantization $\oint p_x\,dx=(N+\tfrac12)h$ with
   $\oint p_x\,dx=\tfrac{8\sqrt{2m}}{3}E^{3/2}/\kappa_n$ gives
   $$E^{\rm BS}_{n,N}=\varepsilon\Big[\frac{3\pi(2n+1)(2N+1)}{16\sqrt2}\Big]^{2/3},
   \qquad\varepsilon=\hbar^{4/3}g^{2/3}m^{-2/3}.$$
   The unit $\varepsilon$ is the exact one of G07, Theorem 5(4), as
   Theorem 1 of G07 requires; the pure numbers are semiclassical estimates
   of $e_n$ and are labelled as such. The lowest level and the first
   spacing are positive: the old quantum theory of this model already has
   a gap.

**Corollary 3 (the commutative model).** For the abelian matrix model, and
for $D=1$, the potential vanishes identically: there is no transverse
oscillation, $\mathsf F(h)$ imposes no condition, the classical energy
shells stay unbounded and the quantum spectrum is $[0,\infty)$ (G07,
Theorem 6(5)). An action floor produces a gap only in the presence of the
commutator potential, which is what supplies the transverse ellipses whose
area the floor bounds.

For the SU(2) model with $D\ge2$ the same argument applies to each of the
two transverse directions of $\vec x_j$ relative to $\vec x_i$: the floor
gives $E_\perp\ge\hbar g|\vec x_i|/\sqrt m$, the bound of G07, Theorem 6(1),
and $|\vec x_i|\le\sqrt m\,E/(\hbar g)$ on the energy shell.

## 3. Backward: a gap forces an action unit, except in the action-critical case

**Proposition 4.** Let the classical model with fixed constants $m$, $g$
(dimension vectors $d_m=(1,0,0)$, $d_g=(\tfrac12,-1,-1)$) be enlarged by
any fixed constants, and suppose the enlarged theory has a positive finite
gap $\Delta$ depending on the fixed constants only. Then the theory has
the action unit
$$A=\Delta^{3/4}\,m^{1/2}\,g^{-1/2},$$
and conversely an action unit $A$ gives the energy unit
$A^{4/3}g^{2/3}m^{-2/3}$.

*Proof.* Energy has dimension vector $(1,2,-2)$ and action $(1,2,-1)$. The
system $a\,d_m+b\,d_g+c\,(1,2,-2)=(1,2,-1)$ has the unique solution
$a=\tfrac12$, $b=-\tfrac12$, $c=\tfrac34$: the length and time components
give $-b+2c=2$, $-b-2c=-1$, hence $c=\tfrac34$, $b=-\tfrac12$, and the mass
component gives $a=\tfrac12$. So $m^{1/2}g^{-1/2}\Delta^{3/4}$ has action
dimension whatever the extra constants are. The converse is G07, Theorem
3 with $k=4$. $\square$

Within the model, therefore, "the gap is positive" and "an action unit
exists" are the same dimensional statement, and G07's Theorem 5 supplies
the dynamical content, $0<\delta_1<\infty$, that turns the unit into the
number $\Delta=\delta_1\varepsilon$.

**Proposition 5 (which field theories share this equivalence).** With the
classical coupling $1/g^2$ of dimension action$\cdot$length$^{4-d}$, the
speed $c$ and a gap $\Delta$, an action unit exists in $d=2$ and $d=3$
and does not exist in $d=4$:

| $d$ | fixed classical constants | action unit from $(1/g^2,c,\Delta)$ |
| --- | --- | --- |
| 2 | $1/g^2\sim(1,4,-1)$, $c$ | $(1/g^2)^{1/3}c^{-2/3}\Delta^{2/3}$ |
| 3 | $1/g^2\sim(1,3,-1)$, $c$ | $(1/g^2)^{1/2}c^{-1/2}\Delta^{1/2}$ |
| 4 | $c$ only | none: $a(0,1,-1)+b(1,2,-2)=(1,2,-1)$ has no solution |
| mechanics, $k=-2$ | $m$, $\lambda\sim(1,4,-2)$ | $\sqrt{m\lambda}$ already classical; $\Delta$ adds nothing |

*Proof.* Solve $a\,d_{1/g^2}+b\,d_c+c'\,(1,2,-2)=(1,2,-1)$: for $d=3$,
adding the length and time equations gives $2a=1$, then $c'=\tfrac12$,
$b=-\tfrac12$; for $d=2$, $3a=1$, $c'=\tfrac23$, $b=-\tfrac23$; for $d=4$
the mass component forces $b=1$, the length component then forces $a=0$,
and the time component reads $-2=-1$. The $k=-2$ row is G07, Section 6.
$\square$

The equivalence "gap if and only if action unit" thus holds whenever the
classical theory carries a dimensionful coupling, and fails exactly at the
action-critical dimension, where the classical theory carries no constant
at all and a mass gap with $c$ yields a length only after $\hbar$ is
supplied. This is the dimensional reason the four-dimensional problem is
one-directional: the gap needs a scale generated by transmutation, and
that scale does not by itself return an action unit.

## 4. What this decides for the positive-action question

- **Direction.** In the solved model the analogy is an equivalence at the
  level of units and an implication at the level of dynamics: the floor
  postulate, used only through the transverse area, produces the gap
  (Theorem 2 and Remark 1), and the gap returns the unit (Proposition 4).
  The mass-gap problem is the forward direction with $\hbar$ and the gauge
  group given; the necessity problem of STATE item 1 is the derivation of
  the floor itself. Inside this model those two problems have the same
  dimensional content, and the necessity problem is exactly as hard as
  proving a gap from a consistency premise that does not name $\hbar$.
- **The second ingredient.** Corollary 3 states the commutative case with
  $h>0$ assumed: an action floor alone gives no gap; the commutator
  potential is what creates transverse oscillations for the floor to act
  on. Any transported statement "$h>0$ gives a gap" must name the
  structure that plays this role.
- **Areas.** The floor is a bound on a phase-space area, the ellipse of
  Proposition 1. The programme's anchor, Galileo's area
  $vF\tau^3/(6m)$ between the inertial line and the parabola, is a
  configuration-space area converted to action by the factor $3F/v$
  ([N01](newton-insertion-action.md) §1). The model shows what a
  successful floor would have to look like on the phase-space side: a
  lower bound on the area of a closed transverse orbit, invariant under the
  adiabatic deformation of the orbit. A constant-force motion has no
  closed transverse orbit, which is one more statement of why the Galileo
  class is similarity-covariant (G07, Proposition 14).
- **Gate.** For gap-track work the supplied/generated gate of G07 can be
  applied in phase-space terms: a generated gap needs a family of closed
  orbits whose area can fall below $h$ along a non-compact direction.

## 5. Strategic consequence

G08 closes the loop inside the Yang--Mills quantum-mechanical model: floor
gives gap, gap gives unit, and the commutative model is inert under the
floor. Two dimensional facts are retained for the programme: the
equivalence of gap and action unit holds exactly when the classical theory
has a dimensionful coupling, and fails at $d=4$; and the phase-space area
of a closed transverse orbit is the object a floor must bound. Neither
changes STATE item 1's target, which remains the derivation of the floor
from consistency premises; N02 gains the phase-space form of the floor as
the statement to aim at. No ledger claim is promoted; Theorem 2 and
Propositions 1, 4, 5 are elementary and the semiclassical remarks are
labelled estimates. Sources are in [B79](../references/batches/B79.md).
