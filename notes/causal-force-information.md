# New information behind a delayed record

A delayed observer of a particle with an unknown bounded force has a sharp
prediction error, even with perfect records of its earlier state. The joint
position–momentum uncertainty is a curved reachable region with a finite
phase-space area. Both scales come from the force budget and the delay;
refining records strictly before the delay boundary leaves them unchanged.

R07, 2026-09-10: C070–C071 accepted by written proof and
[coordinator review](../reviews/causal-information-B38.md).
[B38](../references/batches/B38.md) identifies established bounded-input
double-integrator machinery; these fixed-time formulas are derived
specializations, with exact prior publication unassessed.

## 1. Experiment and information boundary

Take a particle on the line with mass $m>0$, on an observation window
$[0,\ell]$, $\ell>0$. The state at zero, $(q_0,p_0)$, and the complete
earlier history are known exactly. The observer receives no information about
the force or state after zero before making a prediction at time $\ell$.
This is a delay assumption about the accessible records, not a minimum time
axiom. The future force lies in the fixed admissible class

$$\mathcal F=\{f\in L^\infty([0,\ell]):|f|\le F\text{ a.e.}\},\qquad F>0.$$

Both signs and independent future profiles are allowed by this information
model. The external force is an unresolved input, rather than a previously
reconstructed deterministic receiver. No probability law is assigned to it.
For each $f$ the classical dynamics is

$$\dot q=p/m,\qquad \dot p=f,$$

with unique absolutely continuous momentum and continuously differentiable
position. All experiments share the same accessible past. Constant or
piecewise constant forces are permitted; they create no momentum impulses.
If desired, set $p_0=0$ and choose $F\ell/m<c$ to keep every admitted particle
speed strictly below $c$. A finite propagation law for the recording apparatus
would need its own model.

The exact endpoint increments from inertial prediction are

$$v:=p(\ell)-p_0=\int_0^\ell f(s)ds,\qquad
u:=q(\ell)-q_0-\frac{p_0\ell}{m}
=\frac1m\int_0^\ell(\ell-s)f(s)ds.$$

## 2. Sharp causal prediction bounds

For a deterministic predictor based only on the accessible records, define
separate worst-case absolute errors $R_q=\sup_{f\in\mathcal F}|\widehat q-q_f(\ell)|$
and $R_p=\sup_{f\in\mathcal F}|\widehat p-p_f(\ell)|$.
The two forces $f=+F$ and $f=-F$ give indistinguishable input records and
endpoint separations $F\ell^2/m$ in position and $2F\ell$ in momentum.
The triangle inequality therefore gives

$$R_q\ge\frac{F\ell^2}{2m},\qquad R_p\ge F\ell.$$

The inertial predictor $(\widehat q,\widehat p)=(q_0+p_0\ell/m,p_0)$ attains
both bounds, since the endpoint integrals above have these absolute maxima.
Thus the coordinatewise minimax errors and their product are

$$r_q=\frac{F\ell^2}{2m},\qquad r_p=F\ell,\qquad
r_qr_p=\frac{F^2\ell^3}{2m}.$$

The product has action units $ML^2/T$. It is a product of prediction risks
for one information task, not a variance product or a measurement-disturbance
relation. Its lower bound concerns estimators; individual admitted motions
include the undisturbed inertial trajectory.

## 3. The joint uncertainty region

Independent coordinate error bars obscure correlations between the two
increments. Put $d=v/(F\ell)$ and $z=mu/(F\ell^2)$. Their exact reachable
region is

$$\boxed{-1\le d\le1,\qquad
\left|z-\frac d2\right|\le\frac{1-d^2}{4}.}$$

To prove the upper boundary, fix $v$ and write $f=2Fh-F$ with $0\le h\le1$.
Then $\int_0^\ell h(s)ds=a:=\ell(1+d)/2$. The decreasing weight
$\ell-s$ makes its weighted integral largest when $h=1$ on $[0,a]$ and
zero afterwards. Indeed the integral of
$[(\ell-s)-(\ell-a)]\,[h(s)-\mathbf1_{[0,a]}(s)]$ is nonpositive
on both sides of $a$, while the constant-weight integral vanishes.
Evaluating the weighted integral gives
$z=d/2+(1-d^2)/4$. Putting the positive-force portion last gives the lower
boundary $z=d/2-(1-d^2)/4$. Convex combinations of these two force profiles
give every intermediate $z$ at the same $d$. This proves necessity and
sufficiency without a numerical reachability calculation.

With canonical area measure $dq\,dp=du\,dv$, the region has area

$$\mathcal A_{\rm reach}
=\frac{F^2\ell^3}{m}\int_{-1}^{1}\frac{1-d^2}{2}\,dd
=\frac{2F^2\ell^3}{3m}.$$

There is no $2\pi$ normalization: this is ordinary canonical area of the
reachable set, not an orbital action. The extremal controls are the familiar
one-switch bounded-force profiles of the double integrator.

## 4. What the result selects

At fixed $F,m,\ell$ the unresolved endpoint region persists despite arbitrarily
fine observation of the accessible past. This is genuine missing information
relative to the stated observer, whereas R06 reconstructs a known deterministic
flow from sufficient stored records. It does not require ontic randomness.

The positive scale depends on the allowed force range and the observation
delay. Taking $F\downarrow0$ at fixed $m,\ell$, or $\ell\downarrow0$ at fixed
$m,F$, closes both action-valued quantities. A force ceiling alone specifies
a worst-case class; it supplies no irreducible force fluctuation in every
trajectory. A derivation of a universal action scale must explain what fixes
the relevant force–delay combination and why the observer's information
boundary is physically unavoidable.

## 5. Next comparison: insert a cut inside the hidden window

R08 should compose the reachable descriptions before and after inserting a
time node. Keep the same bounded-force class and distinguish an unobserved
node, which must be eliminated, from an observed node, which supplies new
information. Determine which joint position–momentum correlations must be
carried for the old endpoint region to remain unchanged. This connects the
[ancient-cut compatibility question](ancient-cuts-provenance.md) to an explicit
classical information region rather than merely to a newly sampled point.

The present formulas are elementary bounded-input reachability and deterministic
minimax specializations. [Liberzon §4.4.1](https://liberzon.csl.illinois.edu/teaching/cvoc/node85.html)
supplies the classical double-integrator and one-switch control precedent.
His task minimizes arrival time; our fixed-time lens is proved directly above.
[B38's companion](../docs/batches/B38/causal-information-source-companion.md)
records the one readable primary passage and two failed source routes.
