# Quantum record bounds: aperture, disturbance and retained resources

With supplied canonical quantum kinematics at physical $\hbar>0$, a record
that distinguishes constant force from free motion with equal-prior error
$\epsilon<1/2$ must pay in explicitly bounded resources. For the same initial
preparation, the aperture bound is

$$JL+sP\ge\hbar\theta_\epsilon,\qquad
J=F\tau,\quad s=F\tau^2/(2m),\quad
\theta_\epsilon=\arcsin(1-2\epsilon).$$

For a test required to work for every pair of initial states, a different
bound charges the marks:

$$\frac s8\sum_j\sup\Delta\hat D_j+
\frac J2\sum_j\sup\Delta\hat X_j\ge\hbar\theta_\epsilon.$$

The suprema must cover the **conditional and interpolating states of the
proof**, including its hybrid protocols. Bounds on the two physical endpoint
experiments alone are insufficient. The two preparation requirements also
differ. A separated-packet counterexample defeats any preparation-independent
Galileo action floor; non-Gaussian grid probes defeat the Gaussian error law
while paying increasing recoil. These countermodels are part of the result.

This treatment integrates the probabilistic, recoil, general-disturbance and
Bures-path arguments. The Gaussian and hard-width theorems with their separate
assumptions are in [marking models](mark-cost-and-statistical-floor.md).
Historical model/coordinator checks are internal, not independent peer review;
no literature novelty is asserted for this assembly.

## One distance lemma and the exact single-shot constant

For density matrices let
$F_0(\rho,\sigma)=\operatorname{Tr}|\sqrt\rho\sqrt\sigma|$ be root fidelity
and $A(\rho,\sigma)=\arccos F_0\in[0,\pi/2]$ the Bures angle. We use its
triangle inequality, contraction under channels, Uhlmann purification, and
$\tfrac12\|\rho-\sigma\|_1\le\sin A$. Consequently a record test with
error at most $\epsilon$ requires $A\ge\theta_\epsilon$, where

$$\theta_\epsilon=\arccos(2\sqrt{\epsilon(1-\epsilon)})
 =\arcsin(1-2\epsilon),\qquad\theta_0=\pi/2.$$

If a unitary path has generator $K(u)$ and differentiable purification,
its Fubini–Study speed is $\Delta K(u)$, hence

$$A(\rho,V\rho V^\dagger)\le\int_0^1\Delta_{V(u)\rho V(u)^\dagger}K(u)du.$$

For an adaptive classical register $x$, the states and controlled unitary are
block diagonal. Fidelity is $\sum_xp_xF_{0,x}$, which is at least
$\cos(\sup_xA_x)$; the same bound with a supremum over conditional blocks
therefore holds. Integrals replace sums for continuous records. A hybrid
chain differing in one unitary step at a time is bounded by the sum of these
lengths, since its common prefix/remainder channels contract $A$.
Purifying a body–apparatus state leaves generator moments equal to those in
the body's marginal when the generator acts on the body alone.

All unbounded-generator uses below assume the indicated paths preserve the
required domains and have differentiable purifications with integrable
variance bounds. Smooth finite-moment states on a common invariant core
suffice for the written argument; extensions require the corresponding
controlled limits. Infinite resource suprema give vacuous bounds. Merely
calling an arbitrary unitary an instrument does not discharge domain or
hybrid-state hypotheses.

Sources (metadata unless indicated): Uhlmann
[1976](https://doi.org/10.1016/0034-4877(76)90060-4) and
[1992](https://doi.org/10.1016/0375-9601(92)90555-Z),
Anandan–Aharonov [1990](https://doi.org/10.1103/PhysRevLett.65.1697),
Fuchs–van de Graaf [1999](https://doi.org/10.1109/18.761271),
Wootters [1981](https://doi.org/10.1103/PhysRevD.23.357),
Braunstein–Caves [1994](https://doi.org/10.1103/PhysRevLett.72.3439), and
the hybrid-method comparison of Bennett et al.
[1997](https://doi.org/10.1137/S0097539796300933).

## Single-shot displacement and the aperture theorem

The body has $[\hat y,\hat p]=i\hbar$, mass $m>0$, and hypotheses
$H_I=\hat p^2/(2m)$, $H_F=H_I-F\hat y$, $F>0$. With

$$D(a,b)=e^{i(b\hat y-a\hat p)/\hbar},\qquad
D^\dagger\hat yD=\hat y+a,\quad D^\dagger\hat pD=\hat p+b,$$

linear dynamics gives

$$U_I(t)^\dagger U_F(t)=e^{i\varphi(t)}D(\alpha(t),\beta(t)),\qquad
\alpha(t)=-Ft^2/(2m),\quad\beta(t)=Ft.$$

Indeed forced evolution is $D(Ft^2/(2m),Ft)U_I$ up to scalar phase, and
free conjugation maps $(a,b)$ to $(a-bt/m,b)$. Thus one undisturbed shot
from the same preparation distinguishes it from its displacement. The
single unitary generator has spread at most
$(|\beta|\Delta y+|\alpha|\Delta p)/\hbar$. The distance lemma proves
$JL+sP\ge\hbar\theta_\epsilon$ for position/momentum bounds $(L,P)$ in
that input state. For pure states this is equivalently Helstrom's overlap
criterion and Mandelstam–Tamm; purification gives the mixed-state bound.

For a finite adaptive instrument protocol, use the free interaction picture.
The force increments are displacements
$D(\Delta\alpha_r,\Delta\beta_r)$ up to scalar phases. Replace them one at
a time, keeping the outcome-dependent instruments and all memory registers.
If the body marginals of **all hybrid conditional states** satisfy
$\Delta y\le L$, $\Delta p\le P$ in this picture, the distance lemma gives

$$\hbar A(P_I,P_F)\le\sum_r(|\Delta\beta_r|L+|\Delta\alpha_r|P)
 =F\tau L+\frac{F\tau^2}{2m}P.$$

Both displacement components are monotone, so the sums telescope independently
of the instrument number, times and Kraus rank. This proves the stated aperture
theorem for arbitrary memory and adaptive choices under its uniform resource
and domain assumptions.

For a general integrable force history $f(t)$ there is a laboratory-frame
kick form. Let $L(t)$ bound the body's position spread over all conditional
states in the chain that turns the force off after any intermediate time.
Assume the finite-moment/partition limits used by the chain are controlled.
Then

$$\boxed{\hbar\theta_\epsilon\le\int_0^\tau|f(t)|L(t)dt.}$$

On a mark-free cell, forced versus free evolution differs by a translation
with momentum component $\int f$ and position component
$m^{-1}\int(t+\delta-u)f(u)du$. Its angle cost is bounded by
$|\int f|\Delta y/\hbar+O(\delta^2)\Delta p/\hbar$ for bounded forces.
Summing and refining gives the integral; approximation extends to controlled
integrable histories. The supplied uniform envelopes are those of this chain.
If the laboratory marginals after each mark and in its hybrids obey
$(L,P)$, then between marks $L(t)\le L+P(t-t_j)/m$. For constant force this
again yields $F\tau L+F\tau^2P/(2m)\ge\hbar\theta_\epsilon$; a maximum
mark separation $\delta t$ improves the second term to
$F\tau\delta t P/(2m)$. Laboratory and interaction-picture aperture
conditions are two sufficient hypotheses and must not be conflated.

At $A_0=LP$ and $r=L/\sqrt{\tau A_0/(2m)}$, the aperture inequality is

$$\tau\Delta E\ge\frac{2m\theta_\epsilon^2\hbar^2\tau}{(2mL+\tau P)^2}
 =\frac{\theta_\epsilon^2\hbar^2}{A_0(r+r^{-1})^2}.$$

At fixed $A_0$ this lower bound is **largest** at the balanced shape $r=1$,
and tends to zero under unbounded squeezing. The minimum-uncertainty balanced
aperture $A_0=\hbar/2$ gives $\tau\Delta E\ge\hbar\theta_\epsilon^2/2$,
which is $\pi^2\hbar/8$ at zero error. Area alone does not fix a floor.

## A preparation counterexample with growing aperture

Let $a=F\tau^2/(2m)>0$, $b=F\tau>0$ and
$\eta=ab/\hbar=\tau\Delta E/\hbar<1$. Choose a fixed real normalized
$\chi$ supported on $[-1/2,1/2]$ with $\|\chi'\|_2<\infty$, and prepare

$$\psi=\frac{\chi_++\chi_-}{\sqrt2},\qquad
\chi_\pm(y)=w^{-1/2}\chi((y\mp d/2)/w),\qquad
d=\pi\hbar/b,\quad w=\sqrt{a\hbar/b}.$$

Here $w/d=\sqrt\eta/\pi$ and $a/w=\sqrt\eta$. The packets and their
cross-displacement overlaps are disjoint in the stated regime. Under
$D(a,b)$ each same-packet contribution has phase $e^{\pm ibd/(2\hbar)}$,
whose leading terms cancel. Translation continuity and
$|e^{ix}-1|\le|x|$ give the sufficient estimate

$$|\langle\psi,D(a,b)\psi\rangle|
 \le(a/w)\|\chi'\|_2+bw/\hbar
 =\sqrt\eta(\|\chi'\|_2+1).$$

For overlap modulus $x\le1$, the exact Helstrom error is
$x^2/[2(1+\sqrt{1-x^2})]\le x^2/2$. Thus
$p_{\rm err}\le C\eta$ with $C=(\|\chi'\|_2+1)^2/2$; this corrects the
old erroneous upper constant $x^2/4$. The position spread is of order
$d/2=\pi\hbar/(2F\tau)$, diverging as $F\downarrow0$ at fixed $m,\tau$.
Momentum spread is of order $\hbar/w=\sqrt{2m\hbar/\tau}$ and remains
bounded in that family. The kick cost approaches $\pi\hbar/2$ as the action
and error tend to zero. The example locates the missing uniform aperture;
it neither excludes nor selects an action scale.

## General disturbance theorem with an unknown preparation

Now require the test's equal-prior error to be at most $\epsilon$ for
**every pair** of initial body states under the two hypotheses. Define

$$\hat D_j=U_j^\dagger\hat pU_j-\hat p,\qquad
\hat X_j=U_j^\dagger\hat yU_j-\hat y.$$

The unitaries may involve body-dependent noise, quantum memory and adaptive
control. For any line $a+bt$, set
$c(t)=P(t)-a-bt$ and $w(t)=(c(t),mc'(t))$, where $mP''=f$ and
$P(0)=P'(0)=0$. Translating the forced initial state by $w(0)$ makes
its mark-free dynamics the free state's translate by $w(t)$.

**Disturbance theorem.** Under the distance lemma's domain hypotheses,

$$\hbar\theta_\epsilon\le
 \sum_j\sup\Delta\bigl(c(t_j)\hat D_j-mc'(t_j)\hat X_j\bigr).$$

The supremum covers the entering conditional states of the offset-removal
hybrids and their translations by $u w(t_j)$, $0\le u\le1$.

*Proof.* A hybrid carries the force offset through the first $j$ marks,
removes it immediately afterwards, then follows the free protocol. Consecutive
hybrids differ at mark $j$ by
$E=T(w)^\dagger U_jT(w)U_j^\dagger$. Put
$G=(c\hat p-mc'\hat y)/\hbar$ and
$E(u)=e^{iuG}U_je^{-iuG}U_j^\dagger$. Its generator is
$K(u)=e^{iuG}(G-U_jGU_j^\dagger)e^{-iuG}$.
Conjugating its current-state spread back to the entering translated state
gives precisely the spread of

$$U_j^\dagger GU_j-G=(c\hat D_j-mc'\hat X_j)/\hbar.$$

The Bures triangle inequality and common remainder channels add these costs;
the chosen pair of initial states must meet the composite testing criterion.
$\square$

For constant force the best uniform affine approximation to
$P(t)=Ft^2/(2m)$ is $F(\tau t-\tau^2/8)/(2m)$. It gives
$|c|\le s/8$ and $m|c'|\le J/2$. The variance seminorm proves the leading
bound. This line optimizes the momentum term alone; joint optimization with
position disturbance may use another line. A momentum-reading pulse
$U=e^{-i\mu\hat p\hat Q_A/\hbar}$ has $\hat D=0$, $\hat X=\mu\hat Q_A$
and pays in position disturbance. The product sagitta–momentum and
impulse–position pairing is fixed by the displacement generator.

These variances charge operators on particular states. They are not a claim
that all complete records leave a classical random impulse unrecoverable.
Physical finite-duration couplings require a controlled slicing limit; a
formal subdivision alone does not establish that limit or a finite budget.

## Recoil-only bound for arbitrary probe states

For momentum-transfer marks
$U_j=e^{-i\lambda_j\hat y\hat P_j/\hbar}$, write
$\hat N_j=\hat Q_j/\lambda_j$, $\hat D_j=-\lambda_j\hat P_j$ and
$\Delta_j=\Delta\hat D_j$. Their commuting Heisenberg readings are

$$\hat R_j=\hat y+\hat p t_j/m+\theta P(t_j)
 +\sum_{i<j}(t_j-t_i)\hat D_i/m+\hat N_j.$$

Translate the forced initial body by $(-a,-mb)$. Its record distribution
is the free protocol's record with each initial pointer translated by
$\lambda_jc_j$, $c_j=P(t_j)-a-bt_j$: the pointer coordinate appears only
in its own reading, and its translation fixes every recoil. Data processing
and the distance lemma therefore prove

$$\hbar\theta_\epsilon\le\inf_{a,b}\sum_j\Delta_j|P(t_j)-a-bt_j|.$$

For product probes this is a factor-by-factor hybrid chain. Correlated probes
use one unitary generated by $\sum_j\lambda_jc_j\hat P_j$ and
$\Delta(\sum A_j)\le\sum\Delta A_j$. Adaptive choices require uniform
branch envelopes. The [body-independent-noise classification](mark-cost-and-statistical-floor.md#quantum-probe-cost-and-body-independent-noise)
extends the same argument even when position jumps occur: the recoil-generated
translation changes $\hat N_j$ and commutes with both $\hat D_j,\hat X_j$.
For constant force,

$$\boxed{s\sum_j\Delta_j\ge8\hbar\theta_\epsilon,}$$

and for a general displacement the sagitta factor becomes
$E_1(P)=\inf_{a,b}\max|P-a-bt|$. This recoil-only statement is stronger
than simply adding a position-disturbance charge for this special noise class.

A three-mark Gaussian protocol with sharp outer marks has unbounded outer
recoils, so its weighted bound uses the endpoint chord, not the displayed
unweighted sum. With middle noise
$\hat S=\alpha\hat Q+\beta\hat P$, $\alpha=2/\lambda$,
$\beta=\tau\lambda/(2m)$, Robertson at fixed recoil gives
$\Delta S\ge\hbar/\Delta_2$, attained by a suitable pure Gaussian.
The test succeeds when $s\Delta_2\ge4z_{1-\epsilon}\hbar$, hence the
weighted cost is $\Delta_2|c_2|=z_{1-\epsilon}\hbar$.
Its ratio to the necessary bound is $z_{1-\epsilon}/\theta_\epsilon$
(about $1.47$ at five per cent error), diverging at zero error. General
attainment is not proved.

## A non-Gaussian grid defeats the Gaussian error law

In that three-mark statistic, put
$\hat S=\alpha\hat Q+\beta\hat P$, $\alpha\beta=\tau/m$.
Real approximate grid wavefunctions with teeth of width $w$ under an
envelope of width of order $1/w$ can have
$\operatorname{Cov}_{\rm sym}(Q,P)=0$, yet both stabilizer expectations
approach one for

$$S_1=e^{i\ell_Q\hat P/\hbar},\quad S_2=e^{i\ell_P\hat Q/\hbar},
\quad\ell_Q\ell_P=2\pi\hbar,\quad\ell_P/\ell_Q=\alpha/\beta.$$

The stabilizers commute. BCH gives $S_1S_2=-e^{ic\hat S}$,
$c=\ell_P/(\hbar\alpha)$. Since
$\|(S_k-1)\psi\|^2=2(1-\operatorname{Re}\langle S_k\rangle)\to0$,
$e^{ic\hat S}$ concentrates at $-1$. The law of $c\hat S$ modulo $2\pi$
therefore concentrates at $\pi$. Under the force the statistic shifts by
$d=F\tau^2/(4m)$, giving a distinct limiting modular point whenever

$$d\notin\sigma\mathbb Z,\qquad
\sigma=2\pi/c=\sqrt{2\pi\hbar\tau/m}.$$

A modular test then has error tending to zero. For this real family the
error–recoil correlation remains zero, while
$\Delta_2=\lambda\Delta P\to\infty$ with momentum-envelope width of order
$\hbar/w$. At finite teeth the signal must remain separated from the modular
lattice by more than the width. Thus zero correlation does not extend a
Gaussian threshold to arbitrary states; the exact recoil bound is respected.
GKP [2001](https://doi.org/10.1103/PhysRevA.64.012310) and grid sensing
[2017](https://doi.org/10.1103/PhysRevA.95.012305) are metadata-level
comparisons, not a priority claim for this application.

## Splitting the force: one conditional accounting

Under the composite preparation requirement, split $f=g+h$ and choose
$c''=g/m$. Switching off $h$ at the body and then transporting the $g$
offset through marks gives

$$\hbar\theta_\epsilon\le\int_0^\tau|h(t)|L(t)dt
 +\sum_j\sup\Delta(c(t_j)\hat D_j-mc'(t_j)\hat X_j).$$

The first leg is the kick chain and the second the disturbance chain; both
use their actual common conditional-state envelopes. A same-preparation-only
test does not automatically meet this composite criterion. A test uniform
over same-preparation pairs bounds each individual hypothesis error by
$2\epsilon$, giving only $\arcsin(\max\{0,1-4\epsilon\})$ for an arbitrary
mixed pair through that argument.

For a force of one sign and recoil-only marks, take $g=\chi f$,
$0\le\chi\le1$, and $c$ pinned at both endpoints. With the Dirichlet Green
function,

$$G_\tau(t,u)=\frac{\min(t,u)(\tau-\max(t,u))}{\tau},\qquad
c(t)=-\frac1m\int G_\tau(t,u)g(u)du,$$
$$R(u)=\frac1m\sum_j\Delta_jG_\tau(t_j,u).$$

If $L(u)$ and $\Delta_j$ are **common bounds uniform over the entire
chosen split family and its hybrids**, the two costs are
$\int|f|[(1-\chi)L+\chi R]$, and pointwise minimization proves

$$\hbar\theta_\epsilon\le\int_0^\tau|f(u)|\min\{L(u),R(u)\}du.$$

The former claim that conditional spreads are automatically independent of
$\chi$ for every von Neumann protocol was too broad, particularly with
outcome-dependent control. Uniform envelopes, or a separately proved
covariance property, are required before this minimization. End marks give
no $R$ contribution. A middle mark at $\tau/2$ gives
$R(u)=\Delta_2\min(u,\tau-u)/(2m)$, of height $\Delta_2\tau/(4m)$;
its pure recoil cost is $\Delta_2s/4$. No optimal split or physical
attainment theorem follows solely from this upper cost.

## Consequence for STATE

The necessary quantum resource bounds retain their sharp single-shot angle
constant and explicit assumptions on initial states, domains and hybrids.
They permit classical limits and arbitrarily small Galileo actions when
preparation aperture or probe recoil is allowed to grow. Gaussianity,
correlation control and the composite nuisance criterion are additional
premises. These supplied-$\hbar$ statements do not prove action necessity,
universal scale identification or uniqueness of a quantum completion.
