# Fixed coupling permits precise calibrated readout

R06's four-record apparatus admits arbitrarily accurate reconstruction at one
fixed sufficiently small **nonzero coupling**. Use its exact nonlinear
calibration map, then contract the incoming apparatus preparation and final
record errors. Masses, pulse widths, clock mean energy and observation duration
remain fixed. The receiver disturbance stays bounded; multiplying it by the
vanishing reconstruction error gives a vanishing action-valued product.

R16, 2026-09-11. This tests whether fixing coupling closes R06's counterclass.
The resources still supplied are arbitrarily concentrated classical
preparations, improving access to four final momenta, and exact knowledge of
the Hamiltonian. This is delayed deterministic reconstruction, not a
complete-history observation oracle.

## 1. Fixed apparatus, finite error vector

Use [R06](autonomous-finite-readout.md)'s Hamiltonian H_lambda, clock and
four probes, with its positive m,k,E,T and fixed smooth pulse geometry.
Initial receiver states z lie on the compact shell S={H_s(z)=E}. Write a
for the ten apparatus initial coordinates in fixed dimensionless component
units, centred on the nominal clock and zero probe phase; ||a||_infinity<=b.
Each b>0 permits the same full rectangular support as R06. Denote the four
final probe momenta, expressed in fixed momentum units, by

$$G_\lambda(z,a)\in\mathbb R^4,\qquad
F_\lambda(z)=G_\lambda(z,0).$$

The actual observation is the finite vector Y=G_lambda(z,a)+e with
||e||_infinity<=rho. Neither a nor e is known individually. The exact map
F_lambda, including clock reaction and receiver back-reaction, is supplied
as the calibration. Norms below use the declared component units; fixed
constants restore dimensions when action products are formed.

## 2. The nominal record map is uniformly invertible

On a fixed convex neighbourhood of the receiver energy ball, R06's
invertible signal matrix A obeys

$$F_\lambda(z)=-\lambda\mathcal A z+\mathcal R_\lambda(z),
\qquad \|\mathcal R_\lambda\|_{C^1}\le C\lambda^3.$$

Here is the derivative step in addition to R06's value estimate. At nominal
apparatus data, probe coordinates and momenta are O(lambda), and receiver
and clock deviations from their uncoupled paths are O(lambda^2). The same
orders hold for their derivatives with respect to initial receiver z:
differentiate the smooth finite-time Hamilton equations. Probe derivative
forcing is O(lambda); receiver and clock reaction derivatives contain
lambda times a probe or its derivative, and are O(lambda^2). Variation of
constants and finite-time Gronwall bounds preserve these orders uniformly
on the larger compact energy neighbourhood. The integrated record equation

$$F_{\lambda,j}(z)=-\lambda K\int_0^T f_j(s(t;z))x(t;z)\,dt$$

therefore differs from -lambda A z by O(lambda^3) in both value and first
derivative. Fixed cutoff margins keep the exact equations in R06's linear
cutoff regions for all those trajectories. Smooth dependence on initial data
justifies differentiation; no numerical calibration experiment is used.

Let alpha>0 satisfy ||A v||>=alpha||v|| in the chosen norms. Integrate
the remainder derivative along the line segment between z and w inside the
convex neighbourhood. For all sufficiently small positive lambda,

$$\|F_\lambda(z)-F_\lambda(w)\|
\ge (\lambda\alpha-C\lambda^3)\|z-w\|
\ge\tfrac12\lambda\alpha\|z-w\|.$$

Choose such a lambda once and hold it fixed from here on. This proves a
global lower Lipschitz bound on S, rather than inferring global injectivity
from a pointwise rank condition. The inverse exists on the image F_lambda(S).

## 3. Robust exact calibration

Smooth finite-time dependence on a on the compact preparation class gives

$$\|G_\lambda(z,a)-F_\lambda(z)\|\le C_\lambda b.$$

Use the sup norm for records, so the effective finite record error is at most
delta=C_lambda b+rho. Choose any minimum-residual estimate

$$\widehat z\in\operatorname*{argmin}_{w\in S}
\|F_\lambda(w)-Y\|_\infty.$$

The minimum exists by compactness. Since the true z is a competitor, the
residual at the estimate is at most delta. The triangle inequality and the
lower Lipschitz bound yield

$$\boxed{\|\widehat z-z\|\le
\frac{4}{\lambda\alpha}(C_\lambda b+\rho).}$$

At fixed coupling this tends uniformly to zero as b,rho tend to zero. In
contrast, R06's first-order inverse -A^(-1)Y/lambda retains an O(lambda^2)
calibration remainder at fixed lambda. Exact calibration accounts for that
known systematic response; it does not treat it as arbitrary record noise.
The minimum-residual rule is an existence construction, with no assertion
about numerical cost or robustness to an uncertain Hamiltonian.

## 4. Action products and the limit being taken

Let epsilon_x be the worst initial canonical-position reconstruction error,
and D_P the worst canonical momentum disturbance relative to the unmeasured
reference over [0,T], as in R06. Fixed length and momentum units L_*,P_*
give

$$\epsilon_x\le C_\lambda L_*(b+\rho),\qquad
D_P\le C P_*(\lambda b+\lambda^2),$$

$$0\le\mathcal U=\epsilon_xD_P
\le C_\lambda L_*P_*(b+\rho)(\lambda b+\lambda^2)
\longrightarrow0.$$

The product of the two initial canonical coordinate reconstruction errors
likewise obeys H_rec<=C_lambda L_*P_* (b+rho)^2. Both have action units
without a 2 pi factor. Disturbance itself is not required to vanish in this
fixed-coupling limit. Known reference trajectories can be reconstructed from
the recovered initial state, uniformly on the fixed horizon. That statement
differs from weakly disturbing fresh measurements along an unknown motion.

The finite apparent record-error set is contained in a shrinking four-dimensional
ball. This proves a sufficient upper error bound, not equality with an
independently supplied norm ball of the R14/R15 oracle models. Any imposed
positive rho or lower preparation volume is a further resource premise.
Fixed apparatus masses, coupling, duration and upper energy/force ceilings
alone permit the preparation/record-access sequence above.

## 5. Next test: a fixed incoming preparation width

R17 should hold b>0 fixed and use exact final record access. Test whether
unknown incoming probe momenta can compensate changes in the receiver state,
producing identical four-record vectors under the full nonlinear calibration.
Use an explicit implicit-function argument with the preparation box margins,
and quantify the resulting initial-state ambiguity. This isolates what an
independently justified lower preparation width would contribute, rather
than identifying a calibration remainder with a physical gap.

C088–C089 are accepted by [written review](../reviews/fixed-calibration-B47.md).
[B47](../references/batches/B47.md) supplies the bounded source/assumption
audit; its ODE precedent supports smooth dependence, while the uniform
remainder and inverse bound are derived here.
