# Referee reports on Theorem 1 (self-sufficiency contrast), notes/self-sufficiency-contrast.md

Referee: GPT-6.1 Sol via `codex exec` (config model gpt-6.1-sol, reasoning effort medium), 2026-10-01; reports signed "GPT-6 (Codex)". Saved because the session goal requires the report.

## Pass 1 (REFINE), on commit 027a052

# Bounded referee report: self-sufficiency-contrast.md
VERDICT: REFINE
The principal classical/quantum contrast survives, but Theorem 1 as written
contains a false collision-time bound and needs the following scope and
Gaussian-phase corrections. Proposition 2 is assessed separately below.
Read: AGENTS.md; the entire target note; Theorem A of the fifth-postulate
note; Theorems 1 and 2(a,b) of the 1998-conjecture note; and §4c, including
the proof of Theorem 5, of the reachability note (also its cited §3c).
No web search or numerical/symbolic verification scripts were used.
(a) Collision and incompleteness.
The energy equation, inward sign, substitution r=r0 sin²θ, and integral
πr0/2 are correct. Thus (1) is correct, with time units since [k]=ML³/T².
The claimed general bound by ONE fall time from r_max is false for an
initially outward-moving bound radial datum. Put R=-k/E and
F(R)=(π/2)√(mR³/(2k)), I(r0)=∫₀ʳ⁰√(m/(2k))√(rR/(R-r)) dr.
For 0<r0<R on the outward branch, the remaining collision time is
2F(R)-I(r0)>F(R). This is a counterexample within the stated hypotheses.
Required correction: retain t_c≤F(R) for inward/zero-velocity bound data;
for outward bound data use the displayed exact expression, or t_c≤2F(R).
For inward E≥0 the proof's bound (2/3)√(m/(2k))r0^(3/2) is correct.
Give that separate bound instead of an undefined/ambiguous r_max: an
unbound incoming orbit has no largest radius on its whole maximal orbit.
The collision set is correct on phase space {(x,p):x≠0}, with the logical
parentheses L=0 AND (radial velocity≤0 OR E<0). Its classification and
finite forward collision are correct; no L≠0 datum reaches the centre.
Invariance is correct while solutions exist: for E<0 it is automatic;
for E≥0, radial velocity cannot vanish, so its inward sign is preserved.
Conservation of L and E alone is not the whole sign argument; add this.
For x≠0, p parallel to x gives a four-dimensional subset of six-dimensional
phase space, hence zero Lebesgue/Liouville measure; it is nonempty.
The force has magnitude k/r² and |p| diverges like √(2mk/r) at collision.
There is no continuation as a finite-phase-space classical solution of
the original vector field. Regularized continuations require an enlarged
notion of solution/prescription. This establishes incompleteness, not that
no classical completion is possible. Replace the bare appeal to failure
of existence theorems by this direct singularity argument.
(b) Kato and global quantum dynamics.
The quoted real L²+L∞ theorem in dimension three is correct: multiplication
by V is infinitesimally -Δ-bounded, and Kato--Rellich gives self-adjointness
on H² and a lower bound for each a>0. The Sobolev estimate supplies exactly
the required relative bound; no smallness restriction on k is needed.
The Coulomb split and integral 4πk² are correct in length units with cutoff
radius one. To make units explicit use R>0: ||V1||²₂=4πk²R and
||V2||∞≤|k|/R. Taking a=h²/(2m)>0 verifies all stated hypotheses.
Stone's theorem gives the claimed global strongly continuous unitary group
on all L² states, and preserves H². Arbitrary L² states have mild unitary
evolution; differentiable Schrödinger solutions require the operator domain.
The metadata-only reading label is candid; no reproof of Kato is needed.

(c) Quartic reference and its limits.
Add λ>0 to Theorem 1(c), as in the cited theorem. Its fixed-h strong
product limit for arbitrary partitions of fixed duration with mesh→0,
and its two-cell oscillatory failure, are accurately referenced.
However, “repairs it only by a branch rule” is not proved: 2(a) exhibits
ONE repair; the referenced note also defines the unrestricted classical
δ(S') distribution and discusses diagonalization. Neither establishes
that quartic Newtonian motion itself requires a branch rule: its initial-
value problem is globally well posed. Required correction throughout (c)
and the Conclusion: restrict the failure to the specified unrestricted
halved oscillatory prescription; say branch selection is one repair.
Do not infer classical axiomatic incompleteness for the quartic from it.

(d1) Quadratic forces.
For real quadratic V and normalized states with finite q² and p² moments,
(3) is exact, with the stated signs and factor 1/m. Affine Heisenberg
transport justifies expectations on these form domains without requiring
all states to be in D(H). Gaussian preservation, centroid, and covariance
M_t Σ_h M_tᵀ are correct, including squeezing and quadratic phase.
The extra claim s_t(h)→σ under mass scaling is not generally correct.
At fixed Hooke frequency, scaling m and V together preserves geometry but
gives s_t²=σ²cos²(ωt)+h²sin²(ωt)/(4m²ω²σ²), tending to σ²cos²(ωt).
Delete the general width claim or restrict it to flows with M11→1 and
M12→0 (e.g. free motion). This does not affect exact centroid transport.

(d2) Hepp, regularization, and localization.
The stated smooth subquadratic hypotheses are sufficient for the standard
finite-time coherent-state propagation result: real W, bounded derivatives
of order≥2, fixed minimum-uncertainty squeezing, complete classical flow.
A smooth bounded-core Vδ with a smooth matching collar satisfies them;
its orbit and linearization coincide with Kepler's on [0,T]. The width
σ_h²=hL*/P* has length-squared units. Constants may depend on δ and T;
no uniform δ→0 or long-time result follows.
Equation (4) must define the Gaussian's phase, not merely its covariance.
Use the continuously lifted metaplectic propagation of the initial centred
Gaussian, followed by phase-space translation, and multiply by exp(iS_t/h)
with S_t=∫₀ᵗ(p·ẋ-H_cl)ds in the matching translation convention.
Otherwise covariance leaves an undetermined order-one phase and (4) need
not hold in L²: even a free centred Gaussian acquires the dispersive phase
-(3/2) arctan(ht/(2mσ_h²)), while its centroid action is zero.
With this convention the quoted approximation is valid; metadata does not
verify the exact historical formulation, but the hypotheses suffice.
Duhamel's sign, factor 1/h, and T/h bound are correct on the common H²
domain for the coherent initial state. Write sup_{0≤s≤T}, not sup_{s≤T}.
(L) is explicitly and honestly unproved, and gives precisely the needed
o(1) transfer. Gaussian weighted tails are exponentially small (use a
local cutoff before Hardy); an o(1) L² remainder alone gives no (L).
Carry “under (L)” into the Conclusion and §6's Coulomb recovery assertion;
interpret “large action” here as the stated fixed-scale h→0 limit only.

Proposition 2 — separate assessment (not part of the verdict).
For positive ν, the standard Dirac bounds are ν<1 (distinguished extension) and ν≤√3/2 (essential self-adjointness).
KG ν≤1/2 is the real-indicial-exponent threshold, not automatic uniqueness:
u~r^(1/2±√(1/4-ν²)); at equality the second solution has a logarithm.
Calling this “regular iff” and sufficient for rule-free dynamics is unjustified.
(5) must distinguish Dirac h>k/c from any closed KG interval; its proof
uses a strict inequality for both and contradicts its closed-interval prose.
The cited thresholds do not establish an exhaustive set of self-sufficient
theories; a universal h-gap reading requires additional model/selection premises.

Signed: GPT-6 (Codex).

## Pass 2 (ACCEPT on Theorem 1; Proposition 2 assessed separately), on commit b2e1f1e

# Second-pass referee report: self-sufficiency-contrast.md

VERDICT: ACCEPT

This verdict concerns Theorem 1's stated, conditional claims and proof.
It does not endorse Proposition 2 or an unconditional necessity of h.
I read the target note in full and the requested contextual results.
No web search or numerical/symbolic verification scripts were used.

(a) Classical collision: correct.
Energy conservation for L=0 gives rdot²=(2k/m)(1/r-1/r0) for rest data.
The substitution r=r0 sin²(theta) gives the integral pi r0/2 and hence
F(r0)=(pi/2)sqrt(m r0³/(2k)); the sign and constant in (1) are correct.
For E<0, R=-k/E, the inward time is
I(r0)=sqrt(m/(2k)) integral_0^r0 sqrt(rR/(R-r)) dr <= F(R).
For outward bound data, the time is exactly 2F(R)-I(r0), between
F(R) and 2F(R). The corrected distinction between the branches holds.
For inward E>=0, |rdot|>=sqrt(2k/(mr)) gives the stated 2/3 bound.
Zero radial velocity necessarily has E=-k/r<0 and immediately falls.
The phase-space restriction x!=0 and the parentheses defining C are
correct; outward unbound/parabolic radial data do not collide forward.
L and E are conserved. For E>=0, rdot cannot vanish, so its sign is
preserved. Thus C is invariant for all times in each maximal solution.
The smooth parametrization (x,a)->(x,ax), x!=0, has dimension four;
C is a subset and has zero six-dimensional Liouville measure.
Rest data show nonemptiness. At collision, k/r² diverges and
|p|=sqrt(2m(E+k/r)) ~ sqrt(2mk/r), so no finite phase-space endpoint
exists. The original vector field has no continuation there.
The revised wording correctly proves incompleteness and permits added
regularizations; it does not prove that classical completion is impossible.

(b) Kato and Stone: correct as cited, without reauditing Kato's proof.
Real V in L²(R³)+L-infinity(R³) is a sufficient hypothesis for
self-adjointness on H² and semiboundedness of -a Delta+V, a>0.
The stated adjustable Sobolev estimate makes multiplication by V
infinitesimally operator-bounded relative to Delta; no small-k or
small-coupling restriction is needed. This also supplies the usual
semiboundedness conclusion of the perturbation theorem.
For the explicit radius R>0, ||V1||²=4pi k²R and
||V2||_infinity<=|k|/R, exactly as written, for either sign of k.
Taking a=h²/(2m)>0 verifies the hypothesis separately for every h>0.
Stone's theorem gives e^(-itH/h) for every real t and every L² state.
H² is invariant; strong Schrödinger evolution on H² and mild evolution
outside that domain are correctly distinguished. No assertion at h=0
or uniform lower bound as h->0 is made. The planar remark correctly
uses a different, form-theoretic route rather than the 3D L² split.

(c) Quartic reference: faithful to the specified contextual theorems.
lambda>0 ensures the cited confining quartic operator and global
classical initial-value problem. Theorem 2(b)'s strong product limit
is at fixed h>0 and arbitrary vanishing partition mesh, not uniform in h.
Theorem 1's two-cell obstruction has three nondegenerate stationary
points; its nonzero sine term prevents the unrestricted halved limit.
Theorem 2(a) selects the zero branch before refinement and is one repair.
The restriction to that prescription, rather than the quartic Newtonian
initial-value problem or all classical constructions, is now explicit.

(d1) Quadratic forces: correct.
[q,H]/(ih)=p/m and [p,H]/(ih)=-V'(q) have the stated signs.
For real quadratic V, V' is affine; expectations therefore close exactly.
Finite position and momentum second moments suffice, with the identities
understood through quadratic-flow transport or quadratic-form arguments.
The affine symplectic flow transports a Gaussian's mean and covariance
as z_t and M_t Sigma_h M_t^T, including squeezing and position-momentum
correlations; no claim that its original coherent-state shape persists.
Free-flight variance is sigma²+t²h²/(4m²sigma²). The Hooke formula
has the correct 1/4 and m² omega²; its fixed-frequency mass limit is
sigma² cos²(omega t), not the free-flight limit sigma². Both repairs hold.

(d2) Semiclassical propagation: correct in the stated conditional form.
Real smooth W with bounded derivatives of order >=2 is a sufficient
subquadratic hypothesis for the cited coherent-state propagation theorem,
self-adjoint evolution and complete classical flow. Fixed squeezing
sigma_h²=h L*/P* fits that hypothesis; both packet widths are O(sqrt(h)).
The continuous metaplectic lift fixes the Gaussian phase. The displayed
S_t=int(p.xdot-H)dt is correct with translation
(T_(x,p)f)(y)=exp(ip.(y-x)/h)f(y-x); Weyl-symmetric translation instead
requires the corresponding endpoint phase adjustment. The note explicitly
requires the matching convention. Its free centred dispersive phase is correct.
A globally smooth bounded V_delta can match -k/r outside delta; its
higher derivatives are bounded for fixed delta. The classical orbit and
linearized flow coincide with Kepler's on [0,T]. No negative-time
collision avoidance is needed for the application restricted to [0,T].
The Duhamel sign is -i/h, its common domain is H², and unitarity gives
(T/h) sup_(0<=s<=T)||(V-V_delta)U_delta(s)phi|| as stated.
Thus (L), precisely the uniform o(h) weighted-potential norm bound,
is sufficient. Gaussian tails satisfy it, but an o(1) L² remainder does
not. The note explicitly leaves (L) unproved, including in the Conclusion
and section 6; the fixed-T, fixed-delta, fixed-orbit meaning of h->0 is honest.
All action phases, collision times, widths and Duhamel factors have the
correct units (k=energy*length, h=action, sigma_h²=length²).
Scope caution: (4)+(L) prove norm approximation and bounded-observable
localization, not by themselves convergence of unbounded q,p expectations.
Theorem 1(d2) states the former correctly; section 6's and section 7's
centroid shorthand should be read accordingly or supported by moment bounds.

Proposition 2 (separate assessment; excluded from verdict):
Dirac nu<1 distinguished-extension and nu<=sqrt(3)/2 essential-SA thresholds are standard for this point-Coulomb model.
The nu=1 endpoint needs its own extension criterion; the cited strict subcritical result does not settle it.
KG exponents and the logarithmic second solution at nu=1/2 are correct for the reduced radial function u=rR.
But for 0<nu<1/2 both u branches are finite (both R branches diverge); finiteness alone selects neither.
For nu>1/2, u=r^(1/2)exp(+-i beta log r) tends to zero; it is its logarithmic phase that oscillates.
Thus nu<=1/2 is the standard real-indicial threshold, not a demonstrated unique-dynamics threshold under the stated criterion.
Equation (5)'s algebra and action units are correct, but KG selection/endpoints and “smallest” versus infimum require repair.
The explicit two-model, nonuniversal scope is honest; its claimed admissible interval still requires the missing selection argument.

Signed: GPT-6 (Codex)
