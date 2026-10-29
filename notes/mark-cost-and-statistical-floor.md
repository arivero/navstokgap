# Marking Newton's comparison: classical widths and quantum probe costs

Two conditional recording theorems use different notions of error. In the
classical independent-box model, a finite marking protocol distinguishing
constant force from free motion requires $F^2\tau^3>9m\kappa$ when every
resolution–recoil width product is at least $\kappa$. A specified balanced
two-mark construction succeeds above $36m\kappa$. In the non-adaptive Gaussian
model, tests invariant under unknown initial position and velocity instead
obey the sharp bound $\tau\Delta E\ge48z_{1-\epsilon}^2\kappa$.
A quantum position-coupled probe supplies the **standard-deviation** product
$\delta\Delta\ge\hbar/2$; its correlations change the Gaussian threshold.
None of these statements derives physical $\hbar>0$ from classical dynamics.

The hypotheses are integral to each theorem. Hard support widths, standard
deviations, conditional posterior uncertainty and the hybrid-state disturbance
spreads of [general record bounds](record-distance-path-length.md) are separate
quantities. This treatment incorporates the classical marking stages,
body-independent-noise classification and Gaussian unread-record channel.
Written model/coordinator checks are internal; the uncertainty and Gaussian
channel ingredients are established, and no literature-priority claim is made.

## Geometry and the independent-box record model

For mass $m>0$, constant force $F>0$ and duration $\tau>0$, write

$$P(t)=\frac{Ft^2}{2m},\quad s=P(\tau),\quad J=F\tau,\quad
\tau\Delta E=Js=\frac{F^2\tau^3}{2m},\quad
A_{\rm inertial,fall}=\frac{vF\tau^3}{6m}.$$

Thus $(3F/v)A=\tau\Delta E$, for horizontal speed $v>0$. Unmarked polygon
impulses, sagittas and areas vanish with mesh, with
$\sum_jvF\tau_j^3/(6m)\le vF\tau|\pi|^2/(6m)$ while
$2mP(\tau_j)/\tau_j^2=F$. No geometric inconsistency supplies a floor.
The historical/action conventions are in
[Newton insertion](newton-insertion-action.md).

Marks occur at $0=t_0<\cdots<t_k\le\tau$. A datum is an interval of
length $\delta_i>0$ containing position; the initial momentum difference
is bounded by $\Delta_0$, and later impulse differences by $\Delta_j$.
The **model assumes the full independent adversarial feasibility box**:
two histories share a record exactly when some $x\in\mathbb R$,
$|w|\le\Delta_0/m$ and $|r_j|\le\Delta_j$ satisfy

$$|P(t_i)+d(t_i)|\le\delta_i,\qquad
d(t)=x+wt+\frac1m\sum_{j\ge1}r_j(t-t_j)_+.$$

A statement about marginal widths alone does not imply this independent
feasibility model if physical correlations remove allowed combinations.
The last recoil is irrelevant to recorded positions. Assume
$\delta_j\Delta_j\ge\kappa$ for every available mark.

**Separation certificate.** The protocol decides in the worst case iff some
$\mu_0,\ldots,\mu_k$ with $\sum_i\mu_i=0$ satisfy

$$\sum_i\mu_iP(t_i)>
 \sum_i|\mu_i|\delta_i+\frac1m\sum_j\Delta_j|S_j|,\qquad
S_j=\sum_{i>j}\mu_i(t_i-t_j).$$

Indeed the feasible displacement set is the sum of a line and the image of
a compact box, hence closed convex. Strict separation from the compact
position-data box eliminates the free $x$ by $\sum\mu_i=0$. Minimizing
independently over $w,r_j$ gives exactly the displayed support function;
conversely pairing a feasible history with the certificate contradicts it.
Here $S_0=\sum_i\mu_it_i$ and $S_k=0$.

Define the continuous piecewise-linear function

$$T(u)=\int_u^\tau\sum_{i:t_i>w}\mu_i\,dw.$$

It is constant before zero, zero after $\tau$, has slope jump $\mu_j$ at
$t_j$, and $T(t_j)=S_j$. Integration by parts gives

$$\sum_i\mu_iP(t_i)=\frac Fm\int_0^\tau T,\qquad
\sum_j\mu_jS_j=-E,\qquad E=\int_0^\tau T'^2.$$

The boundary terms vanish because $P'(0)=0$, $T(\tau)=0$ and $T'$ is
zero outside the interval. Termwise AM–GM bounds the certificate cost below
by $2\sqrt{\kappa/m}\sum_j\sqrt{|\mu_jS_j|}\ge2\sqrt{\kappa E/m}$.
Also $|T(u)|\le\sqrt{\tau-u}\sqrt E$, so
$\int T\le(2/3)\tau^{3/2}\sqrt E$. A strict certificate has positive
$\int T$, and division proves

$$\boxed{F^2\tau^3>9m\kappa.}$$

If the model offers a preparation mark
$\delta_0=\sqrt{\kappa\tau/m}$, $\Delta_0=\kappa/\delta_0$, and a
terminal mark $\delta_1\le\sqrt{\kappa\tau/m}$, the inertial prediction
interval has width $2\sqrt{\kappa\tau/m}$. It and its forced translate
cannot share a terminal datum when $s>3\sqrt{\kappa\tau/m}$, giving
$F^2\tau^3>36m\kappa$. With this availability at every duration and
$\kappa>0$, the infimum deciding duration obeys

$$9m\kappa\le F^2\tau_*^3\le36m\kappa,\qquad
\frac92\kappa\le\tau_*\Delta E(\tau_*)\le18\kappa,$$
$$\frac{3v\kappa}{2F}\le A(\tau_*)\le\frac{6v\kappa}{F}.$$

The last line corrects the factor-two area conversions in the earlier
standalone derivation. A zero infimum of products **alone** does not imply
arbitrarily short deciding protocols: the balanced widths may be unavailable,
or a fixed minimum position resolution may remain. The zero-floor conclusion
requires access to appropriately balanced arbitrarily small positive costs.
The constants $9$ and $36$ are proved bounds, not an optimal threshold.

On a subwindow whose initial momentum is wholly unknown, the certificate
additionally has $\sum_i\mu_it_i=0$. The same proof gives
$F^2(t_b-t_a)^3>9m\kappa$ when only its own marks are used. This is a
necessary condition for exhibiting force from that window, not a cessation
of mathematical refinement or a sufficient decision criterion.

## Determinate probes and the historical premise

For freely travelling classical probes with known incoming momentum,
momentum conservation transfers uncertainty in outgoing momentum to recoil.
Two recorded positions, separated by a freely chosen flight distance $D$,
with bounded resolutions $\delta,\delta_s$, determine outgoing transverse
momentum to width at most

$$p_\parallel(\delta+\delta_s)/D\longrightarrow0.$$

This defeats an irrecoverable-recoil premise if those remote records are
admissible. The infimum recoil width is zero; exact zero at a finite distance
is not asserted. With a remaining minimum resolution $\Lambda$, the fixed-force
time threshold need not vanish. In the simple two-mark construction,
$s>3\Lambda$ suffices after negligible recoil, giving an action scale
$\sqrt{54mF\Lambda^3}\to0$ as $F\downarrow0$. The class and parameter being
varied matter. The [complete apparatus](autonomous-finite-readout.md) and
[calibration fibres](calibration-tolerance-recovery.md) supply separate finite
mechanical tests of preparation and record assumptions.

Newton's *Opticks* supplies a measured interval of fits
$\Lambda=1/89000$ inch and a corpuscular hypothesis. The
[held companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md)
contains Book II Part III Definition/Props. XII and XVIII, Book II Part I
Obs. 13 and Queries 1 and 29 (passages). A historical reconstruction posits
M1, a corpuscular momentum scale $p$; M2, a gauge resolution at least
$\Lambda$; and the **additional** M3,
$\delta\Delta\ge\Lambda p$ even after subsequent records. Fits are
longitudinal periods, not measured transverse standard deviations, and
corpuscle size does not determine a momentum spread. M3 is therefore a modern
record-level interpretation, not a theorem or explicit assertion of Newton.
The remote-screen example shows why deterministic transport plus sufficiently
rich readout does not derive it. A printed periodic disposition alone settles
neither an operational uncertainty principle nor its negation.

For the original two-mark protocol, M3 gives prediction width at least
$2\sqrt{\Lambda p\tau/m}$ and hence the necessary
$\tau\Delta E>8\Lambda p$. The three-mark mid-chord calculation instead
gives $F^2\tau^3>64m\Lambda p$, correcting the old factor $128$;
neither is the general sharp protocol theorem. The modern substitutions
$p=h/\lambda$ and $\Lambda=\lambda/2$ give $\Lambda p=h/2=\pi\hbar$.
They are supplied quantum identifications, not the probe standard-deviation
minimum $\hbar/2$. Colour-dependent positive products need not have a
positive infimum without a uniform bound; no cross-colour universality is
inferred from bounded spectral range alone.

## Quantum probe cost and body-independent noise

Supply canonical quantum kinematics, with physical $\hbar>0$. For
$U=\exp(-i\lambda\hat y\hat P_A/\hbar)$,

$$U^\dagger\hat Q_AU=\hat Q_A+\lambda\hat y,\qquad
U^\dagger\hat pU=\hat p-\lambda\hat P_A.$$

Position and probe momentum are unchanged. Thus the **Heisenberg output**
reading error and recoil are

$$\hat N=U^\dagger(\hat Q_A/\lambda)U-\hat y=\hat Q_A/\lambda,
\qquad \hat D=-\lambda\hat P_A,\qquad [\hat N,\hat D]=-i\hbar.$$

The two commutators terminate the BCH series and prove these identities.
For every joint state with finite relevant moments, Robertson–Schrödinger
therefore gives

$$\delta^2\Delta^2-c^2\ge\hbar^2/4,\qquad
\delta=\Delta\hat N,\quad\Delta=\Delta\hat D,\quad
c=\operatorname{Cov}_{\rm sym}(\hat N,\hat D).$$

The coupling cancels. Pure Gaussian probes attain equality; $c$ may be
nonzero. These are operator spreads in a stated state, not an assertion
that no subsequent record can estimate a realized kick. The general
[record bounds](record-distance-path-length.md) specify exactly which
interpolating states are charged.

For any unitary mark and apparatus pointer $\hat R$, define
$\hat N=U^\dagger\hat RU-\hat y$,
$\hat D=U^\dagger\hat pU-\hat p$ and
$\hat X=U^\dagger\hat yU-\hat y$. Expanding the output commutators gives

$$[\hat N,\hat D]=-i\hbar-[\hat y,\hat D]-[\hat N,\hat p].$$

If all three noises strongly commute with the body's Weyl operators, they
are apparatus operators and
$[\hat N,\hat D]=-i\hbar$, $[\hat X,\hat N]=[\hat X,\hat D]=0$.
When $\hat X=0$, the coupling has the form

$$U=(1\otimes U_0)e^{-i\hat y\otimes\hat B/\hbar},\qquad
\hat D=-\hat B,\quad\hat R_0=U_0^\dagger\hat RU_0=\hat N,\quad
[\hat R_0,\hat B]=i\hbar.$$

Here commutation and canonical relations are in the regular strong Weyl
sense, with the common domains needed for moments. To prove the form,
$U$ commutes with position and decomposes into measurable apparatus fibres
$U(y)$. Exponentiating $U^\dagger\hat pU=\hat p+\hat D$ yields
$U(y)^\dagger U(y+a)=e^{ia\hat D/\hbar}$, hence
$U(y)=U_0e^{iy\hat D/\hbar}$ up to choice of representative. The pointer
identity then gives the displayed Weyl relation. Stone–von Neumann with
multiplicity identifies a canonical probe factor $L^2(\mathbb R)\otimes
\mathcal K$. Continuous unbounded canonical pointers are essential.

Even if $\hat X\ne0$, translations generated by $\hat D$ shift $\hat N$
and fix both $\hat D$ and $\hat X$. This is why the recoil-only theorem
in [general bounds](record-distance-path-length.md) extends to this
body-independent class, including correlations across marks. Body-dependent
noise needs the full displacement/disturbance theorem. Source parallels:
Ozawa's independent-intervention setting
([2003](https://doi.org/10.1103/PhysRevA.67.042105), metadata), Arthurs–Goodman
([1988](https://doi.org/10.1103/PhysRevLett.60.2447), metadata), and Davies's
translation-covariant instrument framework (1976, metadata). No priority
claim is made for the classification.

A compactly supported nonzero wavefunction cannot have compact Fourier
support (Paley–Wiener). This obstructs simultaneous hard position/momentum
support in the standard probe model. It does **not** by itself prove a
universal assertion about the difference of noncommuting pre/post momenta
for arbitrary instruments. The old passage from post-mark momentum tails
to an infinite universally defined recoil width was unjustified. No quantum
value is assigned here to the independent-box $\kappa$; quantum results
use the explicit standard-deviation and operational formulations.

## Sharp Gaussian invariant tests and their escape routes

Take non-adaptive marks with

$$R_i=y_0+v_0t_i+\theta P(t_i)+\xi_i
 +\frac1m\sum_{j<i}\iota_j(t_i-t_j),\qquad\theta\in\{0,1\}.$$

The pairs $(\xi_j,\iota_j)$ are centred Gaussian, independent across marks,
with standard deviations $\delta_j,\Delta_j$ and covariance
$c_j=\rho_j\delta_j\Delta_j$. Require tests invariant under both unknown
$y_0,v_0$. On their Gaussian quotient the optimal equal-prior error is
$\Phi(-d/2)$, where

$$d^2=\sup_{\sum u_i=\sum u_it_i=0}
 \frac{(u^TP)^2}{u^T\Sigma u},\qquad
u^T\Sigma u=\sum_j\left(\delta_j^2u_j^2+
 \frac{2c_j}{m}u_jS_j+\frac{\Delta_j^2}{m^2}S_j^2\right).$$

Now $S_j,T,E$ are the same certificate objects with $\mu=u$. The extra
velocity invariance gives $T(0)=T(\tau)=0$, and

$$(\int_0^\tau T)^2\le\tau^3E/12.$$

This follows by integrating against $g(t)=t(\tau-t)/2$, $-g''=1$:
$\int T=\int g'T'$, $\int g'^2=\tau^3/12$. If
$\delta_j\Delta_j(1-|\rho_j|)\ge\kappa_{\rm eff}$, termwise AM–GM gives
$u^T\Sigma u\ge2\kappa_{\rm eff}\sum|u_jS_j|/m\ge2\kappa_{\rm eff}E/m$.
Consequently

$$d^2\le\frac{F^2\tau^3}{24m\kappa_{\rm eff}},\qquad
\tau\Delta E\ge48z_{1-\epsilon}^2\kappa_{\rm eff}.$$

For independent error and recoil, $\kappa_{\rm eff}=\kappa$. Dense marks
whose piecewise-linear $T$ approaches $t(\tau-t)$ attain the bound in the
limit: interior $u_jS_j$ share one sign and are balanced by
$\delta_j|u_j|=\Delta_j|S_j|/m$, while endpoint marks become sharp with
recoils invisible to the invariant statistic. Finite dense approximants
preserve the trade-off. The constant is a limiting sharp constant, not an
attained finite-mark minimum.

Quantum Gaussian probes and linear transport reproduce this statistic's
Gaussian law through positive probe Wigner covariances. The body state
cancels from every invariant statistic and need not be Gaussian. If
$|\rho_j|\le\rho<1$, the quantum covariance inequality gives

$$\kappa_{\rm eff}\ge\frac\hbar2\sqrt{\frac{1-\rho}{1+\rho}},\qquad
\boxed{\tau\Delta E\ge24z_{1-\epsilon}^2\hbar
 \sqrt{\frac{1-\rho}{1+\rho}}.}$$

Three marks at $0,\tau/2,\tau$ with statistic $R_1-2R_2+R_3$ approach
within $4/3$ in action. The signal is $F\tau^2/(4m)$; outer recoils cancel.
For the middle probe, balance $2\delta=\tau\Delta/(2m)$ and choose the
favourable $\rho>0$. The variance becomes
$(\tau\hbar/m)\sqrt{(1-\rho)/(1+\rho)}$, giving the sufficient limiting
threshold $32z_{1-\epsilon}^2\hbar\sqrt{(1-\rho)/(1+\rho)}$. Outer marks
are arbitrarily sharp in this limit. The threshold tends to zero as
$\rho\uparrow1$; correlation control, not covariance area alone, is required.

These are Gaussian, invariant, preparation-ignorant tests. A known contractive
preparation focused at the final time can escape using one sharp readout;
non-Gaussian real grid probes can escape even with $\rho=0$, paying diverging
recoil. Their exact construction and the preparation-aperture counterexample
are in [general bounds](record-distance-path-length.md). Yuen's
[contractive-state mechanism](https://doi.org/10.1103/PhysRevLett.51.719)
(metadata) is an established comparison, not a new literature claim.

## Forgotten Gaussian records and the refinement limit

For Gaussian position Kraus operators

$$M_y(x)=(2\pi\sigma^2)^{-1/4}e^{-(x-y)^2/(4\sigma^2)},$$

forgetting the outcome multiplies the density matrix by
$e^{-(x-x')^2/(8\sigma^2)}$, because direct integration of
$M_y(x)M_y(x')$ completes the square. Fourier transformation to the Wigner
function gives momentum convolution with a centred Gaussian of variance
$v=\hbar^2/(4\sigma^2)$. Position marginals are unchanged. Concurrent
precisions and variances add, while free/constant-force transport shears a
kick at $t_j$ to final displacement $((T-t_j)\delta p/m,\delta p)$.
The final noise covariance is therefore

$$\sum_jv_j\begin{pmatrix}(T-t_j)^2/m^2&(T-t_j)/m\\
(T-t_j)/m&1\end{pmatrix}.$$

For a nested family of retained kicks, $\sum_j\sigma_j^{-2}<\infty$ makes
this matrix converge by absolute domination. A divergent sum gives divergent
momentum variance and no normal momentum-probability limit. For general
triangular refinement arrays, convergence of total precision alone is
insufficient: all three displayed weighted moments must converge. At the
regular rate $\sigma_j^{-2}=\kappa\tau_j$, Riemann sums give the finite
continuous-measurement covariance and momentum diffusion rate
$\hbar^2\kappa/4$, with density-matrix generator
$-\kappa[x,[x,\rho]]/8$. Free-motion Fisher information about initial place
with known momentum is $\sum_j\sigma_j^{-2}$. Harmonic forces rotate kicks
and require the corresponding transport matrix instead.

This channel and continuous limit are standard
([Caves–Milburn 1987](https://doi.org/10.1103/PhysRevA.36.5543), metadata).
The comparison with a gauge parallel move is structural: an observed insertion
adds a pointer and forgetting leaves a channel, whereas an unobserved time
insertion is a different operation. In the classical zero-recoil analogue,
Bayesian updating followed by forgetting returns the prior. That identity
does not establish quantum kinematics or select $\hbar$.

## Consequence for STATE

The classical interval theorem, Gaussian invariant theorem and supplied
quantum probe uncertainty are maintained with their distinct assumptions.
Post-record restrictions, preparation access, Gaussianity and correlation
bounds cannot be silently exchanged. The positive action parameter in the
quantum statements is supplied physical $\hbar$; classical completion,
quantum instruments, universality and scale identification remain separate.
