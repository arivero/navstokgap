# A finite mechanical clock and four persistent readout records

A fixed finite-mass classical apparatus can reconstruct the initial state of
R04's receiver with vanishing error and disturbance over a fixed positive
observation time. Five apparatus coordinates suffice: one clock and four free
probe pointers. The interaction is a smooth coordinate potential, all kinetic
terms are positive, and force and coupling ceilings are uniform. The closing
limit weakens the coupling and concentrates the incoming apparatus preparation;
it retains exact access to four final momentum records. Thus these upper
resource bounds alone do not select a positive accuracy–disturbance action.

This is a delayed reconstruction of a known deterministic trajectory. It
supplies four physical records from which arbitrarily fine samples may be
computed, with one fixed observation latency. It does not perform a fresh
measurement at every refined cut. Preparation precision, final record access,
and knowledge of the receiver dynamics are explicit resources of the result.

Proof status: C068–C069 accepted by written derivation and coordinator review,
2026-09-10. Literature status: derived consequences, novelty unassessed;
[B37](../references/batches/B37.md) and
[review](../reviews/autonomous-readout-B37.md) record the bounded audit.

## 1. Fixed class and autonomous Hamiltonian

Use the reduced three-body receiver of [R04](three-body-cut-memory.md), with
$z=(x,P,y,Q)$, positive masses $\mu=3m/2$, $\nu=m/2$, and

$$H_s(z)=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
 +\frac a2x^2-gxy+\frac d2y^2,
\qquad (a,g,d)=(9k/4,3k/4,5k/4).$$

Fix $m,k,E,T>0$ and initial receiver support $H_s=E$. The reference motion
is $z^0(t)=\Phi_tz_0$ on $0\le t\le T$. The physical tagged momentum is
$2P/3$; all products below use canonical $P$. Add a clock $(s,p_s)$ of
mass $M_c>0$ and four probe pairs $(q_j,\pi_j)$ of fixed masses $M_j>0$.
All coordinates have length units and all conjugate momenta momentum units;
the phase domain is $\mathbb R^{14}$. The added total mass
$M_c+\sum_j M_j$ is fixed.

Let $X(x)$ and $R(q)$ be smooth bounded functions with bounded derivatives,
equal to $x$ and $q$ respectively on fixed neighbourhoods containing the
reference receiver trajectory and zero probe position. They have length units.
For fixed dimensionless smooth compactly supported functions $f_j(s)$, put

$$H_\lambda=H_s+\frac{p_s^2}{2M_c}
 +\sum_{j=1}^4\frac{\pi_j^2}{2M_j}
 +\lambda K\sum_{j=1}^4 f_j(s)X(x)R(q_j),
\qquad 0<\lambda\le\lambda_0,$$

where $K>0$ is a fixed stiffness and $\lambda$ is dimensionless. There is no
external time dependence. A fixed additive constant can make the Hamiltonian
nonnegative, since the interaction is uniformly bounded below. Its kinetic
quadratic form is positive definite. The reduced receiver coupling is an
internal-coordinate interaction; no spatial locality or finite signal speed
is assumed for this finite-dimensional potential model.

Fix a nominal clock trajectory $s^0(t)=s_0+vt$, $v>0$. Place all supports of
$f_j$ strictly inside $(s_0,s_0+vT)$ with a fixed endpoint margin. Their
shapes, widths and derivatives are fixed before taking any limit. Preparation
has full rectangular support of dimensionless half-width $b>0$ about
$q_j=\pi_j=0$, $s=s_0$, $p_s=M_cv$, using fixed length and momentum units.
An independent uniform density on this rectangle is admissible. Each $b>0$
has positive phase volume. The class permits $b\downarrow0$; there is no
lower phase-volume or temperature constraint. Energy, coordinate and momentum
upper bounds are fixed across this class. In particular the clock has fixed
positive nominal energy $M_cv^2/2$, which is never cooled to zero.

The interaction forces are bounded globally by constants independent of
$\lambda,b$, including the clock force involving $f'_j$. The harmonic
receiver forces are uniformly bounded on the admitted trajectories: conservation
of $H_\lambda$, bounded interaction and positive receiver quadratic energy
bound all receiver positions and momenta. Thus a common finite total force
ceiling and speed ceiling hold on this preparation class. A global ceiling
outside the admitted energy class is not asserted for the harmonic springs.
Any prescribed positive apparatus-force ceiling can be met by reducing
$\lambda_0$ after fixing the shapes. The constants may depend on $E,T$, all
masses, $K$, the cutoffs and the chosen pulse shapes.

## 2. Four fixed-duration signals determine the receiver state

The scalar history $x^0(t)=e_x\Phi_tz_0$ observes all four receiver
coordinates. At $t=0$ the first four derivative rows are

$$
x=x_0,\qquad \dot x=P_0/\mu,\qquad
\ddot x=(-a x_0+g y_0)/\mu,\qquad
x^{(3)}=-aP_0/\mu^2+gQ_0/(\mu\nu).
$$

The map from $z_0$ to these four derivatives is triangular with diagonal
$1,1/\mu,g/\mu,g/(\mu\nu)$ and is invertible since $g>0$.
Consequently the analytic row functions $e_x\Phi_t$ span four dimensions on
any open time interval: a vector annihilated by every row on an interval has
an analytic output identically zero and hence all four initial coordinates
zero. Four distinct times $t_j\in(0,T)$ can therefore be selected with
independent evaluation rows.

Choose nonnegative smooth bumps $f_j(s_0+vt)$ near those times, with
disjoint supports and positive time integrals $c_j$. Their widths can be
chosen positive and sufficiently small that the matrix

$$\mathcal A_{j\cdot}=K\int_0^T f_j(s_0+vt)e_x\Phi_t\,dt$$

is invertible: after dividing row $j$ by $Kc_j$, its limit as the design width
shrinks is the independent evaluation row. Continuity of the determinant
then gives a fixed nonzero width. This existence argument selects the design
once; no pulse width shrinks with $\lambda$, $b$ or the output mesh. Small
signal gains or poor conditioning enter the fixed constant
$\|\mathcal A^{-1}\|$; there is no uniform bound as $T\downarrow0$.
The rows carry the appropriate units so that $\mathcal A z_0$ is momentum.
All following norms use the fixed component units of section 1.

## 3. Finite-duration motion, clock reaction and stored records

Uniformly over receiver data and allowed apparatus preparation, the probes,
receiver disturbance and clock deviation obey

$$\sup_{[0,T]}(|q_j|+|\pi_j|)=O(b+\lambda),$$
$$\sup_{[0,T]}\|z(t)-z^0(t)\|=O(\lambda b+\lambda^2),$$
$$\sup_{[0,T]}\bigl(|s(t)-s^0(t)|+|p_s(t)-M_cv|\bigr)
 =O(b+\lambda^2).$$

Here and below component sums mean dimensionless values. To prove these
bounds, the global interaction-force bound gives
$\dot\pi_j=O(\lambda)$; integrating it and $\dot q_j=\pi_j/M_j$
gives the first estimate. For sufficiently small $\lambda,b$, the cutoffs
are therefore linear along every admitted trajectory. Hamilton's equations
then give exactly

$$\dot\pi_j=-\lambda K f_j(s)x,\qquad
\dot P=-ax+gy-\lambda K\sum_j f_j(s)q_j,$$
$$\dot p_s=-\lambda K\sum_j f'_j(s)xq_j.$$

Variation of constants in the receiver equations gives the second estimate.
The clock equation has force $O(\lambda b+\lambda^2)$, which together with
its initial uncertainty gives $O(b+\lambda^2)$ over fixed $T$. Uniform
energy bounds and cutoff margins justify these estimates by continuation.
This proves the bounds without treating the clock as an unaffected external
parameter. In particular $p_s>M_cv/2$ for small enough parameters, so the
clock traverses every pulse and leaves their supports before $T$.

The four final momenta satisfy

$$\pi_j(T)=\pi_j(0)-\lambda(\mathcal A z_0)_j
 +O(\lambda b+\lambda^3).$$

Indeed replace $s(t)$ and $x(t)$ in the integrated force by $s^0(t)$ and
$x^0(t)$; bounded derivatives of $f_j$ give integrand error
$O(b+\lambda^2)$, and multiplication by $\lambda$ gives the stated
remainder. Once the clock has passed all supports, each $\pi_j$ and $p_s$
is exactly conserved. The clock continues forward, so there is no later
recoupling. These momenta are persistent mechanical records although their
conjugate positions subsequently drift. The bounded-coordinate resource claim
concerns the fixed observation horizon, not unlimited storage space.

## 4. Reconstruction, action product and output refinement

Assume the final four momentum records can be accessed exactly. Define the
calibrated estimate

$$\widehat z_0=-\mathcal A^{-1}\frac{\boldsymbol\pi(T)}{\lambda}.$$

The incoming momenta are unknown but bounded by $O(b)$, so

$$\sup\|\widehat z_0-z_0\|
 =O(b/\lambda+b+\lambda^2).$$

Choose $b=\lambda^3$. Then reconstructed initial-state error and receiver
trajectory disturbance are both $O(\lambda^2)$. This choice keeps all masses,
the receiver's initial preparation, observation duration, clock mean energy,
pulse geometry and upper resource ceilings fixed. Probe incoming phase-volume
and clock uncertainty shrink; coupling strength decreases within one fixed
upper bound. A fixed nonzero coupling or a lower preparation-width constraint
is a different class.

For a precise action-valued observable put

$$\epsilon_x=\sup|\widehat x_0-x_0|,\qquad
D_P=\sup_{0\le t\le T}|P(t)-P^0(t)|,\qquad
\mathcal U=\epsilon_xD_P.$$

Suprema include all permitted receiver and apparatus initial data. This is an
accuracy–disturbance product for reconstruction of initial canonical position
and finite-horizon canonical momentum disturbance, in units $ML^2/T$, without
a $2\pi$ factor. It is not R05's intrinsic single-shear support product.
For fixed length and momentum units $L_*,P_*$,

$$0\le\mathcal U\le C L_*P_*\lambda^4\longrightarrow0.$$

Thus no uniform positive bound on this specified observable follows from
fixed finite mass, finite duration, bounded forces and positive kinetic energy
within this preparation and record-access class. The fixed nonzero clock
energy does not change the conclusion.

For any partition of $[0,T]$, report
$\widehat z(t_i)=\Phi_{t_i}\widehat z_0$. Boundedness of $\Phi_t$ gives
uniform $O(\lambda^2)$ error relative to both the unmeasured reference and
the actual receiver. Refining only the reporting partition uses the same four
records and leaves all old estimated nodes unchanged. Taking also
$\lambda\downarrow0$ changes the experiment but improves that common bound
independently of the mesh. This is reconstruction after latency $T$ with
known equations; causal repeated interventions, unknown forcing and model
error are not covered by the theorem.

If final record errors have component support width at most $r$ in fixed
momentum units, the same estimator instead has bound
$O((b+r)/\lambda+b+\lambda^2)$. For this scheme $r=O(\lambda^3)$
suffices to retain the stated rate. A fixed nonzero $r$ prevents this particular
weak-coupling estimate from proving convergence. That upper-bound observation
is not an impossibility theorem for every estimator or apparatus.

## 5. Source connection and next research obligation

Theurel's [existing B36 audit](../references/batches/B36.md) supplies the
conserved-momentum record and isolates thermal preparation as an action-scale
input; its delta interaction does not supply this finite-duration clock.
Hermann–Krener's observability construction, routed through
[B34](../docs/batches/B34/receiver-memory-source-companion.md), motivates using
four output histories instead of shrinking R04's two-sample baseline. The
explicit derivative-rank argument, autonomous equations and bounds above are
written derivations for this apparatus.

R06's bounded result advances the exclusion-of-zero test by identifying a
finite apparatus counterclass with delayed records. The next task R07 is to
fix a physically justified preparation or record-resolution restriction and
require causal new information at shrinking latency. Specify that information
task before seeking a lower bound; distinguish a latency or precision cost
from a uniform positive action product. Theorem acceptance and the bounded
prior-literature comparison are recorded separately in the ledger and review.
