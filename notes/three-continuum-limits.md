# What survives refinement: the pion, the Yang--Mills gap and Newton's action

**Working conclusion, 2026-09-26.** The common problem is to construct a
limit while preserving a specified physical structure. In pure $SU(3)$
Yang--Mills it is a positive energy threshold. In chiral QCD it is the
broken global symmetry and observable spectral weight that require a
zero threshold. In Newton's comparison it is a positive action cost of
physical records while the time partition becomes arbitrarily fine.
All three require control independent of the regulator. The quantities
controlled, and the reasons for their survival, differ.

User direction of this date makes this comparison the intended frame of
the eventual paper. **The two main proof goals remain the pure $SU(3)$
mass gap and the necessity of a positive action scale in Newton's
comparison.** QCD with massless and with nonzero quark masses is an
orientation and a source of mechanisms, rather than a third full
construction programme. This note supplies the definitions, two elementary
limit criteria, and the plan. It proves neither main goal.

The [Planck paper](planck-gap-paper.md) remains the developed Newton
component; the [Yang--Mills position](mass-gap-position.md) and
[conditional theorem](mass-gap-conditional-theorem.md) remain the
technical map for pure gauge theory. Their results retain their stated
hypotheses. The present note changes the destination of the synthesis.

## 1. Compare physical quantities, with the regulators separate

Use $a$ for the spacetime lattice spacing, $L$ for spatial box size,
$m_q$ for a renormalized quark mass, and $\varepsilon=|\pi|$ for the
largest step of a Newtonian time partition. Euclidean time extent is
taken to infinity to select zero temperature. Write $E_*$ for an energy
threshold, $M_*=E_*/c^2$ for a mass, and $\mu_*=E_*/(\hbar c)$ for an
inverse correlation length. This avoids the convention in older notes
where $m$ sometimes denotes an energy.

For an isotropic reflection-positive lattice theory, on a specified
physical channel, normalize the transfer matrix by its vacuum
eigenvalue and write

$$T_a=e^{-aH_a/(\hbar c)},\qquad
\delta_a=\frac{aE_*(a)}{\hbar c}=a\mu_*(a).$$

A continuum theory with $0<E_*<\infty$ therefore has
$\delta_a\to0$. A massless channel also has $\delta_a\to0$. Their
distinction is the limit of $\delta_a/a$, together with convergence of
the states and observables that detect it. A strong-coupling lattice gap
at fixed bare coupling does not specify that limit.

| Comparison | Quantity to retain in physical units | Required limiting structure |
| --- | --- | --- |
| Pure $SU(3)$ | $0<E_{\rm YM}<\infty$ | A nontrivial continuum theory; a gap above its vacuum |
| Two-flavour QCD, $m_q=0$ | $E_\pi=0$ with nonzero pion spectral weight | Conserved non-singlet axial current and a broken-symmetry vacuum |
| Two-flavour QCD, small $m_q>0$ | $E_\pi(m_q)>0$, tending to zero with $m_q$ | Controlled explicit symmetry breaking and the same physical scale |
| Newton comparison | $h_*>0$ in a specified class of physical records | A record algebra and cost surviving $\varepsilon\to0$ |

The first three rows use a quantum theory with $\hbar>0$ already in
its definition. The last main goal asks how that positive action
structure is justified. The pion supplies a useful check: positive
$\hbar$ and a dynamically generated strong-interaction scale can coexist
with zero energy gap.

## 2. Pure Yang--Mills: retain coercivity through the limit

The target is a nontrivial four-dimensional $SU(3)$ theory with the
Wightman or Osterwalder--Schrader properties, and physical Hamiltonian
$H$ satisfying

$$H\Omega=0,\qquad
E_{\rm YM}:=\inf\bigl(\operatorname{spec}H\setminus\{0\}\bigr)
\in(0,\infty).$$

One chooses a vacuum sector and proves the corresponding vacuum and
clustering properties. This target requires a gap above the vacuum;
it does not prescribe every point of the spectrum above the threshold.
The official statement explicitly couples existence, axioms and the gap
([Jaffe--Witten, §§4--6](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
passage).

For the lattice route, fix a renormalized physical scale and tune
$g_0(a)$ toward zero. A sufficient spectral estimate has the form

$$H_{a,L}-E_{0,a,L}\ \ge\ E_-(1-P_{0,a,L}),\qquad E_->0,$$

uniformly along the trajectory in sufficiently small $a$ and arbitrarily
large $L$, on the gauge-invariant Hilbert space. To pass this estimate
to a continuum theory one still needs convergence of renormalized local
observables, positivity, covariance, regularity and nontriviality. An
upper estimate or a surviving finite-energy excitation prevents all
non-vacuum states from escaping to infinite energy.

A corresponding correlation route is a bound
$C_O(t)\le K_Oe^{-E_-t/\hbar}$ for positive Euclidean time
autocorrelations of a dense family of vacuum-subtracted local vectors.
The constants must survive the cutoff limit for their chosen
renormalizations. One rapidly decaying glueball correlator establishes
only a channel statement. Reflection positivity and reconstruction are
part of the route from correlations to the physical Hamiltonian; a
Langevin relaxation rate by itself is a different object.

The existing H1/H2 route aims to deliver
$E_-=(\hbar c/a_*)\min(\gamma_*,\gamma')$. It remains conditional on
the blocking and mixing estimates. Construction and nontriviality,
called T4 in the [obligations map](mass-gap-obligations-lattice.md), must
remain explicit as well. We choose $L\to\infty$ at fixed $a$ followed
by $a\to0$ along the trajectory as the working order; interchanging
these operations requires its own uniform estimates.

## 3. The pion: preserve the symmetry that requires a soft channel

Take $SU(3)$ colour with two degenerate quarks, zero temperature, vacuum
angle zero, and no electromagnetism. This fixes what is meant by the
comparison with and without a quark mass. Additional flavours or
electromagnetism would change the statement.

**Massless case.** Conditional on a local relativistic continuum theory
and spontaneous breaking
$SU(2)_L\mathbin{\times}SU(2)_R\to SU(2)_V$, the Goldstone theorem
requires three massless modes with nonzero axial-current matrix elements.
These are the pion modes. The theorem's symmetry-breaking premise is a
dynamical obligation in QCD; the theorem does not establish it merely
from the presence of fermions
([Goldstone--Salam--Weinberg 1962](https://doi.org/10.1103/PhysRev.127.965),
abstract; [Leutwyler 1993, §§2--3](https://arxiv.org/pdf/hep-ph/9311274),
passage).

A possible order of limits for the per-flavour order parameter is

$$\Sigma_R=-\lim_{m_q\downarrow0}\lim_{L\to\infty}\lim_{a\to0}
\langle\bar u u\rangle_{R,a,L,m_q}>0,$$

with a positive mass selecting the vacuum and the physical scale held
fixed. The inner continuum limit is taken at fixed physical $L,m_q$.
An exactly symmetric finite-volume state has zero symmetry-breaking
expectation at zero source; it cannot select the required vacuum by
itself. Finite-volume zero modes and the infinite-volume order
parameter must be distinguished
([Damgaard--Fukaya 2009, introduction](https://arxiv.org/pdf/0812.2797),
passage). The displayed order is a proposed construction order, with
existence at each stage an obligation.

**Nonzero case.** At fixed small positive $m_q$, removing $a$ retains
explicit chiral breaking. In the conventional broken-phase low-energy
description, put $e_q=m_qc^2$ and let $B_E>0$ have energy units. Then

$$E_\pi^2=2B_Ee_q[1+r(e_q)],\qquad r(e_q)\longrightarrow0
\quad(e_q\downarrow0).$$

This is the leading chiral mass relation, conditional on the broken
phase and its controlled low-energy expansion; higher orders include
chiral logarithms. In particular, $a\to0$ at fixed $e_q>0$ is different
from $e_q\to0$
([Leutwyler, *Light Quark Masses*, eq. (1)](https://arxiv.org/pdf/hep-ph/9609467),
passage). We use this as a benchmark, without claiming a constructive
proof of massive QCD or a lower bound on every channel from this formula.

There is a sharper identity underneath the expansion. Define
$\mu_q=m_qc/\hbar$ and $\mu_\pi=E_\pi/(\hbar c)$, both inverse lengths.
Assume the renormalized non-singlet Ward identity in compatible
Euclidean conventions, away from contact insertions:

$$\partial_\alpha A^b_\alpha=2\mu_q P^b.$$

With pole amplitudes defined by
$\langle0|A^b_\alpha|\pi^d(k)\rangle=i\delta^{bd}{\cal F}_\pi k_\alpha$
and $\langle0|P^b|\pi^d\rangle=\delta^{bd}{\cal G}_\pi$, its
one-pion matrix element reads

$$\mu_\pi^2{\cal F}_\pi=2\mu_q{\cal G}_\pi.$$

The conventional continuation fixes the displayed phases. The equation
is exact once the current identity and the pion pole exist; deriving
the leading mass formula also uses the small-mass behaviour of the
residues. A pole with nonzero residue must survive the limit. An
unrenormalized divergent pseudoscalar susceptibility is insufficient:
contact terms and ultraviolet divergences need separate control.

At finite $a$ the regulator matters. A Ginsparg--Wilson Dirac operator
has an exact lattice non-singlet chiral symmetry
([Lüscher 1998](https://arxiv.org/abs/hep-lat/9802011), abstract).
Wilson fermions instead require critical-mass tuning and a restored,
renormalized Ward identity
([Bali et al. 2019, §2](https://doi.org/10.1140/epjc/s10052-019-7287-1),
passage). Exact lattice chirality alone supplies
neither spontaneous breaking nor a continuum construction.

For the final paper this comparison earns its place by testing the
mechanism. A proposed pure-gauge estimate cannot be carried unchanged
to chirally broken QCD if it gaps the pion channel. Colour gauge
symmetry and global axial flavour symmetry have different roles.
Supersymmetric cancellation of transverse zero-point energies, recorded
in [G07](low-dimensional-mass-gap.md), is a separate mechanism from QCD's
Goldstone pions. Nor does a massless pion imply a massless coloured gluon.

## 4. Newton: retain a record cost while the polygon error vanishes

Use $M$ for the body's mass, constant force $F$, horizontal speed $v$,
and comparison duration $T$. The specified Galileo comparison is

$$q_I(t)=(vt,0),\qquad q_F(t)=(vt,Ft^2/2M),$$
$$A(T)=\frac{vFT^3}{6M},\qquad
{\cal A}(T):=\frac{3F}{v}A(T)=\frac{F^2T^3}{2M}=T\Delta E.$$

For a partition $\pi$ of $[0,T]$, the action difference associated with
its inscribed chord segments is

$$K_\pi=\frac{F^2}{24M}\sum_j(\Delta t_j)^3,
\qquad 0\le K_\pi\le\frac{F^2T}{24M}\varepsilon^2\to0.$$

This follows by $(\Delta t_j)^3\le\varepsilon^2\Delta t_j$ and
$\sum_j\Delta t_j=T$. In the supplied quantum lift the phase difference
is $K_\pi/\hbar$, which also tends to zero at fixed $\hbar>0$.
The [polygon note](polygon-lift-phase.md) separately gives an ordering
phase $\Phi_\pi$ with

$$\hbar\Phi_\pi+4K_\pi=\frac{{\cal A}(T)}3.$$

Thus one geometric action defect vanishes while the ordering comparison
retains a finite action at fixed $T$. Reading that phase requires a
relative-phase experiment. Its derivation already assumes the Weyl
relations and positive $\hbar$.

The proposed $h$ gap concerns what a physical record must cost. For a
fixed class $\mathfrak M_\varepsilon$ of calibrated marks, define

$$\kappa_\varepsilon
=\inf_{M_j\in\mathfrak M_\varepsilon}\delta_j\Delta_j,$$

where $\delta_j$ is reading error and $\Delta_j$ impulse uncertainty.
The class, available preparations, apparatus resources and meaning of
the uncertainty must be specified, with feasible informative records of
finite cost retained in the limit. A restricted theorem might establish
$\inf_{0<\varepsilon<\varepsilon_0}\kappa_\varepsilon\ge\kappa_*>0$.
The general-instrument formulation instead bounds the disturbance
functional defined in the [disturbance note](record-costs-disturbance.md).
These are distinct formulations of record cost; a single-mark product
does not by itself establish a universal protocol bound.

The current paper proves such conditional bounds using quantum
kinematics or an assumed positive mark trade-off. The main necessity
goal is to supply independently justified physical premises that force
a positive scale and its universality, without placing that scale in
the premise. Identification with $h=2\pi\hbar$ is a further calibration
obligation. Newton's optical fits provide a candidate product $\Lambda p$;
the [paper's §8](planck-gap-paper.md) keeps its extra indeterminacy and
cross-colour universality premises visible.

Two refinement operations must stay separate: making more marks within
fixed $T$, and asking each shrinking cell to decide the force on its
own. The Gaussian result bounds the latter decision window; it permits
marks much denser than that window. A positive action cost is compatible
with continuous time and with convergence of the polygon. It is also
compatible with zero energy gap, as the quantum free particle illustrates.

## 5. Two elementary criteria for carrying spectral information to a limit

These statements are standard consequences of the spectral theorem and
weak convergence of positive measures, included to state exactly what
the comparison needs. They are written derivations, with no numerical
test and no claim of novelty.

**Proposition 1 (a surviving lower bound).** Suppose renormalized,
vacuum-subtracted local vectors $O_n\Omega_n$ have finite positive
energy spectral measures $\nu_n$ converging weakly to $\nu$ in a
reconstructed limiting theory. If every $\nu_n$ is supported in
$[E_-,\infty)$ for one $E_->0$, then so is $\nu$.

*Proof.* Every nonnegative continuous test function compactly supported
in $[0,E_-)$ integrates to zero against every $\nu_n$, hence against
$\nu$. Such test functions exhaust the interval. If the statement holds
on a dense family of local vectors orthogonal to the vacuum, the
spectral projection of $H$ onto $(0,E_-)$ is zero. A nonzero limiting
measure supplies surviving finite-energy spectral content. $\square$

For positive autocorrelations
$C_n(t)=\int e^{-Et/\hbar}\,d\nu_n(E)$, a uniform physical decay rate
is another way to obtain the support condition. The normalization of
the observables and their nonzero limit are part of the hypotheses.

**Proposition 2 (a surviving zero threshold).** Suppose instead that
$\nu_n\Rightarrow\nu$, that $\nu(\{0\})=0$, and that for every
$\eta>0$ there is $w_\eta>0$ such that, for all sufficiently large $n$,

$$\nu_n([0,\eta/2])\ge w_\eta.$$

Then $\nu((0,\eta))>0$ for every $\eta>0$, and the channel's excited
energy threshold is zero.

*Proof.* The closed-set inequality for weak convergence gives

$$\nu([0,\eta/2])\ge\limsup_n\nu_n([0,\eta/2])\ge w_\eta.$$

Removing the zero atom leaves positive weight in $(0,\eta)$.
$\square$

The no-atom hypothesis distinguishes arbitrarily soft excitations from
an extra vacuum contribution. It belongs to a selected pure vacuum and
a connected observable. The chiral comparison suggests obtaining the
required surviving weight from an axial Ward identity and a nonzero
order parameter, with the Goldstone theorem supplying the continuum
implication.

**Why convergence of eigenvalues alone is too weak.** For $E_0>0$ let
$\mathrm d_x$ denote unit point mass at energy $x$, and set

$$\nu_n=(1-e^{-n})\mathrm d_{E_0}+e^{-n}\mathrm d_{E_0/n}.$$

Every $\nu_n$ has lowest energy $E_0/n\to0$, yet
$\nu_n\Rightarrow\mathrm d_{E_0}$. The soft state's observable weight
disappears. Conversely, a positive gap at each $n$ can collapse with
nonvanishing weight. These examples identify the estimates a continuum
argument must actually carry. Compact $U(1)$ gauge theory in three
dimensions realizes the collapse as a theorem: every lattice has a
positive Debye mass, and at fixed coupling the continuum limit is the
massless free field, so the uniform $E_-$ of Proposition 1 fails; the
[series/parallel note, §4](series-parallel-gauge-refinement.md) traces
the failure to the error density of one refinement step in physical
units.

For Newton the analogous surviving object is a calibrated record and
its information about the comparison. No spectral measure is supplied
by classical mechanics for this purpose. The useful transfer is the
proof discipline: compatible observable limits, nonvanishing response,
and a bound uniform over admitted refinements. Any stronger equivalence
requires a constructed mathematical map.

## 6. The mechanism worth developing across the two main goals

The [action-floor note G08](action-floor-yang-mills-gap.md) supplies one
concrete bridge. A transverse oscillator of frequency $\Omega(x)$ obeys

$$\frac{p_y^2}{2M}+\frac12M\Omega(x)^2y^2
\ \ge\ \frac12\hbar\Omega(x).$$

When $\Omega(x)$ grows along a classically escaping valley, this
all-state operator bound can confine that valley. Its force comes from
the action scale together with the non-abelian commutator potential.
The solved matrix models establish the mechanism in a specified
Hamiltonian; extension to four-dimensional gauge theory requires
uniform control of the additional modes and renormalization.

The pion comparison asks which flat directions an interaction is
allowed to lift. A broken exact global symmetry protects Goldstone
directions. Pure Yang--Mills has no corresponding axial flavour
symmetry. The absence of that protection makes lifting possible; the
positive bound still has to be proved. Finite quark mass then supplies
a controlled way to lift the protected direction, which is why both
pion cases are useful as orientation.

The candidate unifying question is therefore: **which structures enforce
an irreducible cost, which protect a soft direction, and which survive
the removal of the regulator?** Quantum kinematics supplies an action
unit to both QCD theories. Their different spectra depend on dynamics
and symmetry. A successful Newton necessity argument must explain the
action structure at the preceding level.

## 7. Work toward the final paper

The intended paper can be called *What survives refinement: action,
symmetry and the continuum*. Its architecture is: Galileo's comparison
and the three regulators; the pion benchmark with and without explicit
breaking; physical spectral limits and reconstruction; the established
Newton record bounds; the valley-lifting bridge; and the two remaining
proof obligations. Historical claims stay tied to the held source
companions and the sibling `newtonlean` work. The present Planck paper
becomes a component of this synthesis. This working architecture does
not designate either open goal as solved.

The research order is deliberately bounded.

1. **Next constructive step: the $SU(3)$ small-volume bridge.** Develop
   the H3 estimate for the zero-mode Hamiltonian plus the even torus
   valley potential in the [Feshbach note](weak-coupling-feshbach-reduction.md).
   Seek an explicit lower bound
   $$E_{\rm small}(L)\ge
   (d_3-Cg(L)^{2/3})g(L)^{2/3}\frac{\hbar c}{L},\qquad d_3>0,$$
   with an explicit admissible coupling interval. State the operator,
   gauge sector and cutoff dependence. A confining potential or a
   positive ground energy alone does not establish the excitation gap;
   the first excited energy and the ground energy need comparison.
   Stop at one proved estimate, or the precise uncontrolled term in
   that estimate. Fixed-cutoff H3 would be a result, with its boundary
   retained; it would not close H1/H2 or T4 of the full mass-gap map.
2. **Newton necessity: construct the missing physical premise.** Use
   one explicit model of records and their composition, with calibrated
   lengths, impulses and time. Seek a refinement-independent positive
   cost from dynamical or optical premises that have their own
   justification. The deliverable is one implication with its full
   admissible class, or an explicit identification of the additional
   premise needed. A result starting from the canonical commutator or
   M3 belongs to the existing conditional branch. For the optical
   route, observable relative phase and a common action unit across
   probes must be established separately. Attainment of the existing
   disturbance bounds remains useful, but secondary to this task.
3. **Use the pion as a bounded test of a proposed mechanism.** Carry a
   non-singlet Ward identity and its nonzero residue through the chosen
   regulator, or state these as explicit inputs. Recover the zero-mass
   case and its small-mass lifting. This is one comparison section;
   a full fermionic-QCD construction is outside the active queue.
4. **Return the successful bridge to the field theory.** Determine
   whether the small-volume estimate survives eliminating nonzero
   modes with constants uniform in $a$, and then whether it supplies
   the order-one-coupling blocking estimate missing from H1. Preserve
   the chosen vacuum, physical scale and observable normalization.
   Reconstruction and nontriviality stay separate obligations; their
   order may interact with the estimates rather than follow a single
   irreversible chain.
5. **Integrate proved results into the final synthesis.** Replace the
   corresponding conditional statements only when their hypotheses
   are discharged. Complete the historical reading obligations in
   the Planck paper before submission. Keep the pion's role
   explanatory unless it actually changes one of the two proofs.

**Status on 2026-09-29 (pointers only).** The active gauge route since
2026-09-27 is the ultraviolet halving construction organized by the
[halving atlas](halving-atlas.md), rather than item 1's small-volume
bridge, which did not move this week. Its cell 2 now has one normalized
small-field step for $SU(2)$ in $1+2$, uniform in plane size
([small-field note](su2-midplane-small-field.md), §§13--14), the
covariant link-kernel estimate conditional on two local jet bounds (§20.3),
a reduction of the third response and an all-order polymer criterion
(§21), and a transcription to $SU(3)$ (§16; order-$t$ coefficients in the
[order-$t$ note](su2-midplane-order-t.md), §7b). For item 2, the missing
premise has an equivalent Newton-age form, Leibniz's law of continuity read
on records ([continuity note](leibniz-continuity-records.md)), and the cut
measure coincides with the record measure at every finite stage
([cut measure](cut-measure-newton.md), Proposition 7); the premise itself
remains open.

## 8. Consequence for STATE

The destination becomes a joint paper on survival under refinement,
with the Newton action necessity and pure $SU(3)$ continuum mass gap as
the two main goals. Pion physics, at zero and nonzero quark mass, is the
symmetry and limit-order benchmark requested by the user. The next
bounded constructive task is the H3 small-volume bridge; the Newton
necessity task retains the independent-premise requirement. The three
review batches of the existing Planck paper are complete; attainment
and its submission obligations remain open. This note is the live
plan, and adds no claim of a four-dimensional construction or an
independent derivation of $h>0$.
