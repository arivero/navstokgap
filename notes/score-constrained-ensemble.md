# Score-constrained ensembles and population transport

**Status, 2026-10-01 (night).** Sections 1–5 (Sol/Astra) give the
constrained action, compact-shape obstruction, positive non-Gaussian
forward orbit and nonlinear-copy recoil/tail test. Sections 6–8 (Claude
Fable) derive the two-sheet dynamical realization on any positive
solution and on (18): balance, force, impulses, exact mean energy
cancellation and all-time nonexplosion (Propositions 7–8), identify its
controller with the field pair within this sheet architecture
(Proposition 9), pass the two-unread-width test with branch controllers
against a marginal-score controller (Proposition 11), and state closure
under coordinate copies at every $\kappa\ge0$ with its protocol
hypothesis (Proposition 12). Refereed by GPT-6.1 Sol (Codex) on
2026-10-01: Propositions 6 and 8 accepted; 7, 9, 11 and 12 refined; the
former Corollary 10 (no finite controller) rejected by a
finite-parameter counterexample and replaced; corrections applied.
Verdict (§8): the realization is a stochastic pilot-wave representation
of the supplied law; composition closure cannot select $\kappa$, so the
route from apparatus closure to positive action is closed, while the
impossibility of every other realization and literal full-history
storage are not claimed. Physical constraint enforcement and positive
action selection have not been derived.

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

## 6. The two-sheet realization on any positive solution

The handout's candidate balance equations are now derived and checked
on every smooth positive solution of (4), with the explicit orbit (18)
as the test case. From here on $v=S_q/m$ is the mean velocity and
$$d=\frac{\kappa}{m}\partial_q\log\rho,\qquad
p_\sigma=m(v+\sigma d),\qquad\sigma\in\{+1,-1\},\tag{24}$$
so that $p_\sigma=W_{\sigma,q}$ in (2). A smooth external potential
$U(q,t)$ is allowed: it adds $-U$ to the right side of (4)'s second
equation and $\int\rho U\,dq$ to $\mathcal H$. The two sheet velocities
$v\pm d$ are the forward and backward mean velocities of Nelson's
stochastic mechanics with diffusion coefficient $\kappa/m$
[@Nelson1966; reading: abstract, as in the
[stochastic route](stochastic-route-velocitas-ultima.md)]. The
realization below replaces his Brownian motion by one sign that switches
at a finite rate, as §8.23 of the recording note did for the Gaussian.
The proofs are written derivations by Claude Fable (2026-10-01),
checked against (146)--(149); they are unrefereed.

**Proposition 6 (sheet field equations).** On a smooth positive
solution of (4) with potential $U$,
$$\begin{aligned}
v_t+vv_q&=-\frac{U_q}{m}+\frac\kappa m\,d_{qq}+d\,d_q,\\
d_t+v\,d_q+d\,v_q&=-\frac\kappa m\,v_{qq}.
\end{aligned}\tag{25}$$

*Proof.* Put $L=\log\rho$, so $(\sqrt\rho)_{qq}/\sqrt\rho
=\tfrac12L_{qq}+\tfrac14L_q^2$. Differentiating (4)'s second equation
in $q$ and dividing by $m$ gives
$v_t=-vv_q-U_q/m+(\kappa^2/m^2)(L_{qqq}+L_qL_{qq})$, which is the
first line because $(\kappa/m)d_{qq}=(\kappa^2/m^2)L_{qqq}$ and
$dd_q=(\kappa^2/m^2)L_qL_{qq}$. Continuity gives $L_t=-v_q-vL_q$;
its $q$-derivative times $\kappa/m$ is the second line. $\square$

**Proposition 7 (two-sheet realization: balance, force, energy).** Let
$(Q_t,\Sigma_t)$ be a process on $\mathbb R\times\{\pm1\}$ with
velocity $\dot Q=v+\Sigma d$ between sign jumps, rate
$\lambda_\sigma(q,t)$ from $\sigma$ to $-\sigma$, and carried momentum
$P_t=p_{\Sigma_t}(Q_t,t)$.

(i) *Balance.* With initial law $\rho(q,0)/2$ for each sign, a
conservative forward evolution with unique paths preserves the law
$\rho(q,t)/2$ at every time iff
$$\lambda_--\lambda_+=\frac\kappa m\frac{\rho_{qq}}{\rho};\qquad
\lambda_\sigma=\frac\kappa m\Big(-\sigma\frac{\rho_{qq}}{\rho}\Big)_+
\ \text{is the minimal nonnegative choice.}\tag{26}$$
The balance identity alone establishes neither existence nor
nonexplosion; Proposition 8 does so for the explicit orbit.

(ii) *Force and impulse.* Between jumps $P$ changes by
$$F_\sigma=-U_q+\kappa d_{qq}+2m\,d\,d_q-\sigma\kappa v_{qq}
=-\partial_qV_\sigma,\qquad
V_\sigma=U-\frac{\kappa^2}{m}\frac{\rho_{qq}}{\rho}
+\sigma\frac\kappa m S_{qq},\tag{27}$$
and at a jump $\sigma\to-\sigma$ by
$\Delta p=-2\sigma md=-2\sigma\kappa\,\partial_q\log\rho$. The symmetric
part of the sheet potential is the rate difference in action units:
$\tfrac12(V_++V_-)-U=-\kappa(\lambda_--\lambda_+)$.

(iii) *Energy.* With $K_\sigma=p_\sigma^2/(2m)$, pathwise
$dK/dt=F_\Sigma\dot Q$ between jumps and $\Delta K=-2\Sigma\,mvd$ at a
jump. In the mean, the $\kappa$-dependent part of the force and the
jumps have powers
$$\begin{aligned}
W_F^{\kappa}&=\int\rho\,[\kappa v d_{qq}+2mv d d_q-\kappa d v_{qq}]\,dq,\\
W_J&=\sum_\sigma\int\frac\rho2\lambda_\sigma(K_{-\sigma}-K_\sigma)\,dq
 =\kappa\int v\,d\,\rho_{qq}\,dq,\qquad W_F^{\kappa}+W_J=0,
\end{aligned}\tag{28}$$
at every time, so that $\frac{d}{dt}E[K]=-\int\rho vU_q\,dq
=d\mathcal H_{\rm kin}/dt$. Individual trajectories exchange energy
with the actuator and at jumps; the ensemble mean does not.

*Proof.* (i) The forward equation for the density $n_\sigma$ of
$(Q,\Sigma=\sigma)$ is
$\partial_tn_\sigma+\partial_q(n_\sigma(v+\sigma d))
=-\lambda_\sigma n_\sigma+\lambda_{-\sigma}n_{-\sigma}$. With
$n_\sigma=\rho/2$ and continuity, the left side is
$\tfrac\sigma2\partial_q(\rho d)=\tfrac{\sigma\kappa}{2m}\rho_{qq}$
and the right side is $\tfrac\rho2(\lambda_{-\sigma}-\lambda_\sigma)$.
The two signs give one equation and its negative. Given a difference,
the nonnegative solutions are the displayed pair plus a common
nonnegative rate.
(ii) Along the sheet flow,
$dP/dt=m\,[\partial_t+(v+\sigma d)\partial_q]\,(v+\sigma d)
=m[(v_t+vv_q)+\sigma(d_t+vd_q+dv_q)+dd_q]$; insert (25). For the
potential, $\kappa d_q+md^2=(\kappa^2/m)(L_{qq}+L_q^2)
=(\kappa^2/m)\rho_{qq}/\rho$ and $\kappa v_q=(\kappa/m)S_{qq}$.
The jump changes $\sigma d$ to $-\sigma d$.
(iii) The pathwise statements restate (ii). For the mean, apply the
generator to $g=K_\sigma(q,t)$: $\partial_tg+(v+\sigma d)\partial_qg
=(v+\sigma d)F_\sigma$, and
$K_{-\sigma}-K_\sigma=-2\sigma mvd$, so
$W_J=\int\rho\,mvd(\lambda_--\lambda_+)\,dq=\kappa\int vd\rho_{qq}\,dq$.
The identity $W_F^\kappa+W_J=0$ is verified directly: with
$\rho d=(\kappa/m)\rho_q$, $\rho_{qq}=\rho(L_{qq}+L_q^2)$ and
$\rho_{qqq}=\rho(L_{qqq}+3L_qL_{qq}+L_q^3)$,
$$W_F^\kappa+W_J=\frac{\kappa^2}{m}\int\big[
 v\rho_{qqq}-\rho_qv_{qq}\big]dq=0$$
after two integrations by parts with vanishing boundary terms. Since
$E[K]=\int\rho\,\tfrac m2(v^2+d^2)\,dq=\mathcal H_{\rm kin}$, the last
statement is the energy balance of (4) with potential. $\square$

On the Gaussian (145) one has $v=ax$, $d=-bx$, $d_{qq}=v_{qq}=0$ and
$\rho_{qq}/\rho=(z^2-1)/B$, so (26)--(28) reduce to (146), (148) and
(149): $F_\sigma=2mb^2x=2\kappa^2x/(mB^2)$,
$\lambda_+=b(1-z^2)_+$ and $W_J=-2mab^2B$. Three independent
features are worth stating. The force is sign-dependent exactly through
$-\sigma\kappa v_{qq}$, so it is sign-independent iff the mean velocity
is affine; the Gaussian hid this. The force is a gradient of a potential
that contains $\rho_{qq}/\rho$ rather than the quantum potential
$-(2\kappa^2/m)(\sqrt\rho)_{qq}/\sqrt\rho$; the two differ by
$-\tfrac m2d^2$, the sheet kinetic excess. And for a state with zero
mean current ($v\equiv0$, for instance a trapped ground state) both
mean powers in (28) vanish and every jump has $\Delta K=0$, although
individual trajectories still exchange energy with the actuator: for
$\rho=N(0,A)$ held by $U=\kappa^2q^2/(2mA^2)$, with $S_t=-\kappa^2/(mA)$,
one has $F_\sigma=\kappa^2q/(mA^2)$ and velocity $-\sigma\kappa q/(mA)$,
so $F_\sigma\dot Q=-\sigma\kappa^3q^2/(m^2A^3)\neq0$ for $q\neq0$. With a
time-dependent $U$ the total energy obeys
$d\mathcal H/dt=\int\rho U_t\,dq$.

**Proposition 8 (nonexplosion on the explicit orbit, all forward
time).** For (18) write $z=q/\sqrt B$, $s=\arctan u$, and
$P(z,s)=1+2\epsilon\sin(2s)H_2+\epsilon^2H_2^2=|F|^2$, the factor of
Proposition 4, so $\rho=\rho_GP/(1+\epsilon^2)$. Then
$$\partial_z\log P=\frac{2\sqrt2\,\epsilon z\,(\sin2s+\epsilon H_2)}{P},
\qquad
\partial_z\operatorname{Arg}F=\frac{\sqrt2\,\epsilon z\cos2s}{P},\tag{29}$$
and in the clock $s$ the sheet motion and rates read
$$\frac{dz}{ds}=-\sigma z+r_\sigma(z,s),\quad
r_\sigma=2\partial_z\operatorname{Arg}F+\sigma\partial_z\log P,\quad
\frac{\lambda_\sigma}{b}=\Big(-\sigma B\frac{\rho_{qq}}{\rho}\Big)_+
\le c_\epsilon(1+z^2),\tag{30}$$
with $|r_\sigma|\le r_\epsilon$ and $c_\epsilon$ finite constants
depending only on $\epsilon$; explicitly
$|\partial_z\log P|\le\max\{4\sqrt2\epsilon/(1-\epsilon/\sqrt2),8/3\}$.
Hence $|z(s)|\le(|z_0|+\tfrac\pi2r_\epsilon)e^{\pi/2}$ for all
$t\ge0$, the hazard integrated over the entire forward half-line is at
most $\tfrac\pi2c_\epsilon(1+\sup z^2)<\infty$ given $Z_0$, the sign
jumps are almost surely finitely many on $[0,\infty)$, and the process
of Proposition 7 exists for all forward time with law (18). The orbit is
even in $q$, so $v(0,t)=d(0,t)=0$: the origin is invariant for both
sheets and no trajectory crosses it.

*Proof.* With $H_2'=\sqrt2z$, $P_z=2\epsilon H_2'(\sin2s+\epsilon H_2)$
gives the first formula of (29). For the phase,
$\partial_z\operatorname{Arg}F=(\operatorname{Re}F\,\partial_z\operatorname{Im}F
-\operatorname{Im}F\,\partial_z\operatorname{Re}F)/P$ with
$\operatorname{Re}F=1+\epsilon\sin(2s)H_2$,
$\operatorname{Im}F=\epsilon\cos(2s)H_2$; the products of $H_2H_2'$
cancel and leave $\epsilon\cos(2s)H_2'/P$. For the bound, note
$P=(\sin2s+\epsilon H_2)^2+\cos^22s$, so
$|\sin2s+\epsilon H_2|\le\sqrt P$ and
$|\partial_z\log P|\le2\sqrt2\epsilon|z|/\sqrt P$. For $|z|\le2$ use
$P\ge(1-\epsilon/\sqrt2)^2$ from (18). For $|z|\ge2$, $H_2\ge0$ and
$\sin2s\ge0$ give $P\ge\epsilon^2H_2^2$ with
$H_2\ge3z^2/(4\sqrt2)$, so $|\partial_z\log P|\le16/(3|z|)\le8/3$.
The same two regions bound $\partial_z\operatorname{Arg}F$ and
$\partial_z^2\log P=P_{zz}/P-(P_z/P)^2$, where
$P_{zz}=2\sqrt2\epsilon(\sin2s+\epsilon H_2+\sqrt2\epsilon z^2)$.
Now $S_q=\kappa uq/B+2\kappa B^{-1/2}\partial_z\operatorname{Arg}F$
and $\partial_q\log\rho=B^{-1/2}(-z+\partial_z\log P)$, so with
$a=ub$,
$v=\sqrt B\,(az+2b\,\partial_z\operatorname{Arg}F)$ and
$d=\sqrt B\,b\,(-z+\partial_z\log P)$. Then
$\dot z=(v+\sigma d)/\sqrt B-az
=b[-\sigma z+2\partial_z\operatorname{Arg}F+\sigma\partial_z\log P]$,
and $ds=b\,dt$ gives (30). Also
$B\rho_{qq}/\rho=(-1+\partial_z^2\log P)+(-z+\partial_z\log P)^2$,
which is bounded by $c_\epsilon(1+z^2)$. Grönwall on
$(|z|)'\le|z|+r_\epsilon$ gives the growth bound; the clock runs only
to $s=\pi/2$ over the whole physical half-line. Conditional on $Z_0$,
successive hazard clocks are dominated by one Poisson clock of finite
rate, as in the proof of Proposition 21 of the recording note, which
proves existence and nonexplosion; uniqueness of the forward solution
with locally bounded rates identifies the law as $\rho/2$ per sign.
Evenness of (18) in $q$ gives the invariance of the origin. $\square$

Two limits of this realization are explicit. It needs $\rho>0$:
at a node, $d$ and the rates diverge, and (18) is positive only
forward in time. And it supplies no crossing, exactly as (145)--(148)
did: packet crossing or relative-phase reunion cannot be tested on an
even orbit. The posterior states (22) with the quadratic copy have
$d\sim-(2\kappa/mC\ell^2)q^3$ at $t=0$, so the $-$ sheet moves outward
with cubic speed and would escape in finite time; its rate
$\lambda_-\sim(m/\kappa)(2\kappa/mC\ell^2)^2q^6$ has infinite integrated
hazard before escape, so a switch to the inward $+$ sheet occurs almost
surely first. Nonexplosion over an interval for these tails needs the
evolved fields and is not claimed here.

## 7. The controller is the field pair

The realization needs four controller functions, $F_\pm(q,t)$ and
$\lambda_\pm(q,t)$. Proposition 22 showed that they cannot be a
preparation-independent law on $(t,q,p,\sigma)$. The following
identification says exactly what they are.

**Proposition 9 (controller identification).** Work in the class of
smooth positive $\rho$ with $\rho,\rho_q\to0$ at infinity and known
$U$.
(a) At one time, the rate difference determines $\rho$: with
$W=(m/\kappa)(\lambda_--\lambda_+)$, two positive decaying solutions of
$\rho_{qq}=W\rho$ have a constant Wronskian that tends to zero, hence
are proportional, and normalization fixes the factor.
(b) Over any open time interval, the rates determine $\rho(\cdot,t)$,
hence $\rho_t$; with the flux hypothesis $\rho v\to0$ at $-\infty$ and
the displayed integral finite, continuity gives
$\rho v=-\int_{-\infty}^q\rho_t\,dq'$, and finite kinetic energy fixes
the constant in any case, since two currents differing by $C$ would
need $C^2\int dq/\rho<\infty$. So they determine $v$, and $S$ modulo a
spatial constant whose time dependence (4) fixes. The forces are then
fixed by (27) and add no data.
(c) The forces alone also determine the field pair over an interval:
$F_+-F_-=-2\kappa v_{qq}$ gives $v$ modulo affine functions;
$\tfrac12(F_++F_-)+U_q=(\kappa^2/m)\partial_q(\rho_{qq}/\rho)$ gives
$\rho_{qq}/\rho$ up to a constant $c$, and two positive decaying
solutions of $\rho''=(W_0+c_i)\rho$ with $c_1\neq c_2$ would have
Wronskian increment $(c_2-c_1)\int\rho_1\rho_2\,dq\neq0$ between
$-\infty$ and $+\infty$, contradicting decay; continuity then fixes
the affine part of $v$.
(d) At $\kappa=0$ the minimal rates vanish, common flips remain
allowed, and $F_\sigma=-U_q$ for every preparation: the zero branch
admits a preparation-independent body law. For $\kappa>0$ no such law
exists for all Gaussian preparations under the assumptions of
Proposition 22 of the recording note; that obstruction leaves open a
fixed preparation, extra apparatus variables, or a different
realization of the field law.

*Proof.* (a) If $\rho_1,\rho_2>0$ solve $\rho''=W\rho$ then
$w=\rho_1\rho_2'-\rho_1'\rho_2$ has $w'=0$, and $w\to0$ at infinity by
decay, so $(\rho_2/\rho_1)'=w/\rho_1^2=0$. (b) Continuity
$\rho_t=-\partial_q(\rho v)$ with the flux hypothesis, or the
kinetic-energy argument. (c) The
displayed combinations follow from (27); the Wronskian computation is
$w'=\rho_1\rho_2''-\rho_1''\rho_2=(c_2-c_1)\rho_1\rho_2$. (d) Insert
$d=0$ in (26)--(27). $\square$

So either half of the controller is informationally the field pair,
within this sheet architecture. An
apparatus implementing Proposition 7 stores $(\rho,S)$, or something
from which $(\rho,S)$ is computed, and updates it by (4). That is the
pilot-wave structure: the field is a dynamical variable of the single
system, carried alongside the particle. The known finite closed
realization of the same law is the interacting-ensemble one, in which
finitely many classical copies interact through a force built from the
Fisher information of their empirical density and the field is recovered
only as the copy number grows [@HallDeckertWiseman2014; reading:
metadata via Crossref and arXiv abstract]. There the controller datum
is the configuration of the other copies and $\kappa$ is the
interworld coupling constant. In both realizations $\kappa$ is a
coupling that nothing in the construction fixes.

**Corollary 10 (one record leaves the bounded-degree family).** Let
$\mathcal C$ be the family of Gaussian-polynomial field pairs of bounded
degree containing (18). One quadratic coordinate copy of (18) with
record $r$ produces, by Proposition 5, a pair $(\rho_r,S)$ outside
$\mathcal C$, and by Proposition 9 the controller functions on any
interval after the copy determine that pair; so a controller confined to
$\mathcal C$ cannot continue. This does not exclude finite-parameter
controllers: the family of normalized pairs
$(\rho_\epsilon(t)e^{-(r-q^2/\ell)^2/(2C)},S_\epsilon(t))$ with parameters
$(t,\epsilon,A,r,C,\ell)$ contains every one-copy posterior, and $n$
identical quadratic copies at one time enter only through the
sufficient statistics $(n,\sum_ir_i)$, the normalization absorbing
$\sum_ir_i^2$. The controller must carry the record-dependent data of
its family, not the literal history.

**Proposition 11 (two unread widths, with a coordinate witness).** Let
a label $J\in\{1,2\}$ with weights $\tfrac12$ select preparations
$N(0,A_j)$, $S=0$, $A_1\neq A_2$, and let $J$ be unread.
(a) *Branch realization.* Two controllers (145)--(148), one per
$A_j$, give the mixture process; the sign stays fair given $(Q,J)$,
the mean kinetic energy is $\tfrac{\kappa^2}{4m}(A_1^{-1}+A_2^{-1})$
for all time, and
$$EQ_t^2=\frac{A_1+A_2}2+\frac{\kappa^2t^2}{2m^2}
 \Big(\frac1{A_1}+\frac1{A_2}\Big).\tag{31}$$
(b) *Single marginal-score controller.* Starting one controller from
$\bar\rho=\tfrac12(\rho_1+\rho_2)$ and $\bar S=0$ gives kinetic energy
$\tfrac{\kappa^2}{2m}I(\bar\rho)$ and, by the free virial identity
$\tfrac{d^2}{dt^2}EQ^2=4\mathcal H_{\rm kin}/m$,
$EQ_t^2=\tfrac12(A_1+A_2)+\kappa^2I(\bar\rho)t^2/m^2$. The two differ
by
$$\frac{\kappa^2t^2}{m^2}\Delta,\qquad
\Delta=\frac12\Big(\frac1{A_1}+\frac1{A_2}\Big)-I(\bar\rho)
=\Big(\frac1{A_1}-\frac1{A_2}\Big)^2\int\frac{q^2\rho_1\rho_2}{4\bar\rho}\,dq>0,\tag{32}$$
which is (119) for this mixture. The single controller loses energy
$\kappa^2\Delta/(2m)$ and underpredicts the variance by
$\kappa^2\Delta t^2/m^2$ at every $t>0$: a difference visible in
coordinate records alone.

*Proof.* (a) Each branch is Proposition 21 with its own $A_j$; the
energies and variances are (143)'s, averaged. (b) The virial identity
is the time derivative of (19)'s structure for any free solution of
(4): $\tfrac{d}{dt}\int\rho q^2=2\int\rho qv$ and
$\tfrac{d^2}{dt^2}\int\rho q^2=2\int\rho(v^2+d^2)\,dq$ by (25) and two
integrations by parts, which is $4\mathcal H_{\rm kin}/m$. For
$\Delta$, the conditional label law is $\pi_j(q)=\rho_j/(2\bar\rho)$
and the branch scores are $-q/A_j$, so
$\operatorname{Var}(\sigma_J(q)\mid q)=q^2\pi_1\pi_2(A_1^{-1}-A_2^{-1})^2$;
insert in (119). $\square$

Within this model, the rule against replacing a discarded label by a
fresh marginal score is therefore a theorem with a coordinate witness,
under one qualification: the single-controller comparison uses the
algebraic evolution (15) of $\sqrt{\bar\rho}$, whose positivity and
nonexplosion as a sheet path law through possible nodes are not proved
here, while the virial comparison needs only (15). It rules out this
marginal-score replacement, not compressed descriptions of the
branches. Closure under unread records holds for branch controllers,
which carry the record-dependent data of Corollary 10.

**Proposition 12 (closure within the theory, at every $\kappa$).**
Coordinate shears $f(q)\pi$ preserve the class (2)/(136) with its fair
sign (Proposition 20 of the recording note), and the sheet dynamics of
Proposition 7, applied to body and pointers alike with their own
potentials, preserves it by construction wherever $\rho>0$. (For
several configuration coordinates with one shared sign and masses
$m_b$, Propositions 6--7 hold with
$\lambda_--\lambda_+=\kappa\sum_b\rho_{bb}/(m_b\rho)$ and
$F_{\sigma,a}=-\partial_a[U-\kappa^2\sum_b\rho_{bb}/(m_b\rho)
+\sigma\kappa\sum_bS_{bb}/m_b]$: the cross terms cancel by
$m_b\partial_av_b=m_a\partial_bv_a$ and its analogue for $d$, which hold
because $v_b=S_b/m_b$ and $d_b=\kappa L_b/m_b$.) Hence every finite
composition of coordinate copies, sheet evolution and conditioning on
coordinate records stays in the class, provided the positive
conservative path evolutions it requires exist, which Proposition 8
establishes for its orbit and not for all posteriors, and provided the
protocol evolves each conditioned branch with the controller of its own
posterior field pair: conditioning an already running process on past
records does not by itself replace its drift and rates, since (22)
changes the score by $(r-f)f'/C$ while a preassigned controller is
unchanged. Under that branch-dependent protocol the floor (138) holds
for every complete coordinate record. The escape (140) reads a
canonical momentum directly; within the theory a momentum is accessed
only through coordinate copies after sheet evolution, which keeps the
floor, and the exclusion of direct conjugate access is a stipulated
measurement rule. At $\kappa=0$ the minimal-switch single-sheet
construction closes before caustics, where (138) reads $\det\ge0$.
Closure under composition and complete coordinate records, where it
holds, holds for every $\kappa\ge0$ and selects no scale. Neither branch is unconditionally closed: the
$\kappa=0$ single-sheet class leaves itself at caustics of the classical
flow, and the $\kappa>0$ realization needs $\rho>0$ and is not continued
through nodes here.

## 8. Assessment: a representation, not an apparatus

The proposed dynamical constraint realization exists and is exact on
the explicit orbit: Propositions 7--8 give its balance, force,
impulses, energy exchange and all-time nonexplosion there, and
Proposition 12 gives its closure under coordinate copies when the
branch-dependent protocol and the required positive path evolutions
are supplied. It is a stochastic pilot-wave representation of the
supplied field law, with a switching sign in place of Nelson's
diffusion. Proposition 9 answers the handout's question within this
architecture: the extra state that controls the force and the rates is
the field pair, recoverable from either half of the controller, and
after records it is the record-dependent data of Corollary 10. The
construction simulates (4); it supplies no physical rule making the
body law preparation-independent, and Proposition 9(d) states the
dichotomy with its scope: $\kappa=0$ admits a preparation-independent
body law, while $\kappa>0$ admits none for all Gaussian preparations
under Proposition 22's assumptions.

Consequently the route "close the apparatus by composition and read
off a positive scale" ends here: closure, where it holds, holds for
every $\kappa\ge0$ (Proposition 12), and every realization of the
field law examined carries $\kappa$ as a coupling, between particle and
field or between copies. Not claimed: that every realization must
store the field, that a controller must store the literal record
history, or that no physical apparatus closure exists; the referee's
scope verdict is recorded with the corrections. What a positive scale
requires is a premise that fails at $\kappa=0$; Proposition 9(d) gives
its physical content without quantum language, as dependence of an
individual body's motion on the statistical state of its preparation,
with the scope just stated. Newton's inflexion Observation 8 records
dependence on apparatus geometry, which admits a local-force
countermodel ([routes, Proposition 3](newton-indeterminacy-routes.md));
it is not evidence for dependence on the ensemble. The two live forms
of the missing premise remain the terminal readout bound and
[Leibniz continuity on records](leibniz-continuity-records.md), and
the [reachability note](zero-branch-reachability.md) now carries the
gap thesis itself.

Retained from this unit for later use: the exact particle picture
consistent with every time partition on the orbit (Proposition 8), the
explicit sheet potential and powers (27)--(28), and the coordinate
witness (32) for the unread-label excess.

## 9. Consequence for STATE

The canonical Fisher structure follows from a specified restriction of
ordinary classical sheet action; a fixed compact-transfer family fails
even with Gaussian width; (18)--(20) complete a width/phase tangent to
an exact positive non-Gaussian forward orbit; a nonlinear record
generates a quartic tail outside the finite mode family with unread
energy (23). The two-sheet dynamical realization on that orbit is a
theorem (Propositions 7--8, refereed), with closure under coordinate
copies under a branch-dependent protocol (Proposition 12) and the
two-unread-width test passed by branch controllers and failed, with a
coordinate witness, by the marginal-score replacement (Proposition
11). Its controller is the field pair within this architecture, and
after records the record-dependent data of its family (Proposition 9,
Corollary 10): the realization is a stochastic pilot-wave
representation of the supplied law, and composition closure selects no
$\kappa$. Decision: the realization route is closed as a source of
positive action necessity; its results are kept as the
partition-consistent particle picture. The Newton work continues in
the [reachability note](zero-branch-reachability.md) under the gap
thesis, with the premises that fail at $\kappa=0$, complete records and
the coherent attachment of determinate preparations, as the hypotheses
to defend, and positivity, universality and radiation calibration
still separate. Reject a further realization of (4) offered as
apparatus closure, a projected residual counted as exact closure,
bridge phase used as population momentum without reservoir costs, or
an unexcluded zero branch presented as positive action necessity.
