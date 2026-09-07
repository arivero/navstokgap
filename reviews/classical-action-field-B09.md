# Review B09: A01 classical action field

## Verdict

The 16 symbolic checks in `scripts/classical_action_field_checks.py` are
consistent with the displayed identities. The paper's proofs are sound after
keeping their domains explicit: finite speed for the microscopic limit,
stationary centered velocity for the covariance formula, integrable covariance
for the long-time limit, and finite irreducible reversible rates for the
strictly positive spectral result. No claim should be promoted as a universal
action gap: rescaling `Q` or taking a zero-variance family destroys a uniform
lower bound.

## Proof and assumption audit

The covariance double integral is valid on finite intervals by stationarity and
Cauchy--Schwarz; dominated convergence at infinity needs `C` integrable. The
finite chain has an inverse on the mean-zero subspace because irreducibility
makes constants the entire nullspace;
detailed balance makes `-Q` self-adjoint and positive. The finite-duration
formula is a positive weighted sum of
`f(y)=1-(1-exp(-y))/y`, whose derivative is positive for `y>0`. The stated
error bound is conservative but correct. The two-state rate convention has
generator eigenvalue `-2 lambda`, hence the exponent and plateau constants are
correct. The second-moment equation and the telegraph PDE are compatible.

## Literature result

Pavliotis is an exact match for the Green--Kubo and generator-Poisson backbone,
not for every finite-state bound. Cinque is an exact match for the finite-speed
alternating telegraph construction and PDE, with Kac scaling as a related
diffusive limit. Nelson's abstract assumes `hbar/(2m)`; Hall--Reginatto assumes
inverse-position momentum fluctuations and fixes `C=(hbar/2)^2`. Neither closes
A01's physical origin or universality obligation.

## Scope requirements and coordinator integration

Call `H_*` a positive model-specific plateau, not a universal constant. The
mass law `lambda_m=m u_m^2/H_*` is a test obligation. The diffusion scaling
`u_lambda^2=a lambda` is formal and violates a fixed speed ceiling; state this
before comparing it with C018.

Coordinator review confirmed that the draft already states the fixed-model
qualification, rate-law obligation and fixed-speed limitation. The integrated
version defines $p_\pm$ explicitly as joint velocity-resolved subprobability
measures, rather than normalized conditional measures. It also specifies
$0<u<c$ in the telegraph section. B09's microscopic-limit commentary was
corrected: each fixed-rate member obeys C018's speed estimate; uniformity fails
as the rate and speed grow together.

Coordinator source checks: Pavliotis p. 5 (2.3)–(2.8), Cinque p. 2 (1.3) and
Kac paragraph, Hall–Reginatto p. 8 (16)–(19) visually verified; all three PDF
hashes recalculated; Nelson's official abstract reopened. C018–C021 are accepted
as the stated model results and literature-classified consequences.
