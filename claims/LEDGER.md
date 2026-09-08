# Results and claim ledger

Updated 2026-09-08. The current mathematical evidence consists of written
derivations, symbolic checks and internal proof review. Each entry names its
assumptions and supporting artifact. IDs remain stable through revision.

## Mechanical and operational results

| ID | Statement | Evidence |
| --- | --- | --- |
| C001 | Constant force, matched endpoints: chord action excess $F^2T^3/(24m)=T\delta E/12$ | Constant-force note and symbolic script |
| C002 | Positive action differences in the fixed-endpoint constant-force class have infimum zero | Foundations Proposition 1; exact family $\eta=a t(T-t)$ |
| C003 | Absolute action differences accumulate at zero along a continuous variation with nonzero second variation | Foundations Proposition 2; restricted action is $C^2$ in its parameter |
| C004 | The constant-force Dirichlet Hessian has lowest eigenvalue $m\pi^2/T^2$; scaling the variation scales its quadratic cost continuously | Foundations §3; $L^2$ normalization |
| C005 | The free Schrödinger kernel tends to $\delta$, with first short-time correction $i\hbar\tau\delta''/(2m)$ | Foundations §4; Schwartz-distribution Fourier proof |
| C006 | Fixed-$N$, equal-prior quantum two-arm discrimination has an explicit positive first-lobe action threshold for $1/2<p\le1$ | Foundations Proposition 3; specified pure states, phase rule and joint measurement |
| C007 | For fixed $1/2<p<1$, C006's threshold tends to zero as $N\to\infty$; at $p=1$ it is $\pi\hbar$ for finite $N$ | Explicit formula and endpoint checks |
| C008 | The free relativistic particle admits arbitrarily small positive fixed-endpoint action differences within a strict speed margin | Foundations §6; explicit small-amplitude family |
| C009 | Free normalized Gaussian kernels on the line compose at every finite partition with unchanged action parameter $\kappa>0$ | Time-refinement Proposition 1; square completion and normalization checks; B06 assumption audit |
| C010 | A weakly continuous centered Gaussian convolution semigroup has variance $at$, $a\ge0$; at fixed mass $\kappa=ma$ remains free | Time-refinement Proposition 2; characteristic-function proof, including the degenerate family |
| C011 | Fixed-endpoint Gaussian bridges have linear mean and variance $\kappa s(T-s)/(mT)$; fixed finite-dimensional laws concentrate on the free classical path as $\kappa\to0$ | Time-refinement §3; square completion, Chebyshev and union bound |
| C012 | For every $\kappa>0$, the free multiplier $\exp[-i\kappa t k^2/(2m)]$ gives a strongly continuous unitary group on $L^2(\mathbb R)$ with Hamiltonian domain $H^2$ | Time-refinement §4; Fourier proof and composition check; B06 assumption audit |
| C013 | At any positive finite time partition, the free endpoint Hessian has determinant $m^{N-1}T/\prod\tau_j$ and inverse $[\min(t_i,t_j)-t_it_j/T]/m$; these give the normalized bridge law | Regulator-limits Proposition 1; B08 proof review; exact nonuniform-partition checks |
| C014 | Under that bridge, $2\Delta S/\kappa\sim\chi^2_{N-1}$; if $\kappa_N\to0$ and $(N-1)\kappa_N\to\ell<\infty$, a common coupling gives uniform almost-sure path convergence and $L^2$ action excess $\ell/2$ | Regulator-limits Proposition 2; B08 review of covariance coupling and moments |
| C015 | Smooth fixed-endpoint sine perturbations with amplitude proportional to $1/n$ retain excess Newtonian action $mv_*^2T/4$ within a strict speed bound; acceleration grows with $n$ | Regulator-limits §4; off-shell paths, direct integration and B08 review |
| C016 | At one SPD quadratic critical point, the normalized oscillatory amplitude has a scalar squared-modulus limit $|O(q_*)|^2/\det A=\langle\delta^{(d)}(\nabla F),|O|^2\rangle$ for each Schwartz test function | Regulator-limits §5; fixed dimension, Fourier proof; B08 constants review |
| C017 | For a physical free Lagrangian, $\epsilon=b\tau$ gives energy units to $b$; choosing the bare coefficient $m_B=\epsilon m_R/\kappa_R$ exactly preserves the normalized reference kernels | Regulator-limits §6; explicit reference condition, fixed square-root branch; B08 algebra/units review |
| C018 | For almost-sure absolutely continuous paths with speed at most $u<c$, $\mathsf h_\Delta=m\operatorname{Var}(X(t+\Delta)-X(t))/\Delta$ lies in $[0,mu^2\Delta]$ and tends to zero as $\Delta\downarrow0$ | Classical-action-field Proposition 1; elementary variance proof; B09 and coordinator review |
| C019 | A stationary finite irreducible reversible velocity chain with nonzero centered velocity gives $\mathsf h(\Delta)\uparrow H_*=2m\langle v,(-Q)^{-1}v\rangle_\pi>0$, with spectral bounds and convergence estimate | Classical-action-field Proposition 2; fixed-model action plateau, mean-zero inverse; spectral proof and B09 review |
| C020 | Symmetric velocities $\pm u$, $0<u<c$, reversed at rate $\lambda>0$, give $H_*=mu^2/\lambda$; universality across masses requires $\lambda_m=mu_m^2/H_*$ | Classical-action-field §§4, 6; exact correlation, variance and telegraph equations; 16-check suite and B09 review |
| C021 | In the formal scaling $u_\lambda^2=a\lambda$, $a>0$, iterated second-moment action limits are $ma$ (rate first) and zero (duration first) | Classical-action-field §5; explicit formula; scaling leaves a fixed speed ceiling; B09 review |
| C022 | A centered bounded refreshed bath, $m\ge M>0$ and independent rate $\nu>0$ give unique stationary tracer variance $S_*=Ms^2/m$, covariance $S_*e^{-\gamma r}$ and action plateau $(m+M)s^2/\nu$, $\gamma=2\nu M/(m+M)$ | Collision-action-relaxation Proposition 1; invariant series and contraction; B10 and coordinator review |
| C023 | With centered bounded initial velocity, $\mathsf a(t)=2m\int_0^\infty\operatorname{Cov}(V(t+r),V(t))dr$ obeys $\dot{\mathsf a}=\beta(H_*-\mathsf a)$, $\beta=4\nu mM/(m+M)^2$; displacement retains a separate window formula | Collision-action-relaxation Proposition 2; physical preparation time and action units; B10 and 15 checks |
| C024 | At fixed masses/clock and rest preparation, scaling incoming velocities by $0<\epsilon\le1$ preserves the collision premises and scales $H_*$ and $\mathsf a(t)$ by $\epsilon^2$ | Collision-action-relaxation §4; class countermodel to a uniform positive plateau; B10 review |
| C027 | For constant-force sampled chords on arbitrary positive partitions, $D_\pi=F^2\sum\tau_j^3/(24m)\le F^2T|\pi|^2/(24m)$; equal steps minimize at fixed count, and every split reduces the error | Cut-point note §1; matched endpoints; B12 and exact checks |
| C028 | In the scalar Gaussian endpoint-bridge family at fixed mass/times, exact restriction consistency forces fixed $\kappa\ge0$; for positive $\kappa$, $D_\pi\to\infty$ in probability but $2D_\pi/(N-1)\to\kappa$ in mean square | Cut-point note §§2–3; covariance proof, C014 finite chi-square law and Chebyshev; B12 |
| C029 | Inserting a node after lengths $a,b>0$ in the fixed-$\kappa$ free bridge adds conditional mean kinetic action $\kappa/2$, using variance $\kappa ab/[m(a+b)]$ | Cut-point note §4; square completion; B12 and nine-check suite |
| C030 | Equal-mass particles prepared with opposite velocities $\pm u$ and separation $u\Delta$ exchange velocities at the midpoint; the tracer returns with $\kappa_{\rm mid}=mu^2\Delta$ and action $\kappa_{\rm mid}/2$ | Physical-cut note §1; total energy $mu^2$, momentum zero, preparation changes with duration; B13 and twelve checks |
| C031 | For absolutely continuous paths with fixed endpoints and speed at most $u$, $\kappa_{\rm mid}=4m\operatorname{Var}Y/\Delta\le m\Delta(u-|v|)^2$, $v=(z-x)/\Delta$; the bound is sharp | Physical-cut note §2; endpoint-conditioned laws, two-segment action with explicit bias term; B13 |
| C032 | A probability convolution semigroup on position with support in $[-ut,ut]$ for all $t\ge0$ is $\delta_{bt}$, $|b|\le u$ | Physical-cut note §3; variance additivity and ballistic bound; spatially homogeneous stationary independent increments only; B13 |
| C033 | The explicit density-disintegrated telegraph return bridge from $(0,+u)$ to $(0,-u)$ has odd-count weights $w_k=(\lambda T/2)^{2k}/[(k!)^2I_0(\lambda T)]$ and midpoint atom $1/I_0(\lambda T)$ at $uT/2$ | [Return-bridge note](../notes/telegraph-return-bridge.md) §§1–3; fixed $u,\lambda,T>0$, independent occupation simplexes, right-continuous velocity version; B14 and coordinator proof/source review |
| C034 | This fixed bridge has consistent cut restrictions and $0\le S[X]-S_\pi\le(mu^2/2)N_T|\pi|$, giving almost-sure and $L^1$ polygon-action convergence to $mu^2T/2$ | Return-bridge note §§4–5; positional samples, kinetic functional, deterministic shrinking meshes; B14, 12 symbolic checks and 45 rational partition cases |
| C035 | Independent composition gives the mass-weighted COM coefficient and complementary reduced-mass coefficient; if a finite nonnegative mass-only coefficient on all $m>0$ equals its COM-composed value, it is constant | [Composition note](../notes/composition-universality.md) §§1–2; common observable and preparation class, product-state memory retained; monotone additive-function proof, B16 and five checks |
| C036 | Under C035 for Green–Kubo plateaus, one stationary two-state reference with $m_0,u_0>0$ and $0<\lambda_0<\infty$ forces the shared coefficient $K=m_0u_0^2/\lambda_0>0$ | Composition note §§3–4; C020 input; finite-product consistency family and preparation/correlation countertests; B16 and coordinator proof/source review |
| C037 | In the C033 bridge, $(Q+1)/2\mid K=k$ is Beta$(k+1,k)$ for $k\ge1$, with $Q=1$ at $k=0$; $\kappa_{\rm mid}/H_*=zR(1-R)$, $R=\int_0^zI_0(s)ds/[zI_0(z)]$, has cubic onset and limit one | [Crossover note](../notes/bridge-crossover.md) §§1–3; same density-disintegrated return preparation, $Q=2X_{T/2}/(uT)$; factorial convolution, beta moments, Bessel integral proof; B17 and 29 exact checks |
| C038 | A prescribed positive increment or return-midpoint coefficient requires $T\ge K_*/(mu^2)$; a common finite window and uniform speed ceiling force a mass-independent coefficient to zero if admissible masses approach zero | Crossover note §4; C018/C031 necessary bounds, explicit small-mass limit; B17 and coordinator review |

These are checked derivations. C006 is conditional on its stated quantum
measurement premises. For a new result, provide quantifiers, units, path/operator
domain, boundary conditions, dependencies and gap-closing limits in the proof.

## Literature status

Proof status above and literature status below are independent. Each accepted
result has a bounded librarian audit; exact source inputs and elementary
consequences are identified separately.

| Claims | Literature classification | Audit |
| --- | --- | --- |
| C001–C004, C008 | Classical geometry/variation framework; specialized formulas are elementary consequences | [B05](../references/batches/B05.md) |
| C005 | Teschl's standard free kernel; Taylor correction is a Fourier consequence | B05 |
| C006–C007 | Holevo–Helstrom theorem specialized to the stated pure-state protocol; threshold inversion and limits are consequences | B05 |
| C009 | Standard Gaussian/Chapman–Kolmogorov formula with mass/action rescaling | [B06](../references/batches/B06.md) |
| C010 | Elementary characteristic-function/additivity consequence within the Gaussian class | B06 |
| C011 | Standard Brownian bridge with rescaling; finite-dimensional concentration is a consequence | B06 |
| C012 | Standard free Schrödinger group and domain, with restored units | B06 |
| C013 | Elementary determinant/Green-function consequence of the standard Gaussian bridge | [B08](../references/batches/B08.md) |
| C014 | Finite chi-square law and joint limit derived from standard Gaussian facts; exact combined statement unmatched in the four-source coverage | B08; bounded coverage, novelty unassessed |
| C015 | Elementary mechanics instance of the established oscillatory weak-limit mechanism | B08; Rindler §§2.1, 3.3 |
| C016 | Exact quadratic Fourier identity in Guillemin–Sternberg (14.7); scalar limit and delta pullback are consequences | B08 |
| C017 | Explicit elementary scaling construction motivated by Rivero; exact map unmatched in the selected sources | B08; bounded coverage, novelty unassessed |
| C018 | Elementary bounded-displacement variance consequence | [B09](../references/batches/B09.md) |
| C019 | Exact Green–Kubo/Poisson backbone in Pavliotis; finite-state bounds and monotonicity are spectral consequences | B09; combined package unmatched in bounded coverage, novelty unassessed |
| C020 | Exact telegraph construction/PDE in Cinque; action normalization and mass-rate law are elementary consequences | B09 |
| C021 | Elementary iterated-limit consequence; related Kac scaling in Cinque | B09; exact double-limit statement unmatched in selected passages |
| C022 | Exact affine collision and bath model in Barkai; bounded invariant law and moments are consequences; stationary covariance matches Barbier–Trizac | [B10](../references/batches/B10.md) |
| C023 | Established stationary covariance integral; preparation-time and window formulas derived for the specified ensemble | B10; combined statement unmatched in selected pages, novelty unassessed |
| C024 | Elementary parameter-scaling countermodel | B10; bounded coverage, novelty unassessed |
| C027 | Elementary arbitrary-partition extension of the audited constant-force formula | [B12](../references/batches/B12.md); existing Newton source route |
| C028–C029 | Elementary Gaussian restriction, chi-square and conditional-variance consequences; action interpretation is project-specific | B12; Pitman–Yor selected bridge/Markov passages, novelty unassessed |
| C030 | Elementary construction using the established equal-mass elastic collision map | [B13](../references/batches/B13.md); Barkai (2)–(3) |
| C031–C032 | Elementary support/variance and convolution consequences; exact statements unmatched in the two-source coverage | B13; novelty unassessed; Cinque supplies the memory comparison, not these theorems |
| C033 | Equal-rate occupation density specializes Cinque (2.6); bridge normalization, midpoint atom and version/protocol comparison are derived consequences | [B14](../references/batches/B14.md); pp. 1–4 and two worker searches; exact combined statement unmatched, novelty unassessed |
| C034 | Elementary pathwise restriction and kinetic square-completion consequences | B14; exact action estimate unmatched in bounded source coverage, novelty unassessed |
| C035–C036 | Standard covariance/product-chain and nonnegative-additivity consequences, with project-specific composition/positive-reference premises | [B16](../references/batches/B16.md); two searches and two cached source pages; combined statement unmatched in bounded coverage, novelty unassessed |
| C037–C038 | Derived midpoint/count specialization and necessary-window consequences; standard telegraph occupation and Bessel-integral ingredients | [B17](../references/batches/B17.md); two searches, Cinque pp. 3–4 and DLMF 10.32.1; exact combined statements unmatched, novelty unassessed |

M03's unaccepted spectral draft has its own completed [B04](../references/batches/B04.md)
literature audit. Its mathematical review and checks remain pending.

## Historical findings and research targets

| ID | Claim or question | Status / evidence |
| --- | --- | --- |
| H001 | The selected Book I passages formulate geometric first and last ratios | Source-grounded interpretation; opening-source companions and note |
| H002 | Doubts about vanishing magnitudes delayed the 1687 first edition | Open historical conjecture; H02/H03 seek dated causal evidence |
| H003 | NATP00385 is a miscellaneous calculus-priority fragment collection | Verified catalogue metadata and H01 audit |
| H004 | Selected NATP00385 passages describe analytic discovery and synthetic presentation | Passage-level audit; exact coverage and chronology question in the historical note |
| H005 | Plutarch's cone-section passage was printed in Xylander's 1570 Latin Moralia, pp. 823–824 | H04 librarian retrieval; coordinator visual verification of IIIF canvases 603151/603152 |
| H006 | How did the cone-section dilemma enter early-modern discussions of indivisibles and the continuum? | H04 bounded search; H05 author-specific reception audit remains |
| Q001 | Which independent premises force a positive universal action parameter? | Open target; WP4 Branch B |
| Q002 | Which additional-field action generates an action-value or spectral gap? | Model design; `ideas/I001-action-field.md` |

## Resolved objections

| ID | Inference assessed | Resolution |
| --- | --- | --- |
| X001 | Equal phases at differences $nh$ imply a smallest positive action difference | Rejected: phase periodicity permits arbitrarily close phases |
| X002 | A toy Hessian/oscillator gap establishes the Yang–Mills gap or NS regularity | Rejected: transfer requires the target operators, spaces and continuum/infinite-volume/regularity estimates |

## Review record

[B17](../reviews/bridge-crossover-B17.md) audited C037–C038 with one
Luna-medium worker. Coordinator verified the even/odd segment density factors,
midpoint Jacobian, atom, beta moments and large-window argument; checked
Cinque p. 4 visually and DLMF's integral formula. The exact mean tends to
$u/(2\lambda)$ at fixed $u,\lambda$, correcting P02's unscaled-mean statement.
Twenty-nine exact checks and seven quadrature/count-series comparisons pass.

[B16](../reviews/composition-B16.md) audited C035–C036 with one Luna-low
worker. Coordinator verified Pavliotis p. 5 and Pitman–Yor printed p. 6
visually, corrected source titles, and retained the preparation class,
all-positive-mass domain, Markov product label and finite-rate assumptions.
Five dedicated algebra checks and P02's independent product-chain checks
support the written proofs. Positivity concerns the common plateau inside
the selected class; rate scaling across classes remains possible.

[B14](../reviews/telegraph-return-B14.md) audited C033–C034. Coordinator
verified Cinque (2.6) against the PDF image, strengthened the affine-simplex
absolute-continuity argument, and corrected a discovery-only source's authors
to Bogachev–Ratanov. Exact conditioning uses a specified path version; the
endpoint-window velocity mixture is a distinct protocol. Algebra and rational
partition checks accompany the general written proof.

[B10](../reviews/collision-action-B10.md) audited C022–C024. Coordinator
verified collision coefficients, covariance, source versions/hashes and the
cooling-clock contrast; added Barkai p. 3 and corrected source page counts.
Receding-centre and polygon-threshold derivations remain drafts pending the
interrupted B11 librarian audit, outside the accepted claim set.

[B09](../reviews/classical-action-field-B09.md) audited C018–C021 after the
draft derivation. Coordinator review checked source formula images and hashes,
the mean-zero inverse, rate convention, limit order and model-specific bounds.
Velocity-resolved measures were defined as joint subprobability measures.
The written proofs support the general statements; 16 exact checks support
their finite algebraic instances. The next obligation is physical universality.

[R01](../reviews/action-gap-foundations-R01.md) audited the three propositions
and supporting calculations behind C001–C008. Its two scope clarifications are
incorporated: endpoint terms mean $dG(q,t)/dt$, and path-space locality requires
continuity of the parameterized paths. The current editorial revision retains
the theorem statements, proof arguments and evidence classifications.

[B08](../reviews/regulator-limits-B08.md) independently checked C013–C017.
Coordinator review verified the source formulas, retained the distinction
between path and action convergence, specified the oscillatory branch and
made the scalar test-function interpretation explicit. All 24 finite checks
pass; the general analytic statements rest on the written proofs.
