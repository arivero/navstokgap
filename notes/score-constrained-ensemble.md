# Score-constrained ensembles and population transport

**Restart, 2026-10-01.** Sections 1–5 are written and internally checked:
the constrained action, compact-shape obstruction, positive non-Gaussian
forward orbit and nonlinear-copy recoil/tail test are established within
their stated models. The unfinished calculation is a dynamical
two-sheet realization on (18), retaining actual velocities and all
force/switch energy. Start with the proposed balance equations in the
[Claude handout](../research/handoffs/HANDOFF-2026-10-01-CLAUDE-NEWTON.md),
which are candidate calculations, then test unread labels. Physical
constraint enforcement and positive action selection have not been derived.

Restricting the ordinary action of two classical phase sheets to the
shared-score preparations gives the canonical Fisher field action
exactly. The restriction is not preserved by free Newtonian transport.
A separate population-transfer construction identifies its full
transport-conjugate action; bridge phase alone omits reservoir costs.
The resulting two-coordinate model satisfies continuity, but its shape
family fails the full field equation, even after adding Gaussian width.
An evolving Gaussian-polynomial construction instead gives an exact
positive, non-Gaussian solution for every forward time. A nonlinear
coordinate copy generates a shape outside every finite Hermite--Gaussian
family, with an exactly retained recoil-energy cost.

These are variational identities, an explicit field construction and
stated closure obstructions,
developed by GPT-6.1 Sol and GPT-6 Astra on 2026-10-01. They do not derive
a physical constraint mechanism, quantum recording, or positive action
necessity. The supplied parameter is $\kappa\ge0$; the field obstruction
below concerns $\kappa>0$. Proof status: written, internally checked.

## 1. What the classical sheet action supplies

Work on a connected position interval or the line. Require smooth
positive densities, finite displayed energies, and vanishing boundary
terms for the variations used below. A classical phase sheet has
position density $r$ and momentum $W_q$. Its canonical one-form and
free Hamiltonian are $\int W\,\delta r\,dq$ and
$\int rW_q^2/(2m)dq$, respectively, with $m>0$.

This one-form follows from the ordinary particle form. If material
coordinates $a$ carry fixed probability mass, $q=X(a)$, $r\,dq=da$, and
$v=\delta X\circ X^{-1}$ is a virtual displacement, then
$\delta r=-\partial_q(rv)$. Integration by parts gives
$$\int W_q(X(a))\delta X(a)da
 =\int rW_qv\,dq=\int W\,\delta r\,dq.\tag{1}$$
Fixed total mass makes a spatially constant shift of $W$ a gauge.
This is a smooth variational identity; no infinite-dimensional
well-posedness theorem is being assumed.

For two sheets of probability mass $1/2$, introduce the constraint
$$r_\sigma=\rho/2,\qquad
W_\sigma=S+\kappa\sigma\log(\rho/\rho_{\rm ref}),\qquad
\sigma\in\{+1,-1\}.\tag{2}$$
Here $\rho$ is normalized, $S$ has action units, and the positive
constant $\rho_{\rm ref}$ only makes the logarithm dimensionless.
Changing it adds sheetwise constants and changes no momentum. Formula
(2) is the field version of the supplied positive classical preparation
in [the recording note, §8.22](sed-closure-under-recording.md#822-a-shared-score-sign-realizes-copying-but-fails-two-completion-tests).

**Proposition 1 (exact constrained action).** Pulling the two-sheet
one-form and energy back to (2) gives
$$\begin{aligned}
\Theta&=\sum_\sigma\int W_\sigma\delta r_\sigma\,dq
       =\int S\delta\rho\,dq,\\
\mathcal H&=\sum_\sigma\int\frac{r_\sigma W_{\sigma,q}^2}{2m}dq
 =\int\frac{\rho S_q^2}{2m}dq+\frac{\kappa^2}{2m}I(\rho),\\
I(\rho)&=\int\frac{\rho_q^2}{\rho}dq.
\end{aligned}\tag{3}$$
The first identity cancels the two score signs; the second expands the
two squares. Thus variation of the *restricted* action
$\int[\int S\rho_t\,dq-\mathcal H]dt$ yields
$$\rho_t=-\partial_q(\rho S_q/m),\qquad
S_t=-\frac{S_q^2}{2m}
 +\frac{2\kappa^2}{m}\frac{(\sqrt\rho)_{qq}}{\sqrt\rho}.\tag{4}$$
No further canonical-field bracket is needed after adopting the
constraint and restricted variation. The Fisher modification is
established prior art [@HallReginatto2002; reading: passages pp. 3--8,
especially the classical action (4) and modified action/equations
(17)--(18); [source companion](../docs/batches/B09/Hall_Reginatto_2002.md)].
The calculation here identifies which correlated sheet restriction
produces that action and tests its invariance.

**Why this is not an invariant reduction.** Unrestricted classical
sheet continuity gives, on (2),
$$\partial_t(r_+-r_-)
 =-\frac\kappa m\partial_q^2\rho.\tag{5}$$
For $\kappa>0$, no strictly positive normalized density on the whole
line has $\rho_{qq}\equiv0$: an affine function cannot have those
properties. Consequently every such constrained preparation departs
from equal sheet densities immediately somewhere. Restricted variation
and ordinary free sheet transport are different dynamics. Additional
constraint reactions or state changes are required, as the exact
Gaussian switching test in [§8.23](sed-closure-under-recording.md#823-a-stationary-switching-process-repairs-the-gaussian-marginal)
also demonstrates. In particular (4)'s current uses the mean momentum
$S_q$; it does not give both physical sheet velocities $W_{\sigma,q}/m$
without further dynamics.

On connected positive support the labeled sheet momenta determine $S_q$
and hence $S$ up to a common constant. At exact vacuum, separate constants
on disconnected components become invisible to the ordinary physical
phase-space measure. This construction cannot carry them into a vacuum
limit merely by declaring them canonical data.

## 2. Population transport includes the reservoirs

Let $h_L,h_R$ be nonnegative smooth normalized bumps with compact,
ordered, disjoint supports. Between them fix a bridge
$B=[q_L,q_R]$. Choose a smooth positive normalized density $\rho_0$ with
finite Fisher information. Put
$$\begin{aligned}
h&=h_R-h_L,&\rho_w&=\rho_0+wh,\\
G(q)&=\int_{-\infty}^{q}(h_L-h_R)(y)dy,&
M(w)&=\int\frac{G(q)^2}{\rho_w(q)}dq,\\
R_B&=\int_B\frac{dq}{\rho_0(q)}.&&
\end{aligned}\tag{6}$$
Here $w$ is probability mass transferred from left to right,
$0\le G\le1$, $G=1$ on $B$, and $G$ vanishes outside the reservoirs
and their connector.
If $K$ is their compact enclosing interval, $c=\min_K\rho_0>0$ and
$H=\|h\|_\infty>0$, then $|w|<c/(2H)$ ensures
$\rho_w\ge c/2$ on $K$. Thus all terms in (6) are finite, with
$M(w)\le2|K|/c$, and smooth in this $w$ range.

Vanishing exterior flux and continuity uniquely require
$j(q)=\dot w\,G(q)$, because $\partial_qj=-\partial_t\rho_w$.
The corresponding total transport kinetic energy is
$mM(w)\dot w^2/2$. Both $M$ and $R_B$ have length-squared units.
Smooth reservoir transport contributes positively, so $M(w)>R_B$.

**Proposition 2 (continuity-compatible canonical family).** Define an
action field, up to a common constant, by
$$S_q(q;w,P)=\frac{P G(q)}{M(w)\rho_w(q)}.\tag{7}$$
The variable $P$ has action units; it is not a point-particle momentum.
Then
$$\begin{aligned}
\Theta&=\int S\delta\rho_w\,dq=P\,dw,\\
H(w,P)&=\frac{P^2}{2mM(w)}+\frac{\kappa^2}{2m}I(\rho_w),\\
\dot w&=\frac{P}{mM(w)},&
\dot P&=\frac{P^2M'(w)}{2mM(w)^2}
       -\frac{\kappa^2}{2m}\frac{dI(\rho_w)}{dw}.
\end{aligned}\tag{8}$$
These local reduced Hamilton equations preserve $H$ while $w$ remains
in the positive-density range and satisfy the ambient continuity
equation exactly.

*Proof.* Since $h=-G_q$, integration by parts yields
$\int S h\,dq=\int S_qG\,dq=P$. The phase energy in (3) is
$P^2/(2mM)$, proving the Hamiltonian and its equations. Their first
equation gives $\rho_wS_q/m=\dot wG$, the required current. $\square$

In this family the actual bridge action difference is
$$\Phi_B=S(q_R)-S(q_L)=\frac{R_B}{M(w)}P.\tag{9}$$
Thus $\Phi_B$ generally differs from the population-conjugate action
$P=\int S h_Rdq-\int S h_Ldq$. The latter is a reservoir-weighted
phase-action difference. Replacing it by bridge endpoint phases omits
the reservoir motion. In coordinates $(w,\Phi_B)$ the canonical
two-form has coefficient $M(w)/R_B$, rather than one.

For a fixed bridge density the exact dual identities are
$$E_{{\rm transport},B}=\frac{mJ^2R_B}{2},\qquad
\inf E_{{\rm phase},B}=\frac{\Phi_B^2}{2mR_B},\qquad
J=\frac{\Phi_B}{mR_B}.\tag{10}$$
The phase infimum is [the bridge lemma, (131)](sed-closure-under-recording.md#821-the-exact-energy-of-a-phase-bridge-and-its-cut-law),
written with $S$ instead of $\hbar\theta$; it is attained in the stated
weighted $H^1$ class. The last identity makes the two energies equal.
A low-density connector makes a fixed phase difference cheap and a
fixed population flux expensive. It selects no absolute action scale.

The costs add over arbitrary spatial cuts, because both integrals of
$1/\rho$ and of $G^2/\rho$ add. This is an exact spatial transport
identity, not Newton's temporal cell action. In the positive-tail family
of recording (133), $R_B$ grows as $\epsilon^{-2}$. If reservoir costs
additionally obey $M-R_B\le C$ uniformly, then
$|P-\Phi_B|\le |P|C/R_B$ and the bridge becomes asymptotically dominant.
That extra bound must be checked; exact vacuum is not such a check.

## 3. Continuity does not close the full field equation

Equations (8) are exact for the restricted model. They do not imply
that its fixed density family is invariant under (4)'s Hamilton--Jacobi
equation. For a Gaussian base $\rho_A=N(0,A)$ and initial $w=P=0$,
the full equation gives
$$\partial_tS_q=\frac{\kappa^2 q}{mA^2}.\tag{11}$$
The family (7) instead permits only a multiple of $G/\rho_A$ at that
initial time. It vanishes outside a compact interval, whereas (11)
does not. This is an immediate nonzero transverse term for $\kappa>0$.
It cannot be removed by a spatially constant action gauge.

Adding Gaussian width supplies the missing global quadratic phase at
$w=0$. The next calculation tests whether that repairs closure for
nonzero population transfer.

**Proposition 3 (a fixed compact transfer shape cannot close).** Fix
$m,\kappa,A>0$ and a nonzero $h\in C_c^\infty(\mathbb R)$ with
$\int h=0$. The density family
$\rho_{A,w}=\rho_A+wh$, allowing width variation and sufficiently small
positive and negative $w$, cannot be locally invariant under (4) while
including zero-phase-gradient states for every such $w$, satisfying
continuity with vanishing exterior flux, and having twice differentiable
parameter trajectories. The same obstruction persists with Gaussian
mean motion allowed. The claim concerns an open family of preparations,
not all finite-dimensional models.

*Proof.* Set $r=\rho_A$ and $G=-\int_{-\infty}^q h$, so $G$ is
smooth and compactly supported. The integrated density tangents for
width and transfer are $G_A=qr/(2A)$ and $G$. At an initially zero
phase gradient, continuity first gives $\dot A=\dot w=0$.
Differentiating it and using (4) requires
$$\begin{aligned}
\rho_wF_w&=c_A(w)G_A+c_w(w)G,\\
F_w&=\frac{2\kappa^2}{m}\partial_q
      \frac{(\sqrt{\rho_w})_{qq}}{\sqrt{\rho_w}},
\qquad c_A=m\ddot A,\quad c_w=m\ddot w.
\end{aligned}\tag{12}$$
Outside the compact supports, $\rho_w=r$ and
$F_w=\kappa^2q/(mA^2)$; hence
$c_A(w)=2\kappa^2/(mA)$ for every small $w$. At $w=0$ this already
matches the full expression, giving $c_w(0)=0$.
Evaluation at any point with $G\ne0$ makes $c_w(w)$ smooth, since the
left side is smooth while $\rho_w>0$.

Put $u=h/r$. Differentiating the square-root ratio gives
$\delta[(\sqrt\rho)_{qq}/\sqrt\rho]
=(u''-qu'/A)/2$. Retaining the variation of the density multiplier in
(12), the necessary linearized identity is
$$u'''-\frac qA u''-\frac{u'}A+\frac q{A^2}u=cg,
\qquad g=G/r,\qquad c=mc_w'(0)/\kappa^2.\tag{13}$$
Since $G'=-h$, one has $u=qg/A-g'$. Substitution yields
$$\begin{aligned}
-g''''+\frac{2q}{A}g'''
 +\left(\frac4A-\frac{q^2}{A^2}\right)g''
 -\frac{4q}{A^2}g'\\
 +\left(\frac{q^2}{A^3}-\frac1{A^2}\right)g&=cg.
\end{aligned}\tag{14}$$
The function $g$ is smooth and compactly supported because $r>0$.
All four initial data vanish at a point outside its support. Uniqueness
for this regular fourth-order linear ODE forces $g\equiv0$, hence
$h=-G'\equiv0$, a contradiction. Allowing the Gaussian mean adds a
term proportional to $r$ in (12); tail matching forces its coefficient
to zero and leaves the same contradiction. $\square$

The zero-phase-gradient and continuity assumptions are essential to the
initial tangency test. The theorem permits isolated states, shapes
depending on parameters or time, and other finite-dimensional families.
It specifically rules out treating a fixed compact transfer bump plus
Gaussian width as an exact free Fisher evolution. Generated shape
information cannot be hidden inside that projection.

## 4. An exact positive nonlinear shape evolution

The compact-shape obstruction permits evolving tails. The following
construction solves (4) exactly within its supplied dynamics. It also
identifies a limitation of the first mode test: the linearized mode is
a width/phase tangent, although its finite-amplitude completion is not
Gaussian.

For $\kappa>0$, introduce the auxiliary algebraic variable
$$\psi=\sqrt\rho\,e^{iS/(2\kappa)},\qquad
\psi_t=\frac{i\kappa}{m}\psi_{qq}.\tag{15}$$
The second equation is equivalent to (4) on positive density: its real
part gives $\rho_t=-\partial_q(\rho S_q/m)$ and its imaginary part
gives (4)'s second equation after differentiating the displayed product.
It is a change of variables in the adopted field equations, not an
independent physical propagation premise.

Fix $A>0$ with length-squared units and put
$$\begin{aligned}
u&=\frac{\kappa t}{mA},&B&=A(1+u^2),&s&=\arctan u,&z&=q/\sqrt B,\\
\psi&=B^{-1/4}e^{iuq^2/(4B)}\chi(z,s),&&
i\chi_s&=\left(-\partial_z^2+\frac{z^2}{4}\right)\chi.
\end{aligned}\tag{16}$$
For completeness, $a=\dot B/(2B)=\kappa u/(mB)$ and
$b=\dot s=\kappa/(mB)$ obey $\dot a+a^2=b^2$.
Differentiating the second line cancels the terms
$-a\chi/2$ and $-az\chi_z$ on both sides of (15). The remaining
quadratic phase coefficient is $bz^2/4$, giving the last equation
in (16). Thus no propagator formula is assumed.

Let
$$\begin{aligned}
\phi_0(z)&=(2\pi)^{-1/4}e^{-z^2/4},&
H_2(z)&=(z^2-1)/\sqrt2,&\phi_2&=H_2\phi_0,\\
\psi_n(q,t)&=B^{-1/4}e^{iuq^2/(4B)}
 e^{-i(n+1/2)s}\phi_n(z),&&n\in\{0,2\}.
\end{aligned}\tag{17}$$
Direct differentiation gives the oscillator eigenvalues $1/2$ and
$5/2$ for $\phi_0$ and $\phi_2$. Gaussian moments give unit norms
and orthogonality. Hence both displayed functions solve (15).

**Proposition 4 (positive forward completion).** For
$0<\epsilon<\sqrt2$, the normalized combination
$\psi_\epsilon=(\psi_0+i\epsilon\psi_2)/\sqrt{1+\epsilon^2}$
gives a smooth solution of (4) on the whole line for every $t\ge0$:
$$\begin{aligned}
\rho_\epsilon(q,t)&=\rho_G(q,t)
 \frac{1+2\epsilon\sin(2s)H_2(z)+\epsilon^2H_2(z)^2}
      {1+\epsilon^2},\qquad \rho_G=N(0,B),\\
S_\epsilon(q,t)&=\kappa\left(\frac{uq^2}{2B}-s\right)
 +2\kappa\arctan\frac{\epsilon\cos(2s)H_2(z)}
                          {1+\epsilon\sin(2s)H_2(z)},\\
\frac{\rho_\epsilon}{\rho_G}&\ge
 \frac{(1-\epsilon/\sqrt2)^2}{1+\epsilon^2}>0.
\end{aligned}\tag{18}$$
The lower bound is relative to the Gaussian envelope; it supplies no
absolute density floor at infinity. All displayed energies and moments
are finite. The density is non-Gaussian for every $\epsilon>0$.

*Proof.* Factoring out $\psi_0$ leaves
$F=1+\epsilon[\sin(2s)+i\cos(2s)]H_2$.
For forward time, $0\le s<\pi/2$, so $\sin(2s)\ge0$;
$H_2\ge-1/\sqrt2$ gives
$\Re F\ge1-\epsilon/\sqrt2>0$. Thus the arctangent in (18)
is one globally smooth phase, and $|F|^2$ gives its density and bound.
Orthogonality gives exact normalization. Gaussian decay times a
polynomial, with this strictly positive denominator, justifies the
derivatives, moments and integrations by parts. The nonconstant quartic
factor cannot be absorbed into a different Gaussian width. Equations
(15)--(17) prove the field equations. $\square$

The conserved energy and first two even moments are explicitly
$$\begin{aligned}
E&=\frac{\kappa^2(1+5\epsilon^2)}{2mA(1+\epsilon^2)},&E Q&=0,\\
E Q^2&=B\frac{1+2\sqrt2\epsilon\sin(2s)+5\epsilon^2}
                  {1+\epsilon^2},\\
E Q^4&=B^2\frac{3+12\sqrt2\epsilon\sin(2s)+39\epsilon^2}
                    {1+\epsilon^2}.
\end{aligned}\tag{19}$$
Indeed (3)'s energy equals $2\kappa^2\int|\psi_q|^2/m$.
Integration by parts in (15) makes its time derivative zero. At time
zero the imaginary coefficient cancels the derivative cross term, and
$\int|\phi_0'|^2=1/4$, $\int|\phi_2'|^2=5/4$, giving $E$.
For the moments use $E_0z^2=1$, $E_0z^2H_2=\sqrt2$,
$E_0z^2H_2^2=5$, and $E_0z^4=3$,
$E_0z^4H_2=6\sqrt2$, $E_0z^4H_2^2=39$.
Here $E_0$ integrates against $\phi_0^2$.
The variance has second derivative $4E/m$, as required by the
free field virial identity; the linear-in-time term records the initial
position/current correlation.

At first order in $\epsilon$ the paired tangents are
$$\delta\rho=2\rho_G\sin(2s)H_2,\qquad
\delta S=2\kappa\cos(2s)H_2.\tag{20}$$
They are width and quadratic-phase tangents, not an independent linear
population-transfer mode. The result is their exact non-Gaussian
nonlinear completion. It carries evolving tails rather than a fixed
compact transfer bump. Restricting this one solution to any time
partition is exactly consistent; no general continuum existence theorem
or separated-packet apparatus has been constructed.

Forward time matters: at $s=-\pi/4$ the factor is
$1-\epsilon H_2$ and has real zeros. Thus (18) does not define a
globally positive real-field family under all backward evolution.
For fixed $t$, $\kappa\downarrow0$ gives a stationary non-Gaussian
density, $S\to0$, and $E\to0$. The construction leaves the zero
branch admissible.

## 5. Recording generates a shape outside the finite mode family

Free completion must survive an actual intervention. Couple a body
state $(\rho,S)$ from (18), or any positive state with the following
finite integrals, to a pointer configuration $Z\sim N(0,C)$, $C>0$,
with zero pointer action. Prepare the joint momenta with the shared
score sign (2), so the full phase-space law need not factor. Apply
the canonical copy (137) in [the recording note](sed-closure-under-recording.md#822-a-shared-score-sign-realizes-copying-but-fails-two-completion-tests),
with smooth length-valued $f(q)$. In the algebraic variables its
pullback is exactly
$$\Psi'(q,z)=\psi(q)\eta_C(z-f(q)),\qquad
\eta_C(y)=(2\pi C)^{-1/4}e^{-y^2/(4C)}.\tag{21}$$
The complete pointer-coordinate record $R=r$ gives
$$\rho_r(q)=\frac{\rho(q)e^{-(r-f(q))^2/(2C)}}
 {\int\rho(y)e^{-(r-f(y))^2/(2C)}dy},\qquad
S_r(q)=S(q),\tag{22}$$
up to a record-dependent constant action. These are the exact
conditional fields; the sign stays fair and independent of coordinates.

**Proposition 5 (generated shape and retained recoil).** For
$f(q)=q^2/\ell$ with fixed length $\ell>0$, every posterior (22)
from (18) lies outside every finite Hermite--Gaussian expansion,
even allowing a different Gaussian mean, width and quadratic phase.
The mean body-energy increase is nevertheless exact:
$$\begin{aligned}
\Delta E_{\rm body}
 &=\frac{\kappa^2}{2mC}E_\rho[f'(Q)^2]
 =\frac{2\kappa^2}{mC\ell^2}E_\rho Q^2,\\
E_R I(\rho_R)-I(\rho)&=\frac1C E_\rho[f'(Q)^2].
\end{aligned}\tag{23}$$
All these posterior densities are smooth and positive, with finite
Fisher information and body energy. The finite-mode failure is a
failure of shape closure, not a violation of the conditional covariance
bound (138).

*Proof.* The logarithmic posterior tail obeys
$\lim_{|q|\to\infty}q^{-4}\log\rho_r(q)
=-1/(2C\ell^2)$. A nonzero finite Hermite expansion over any Gaussian
envelope has polynomial-times-Gaussian density and the same limit is
zero. This proves the stated closure failure, without ruling out
other finite models. For the energy differentiate (21):
$\partial_q\Psi'=\psi_q\eta_C-f'\psi\eta_C'$.
Integration in $z$ kills the cross term since
$\int\eta_C\eta_C'=0$, and
$\int|\eta_C'|^2=1/(4C)$. Multiplication by $2\kappa^2/m$
gives (23)'s first line, which is also the actual canonical recoil
energy under (2). For its second line, the conditional score is
$\partial_q\log\rho+(r-f)f'/C$; conditional on $q$,
$r-f$ has mean zero and variance $C$. Expanding its square proves
the identity. Quartic decay proves the stated posterior integrability.
$\square$

If the coordinate record becomes unread, the marginal position density
and mean current return to the original $\rho$ and $\rho S_q/m$.
The actual body energy keeps the increment (23). Resetting its momenta
to that marginal density's two score sheets would erase precisely
this energy. Here every conditional phase gradient is the same, so
there is no additional current-variance excess; for general branches
both excesses in recording (135) must be retained. The pointer energy
is unchanged by this impulsive shear. The extra body energy therefore
requires work from its actuator; a closed energy-supplying apparatus
has not been derived. Full conjugate access remains the distinct
terminal escape (140). None of these formulas selects $\kappa>0$.

## 6. Consequence for STATE

The canonical Fisher structure follows from a specified restriction of
ordinary classical sheet action; physical preservation of that restriction
remains open. Population memory must carry its full transport-conjugate
action, including reservoirs, before taking a weak-bridge limit.
The fixed compact-transfer family fails even with Gaussian width.
Equations (18)--(20) instead complete a width/phase tangent to an exact
positive non-Gaussian forward orbit. A nonlinear record immediately
generates a quartic exponential tail outside the finite mode family,
with its unread energy fixed by (23). Next lemma: carry the full
generated density/phase and retained record labels through a dynamical
constraint realization, first on this non-Gaussian orbit. It must keep
the actual velocities and force/switch energy exchange, rather than
project back to finite modes or reset an unread marginal. Physical
apparatus closure and the two-unread-width test remain obligations.
Reject a projected residual counted as exact closure, bridge phase used
as population momentum without reservoir costs, or an unexcluded zero
branch presented as positive action necessity.
