# Newton's inscribed polygon differs from the parabola by the phase of its segments

For a body of mass $m$ under a constant transverse force $F$ on $[0,\tau]$,
take any partition into steps $\tau_1,\dots,\tau_N$ and Newton's polygon of
Proposition I inscribed in the Galileo parabola: uniform motion along each
chord, impulses at the vertices. Classically the polygon and the curve are
in the same state at every vertex. Quantum mechanically their evolutions
differ by a pure phase, the same for every state of the body:

$$\boxed{W_{\rm poly}=e^{i\theta_N}\,W_F,\qquad
\theta_N=\frac{F^2}{24m\hbar}\sum_{j=1}^N\tau_j^3
=\frac{F}{2v\hbar}\sum_{j=1}^NS_j ,}$$

where $S_j=vF\tau_j^3/(12m)$ is the parabolic segment cut off by the
$j$-th chord at horizontal speed $v$, half of Lemma XI's tangent area for
that step. Three consequences follow.

- **Insertion.** Inserting a vertex at fraction $\lambda$ of a step of
  duration $\tau_j$ lowers the phase by $F^2\tau_j^3\lambda(1-\lambda)/(8m\hbar)$,
  which is $F/(2v\hbar)$ times the triangle the new vertex inscribes. At
  $\lambda=\frac12$ this is Archimedes' triangle, three quarters of the
  segment, so repeated halving removes the phase in the proportions of
  his exhaustion, $1:\frac14:\frac1{16}:\cdots$.
- **Ordering.** The same Weyl increments composed in reverse order give
  the phase $\Phi_N=F^2(\tau^3-\sum_j\tau_j^3)/(6m\hbar)$ relative to the
  chronological order, the largest over all orderings.
- **Conservation.** For every partition,

  $$\Phi_N+4\theta_N=\frac{F^2\tau^3}{6m\hbar}=\frac{\tau\Delta E}{3\hbar}
  =\frac{F}{v\hbar}\,A_{\rm inertial,fall},$$

  so refinement moves phase from the polygon's segments into the ordering
  holonomy and keeps the total fixed at the Galileo area over $\hbar$.

Both phases are c-numbers, so squeezing, mixing or any other choice of
body state leaves them unchanged. That is the property the two quantum
floors lacked, as corrected on 2026-09-22 in the
[mark-cost](mark-cost-and-statistical-floor.md) and
[probabilistic](planck-gap-probabilistic.md) notes. The single-step case
is the chord lens of the
[constant-force note](principia-constant-force-action.md), and the closed
loop of [N01](newton-insertion-action.md) is another instance of Lemma 2
below. New here are the identity for every partition, the insertion law,
the ordering holonomy and the conservation law. Exploratory; no ledger
promotion.

## 1. Setting and the exact lift

Transverse coordinate $\hat y$, momentum $\hat p$, $[\hat y,\hat p]=i\hbar$,
mass $m>0$; the horizontal motion at speed $v$ is common to every history
considered and cancels. A force history is an impulse density or measure
$f$ on $[0,\tau]$ with Hamiltonian $H_f(t)=\hat p^2/2m-f(t)\hat y$. In the
interaction picture of the free evolution $U_0$, write
$W_f(t)=U_0(t)^\dagger U_f(t)$ and use the Weyl operators of the
probabilistic note,

$$D(a,b)=\exp\!\left[\frac{i}{\hbar}(b\hat y-a\hat p)\right],\qquad
D(z_1)D(z_2)=e^{-i\omega(z_1,z_2)/2\hbar}D(z_1+z_2),$$

with $\omega(z_1,z_2)=a_1b_2-a_2b_1$. An impulse $J$ at time $t$ is
$U_0(t)^\dagger e^{iJ\hat y/\hbar}U_0(t)=D(-Jt/m,J)$, since
$U_0(t)^\dagger\hat yU_0(t)=\hat y+\hat pt/m$. The history's **phase-plane
path** is

$$z_f(t)=\bigl(\alpha_f(t),\beta_f(t)\bigr)
=\Bigl(-\frac1m\int_0^ts\,f(s)\,ds,\ \int_0^tf(s)\,ds\Bigr),$$

the accumulated transverse displacement relative to free motion and the
accumulated impulse. For the constant force, $z_F(t)=(-Ft^2/2m,\ Ft)$, a
parabola in the phase plane.

**Lemma 1.** $W_f(\tau)=\exp\bigl[\frac{i}{2\hbar}\int_0^\tau\omega(z_f,dz_f)\bigr]\,D\bigl(z_f(\tau)\bigr)$.

*Proof.* For finitely many impulses with increments $\delta z_1,\dots,\delta z_N$
in time order, induction on the Weyl relation gives
$D(\delta z_N)\cdots D(\delta z_1)=\exp[\frac{i}{2\hbar}\sum_{i<j}\omega(\delta z_i,\delta z_j)]D(\sum_j\delta z_j)$,
and $\sum_{i<j}\omega(\delta z_i,\delta z_j)=\sum_j\omega(z_{j-1},\delta z_j)$
with $z_{j-1}=\sum_{i<j}\delta z_i$. For a density $f$ the generator
$\frac{i}{\hbar}f(t)(\hat y+\hat pt/m)$ has c-number commutators at
different times, so the Magnus series stops at second order and the Riemann
sums converge to $\int\omega(z_f,dz_f)$, as in N01 §4. $\square$

**Lemma 2.** If $z_f(\tau)=z_g(\tau)$, then
$W_fW_g^\dagger=e^{i\mathcal A(f,g)/\hbar}\,\mathbf 1$, where
$\mathcal A(f,g)=\frac12\oint\omega(z,dz)$ is the signed area enclosed by
$z_f$ followed by $z_g$ reversed.

*Proof.* Lemma 1 for both, and Green's theorem for the closed loop. $\square$

Two histories with equal endpoints leave the body in the same classical
state after $\tau$, whatever happened in between, and Newton's mechanics
has no later observation that separates them. Lemma 2 says the quantum
evolutions still differ, by the enclosed phase-plane area over $\hbar$,
and that the difference is a multiple of the identity. This is the
standard geometric phase of displaced oscillators, used in trapped-ion
phase gates ([Sørensen and Mølmer, PRA **62**, 022311, 2000](https://doi.org/10.1103/PhysRevA.62.022311);
[Leibfried et al., Nature **422**, 412, 2003](https://doi.org/10.1038/nature01492),
both metadata). The $t^3$ phase of a freely falling wave packet is the
single-history form of it
([Greenberger and Overhauser, RMP **51**, 43, 1979](https://doi.org/10.1103/RevModPhys.51.43),
metadata).

## 2. The inscribed polygon

Partition $0=t_0<\dots<t_N=\tau$ with $\tau_j=t_j-t_{j-1}$ and midpoints
$c_j=(t_{j-1}+t_j)/2$. **Newton's inscribed polygon** gives the impulse
$F\tau_1/2$ at $t_0$, $F(\tau_j+\tau_{j+1})/2$ at each interior $t_j$, and
$F\tau_N/2$ at $t_N$: each step's impulse $F\tau_j$ is split equally
between its two ends.

**Theorem 1.** (i) On $(t_{j-1},t_j)$ the polygon moves uniformly with
momentum $Fc_j$ along the chord of the parabola, and its phase-plane path
passes through $z_F(t_j)$ at every vertex. (ii)
$W_{\rm poly}(\tau)=e^{i\theta_N}W_F(\tau)$ with
$\theta_N=F^2\sum_j\tau_j^3/(24m\hbar)$. (iii) With
$S_j=vF\tau_j^3/(12m)$ the area between the $j$-th arc and its chord,
$\theta_N=(F/2v\hbar)\sum_jS_j$.

*Proof.* (i) After the second half of the impulse at $t_{j-1}$ the
momentum is $Ft_{j-1}+F\tau_j/2=Fc_j$, and in time $\tau_j$ it carries the
body through $Fc_j\tau_j/m=F(t_j^2-t_{j-1}^2)/2m$, the parabola's
transverse increment. In the phase plane the two half-impulses of step $j$
are $k_1=(-F\tau_jt_{j-1}/2m,\ F\tau_j/2)$ and
$k_2=(-F\tau_jt_j/2m,\ F\tau_j/2)$, whose sum is the parabola's increment
$\delta z_j=(-F\tau_jc_j/m,\ F\tau_j)$.

(ii) Both evolutions are products over steps, in the same order, of
operators with the same displacements $\delta z_j$, so their ratio is the
product of the per-step phase ratios. By Lemma 1 the polygon's step is
$D(k_2)D(k_1)=e^{i\omega(k_1,k_2)/2\hbar}D(\delta z_j)$ with
$\omega(k_1,k_2)=\frac{F\tau_j}{2}\cdot\frac{F\tau_j}{2m}(t_j-t_{j-1})=\frac{F^2\tau_j^3}{4m}$.
The curve's step, with $s=t-t_{j-1}$ and path
$(-F(s^2+2st_{j-1})/2m,\ Fs)$ from $z_F(t_{j-1})$, has
$\omega(z,dz)=\frac{F^2s^2}{2m}ds$, hence phase
$\frac1{2\hbar}\int_0^{\tau_j}\frac{F^2s^2}{2m}ds=\frac{F^2\tau_j^3}{12m\hbar}$.
Neither depends on $t_{j-1}$. The ratio is
$\exp[\frac{i}{\hbar}(\frac18-\frac1{12})\frac{F^2\tau_j^3}{m}]=\exp[\frac{iF^2\tau_j^3}{24m\hbar}]$.

(iii) Over the step, the chord exceeds the parabola by
$\frac{F}{2m}(t-t_{j-1})(t_j-t)$, and integrating against $dx=v\,dt$ gives
$S_j=vF\tau_j^3/12m$. Then $\frac{F}{2v}S_j=\frac{F^2\tau_j^3}{24m}$. $\square$

Lemma XI's tangent area for the step is $A_j=vF\tau_j^3/6m=2S_j$, so
$\theta_N=(F/4v\hbar)\sum_jA_j$, and Proposition 1 of the
[paper](planck-gap-paper.md) is the statement that this sum vanishes with
the mesh.

**Corollary 2 (insertion).** Replacing step $j$ by steps $\lambda\tau_j$ and
$(1-\lambda)\tau_j$ lowers $\theta_N$ by

$$\frac{F^2\tau_j^3}{24m\hbar}\bigl[1-\lambda^3-(1-\lambda)^3\bigr]
=\frac{F^2\tau_j^3\,\lambda(1-\lambda)}{8m\hbar}
=\frac{F}{2v\hbar}\,T_j(\lambda),$$

with $T_j(\lambda)=S_j-S_j'-S_j''$ the triangle inscribed between the old
chord and the new vertex. At $\lambda=\frac12$, $T_j=\frac34S_j$, which is
Archimedes' *Quadrature of the Parabola*, Propositions 17 and 24 (the
segment is four thirds of its inscribed triangle, by balancing and by
exhaustion;
[companion](../docs/classics/Archimedes_QuadratureParabola_Heath1897_OCR.md)).
After $k$ rounds of halving every step, $\theta$ is $4^{-k}$ of its value.
$\square$

Each inserted point therefore changes the quantum evolution by a computable
phase, fixed by the area the insertion removes, and the change is the same
for every state of the body. A step's own phase reaches one radian at

$$\tau_\hbar=\left(\frac{24m\hbar}{F^2}\right)^{1/3},$$

the scale that the constant-force note found for the single chord lens.
The insertion mesh of the mark theorem,
$\tau_*=(9z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$, has the same form, obtained
there from the cost of a mark and here from the phase of a segment with no
apparatus at all.

## 3. The ordering holonomy and the conservation law

Keep the curve's step operators $V_j=e^{i\varphi_j}D(\delta z_j)$ and
compose them in another order. For a permutation $\sigma$, write $U_\sigma$
for the product with the steps applied in the order $\sigma$.

**Theorem 3.** $U_{\rm chron}U_\sigma^\dagger=\exp[\frac{i}{\hbar}\sum\omega(\delta z_i,\delta z_j)]\mathbf 1$,
the sum over the pairs $i<j$ that $\sigma$ inverts. Every term is positive,

$$\omega(\delta z_i,\delta z_j)=\frac{F^2}{m}\tau_i\tau_j(c_j-c_i)>0\qquad(i<j),$$

so the reversed order is extremal, with

$$\Phi_N=\frac1\hbar\sum_{i<j}\omega(\delta z_i,\delta z_j)
=\frac{F^2}{6m\hbar}\Bigl(\tau^3-\sum_j\tau_j^3\Bigr).$$

*Proof.* The per-step phases $\varphi_j$ are common to every ordering. By
the Weyl relation the phase of a product is $\frac1{2\hbar}$ times the sum
of $\omega(\delta z_a,\delta z_b)$ over pairs with $a$ applied before $b$;
a pair kept in order cancels between the two products, and an inverted
pair contributes $\omega(\delta z_i,\delta z_j)-\omega(\delta z_j,\delta z_i)=2\omega(\delta z_i,\delta z_j)$.
With $\delta z_i=(-F\tau_ic_i/m,\ F\tau_i)$,
$\omega(\delta z_i,\delta z_j)=\frac{F^2}{m}\tau_i\tau_j(c_j-c_i)$. For the
sum, $c_j-c_i=\frac{\tau_i}2+\sum_{i<k<j}\tau_k+\frac{\tau_j}2$, so
$\sum_{i<j}\tau_i\tau_j(c_j-c_i)=\frac12\sum_{i\ne j}\tau_i^2\tau_j+\sum_{i<k<j}\tau_i\tau_k\tau_j$,
and $(\sum_j\tau_j)^3=\sum_j\tau_j^3+3\sum_{i\ne j}\tau_i^2\tau_j+6\sum_{i<k<j}\tau_i\tau_k\tau_j$
gives $\frac16(\tau^3-\sum_j\tau_j^3)$. $\square$

**Corollary 4 (conservation).** $\Phi_N+4\theta_N=F^2\tau^3/(6m\hbar)$ for
every partition, and $F^2\tau^3/6m=\tau\Delta E/3=(F/v)A_{\rm inertial,fall}$
with $A_{\rm inertial,fall}=vF\tau^3/6m$ the paper's area (1). $\square$

In areas, $\hbar\Phi_N=(F/v)(A-\sum_jA_j)$ and $4\hbar\theta_N=(F/v)\sum_jA_j$:
the ordering holonomy carries the part of the Galileo area that refinement
keeps, the polygon defect carries the part that Proposition 1 sends to zero,
and the weighted total is fixed. For the uniform partition,
$\Phi_N=\frac{\tau\Delta E}{3\hbar}(1-N^{-2})$.

The chronological and reversed products realize the same displacement, so
the holonomy is a property of the composition law. Realizing a reversed
order in the laboratory needs displacements as well as impulses, since an
impulse applied at the wrong time must be translated back; trapped-ion
practice supplies such operations. Theorem 1 needs only two force
histories that act on a real body.

## 4. What the phases give as a record

Put the two histories of Theorem 1 on the arms of a control qubit, as in
N01 §4. The body ends in the same state on both arms, so the qubit
acquires the relative phase $\theta_N$ and nothing else, and the optimal
single-shot error in deciding polygon against curve is
$\epsilon=\frac12(1-|\sin(\theta_N/2)|)$, with N01's formula for $n$
copies. A single step is resolved from its chord at error $\epsilon$ only if

$$\frac{F^2\tau_j^3}{24m\hbar}\ \ge\ 2\arcsin(1-2\epsilon),\qquad
\tau_j\ \ge\ \left(\frac{48\,m\hbar\,\arcsin(1-2\epsilon)}{F^2}\right)^{1/3},$$

for every state of the body, pure or mixed, squeezed or not. The bound
concerns this readout: the body's own displacement is a separate record,
priced by the mark and aperture theorems, and squeezing acts on that
record. What the phase supplies is the part of the signal that no
preparation can move.

## 5. The premise, restated

The identities above use the Weyl relations and nothing else: no state, no
variance, no apparatus. Of the two quantum premises used so far in this
programme, Robertson's inequality is the variance consequence of the
commutator, and the 2026-09-22 corrections show that squeezing moves it.
The commutator's phase content is what Theorems 1 and 3 use, and
squeezing leaves it fixed. So the premise that carries $h>0$ into the
Galileo comparison without a resource bound is the **central extension**:
an impulse $J$ and a displacement $d$ compose, in Newton's Corollary I,
only up to the phase $Jd/\hbar$ of their parallelogram. Classically
Corollary I is exact and commutative, the polygon and the curve are the
same state at every vertex, and every $\theta_N$ vanishes.

*Conjecture, to be checked against the text.* Newton's fits supply a
Newton-age form of that premise. In his emission theory the corpuscle
moves faster in the denser medium, and the thickness of a thin plate
showing a given colour is smaller there, so the interval of fits varies
inversely with the corpuscle's speed across media and $\Lambda p$ is
invariant under refraction. A disposition whose phase advances at a rate
proportional to momentum accumulates $\int p\,dq$ in units of
$\Lambda p/2\pi$, and two paths with equal endpoints then arrive with fits
phases differing by their enclosed area over $\Lambda p/2\pi$. The
relevant passages of Book II are not yet in the
[Opticks companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md),
and a Maupertuis phase $\int p\,dq$ gives twice the quantum per-step value
$F^2\tau_j^3/24m$, since the quantum phase is the full action difference.

## 6. Consequence for STATE

STATE's next item 1 is discharged in a stronger form than it was stated.
The state-independent quantity is identified for every refinement:
Newton's inscribed polygon differs from the parabola by
$\theta_N=(F/2v\hbar)\sum_jS_j$, each inserted vertex changes it by the
inscribed triangle over $\hbar$ in Archimedes' proportions, and the ordering
holonomy carries the complement, with $\Phi_N+4\theta_N=\tau\Delta E/3\hbar$.
Next: the Newton-age form of the central extension through the fits (§5),
which needs the Book II passages on plates in different media; the general
force law, where Lemma 2 holds unchanged and Theorem 1's segment areas
become the areas between the phase-plane path and its chords; and a paper
section presenting Theorem 1 and Corollary 4 as the squeeze-immune core.
