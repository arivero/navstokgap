# Shared radiation and closure under recording

**Result, 2026-09-27 (GPT-6 Astra).** A common Gaussian radiation
background permits arbitrarily small two-pointer posteriors in a linear
classical model with the pulse couplings and retained coordinate records
of Theorem I. This holds for **every finite joint covariance**, including
all body--pointer and pointer--pointer correlations. At fixed ultraviolet
cutoff, radiation damping and continuing exposure to the background
preserve the counterexample for sufficiently short finite pulses
(Theorems 1 and 2). The infimum of the body's posterior area is zero.
For ideal resonant marginal covariances of area $\kappa$, finite gains
$2$ and $4$ already give $\sqrt{\det\Sigma_{\rm post}}\le3\kappa/4$.

The decisive instrument premise is classical storage of a pointer
coordinate without an obligatory conjugate disturbance when that pointer
is subsequently reused. An explicit Gaussian recording law restores
closure at $\zeta=\kappa$: readout imprecision and the added conjugate
disturbance must satisfy a product bound $\kappa^2$, with a corresponding
restriction on every retained memory (Proposition 3). Deriving that law
from electrodynamics remains the physical task. The stationary spectrum
alone leaves it unspecified.

**Scope.** The cutoff model below supplies the exact finite-duration
statement. Its background has mode energy $\kappa\omega$ below the
cutoff and a specified regulator above it. A laboratory frequency cutoff
adds a preferred frame. The resonant approximation gives the simpler
constant $3\kappa/4$; the proof for arbitrary finite covariance requires
neither that approximation nor product preparations. The unregulated
full momentum variance is divergent, as stressed in the revised
[SED link](sed-zeta-radiation-link.md), §2 (local full-read).
No limit removing the cutoff is asserted. The controls and classical
readouts are explicitly granted model operations; an electrodynamic
construction of a complete measuring device would have to justify or
exclude them.

## 1. The common field, its damping and its correlations

Use SI units, $\kappa>0$, speed $c$, and three harmonically bound dipole
coordinates $q_i,p_i$, $i=0,1,2$, with masses $m_i>0$, frequencies
$\omega_i>0$, charges $e_i\ne0$, fixed centres $\mathbf r_i$, and unit
directions $\mathbf n_i$. The body has index $0$. The traps and external
quadratic controls define the linear approximation. The incident
Gaussian field has the zero-point spectrum

$$u_0(\omega)=\frac{\kappa\omega^3}{\pi^2c^3},\qquad
\mathcal E_0(\omega)=\kappa\omega. \tag{1}$$

Introduce a real common form factor $f_\Lambda(\omega)$, equal to one
on the frequencies of interest and zero for $\omega>\Lambda<\infty$.
This can regulate the incident force itself or the dipole coupling to
the field. In the latter convention the full incident field retains
(1), while the apparatus response selects a frame and a frequency band.
All covariances below refer to the regulated response.

The angular correlation matrix is

$$K_{ij}(\omega)=\frac{3}{8\pi}\int_{S^2}
\left[\mathbf n_i\!\cdot\!\mathbf n_j
 -(\mathbf n_i\!\cdot\!\widehat{\mathbf k})
  (\mathbf n_j\!\cdot\!\widehat{\mathbf k})\right]
\cos\!\left(\frac{\omega}{c}\widehat{\mathbf k}\!\cdot\!
 (\mathbf r_i-\mathbf r_j)\right)d\widehat{\mathbf k}. \tag{2}$$

It is positive semidefinite and $K_{ii}=1$: the transverse polarization
sum is a Gram matrix, and the integral for a unit direction is $8\pi/3$.
Thus the same field gives both diagonal and cross force covariances.
Define its matrix spectral density by

$$J_{ij}(\omega)=\frac{e_i e_j\omega^3}{6\pi\epsilon_0c^3}
 f_\Lambda(\omega)^2K_{ij}(\omega),$$
$$C_F(t-s)=\mathbb E[F(t)F(s)^{\sf T}]
 =\frac{2\kappa}{\pi}\int_0^\Lambda J(\omega)
       \cos[\omega(t-s)]\,d\omega. \tag{3}$$

For example $C_{F,ii}(0)=e_i^2\kappa\int_0^\Lambda
\omega^3f_\Lambda^2d\omega/(3\pi^2\epsilon_0c^3)$.
The normalization follows directly from $u_0=\epsilon_0\langle
|\mathbf E|^2\rangle$ per frequency, isotropy, and $F_i=e_i E_i$.

Keep radiation damping through a passive oscillator bath with the same
$J$, including the cross damping. Its causal friction kernel is

$$\mu(t)=\frac2\pi\int_0^\Lambda
       \frac{J(\omega)}{\omega}\cos(\omega t)\,d\omega,
\qquad t\ge0. \tag{4}$$

An explicit realization uses harmonic bath coordinates coupled linearly
to the $q_i$, with the quadratic counterterm obtained by completing
each bath potential square. Choose the bath coupling matrix so that
$J(\omega)=\pi L(\omega)L(\omega)^{\sf T}/(2\omega)$; its existence
follows from positivity of (2). Give a free bath coordinate of frequency
$\omega$ the variances $\kappa/\omega$ and $\kappa\omega$ for coordinate
and momentum. Its energy is $\kappa\omega$. Eliminating it gives (3)
and (4). The counterterm keeps the prescribed trap stiffness positive;
the finite-cutoff bath Hamiltonian has positive quadratic energy.

In this realization $\dot q=\partial H_{\rm sys}(t)/\partial p$, and

$$\dot p=-\frac{\partial H_{\rm sys}(t)}{\partial q}
 -\int_0^t\mu(t-s)\dot q(s)\,ds+F(t). \tag{5}$$

An initial-slip term, or the stationary prehistory, is included in
$F(t)$ with its correlations with the initial system. Independent
system--bath initial data are unnecessary below. Before the controls,
the diagonal absorptive part is the usual radiation term
$m_i\tau_i\omega^3 f_\Lambda^2$, where

$$\tau_i=\frac{e_i^2}{6\pi\epsilon_0m_i c^3}.
\tag{6}$$

This finite-cutoff memory equation retains the dispersive part as well.
It avoids using a third-order local radiation equation during arbitrarily
fast controls. Static dipole interactions, when retained, are additional
finite entries of the stiffness matrix; assume stability of the chosen
trapped system.

**Tracking the prior.** Set

$$Q_i=\sqrt{m_i\omega_i}\,q_i,\qquad
P_i=\frac{p_i}{\sqrt{m_i\omega_i}},\qquad
Z=(Q,P,Y,\Pi,Z_2,\Pi_2)^{\sf T}. \tag{7}$$

Here $(Q,P)=(Q_0,P_0)$, $(Y,\Pi)=(Q_1,P_1)$ and
$(Z_2,\Pi_2)=(Q_2,P_2)$. Every coordinate has units
$\sqrt{\rm action}$, every pair remains canonical, and the body's
covariance determinant equals that in $(q_0,p_0)$.
For a stable stationary response, let $H(\omega)$ be the six-by-three
transfer matrix from physical forces to these variables. The complete
prior covariance is

$$V=\operatorname{Re}\int_0^\Lambda
 H(\omega)\frac{2\kappa J(\omega)}{\pi}
 H(\omega)^\dagger\,d\omega. \tag{8}$$

The susceptibility in $H$ includes (4); momentum rows before the controls
are $-i m_i\omega$ times the coordinate rows before scaling. Any
undamped initially populated normal modes add their own covariance.
Formula (8) displays the cross correlations explicitly. Setting its
off-diagonal entries to zero would require a separate preparation or
decoupling argument. The theorems use the actual $V$ instead.

For an isolated weakly damped resonance the ideal narrow-resonance limit
gives $\operatorname{Var}Q_i=\operatorname{Var}P_i=\kappa$.
A finite spectral window and finite damping introduce corrections;
the exact finite-cutoff statements below allow all of them. In
particular, a literal window of only a fixed number of linewidths
captures only a fraction of the resonant Lorentzian. Access to a
temporally filtered variable also requires a recording prescription;
the instantaneous pulse proof is applied to canonical cutoff variables,
or to canonical oscillator amplitudes in the stated resonant model.

## 2. Theorem 1: two correlated pointers permit arbitrarily small area

Assume $Z$ has a centered Gaussian law with finite covariance $V$;
known means can be subtracted. Grant two quadratic Hamiltonian pulses,
their integrated Hamiltonians being

$$\mathcal H_1=GQ\Pi,\qquad
\mathcal H_2=B\Pi\Pi_2,\qquad G,B>0. \tag{9}$$

Both have action units. Their Hamilton equations are linear. The first
pulse sends $Y\mapsto Y+GQ$ and $P\mapsto P-G\Pi$.
Read and store $R_1=Y+GQ$ before the second pulse. That pulse sends
$Z_2\mapsto Z_2+B\Pi$ and $Y\mapsto Y+B\Pi_2$; it leaves the body and
$\Pi$ fixed. Read $R_2=Z_2+B\Pi$. The final body is

$$X=(Q,P-G\Pi)^{\sf T},\qquad R=(R_1,R_2)^{\sf T}. \tag{10}$$

The readouts are classical passive coordinate observations. The first
stored number survives the later change of $Y$. Small independent
Gaussian readout errors can also be allowed, as in §3.

**Theorem 1.** Under these instrument assumptions, for every such $V$,

$$\boxed{\sqrt{\det\operatorname{Cov}(X\mid R)}
\le\frac{\sigma_Y\sigma_P}{G}
       +\frac{\sigma_Y\sigma_{Z_2}}{B}.} \tag{11}$$

Here $\sigma_U^2=\operatorname{Var}U$ in the initial joint state.
In particular the posterior area has infimum zero as $G,B\to\infty$.
All cross correlations in $V$ are allowed, including perfect ones.

*Proof.* Estimate the final body by

$$\widehat X=(R_1/G,-GR_2/B)^{\sf T}.$$

The errors are the exact random-variable identities

$$X-\widehat X=(-Y/G,\ P+GZ_2/B)^{\sf T}. \tag{12}$$

Thus the first pointer's recoil $\Pi$ cancels, including the part
correlated with the body or either pointer. The conditional Gaussian
covariance is independent of the outcome. Conditional expectation
minimizes the error covariance in the positive-semidefinite order, so
it is bounded above by the covariance of (12). In particular,

$$\operatorname{Var}(Q\mid R)\le\sigma_Y^2/G^2,\qquad
\operatorname{Var}(P-G\Pi\mid R)
\le(\sigma_P+G\sigma_{Z_2}/B)^2.$$

The second bound is Cauchy--Schwarz, with either sign of
$\operatorname{Cov}(P,Z_2)$. Bounding a two-by-two determinant by the
product of its diagonal entries proves (11). $\square$

For direct use of a specified common-field response, introduce

$$A=\begin{pmatrix}1&0&0&0&0&0\\0&1&0&-G&0&0\end{pmatrix},
\qquad
L=\begin{pmatrix}G&0&1&0&0&0\\0&0&0&B&1&0\end{pmatrix}.$$

The exact answer, with every entry from (8) retained, is

$$\Sigma_{\rm post}=AVA^{\sf T}
 -AVL^{\sf T}(LVL^{\sf T})^{-1}LVA^{\sf T}. \tag{13}$$

Use a pseudoinverse on the supported record subspace when necessary.
For example the two record covariances include

$$\operatorname{Cov}(R_1,R_2)
 =G V_{QZ_2}+GB V_{Q\Pi}+V_{YZ_2}+B V_{Y\Pi}.$$

The covariance of the error vector in (12) has off-diagonal entry
$-V_{YP}/G-V_{YZ_2}/B$ and second diagonal entry
$V_{PP}+2G V_{PZ_2}/B+G^2V_{Z_2Z_2}/B^2$.
These formulas track the correlations rather than replacing the common
field by three independent baths. Equation (11) bounds their most
unfavourable possible effect.

**Explicit constants.** If $\sigma_Y^2,\sigma_P^2,
\sigma_{Z_2}^2\le K\kappa$, put $B=G^2$. Then

$$\sqrt{\det\Sigma_{\rm post}}
 \le K\kappa(G^{-1}+G^{-2}). \tag{14}$$

Every finite-cutoff prior has a finite such $K$. Taking $G>2K+1$
gives a strict bound below $\kappa$. For ideal resonant marginals,
$K=1$, and $G=2$, $B=4$ give $3\kappa/4$, regardless of the cross
correlations. As an algebraic example only, for $V=\kappa I_6$,

$$\Sigma_{\rm post}=
\begin{pmatrix}
\kappa/(1+G^2)&0\\
0&\kappa[1+G^2/(1+B^2)]
\end{pmatrix}. \tag{15}$$

With $G=2$, $B=4$, its area is $\kappa\sqrt{21/85}$.
Independence is used only in this example. The body momentum's
unconditional spread grows with $G$; the completed record estimates its
kick. The theorem concerns posterior concentration and leaves the
unconditional disturbance cost to its own accounting.

## 3. Theorem 2: a finite-duration version with radiation damping

Fix $\Lambda$, the initial finite Gaussian covariances, and finite gains
$G,B$. Apply the two pulses over successive intervals of total length
$T$, using smooth fixed pulse shapes rescaled by $1/T$. Keep (5) active
throughout and retain the first reading at the interval boundary. Let
$X_T,R_T$ denote the resulting final body and records. Write their
deviations from the ideal expressions (10) as $\Delta Q,\Delta P,
\Delta R_1,\Delta R_2$, and set

$$d_Q(T)=\|\Delta Q-\Delta R_1/G\|_2,\qquad
d_P(T)=\|\Delta P+G\Delta R_2/B\|_2. \tag{16}$$

Norms are centered root-mean-square norms. They include readout errors
when present. The initial field and body can be correlated.

**Theorem 2.** In the finite-cutoff passive linear model (3)--(5), with
the classical readouts of §2, $d_Q(T),d_P(T)\to0$ as $T\downarrow0$.
Moreover

$$\boxed{\sqrt{\det\operatorname{Cov}(X_T\mid R_T)}}
\ \le\left(\frac{\sigma_Y}{G}+d_Q(T)\right)
\left(\sigma_P+\frac{G\sigma_{Z_2}}B+d_P(T)\right). \tag{17}$$

Consequently every strict violation in (11) persists for sufficiently
small positive $T$. At $K=1$, $G=2$, $B=4$, the explicit sufficient
error budget $d_Q,d_P\le\sqrt\kappa/10$ gives area at most
$24\kappa/25<\kappa$.

*Proof.* At fixed cutoff $C_F(0)$, $\mu$ and $\mu'$ are finite.
In particular

$$\left\|\int_0^T F_i(t)\,dt\right\|_2
 \le T\sqrt{C_{F,ii}(0)}.$$

Rapid control-induced changes of $q$ leave the memory term bounded:
integration by parts gives

$$\int_0^t\mu(t-s)\dot q(s)\,ds
 =\mu(0)q(t)-\mu(t)q(0)
       +\int_0^t\mu'(t-s)q(s)\,ds. \tag{18}$$

For the control-only equation each pulse is a finite shear. In the
scaled coordinates its propagator and inverse have norms bounded,
uniformly in $T$, by $(1+G)(1+B)$. Variation of constants, (18), and
the finite force second moment give a uniform mean-square bound on
$q,p$ for sufficiently small $T$ by the integral Gronwall inequality.
Integrating the remaining trap, bath and memory drifts then makes the
endpoint and first-read errors $O(T)$, with constants depending on
$\Lambda,G,B$, the initial covariances and trap parameters. This proves
the asserted convergence, while keeping radiation damping in the
equation. The same conclusion holds for any supplied resonant Markov
model with finite diffusion, with stochastic increments $O(\sqrt T)$.

Apply the estimator of §2 to $R_T$. Its two errors equal (12) plus
the residuals in (16). The triangle inequality in $L^2$ gives (17),
and Gaussian conditioning again makes the posterior covariance
outcome-independent. Finally $(1/2+1/10)(3/2+1/10)=24/25$.
$\square$

**Correlations during the controls.** More explicitly, the four-vector
$O_T=(X_T,R_T)$ has the form $M_T Z+\eta_T$. If
$W_T=\operatorname{Cov}(Z,\eta_T)$ and
$N_T=\operatorname{Cov}(\eta_T)$, then

$$\operatorname{Cov}(O_T)=M_TVM_T^{\sf T}
 +M_TW_T+W_T^{\sf T}M_T^{\sf T}+N_T. \tag{19}$$

For a force-response kernel $D_T(t)$ the driven part is

$$N_T=\int_0^T\!\int_0^T
D_T(t)C_F(t-s)D_T(s)^{\sf T}\,dt\,ds,$$

with any prehistory terms included in $\eta_T$. Thus both the common
increments and their correlation with the initial state are retained.
Equation (17) uses an $L^2$ bound, so none of the cross terms in (19)
has been discarded by assuming fresh independent noise.

Small independent Gaussian readout noises of standard deviations
$r_1,r_2$ add at most $r_1/G$ and $Gr_2/B$ to the two budgets (16).
Every chosen strict violation therefore permits positive readout noise.
A prescribed minimum readout noise, coupling duration, gain ceiling or
memory disturbance could restrict the protocol; those would be added
instrument premises.

**Order and cost of the limits.** For a target area, first fix a finite
cutoff and its actual prior $V$, then choose finite gains using (11),
then choose a positive duration using (17). The constants depend on the
cutoff and the gains. Removing the cutoff before this construction
reintroduces the divergent full momentum variance. The impulsive
limit also spends unbounded control strength and allows idealized
bilinear couplings. This establishes the linear-model obstruction;
relativistic locality, material bounds and an implementation using only
electromagnetic controls would require further estimates with $c$.
Heavy or detuned pointers are unnecessary for the theorem. Increasing
mass can reduce coordinate noise or slow damping, but leaves the
equilibrium resonant area $\kappa$ unchanged.

## 4. A recording law that restores closure

There is a precise point where the two-pulse protocol can be blocked.
After the first pulse, reading $Y+GQ$ and keeping pointer 1 available
for the second pulse must itself have a conjugate cost.

**An explicit repair.** In the product resonant example, let the stored
first reading have independent Gaussian error $N$ of variance $s^2>0$,
and let creating that reading give pointer 1 a further independent
momentum kick $D$ of variance $d^2$. The body has already received
$-G\Pi$; the second pointer now measures $\Pi+D$. Assume

$$s^2d^2\ge\kappa^2. \tag{20}$$

Grant arbitrarily accurate inference of $\Pi+D$ from pointer 2. The
two independent sectors then give

$$\operatorname{Var}(Q\mid R)
=\frac{\kappa(\kappa+s^2)}{\kappa+s^2+G^2\kappa},\qquad
\operatorname{Var}(P-G\Pi\mid R)
=\kappa+\frac{G^2\kappa d^2}{\kappa+d^2}. \tag{21}$$

For $d^2=\kappa^2/s^2$ their product is exactly $\kappa^2$;
larger $d^2$ or finite precision of the second read increases it.
The extra kick makes the later pointer momentum an imperfect record
of the earlier body kick. A weaker statement that every read imparts
some disturbance would leave (20) unproved.

The following sufficient premise handles arbitrary correlations and
composition. Let $\Omega_n$ be the canonical Poisson matrix and impose
on every Gaussian joint state, including reusable apparatus and memory,

$$V+i\kappa\Omega_n\succeq0. \tag{22}$$

Admit symplectic transformations, independent ancillary states obeying
(22), discarding subsystems, and Gaussian measurements on a subsystem
that is then discarded. Such a measurement has independent Gaussian
seed covariance $\Gamma$ with $\Gamma+i\kappa\Omega_A\succeq0$.
Sharp single-coordinate measurements are obtained as squeezed limits.
When a pointer is retained after being read, require a dilation of its
reading within this same class; (20) is the basic coordinate example.

**Proposition 3 (Gaussian closure).** These operations preserve (22)
on the unmeasured systems conditional on the complete record, including
sequential adaptive uses. In particular the body's posterior has
$\sqrt{\det\Sigma}\ge\kappa$.

*Proof.* Symplectic transformations preserve (22), products give a
direct sum, and discarding takes a principal submatrix. For a joint
covariance $V=\left(\begin{smallmatrix}A&C\\C^{\sf T}&B\end{smallmatrix}\right)$,
Gaussian conditioning gives $A-C(B+\Gamma)^{-1}C^{\sf T}$.
Complex conjugation of the seed condition gives
$\Gamma-i\kappa\Omega_A\succeq0$. Adding that positive matrix on the
apparatus block of (22) gives

$$\begin{pmatrix}A+i\kappa\Omega_S&C\\
C^{\sf T}&B+\Gamma\end{pmatrix}\succeq0.$$

Its Schur complement proves the desired conditional inequality.
Limits preserve positivity. Apply this at every branch of a sequence,
retaining all apparatus needed at later stages. $\square$

This is the Gaussian quantum instrument restriction written in classical
covariance language. Bartlett, Rudolph and Spekkens derive Gaussian
quantum preparations, transformations and measurements from an epistemic
restriction ([2012 paper](https://arxiv.org/abs/1111.5057), author
abstract checked). Proposition 3 supplies the needed covariance proof
here. The common-field covariance (8) alone supplies neither the seed
restriction nor the retained-pointer disturbance law. Even separate
one-pair bounds on every prior leave the joint condition (22) to be
established.

## 5. Constants, complementarity and the Newton comparison

The positive constant that a closure law would preserve is the resonant
$\zeta=\kappa$. Under the additional SED/Planck identification in the
[revised link](sed-zeta-radiation-link.md), §3 (local full-read),

$$\kappa=\frac{\hbar}{2}=\frac{h_P}{4\pi},\qquad
h_*=2\zeta=2\kappa=\hbar
=\frac{(\pi^4/15)^{1/3}}{2\pi}\,h_{\rm rad}. \tag{23}$$

That thermal identification retains the conditions and disputed source
status stated there. Theorem U supplies the radiation unit independently
of any record restriction. Theorem B$'$ in the
[fifth-postulate note](principia-fifth-postulate.md), §4 (local full-read),
classifies symplectically invariant, noise-closed one-pair Gaussian
classes. Theorems 1 and 2 show why closure under *conditioning on retained
records* is an additional requirement beyond that classification.

For Proposition 3's restricted Gaussian instruments and the affine
generators of [Theorem F](newton-indeterminacy-routes.md), §4 (local
full-read), Lemma G supplies statistical speed constant $h_*=2\kappa$.
Subject to Theorem F's remaining comparison hypotheses,

$$\frac s8\sum_j\sup\Delta D_j+\frac J2\sum_j\sup\Delta X_j
\ge2\kappa\arcsin(1-2\epsilon),\qquad
s=\frac{F\tau^2}{2m},\quad J=F\tau. \tag{24}$$

The passive retained readings of Theorem 1 fall outside this restricted
class. Their small posterior by itself says nothing about erasing the
unconditional impulse spread charged in (24). The unrestricted,
non-Gaussian comparison requires the further operator/statistical-speed
premises of Theorem C and Theorem F respectively.

**Theorem E's window bound.** Write $z_\epsilon=
\Phi^{-1}(1-\epsilon/2)$ for $0<\epsilon<1/2$, where $\Phi$ is the
standard normal distribution function. For any conditional Gaussian,
windows centred at its conditional means with half-widths
$a=z_\epsilon\sigma_q$ and $b=z_\epsilon\sigma_p$ contain the respective
variables with probability $1-\epsilon$. The diagonal estimates in
Theorem 1 give

$$ab\le z_\epsilon^2\left(
\frac{\sigma_Y\sigma_P}{G}
+\frac{\sigma_Y\sigma_{Z_2}}B\right)\longrightarrow0. \tag{25}$$

The canonical scaling (7) leaves this product unchanged. Thus the
unrestricted classical record class can violate, at any supplied
$\hbar>0$, the necessary quantum condition

$$\lambda_0\!\left(\frac{ab}{\hbar}\right)
\ge(1-2\epsilon)^2$$

of [Theorem E](principia-fifth-postulate.md), §6b (local full-read).
Equation (25) bounds the product of marginal spreads directly, so it
also covers correlated posteriors whose determinant alone would give
insufficient control of axis-aligned windows.

Under (22) with $\hbar=2\kappa$, every Gaussian covariance has a
Gaussian quantum-state realization: a symplectic transform of thermal
oscillator states with covariance eigenvalues at least $\hbar/2$.
Consequently Theorem E applies to those Gaussian marginals. Extending
that statement to all non-Gaussian classical states would require an
additional state/instrument principle.

Finally the [parallel-record note](newton-record-parallel-move.md),
Proposition 1 (local full-read), gives the *forgotten* quantum record's
momentum variance $\hbar^2/(4\sigma^2)=\kappa^2/\sigma^2$ under (23).
Equation (20) requires this same cost when recording a pointer that
will be reused. Forgetting a reading and preserving it for a later
kick estimate impose different conditioning questions; Proposition 3
states a law that covers both.

## 6. Consequence for STATE

The Newton task advances from testing stationary radiation to deriving
an admissible recording law. Shared Gaussian driving, including its
cross correlations and radiation damping, allows the two-pointer
counterexample at every fixed finite cutoff when classical retained
readouts and the stated controls are available. The next physical
premise to justify is a restriction such as (20)--(22) for reusable
pointers and their memories, or an electrodynamic instrument constraint
that excludes this protocol and proves an equally strong closed bound.
The conditional scale identification and the unregulated momentum
problem retain the scope stated in the revised SED link.
