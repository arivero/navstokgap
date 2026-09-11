# A shared record budget changes the composition exponent

For two identical bounded-force constituents sharing one quadratic record-error
budget, the centre experiment has exactly the one-body precision
epsilon/sqrt(2). Retaining both records gives the same centre-coordinate
minimax risks as retaining their average. The long-time canonical risk product
is 2^(1/4) times the one-constituent product, replacing R12's factor 2.

R14, 2026-09-11. This is a deterministic information model. Fix m,F,epsilon>0,
known constituent initial phases, independent arbitrary measurable forces
|f_i|<=F, and complete records y_i=q_i+e_i through T>=0. Forces and errors
can be chosen independently. There is no stochastic law, speed ceiling or
measurement back-reaction. Q and P are separate scalar minimax absolute errors
for centre position R and canonical total momentum Pi; H=QP has action units,
without a 2 pi normalization. The specified error budget is an apparatus
premise whose physical origin remains to be supplied.

## 1. Two constituents: the exact projection and lift

Impose, at every observed time,

$$e_1(t)^2+e_2(t)^2\le\varepsilon^2.$$

Write R=(q_1+q_2)/2, Pi=p_1+p_2, and E=epsilon/sqrt(2).
The averaged record Y=(y_1+y_2)/2 has error at most E by Cauchy--Schwarz,
and R obeys a one-body equation of mass 2m and force bound 2F.
Conversely every such one-body force f and error e is realized by
f_1=f_2=f/2 and e_1=e_2=e. Their budget is 2e^2<=epsilon^2.
Prescribed initial phases sum to the prescribed centre phase. Thus the
aggregate-record experiment is exactly the one-body image (2m,2F,E).

For the full-record experiment, subtract each known inertial path. The central
compatible fibre consists of displacements z_i with zero initial phase,
|m z_i''|<=F and z_1(t)^2+z_2(t)^2<=epsilon^2. Their average z has
|z|<=E and |m z''|<=F. Conversely every scalar path with these properties
lifts by z_1=z_2=z, while errors e_i=-z hide both complete records.
Hence the projected central fibre is exactly that same scalar path class.

R11's half-difference proof applies to this convex symmetric error set as
well as a box: the half-difference of two compatible paths lies in the
central fibre, and opposite central paths share the zero record. Scalar
compatible-interval midpoint estimators attain its radius. Therefore **both
information protocols have exactly the same centre risks**. This equality
uses the identical constituent force/mass parameters and the synchronous lift.

## 2. All finite horizons

Use R13's one-body function

$$V(s)=\begin{cases}
s,&0\le s\le\sqrt2,\\
\sqrt{2s^2+4}-s,&\sqrt2\le s\le4,\\
2,&s\ge4.
\end{cases}$$

With s=T sqrt(F/(mE)), the exact two-constituent risks are

$$\boxed{Q=E\min(s^2/2,1),\qquad
P=2\sqrt{mFE}\,V(s).}$$

R13's scalar extremizer lifts synchronously, so each branch respects the
quadratic budget at every time, not just at the endpoint. Both coordinate
support extrema are attained by the same path. At a blind delay b>=0,

$$P_b=P+2Fb,\qquad Q_b=Q+bP/(2m)+Fb^2/(2m).$$

For T>=4 sqrt(mE/F), put H_1^sat=2 sqrt(mF) epsilon^(3/2). Then

$$H=4\sqrt{mF}\,E^{3/2}=2^{1/4}H_1^{\rm sat}.$$

At T<=sqrt(2mE/F), H=F^2 T^3/m, twice the early one-constituent
product. At fixed T>0, H tends to zero as epsilon tends to zero.
Products here multiply coordinate minimax risks; they are not simultaneous
lower bounds on the two realized errors of every individual motion.

## 3. Norm geometry controls the copy-count law

The same proof covers n identical constituents with a fixed pointwise budget

$$\left(\sum_{i=1}^n|e_i(t)|^r\right)^{1/r}\le\varepsilon,
\qquad 1\le r<\infty.$$

For r=infinity use max_i |e_i|<=epsilon and set 1/r=0. The elementary
norm inequality gives |n^(-1) sum e_i|<=epsilon n^(-1/r).
Equal errors attain it. The synchronous force/path lift gives both exact
aggregate image and exact projected central fibre, just as above. Consequently,
with E_n=epsilon n^(-1/r) and s_n=T sqrt(F/(mE_n)),

$$Q_n=E_n\min(s_n^2/2,1),\qquad
P_n=n\sqrt{mF E_n}\,V(s_n),$$

$$H_n(T)=n H_1(T;E_n),\qquad
\boxed{H_n^{\rm sat}=n^{1-3/(2r)}H_1^{\rm sat}.}$$

The saturation condition is T>=4 sqrt(m epsilon/F) n^(-1/(2r)).
For any fixed T>0 and finite r, sufficiently many copies meet it.
The quadratic case gives n^(1/4); the Cartesian case gives n; r=1 gives
n^(-1/2). At **r=3/2** the saturated product is invariant under copy count.
This supplies a classical, explicitly budgeted constant-product example.
Its value still depends on m,F,epsilon, and its copy-count invariance was
selected by the apparatus norm. It supplies neither A08's independent
preparation closure nor a universal quantum phase constant.

## 4. The physical question after the calculation

Changing from Cartesian to shared error freedom changes the scaling exponent;
it does not by itself explain a positive precision floor. A fixed total budget
also differs from allocating one fresh budget to each independently composed
subsystem. The n-copy family must retain that distinction when interpreted
as a physical apparatus.

The next useful test is **apparatus-budget composition**: partition identical
constituents into blocks, give each block its own stated budget, and compare
that experiment with one shared budget for the whole. Specify the readout
resources that would equate them. This tests whether r=3/2 invariance survives
regrouping without a hidden change of apparatus preparation.

Proof inputs are R11's symmetric-fibre principle, R13's exact one-body radii
and finite-dimensional norm duality. [B45](../references/batches/B45.md)
records bounded prior-art coverage and [the written review](../reviews/shared-budget-B45.md)
accepts C084–C085 as derived consequences, with novelty unassessed.
