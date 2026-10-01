# Referee reports on Theorem 5 (coherence necessity), notes/zero-branch-reachability.md §4c

Referee: GPT-6.1 Sol via `codex exec` (config model gpt-6.1-sol, reasoning effort medium), 2026-10-01. Reports signed "GPT-6 (Codex)" / "GPT-6.1 Sol (Codex)". Saved because the session goal of 2026-10-01 requires the report; AGENTS otherwise discourages review files.

## Pass 1 (REFINE), on commit ff1d8c1

VERDICT: REFINE

The exact quadratic calculation and the regular-value limit are correct.
The unrestricted critical-value claim is false; part (c) also needs the
qualifications below. These corrections preserve the principal countertest
of a coherence-dependent obstruction. Review used written derivation only.

1. State (15), Wigner function, signs and constants.
With W(q,p)=(2πh)^(-1)∫e^(-ipy/h)φ(q+y/2)φ̄(q-y/2)dy,
W_c(q,p)=(πh)^(-1)exp[-(q-c)^2/(2σ_h^2)
                         -2σ_h^2(p-p_0(c))^2/h^2].
It integrates to one, has the stated mean and covariance, zero mixed
covariance, and determinant h^2/4. The phase sign gives +p_0(c).
These are squeezed minimum-uncertainty Gaussian states; arbitrary σ_h
need not be the coherent width of a specified oscillator.

2. Transport and exact mixture record.
For real quadratic V and m>0, the Moyal corrections vanish identically;
the Wigner equation is ∂_tW+(p/m)∂_qW-V'(q)∂_pW=0.
Thus W_t=W_0∘Φ_{-t}, with covariance M_tΣ_hM_t^T and translated mean.
The first-row variance is exactly M_11^2σ_h^2+M_12^2h^2/(4σ_h^2).
Theorem A(b)'s polynomial argument extends here directly by that equation
(or affine symplectic covariance); no semiclassical error is involved.
The first row cannot vanish since M_t is symplectic, so s_t(h)>0.
Linearity of the density operator and the Wigner marginal identity give
(16) exactly. Both width assumptions are sufficient for s_t(h)→0 at each
fixed t, including oscillator focal times. No uniform all-time claim follows.

3. Weak and regular-value convergence.
The initial Wigner mixture converges weakly to μ_Λ by Gaussian concentration
and dominated convergence; compact support bounds its moving centres.
Likewise the stated bounded-continuous-test proof of the record limit works.
At a regular value, the preimages in supp w are finite: an infinite set
would have an accumulation point in that compact set, contradicting local
invertibility there. The complement of their open neighbourhoods is compact;
the displayed Gaussian tail bound is correct and tends to zero.
Near each preimage, substitution u=F_t(c) gives the continuous local density
w(F_t^(-1)(u))/|F_t'(F_t^(-1)(u))|; the Gaussian is an approximate identity.
This proves (17), including boundary preimages where continuity forces w=0.
Uniformity on compact regular-value sets is valid, but justify it by a finite
cover of inverse charts and a common neighbourhood avoiding F_t's critical
values on supp w. The resulting density is uniformly continuous locally;
the remaining mass has a uniform positive separation and Gaussian tail bound.
Fixed neighbourhoods centred at one x alone do not establish that uniformity.

4. Required correction at critical values.
Delete “at a critical value both ρ_h and the classical density diverge” and
“at a critical value it is singular” as unconditional assertions.
Counterexample: choose free motion at t=m (in fixed units), p_0(c)=c^2-c,
so F_t(c)=c^2, and w(c)=C c^2χ(c), with χ a nonnegative smooth compact bump,
χ=1 near zero, and C normalizing. All hypotheses hold and x=0 is critical.
Its classical density for x>0 near zero is C√x, extending continuously by
zero at zero; substituting c=√s_t u into (16) gives ρ_h(0,t)=O(s_t^(1/2))→0.
A valid replacement is: weak convergence still holds at critical values;
pointwise behaviour depends on degeneracy and launch weight. At an isolated
nondegenerate fold F_t''(q_c)≠0 with w(q_c)>0, the local contribution scales
as a positive constant times s_t^(-1/2), and the classical density has a
one-sided |x-x_c|^(-1/2) singularity. Higher degeneracies or vanishing weights
require separate statements; a constant arrival map can even produce an atom.

5. Required qualifications to part (c) and units.
Restrict the comparison to an actual regular interval with the stipulated
illuminated branches; arbitrary smooth p_0 need not have exactly two fold
values or a three-stream interval merely because its derivative changes sign.
Assume ∫a^2=1, or permit unnormalized measures consistently.
Use Theorem 2(i)'s exact B_ω criterion: convergence holds iff all nonzero-
frequency B_ω vanish; its value B_0 can retain equal-action interference.
Thus “unless cross amplitudes cancel” must mean this frequency criterion,
not cancellation of every cross term. Both attachments have the same local
smeared limit by Theorem 2(ii), but they also differ at finite h in their
preparation and phase-space spread, not solely in the coordinate record.
The §3c mixture uses phase S_0(q), whereas (15) uses p_0(c)(q-c).
Do not transfer §3c's fringe formula to (15) as an exact asymptotic formula.
Instead its initial kernel obeys |ϱ_h(q,q')|≤||w||∞exp[-(q-q')^2/(8σ_h^2)],
by completing the square in the two packet envelopes. This rigorously gives
the claimed vanishing coherence bound for fixed distinct launch points;
(16) independently proves the record limit without a fringe approximation.
Finally σ_h^2=hℓ is dimensionally wrong when ℓ is a length and h is action:
replace it by σ_h^2=hL_*/P_* with fixed length L_* and momentum P_*.
M_12 has units length/momentum, so the variance formula itself is consistent.

Scope (separate assessment):
Honest in distinguishing exact quadratic results from cited weak extensions.
Those extensions remain conditional on propagation, symbol and flow hypotheses;
Hepp alone does not automatically cover every allowed squeezing σ_h.
The paragraph supplies no proof of a general-force pointwise limit.

Signed: GPT-6 (Codex)

## Pass 2 (REFINE), on commit 00ed595

VERDICT: REFINE

Second-pass referee report: Theorem 5, zero-branch-reachability §4c.
The substantive theorem and convergence proof check out. One exact
sign correction is required in part (c); no new analytical gap was found.

1. Packet and Wigner function. With the normalized convention
W(q,p)=(2πh)^{-1}∫e^{-ipy/h}φ(q+y/2)overline{φ(q-y/2)}dy,
(15) gives
W_c(q,p)=(πh)^{-1}exp[-(q-c)^2/(2σ_h^2)
                         -2σ_h^2(p-p_0(c))^2/h^2].
Thus the mean, diagonal covariance, zero cross covariance, and widths
σ_h and h/(2σ_h) are correct; det Σ_h=h^2/4. The phase sign gives
+ p_0(c), not - p_0(c). Averaging this positive normalized Gaussian
against w gives the asserted initial Wigner density and weak sheet limit.

2. Transport and exact record. For real quadratic V, the Wigner equation
is exactly ∂_tW+(p/m)∂_qW-V'(q)∂_pW=0. This is the state-dual form
of Theorem A(b); all higher Moyal terms vanish. Affine symplectic
transport preserves volume and sends the mean to Φ_t(c,p_0(c)) and
covariance to M_tΣ_hM_t^T. Its position variance is precisely
M_11^2σ_h^2+M_12^2h^2/(4σ_h^2). No covariance term is missing.
The nonzero first row of M_t proves s_t(h)>0. Linearity in the density
operator proves (16) exactly, including its normalization and lack of
interference terms. The inertia and Hooke arrival maps (14) are correct.

3. Hypotheses and units. Both σ_h→0 and h/σ_h→0 are needed to collapse
the phase-space covariance; they imply s_t(h)→0 at each fixed time.
The example σ_h^2=hL_*/P_* is dimensionally correct for positive fixed
L_* and P_*. M_12 has units length/momentum, so both variance terms
have units length squared. h is the action parameter in exp(iS/h);
no extra 2π belongs in these formulas. Nonnegative continuous compactly
supported w of integral one suffices; no derivatives of w are used.

4. Weak and regular-point convergence. The bounded-continuous-test
argument is valid by dominated convergence. At a regular value, the
preimages in supp w are finite: any infinite sequence would accumulate
at a preimage there, contradicting local invertibility. The remaining
compact support has |F_t(c)-x|≥η>0. The displayed Gaussian tail bound
is correct and tends to zero exponentially despite its 1/s_t prefactor.
On each inverse chart, substitution gives w(F_t^{-1}(u))/|F_t'|,
with the absolute Jacobian correctly accommodating reversed orientation.
The Gaussian approximate identity gives (17), also at support boundaries
where continuity makes the weight zero. The finite-chart-cover argument
establishes uniformity on compact regular-value sets: shrink to compact
subcharts and use a finite partition of unity if charts overlap. The
remaining support is uniformly separated; local densities are uniformly
continuous. This is a standard implementation of the stated argument.

5. Critical values. The revised claim correctly retains weak convergence
without promising a universal pointwise limit. At an isolated fold,
c-q_c=s_t^{1/2}u yields the stated positive coefficient
w(q_c)(2π)^{-1/2}∫exp[-F_t''(q_c)^2u^4/8]du multiplying s_t^{-1/2}.
The two classical inverse branches together give the stated one-sided
w(q_c)√(2/|F_t''(q_c)(x-x_c)|) singularity. For F_t(c)=c^2 and
w=Cc^2χ(c), choosing χ=1 near zero gives C√x on the covered side
and ρ_h(0,t)=O(s_t^{1/2})→0. The vanishing-weight correction is valid.

6. Comparison and coherence. The restriction to a regular interval with
K illuminated arrivals avoids reliance on Theorem 3's broader fold
existence claims. The frequency criterion and equal-action value B_0
are correctly retained, and Theorem 2(ii) supplies the common smeared
limit there. The exact kernel bound follows from completing the square;
its factor exp[-(q-q')^2/(8σ_h^2)] and prefactor ||w||_∞ are correct.
Unlike §3c's fixed-width shared-phase components, (15) uses localized
linear phases; replacing the fringe-formula argument by this bound is
valid. It establishes vanishing coherence at fixed distinct launch points.

Required correction: replace “|ψ_0(q)ψ_0(q')|=a(q)a(q')” in part (c)
by “|ψ_0(q)ψ_0(q')|=|a(q)a(q')|”. Equation (5) assumes a real amplitude,
not a nonnegative one. A normalized smooth amplitude with oppositely
signed disjoint bumps gives a negative right-hand side as currently
written. The correction leaves every transport and comparison conclusion
unchanged; alternatively impose a≥0 explicitly for this comparison.

Scope paragraph: Honest about quadratic exactness and cited-only general
weak propagation, including potential, flow, and squeezing hypotheses.
It excludes raw Kepler singularities; metadata citations do not themselves
verify applicability to every proposed angle-record Hamiltonian.

Signed: GPT-6.1 Sol (Codex).

## Pass 3 (ACCEPT), on commit 4858299

# Referee report: Theorem 5, third pass

VERDICT: ACCEPT

The statement and proof of Theorem 5 are correct under their stated setting.
No further correction is required. The second-pass modulus correction is verified.
This review concerns Theorem 5 and its cited local arguments, not every claim
elsewhere in Theorem 3 or the introductory prose.

1. Packet and Wigner covariance.
With the convention whose position marginal is |phi(q)|^2, (15) gives
W_c(q,p) = (pi h)^(-1) exp[-(q-c)^2/(2 sigma_h^2)
                          -2 sigma_h^2 (p-p_0(c))^2/h^2].
It integrates to one; its mean is (c,p_0(c)), its cross covariance is zero,
and its variances are sigma_h^2 and h^2/(4 sigma_h^2).
Thus Delta q Delta p = h/2. The phase sign gives positive p_0(c).
These are minimum-uncertainty squeezed Gaussians, as the text explicitly says.

2. Transport and exact record.
For real quadratic V, higher Moyal terms vanish. The displayed equation
partial_t W + (p/m) partial_q W - V'(q) partial_p W = 0 has the correct signs.
Theorem A(b)'s quadratic bracket identity supports this exact state transport.
The affine symplectic flow preserves phase-space volume, so W_t=W_0 o Phi_-t
needs no Jacobian factor. The covariance is M_t Sigma_h M_t^T, giving exactly
s_t^2=M_11^2 sigma_h^2+M_12^2 h^2/(4 sigma_h^2).
Its positivity follows from the nonzero first row of M_t. Both width hypotheses
are used to obtain s_t -> 0 for fixed t; no uniform-in-time limit is claimed.
Linearity of density-matrix evolution and the Wigner marginal give (16)
exactly, including its normalization and absence of inter-component cross terms.
The units agree: h/sigma_h is momentum, M_12 is length/momentum, and
sigma_h^2=h L_*/P_* is a squared length. Equation (14) is consistent.

3. Weak and regular-value convergence.
Dominated convergence against bounded continuous g proves the stated weak
limit, including when the pushforward has singularities or atoms.
At a regular value, preimages in the compact launch support are finite:
an accumulation point would itself be a preimage and contradict local invertibility.
Outside their inverse neighbourhoods, compactness gives eta>0; the displayed
O(s_t^(-1) exp[-eta^2/(2s_t^2)]) bound tends to zero.
Inside each neighbourhood, u=F_t(c) gives the absolute Jacobian 1/|F_t'|.
The resulting continuous local density is recovered by the Gaussian approximate
identity. This proves (17), including zero-weight or support-boundary preimages.
The finite-chart uniformity argument is valid: subordinate cutoffs can combine
possibly overlapping charts without double counting. Their pushforward densities
are continuous near the compact regular set and uniformly continuous locally;
the remaining compact support has its image a positive distance from that set.
The same tail bound and approximate-identity estimate then hold uniformly.

4. Critical values.
Writing A=F_t''(q_c), c-q_c=s_t^(1/2)u gives exactly the stated positive constant
w(q_c) integral (2pi)^(-1/2) exp[-A^2 u^4/8] du times s_t^(-1/2).
Taylor expansion with local Gaussian domination justifies the little-o remainder.
The two local inverse branches give w(q_c) sqrt(2/|A(x-x_c)|) on the covered
side. Both constants and powers are correct. For F_t(c)=c^2 and a bump equal
to one near zero, w=Cc^2 chi gives C sqrt(x) and rho_h(0)=O(s_t^(1/2)).
Thus vanishing weight can remove the divergence; it need not always do so.
The theorem correctly leaves other degeneracies and weights unspecified.

5. Part (c) and coherence.
The free covariance and branch Jacobian specialize correctly. On the stipulated
regular multi-arrival intervals, stationary phase and Theorem 2(i) give precisely
the frequency criterion and B_0; Theorem 2(ii) supplies the common smeared limit.
The exact kernel bound follows by the triangle inequality and the normalized
Gaussian integral at the midpoint: no missing width prefactor remains.
The corrected pure-state modulus is |psi_0(q) psi_0(q')|=|a(q)a(q')|,
correct even when real a changes sign. Fixed distinct illuminated launch points
therefore retain coherence in (5), whereas the mixture's coherence vanishes.
The exponent agrees with section 3c's factor exp[-Delta q_0^2/(8 sigma^2)].
That proposition uses a different component phase and fixed-width asymptotics;
Theorem 5 correctly proves its shrinking-width conclusion independently.
The necessity conclusion concerns the crossing-stream interference mechanism,
not a derivation of a universal positive physical action scale.

Scope paragraph (separate assessment):
Honest: exactness is restricted to quadratic forces; general-force extensions
are explicitly cited, conditional on propagation and squeezing hypotheses,
and limited to weak convergence. They are not presented as proved here.
The cited angle-model applicability remains a contextual claim, not this proof.

Signed: GPT-6 (Codex)
