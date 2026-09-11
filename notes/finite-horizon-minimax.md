# Exact finite-horizon phase recovery

Known initial position and momentum give three momentum-risk regimes under a
complete noisy position history: free acceleration, a two-arc transient, and
record-limited saturation. Position risk saturates earlier. Composition can
therefore lose position information as well as momentum information during
the transient.

R13, 2026-09-11. Let m,F,epsilon be positive, T >= 0, with known initial
state, arbitrary measurable forces |f| <= F, and records y(t)=q(t)+e(t)
for every t in [0,T], |e(t)| <= epsilon. There is no speed ceiling, stochastic
law or measurement disturbance. Subtract the known inertial trajectory.
The separate scalar minimax absolute errors are Q for position and P for
canonical momentum. H=QP has action units, with no 2 pi normalization.
Proof and literature status are recorded in C082–C083 and B44.

## 1. The exact radii

Put a=F/m, tau=sqrt(epsilon/a), and s=T/tau. Then

$$Q(T)=\varepsilon\min\{s^2/2,1\},\qquad
P(T)=\sqrt{mF\varepsilon}\,V(s),$$

$$\boxed{V(s)=\begin{cases}
s,&0\le s\le\sqrt2,\\
\sqrt{2s^2+4}-s,&\sqrt2\le s\le4,\\
2,&s\ge4.
\end{cases}}$$

Both coordinate extrema are attained by the same central-fibre motion.
Consequently a blind interval b >= 0 after the last record has exact risks

$$P_b=P(T)+Fb,\qquad
Q_b=Q(T)+bP(T)/m+Fb^2/(2m).$$

Here T is the observed horizon and T+b the prediction time. These products
are products of global coordinate risks, not lower bounds on both errors
for every individual motion.

## 2. Written proof through bounded-curvature paths

R11's symmetric-fibre argument reduces each scalar minimax risk to the
largest endpoint deviation of a path hidden by the zero record. Scale time
by tau and position by epsilon. The admissible paths satisfy
x(0)=x'(0)=0, |x''|<=1 almost everywhere, and |x(t)|<=1 on [0,s].
Let v=x'(s)>=0; symmetry covers the other sign.

First v<=s. For fixed v the acceleration u obeys integral u=v. Write
u=2w-1 with 0<=w<=1 and integral w=(s+v)/2. The endpoint position
is integral (s-t)u(t)dt. Its minimum places w=1 on the final interval
of length (s+v)/2, since the weight s-t is decreasing. For a direct proof, let w_* be that final-interval indicator and c its
left endpoint. Since integral (w-w_*)=0 and
[(s-t)-(s-c)](w-w_*) >= 0 pointwise, integrating proves the minimum. Hence

$$x(s)\ge\frac{v^2+2sv-s^2}{4},\qquad
v\le\sqrt{2s^2+4}-s.$$

Finally, for t in [s-v,s], x'(t)>=v-(s-t). This interval exists because
v<=s, and integration gives

$$2\ge x(s)-x(s-v)\ge v^2/2,\qquad v\le2.$$

These three upper bounds have lower envelope V(s): the first and second
meet at sqrt(2), the second and third at 4; the middle expression increases
from sqrt(2) to 2 on that interval. The endpoint position separately obeys
x(s)<=min(s^2/2,1).

For s<=sqrt(2), take u=+1 throughout. For sqrt(2)<=s<=4, set
h=(s-V(s))/2=s-sqrt(s^2/2+1). Take u=-1 for h time and then u=+1
until s. The endpoint has x(s)=1 and x'(s)=V(s). Its minimum occurs
at time 2h and equals -h^2. Since 0<=h<=1 and 2h<=s, the entire
path stays in [-1,1]. For s>=4, wait at zero for s-4, apply u=-1
for one unit, then u=+1 for three units. This reaches -1 with zero
velocity after the first two active units, then ends at +1 with velocity 2.
Thus every upper bound is attained, including both regime junctions and s=0.

Opposite paths admit the same inertial record and share the exact initial
state. Compatible-interval midpoint estimators give matching upper minimax
bounds by R11. Because one extremizer maximizes position and momentum with
the same sign, appending force +F for the blind interval attains both displayed
prediction bounds. The triangle inequality and the force bound give the
matching upper bounds on the central fibre.

## 3. Composition at every horizon

Let constituent i have (m_i,F_i,epsilon_i) and the same observed T. Allow
the Cartesian product of force/error classes, as in R12. Set
M=sum m_i, F_Sigma=sum F_i, E=sum m_i epsilon_i/M. With every constituent
record retained the exact centre and total-momentum radii are

$$Q_A=\frac{\sum_i m_iQ_i(T)}M,\qquad P_A=\sum_iP_i(T).$$

With only the centre record retained, R12's proportional force/error lift
works at every T. Thus Q_B,P_B are exactly section 1's single-body formulas
with (m,F,epsilon)=(M,F_Sigma,E). Information inclusion gives Q_B>=Q_A
and P_B>=P_A without any common-regime assumption.

There is a precise transient position-loss criterion. Put
A_i=F_iT^2/2 and B_i=m_i epsilon_i. Then

$$M Q_A=\sum_i\min(A_i,B_i),\qquad
M Q_B=\min(\sum_iA_i,\sum_iB_i).$$

The difference is strictly positive exactly when at least one A_i<B_i
and at least one A_j>B_j. To see this, if sum A_i<=sum B_i the difference
is sum (A_i-B_i)_+; in the other case it is sum (B_i-A_i)_+.
The weak-side total inequality forces the opposite strict sign whenever the
sum is positive. Equality cases with A_i=B_i cause no ambiguity.

For a concrete mixed-regime example, choose equal masses m and precision
epsilon, F_1=F and F_2=16F, at T=sqrt(m epsilon/F). Then s_1=1,
s_2=4, while the aggregate s_B=sqrt(17/2). The exact radii are

$$Q_A=\tfrac34\varepsilon,\qquad Q_B=\varepsilon,$$
$$P_A=9\sqrt{mF\varepsilon},\qquad
P_B=(\sqrt{714}-17)\sqrt{mF\varepsilon}>P_A.$$

Indeed sqrt(714)>26 since 714>676. The products are respectively
(27/4)sqrt(mF) epsilon^(3/2) and
(sqrt(714)-17)sqrt(mF) epsilon^(3/2). The second exceeds the first.
For identical copies H_A=H_B=n H_1(T) at every horizon.

## 4. Limits and next physical premise

At fixed positive m,F,epsilon and T down to zero, H=F^2T^3/(2m).
At fixed T>0 and epsilon down to zero, H=2 sqrt(mF) epsilon^(3/2)
once T>=4 sqrt(m epsilon/F). The gap closes in either limit. The precision
and force parameters set the scale; the finite preparation time sets when
it is reached. R11's sufficient time 4 tau is the exact earliest momentum
saturation time for this known-initial-state experiment.

The source capsule is Seeber–Haimovich's prepared bounded-curvature pair
(B42) plus R12's product-fibre and aggregate-image proofs. The finite-horizon
rearrangement supplies the missing transient. The next bounded task R14
should restrict the record errors by one explicit shared apparatus constraint,
for example sum_i (e_i/epsilon_i)^2<=1 pointwise, and derive the changed
central fibre and aggregate image for two identical constituents. This tests
which composition conclusion depended on freely aligned full-width errors.
