# Results and claim ledger

Updated 2026-09-12. Current verification uses written derivations and source/proof
review. Script checks in earlier entries are historical under AGENTS.md's hard
rule. Each entry names its
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
| C037 | In the C033 bridge, $(Q+1)/2\mid K=k$ is Beta$(k+1,k)$ for $k\ge1$, with $Q=1$ at $k=0$; $\kappa_{\rm mid}/H_*=zR(1-R)$, $R=\int_0^zI_0(s)ds/[zI_0(z)]$, has cubic onset and limit one | [Combined return-bridge note](../notes/telegraph-return-bridge.md) §§6–8; same density-disintegrated return preparation, $Q=2X_{T/2}/(uT)$; factorial convolution, beta moments, Bessel integral proof; B17 and 29 exact checks |
| C038 | A prescribed positive increment or return-midpoint coefficient requires $T\ge K_*/(mu^2)$; a common finite window and uniform speed ceiling force a mass-independent coefficient to zero if admissible masses approach zero | Combined return-bridge note §9; C018/C031 necessary bounds, explicit small-mass limit; B17 and coordinator review |
| C039 | The normalized coin $C_\varepsilon=(I-i\omega\varepsilon\sigma_x)/\sqrt{1+\omega^2\varepsilon^2}$ with opposite translations gives $U_{T/N}^N\to e^{-iTH_D/K}$ strongly on $L^2$; the rest-subtracted positive branch tends to free Schrödinger evolution as $c\to\infty$ | [Checkerboard note](../notes/checkerboard-dynamics.md) §§1–4; supplied $m,c,K>0$, $\omega=mc^2/K$, complex amplitudes; self-adjoint domain $H^1$, Fourier/dominated-convergence proof; B18, 28 exact checks and three mode tests |
| C040 | Ideal direction measurement after every coherent step gives flip probability $q_\varepsilon=\omega^2\varepsilon^2/(1+\omega^2\varepsilon^2)$ and probability of any flip at most $\omega^2T\varepsilon\to0$, a ballistic limit | Checkerboard note §5; initial definite direction, Born rule and repeated projective measurement, fixed $\omega,T$; B18 addendum and coordinator proof review |
| C041 | The C019 product bounds give an upper bound on the full relaxation gap; an independent slow label keeps $H=mu^2/\lambda$ fixed while $\gamma_1=2\min(\lambda,\epsilon)\to0$ | [Spectral-control note](../notes/susceptibility-gap.md) §§1–3,5; finite reversible $L^2(\pi)$, fixed positive $m,u,\lambda$, supplied energy unit; B20, 20 finite checks |
| C042 | If centered velocity-unit observables have frame lower bound $\alpha>0$ and total susceptibility $S$, then $\gamma_1\ge\alpha/S$; uniform coverage and response bounds give a uniform family gap | Spectral-control note §4; full centered-space frame, eigenbasis proof, varying-mass normalization; B20 and coordinator review |
| C043 | The bounded-acceleration return is feasible iff $T\ge2u/a$ and has unique minimum kinetic cost $mu^3/(3a)$; longer durations allow positive excess costs tending to zero | [Bounded-turn note](../notes/bounded-acceleration-return.md) §§1–2; $W^{2,\infty}$, prescribed $\pm u$, return endpoints, $m,u,a>0$; external-control kinetic functional; B21 and 27 checks |
| C044 | Lipschitz velocity gives sharp chord kinetic error $0\le S_K-S_\pi\le ma^2\sum d_i^3/24\le ma^2T|\pi|^2/24$ | Bounded-turn note §3; arbitrary partition, pair-variance proof, affine equality case; uniform fixed-$m,a,T$ convergence; B21 |
| C045 | Four distinct bounded velocities can have fixed positive $H=mu^2/\lambda$ and closing gap $2\lambda\delta^2$; recovering the slow sign requires gain at least $\sqrt2/\delta$ | Spectral-control note §6; independent signs, $\epsilon=\lambda\delta^2$, $0<\delta\le1/4$, fixed $m,u,\lambda>0$; B22 and exact checks |
| C046 | Independent reversible factors with local frame bounds satisfy $\gamma_{\rm prod}=\min_i\gamma_i\ge\min_i\alpha_i/S_i$ despite an unobserved mixed sector | Spectral-control note §7; tensor eigenbasis, unchanged constituent clocks, $S_i=\sum_aH_i/(2m_i)$; B22 and product-matrix checks |
| C047 | Finite connected harmonic receiver at fixed centre velocity and independent fixed-energy uniform phases has $h_i(\Delta)=2m_i\sum_j w_{ij}(1-\cos\omega_j\Delta)/(\Delta\omega_j^2)\to0$; independent random centre velocity adds $m_i\sigma_0^2\Delta$ | [Conservative receiver note](../notes/conservative-harmonic-receiver.md); exact modal/two-body proof, bounded-energy speed margin, necessary joint-limit bound; B23 review and 15 checks |
| C048 | Equal-mode-energy odd harmonic rings have iterated action limits $2\Theta/\Omega$ and zero in opposite size/window orders; $z\to\infty$, $z^2/N\to0$ gives the positive joint limit | Receiver note §5; $\Omega=2\sqrt{k/m}$, fixed $m,k,\Theta>0$, zero centre mode, density and Lipschitz proofs; B24 |
| C049 | A common hard speed ceiling in C048's phase preparation forces $\Theta_N=O(N^{-1})$ and $\sup_\Delta h_N\to0$; bounded total energy also suffices for this closure | Receiver note §6; exact site-zero support maximum, cosecant sum and uniform bound; B24 and checks |
| C050 | Equal-mass Poisson hard-point gas at density $\rho$ with iid velocities $\pm u$ and Palm tag has independent reversal waits of rate $\rho u$ and plateau $mu/\rho$; fixed-density cooling scales it linearly | Collision paper §5; ordered-gap proof, stationary velocity preparation, infinite gas first; [B25 review](../reviews/jepsen-receiver-B25.md) |
| C051 | Independent uniform phases of two opposite-speed lattices, each spacing $2/\rho$, give a stationary square-wave tag and $0\le\mathsf h(\Delta)\le m/(3\rho^2\Delta)\to0$ at C050's mass, speed, density and mean collision rate | Collision paper §6; Palm/intersection proof and folded cubic variance; [B26 review](../reviews/ordered-preparation-B26.md); joint mark/position preparation changes |

| C052 | Fixed external relativistic Kepler potential has regular bound domain $\lvert L\rvert>k/c$, $E_{\min}(L)\le E<mc^2$ and excluded angular-action infimum $k/c$ | [M07 note](../notes/relativistic-kepler-threshold.md); written effective-potential, continuation and endpoint-time proofs; B27/B28 and coordinator visual/source review |
| C053 | For every fixed softened core $a>0$ and $m,k,c>0$, every $\lvert L\rvert>0$ admits a regular bound circle, giving angular-action infimum zero; at each fixed $0<\lvert L\rvert<k/c$ minimizing radii tend to zero as $a\downarrow0$ | M07 note and gap laboratory Kepler section; compact-sublevel and scaling proofs; B28 and coordinator review; no computational verification |

| C054 | Uniform circular phase gives transport response $\ell(1-\cos z)/(\gamma z)$ and averaged position-conditioned coefficient $\ell\sin^2z/(2\gamma z)$; fixed positive action fraction bounds window ratios | [A15 note](../notes/bound-orbit-action-observable.md), $z=\omega\Delta$; phase-average proofs and B29 |
| C055 | Twice the projected canonical covariance area equals orbital action for uniform circular phase and is affine-symplectic invariant; other phase preparations conserve their own value, including zero; C052/C053 thresholds transfer within uniform preparation | A15 covariance/orbit-map proofs, gap laboratory, B29 and coordinator source review |

| C056 | External-potential dilation preserves mass, velocity, energy and invariant pushforward preparation; normalized orbit action, covariance area and corresponding-window response scale by $a$ | [A16 proof](../notes/action-scale-dilation.md); smooth transformed domain, finite moments; B30 and coordinator written review |
| C057 | A class containing arbitrarily small contractions of one positive finite degree-one action observable has positive-value infimum zero; a common finite value must be zero under any nontrivial admitted contraction | A16 closure proposition; model/preparation class explicit; coupling and force countertests; B30 |

| C058 | One fixed smooth confining potential with global force ceiling admits radially stable uniform-phase circles with $\ell_R\sim\sqrt{mK}R^2\to0$, vanishing speed/acceleration and finite limiting period | [A17 proof](../notes/fixed-force-small-circles.md); exact force balance, effective energy and asymptotics; B31 |
| C059 | Relativistic circular motion with $f\le F_{\max}$ and independent speed floor $v\ge v_*>0$ satisfies $\ell\ge m^2v_*^3/[F_{\max}(1-v_*^2/c^2)]$ | A17 identity $\ell=P^2v/f$ and monotonicity; uniform-phase covariance transfer C055; B31 and coordinator review |

| C060 | Regular closed $C^2$ trajectories with speed floor, stated momentum law and force ceiling satisfy $T\ge P_*\mathcal K/F_{\max}$ and normalized orbit action $J\ge P_*^2v_*\mathcal K/(2\pi F_{\max})\ge P_*^2v_*/F_{\max}$ | [A18 proof](../notes/closed-orbit-force-action.md); Fenchel–Borsuk input, momentum derivative and monotonicity; B32 and coordinator review |
| C061 | C060's lower constant is attained by a circle in a smooth globally force-bounded confining potential | A18 cutoff construction; equality over the admissible model class, not every fixed potential; B32 review |

| C062 | Fixed-energy uniform-phase two-body spring receiver: stationary position-conditioned kernels have mean composition defect $-q\sin\omega s\sin\omega t$; phase state restores exact composition, and two positions recover momentum off half-period sampling | [R03 §§1–2](../notes/classical-cut-state.md); written derivation, B33 and coordinator review |
| C063 | At fixed duration and initial position, independent equal-step conditional direction resets converge terminally in $L^2$ to that position; stationary one-time law is preserved but two-time correlation freezes. Canonical $J=E/\omega$ tends to zero across cooled preparations at fixed Hamiltonian | R03 §§3–4; explicit moment recurrences and ellipse integral; B33 review |

| C064 | Centre-reduced equal-mass three-body chain with tagged phase retained has exact cosine memory $\Gamma(t)=(9k/20)\cos(\sqrt{5k/(2m)}t)$ and inherited receiver quadratures; identical tagged phase can have different futures at fixed energy | [R04 §§1–3](../notes/three-body-cut-memory.md); canonical reduction, elimination and fixed-energy pair; B34 review |
| C065 | Two sufficiently close exact tagged-phase samples recover the receiver pair through $\det B_\delta=g^2\delta^4/(12\mu\nu)+O(\delta^6)$; inverse sensitivity grows while cooling closes modal actions without changing the memory kernel | R04 §§4–5; Taylor coefficients, analytic determinant and normal-mode scaling; B34 review |

| C066 | Two ordered canonical probe shears give exact pre-cut phase errors and back-reaction; intrinsic rectangular-support products are $s_qt_q$ and $s_rt_r$, with zero infimum across shrinking positive-volume probe preparations | [R05 §§1–2](../notes/classical-readout-refinement.md); fixed gains, ideal impulses and records; B35 and coordinator written review |
| C067 | At fixed receiver, system preparation and horizon, fresh probe widths $O(\eta^4)$ give uniform hidden-state reconstruction error $O(\eta)$ and trajectory disturbance $O(\eta^3)$, while probe count and fixed-mass apparatus mass grow as $O(\eta^{-1})$ | R05 §§3–4; exact kick-inclusive error identity and bounded-flow sum; B35 review; scalable impulsive instrument |
| C068 | Fixed finite-mass clock and four probes with smooth coordinate coupling $\lambda K\sum f_j(s)X(x)R(q_j)$ give persistent momentum records $\boldsymbol\pi(T)=\boldsymbol\pi(0)-\lambda\mathcal A z_0+O(\lambda b+\lambda^3)$ with invertible fixed-width pulse matrix; receiver disturbance is $O(\lambda b+\lambda^2)$ at fixed horizon | [R06 §§1–3](../notes/autonomous-finite-readout.md); positive kinetic energy, compact receiver preparation, bounded forces, clock reaction included; B37 and coordinator written review |
| C069 | For C068 with known dynamics and exact final momentum records, incoming apparatus width $b=\lambda^3$ gives delayed initial-state reconstruction and trajectory disturbance $O(\lambda^2)$; canonical initial-position error times finite-horizon momentum disturbance tends to zero as $O(\lambda^4)$ | R06 §4; fixed masses, pulse widths and clock mean energy; increasingly precise preparation and weak coupling; reporting refinement is sampling after fixed latency; B37 review |

| C070 | Exact delayed past records with unresolved force $f\in L^\infty$, $|f|\le F$, give coordinate minimax prediction errors $F\ell^2/(2m)$ and $F\ell$, simultaneously attained by inertial prediction; risk product is $F^2\ell^3/(2m)$ | [R07 §§1–2](../notes/causal-force-information.md); identical-record force pair and endpoint-integral upper bounds; B38 review |
| C071 | R07's exact joint reachable region satisfies $|z-d/2|\le(1-d^2)/4$, $|d|\le1$, and has canonical area $2F^2\ell^3/(3m)$; force-budget or delay closure sends the area to zero | R07 §§3–4; fixed-impulse extremizers, convex interpolation and area integral; B38 review |

| C072 | For arbitrary measurable bounded force, $K_T=S_bK_a+K_b$ at every interior cut; all unobserved refinements preserve the endpoint set, while replacing the intermediate lens by its marginal rectangle strictly enlarges it | [R08 §§1–2](../notes/reachable-cut-composition.md); split/concatenate proof and saturated-impulse counterexample; [B39 review](../reviews/cut-composition-B39.md) |
| C073 | Exact cut position leaves momentum interval of width $D(\zeta)=Fa[\sqrt{2-4\zeta}+\sqrt{2+4\zeta}-2]$ and terminal canonical area $2F^2b^3/(3m)+Fb^2D(\zeta)/m$; area tends uniformly to zero as $b\to0$ although the central momentum width stays positive | R08 §§3–4; ideal available records, lens inversion and determinant-one shear; B39 written review |

| C074 | A bounded-error position strip clipped to the force lens has terminal area $A_C+2F^2b^3/(3m)+2Fbw+Fb^2D_*/m$, with strip width $w$ and extreme compatible momentum span $D_*$ | [R09 §§1–2](../notes/finite-precision-cut.md); segment extrusion, monotone fibres and [B40 review](../reviews/finite-precision-B40.md) |
| C075 | At fixed $F,m,T$, R09's area is at most $4FT\varepsilon+2F^2ab^2/m+2F^2b^3/(3m)$ and closes uniformly as precision error and delay vanish at any relative rates; central momentum uncertainty persists | R09 §3; written bound and exact/full/no-delay endpoint checks; B40 review |

| C076 | Two bounded-error positions give exact compatible-set propagation and estimator-specific worst-case terminal errors $R_p=B+Fb$, $R_q=\varepsilon_2+bB/m+Fb^2/(2m)$, where $B=m(\varepsilon_1+\varepsilon_2)/\delta+F\delta/2$ | [R10 §§1–2](../notes/two-position-recovery.md); weighted force integral and simultaneous saturation; [B41 review](../reviews/two-record-B41.md) |
| C077 | If $\delta,b\to0$ and $(\varepsilon_1+\varepsilon_2)/\delta\to0$, both coordinate errors close uniformly; equal errors and $b=\delta_*=2\sqrt{m\varepsilon/F}$ give action-error product $28\sqrt{mF}\varepsilon^{3/2}$ at fixed horizon | R10 §3; timing feasibility and written bounds; established equal-error differentiation optimum, derived mechanical product |

| C078 | For compact centrally symmetric convex inputs, linear records with bounded errors and a scalar linear target, global minimax error equals the maximal target magnitude in the central compatible fibre | [R11 §1](../notes/indistinguishable-phase-bound.md); half-difference and midpoint proof; [B42 review](../reviews/indistinguishability-B42.md) |
| C079 | At $d=2\sqrt{m\varepsilon/F}$, $T-b\ge2d$, two position records and the entire bounded-error position history have identical coordinate minimax risks $P_*=Fd+Fb$ and $Q_*=\varepsilon+Fdb/m+Fb^2/(2m)$; at $b=0$ their product is $2\sqrt{mF}\varepsilon^{3/2}$ | R11 §§2–3; established prepared opposite-motion pair, R10 upper bound, blind-delay extension; B42 review |
| C080 | Product symmetric convex input/error classes with all constituent records give exact scalar minimax radius $\sum_i \lvert a_i\rvert r_i$; canonical centre/relative radii follow, and n identical copies have $H_R=nH_1$. Mass-only nonnegative coordinate-radius closure on all positive masses forces $Q(m)=q_*$, $P(m)=p_*m$ | [R12 §§1,4](../notes/minimax-composition.md); product-fibre extremizers and nonnegative additivity; [B43 written review](../reviews/minimax-composition-B43.md) |
| C081 | For product bounded forces/errors, complete records, known initial states and $T\ge\max_i4\sqrt{m_i\varepsilon_i/F_i}$, centre risks are $Q_A=E$, $P_A=2\sum_i\sqrt{m_iF_i\varepsilon_i}$; retaining only the centre record gives $Q_B=E$, $P_B=2\sqrt{MF_\Sigma E}$, strictly larger momentum risk unless $F_i/(m_i\varepsilon_i)$ is common | R12 §§2–3; R11 sharp radii, exact force/error image, Cauchy–Schwarz; B43 written review |


| C082 | Known initial phase, complete position records of error epsilon and arbitrary force bound F give exact finite-horizon radii $Q=\varepsilon\min(s^2/2,1)$ and $P=\sqrt{mF\varepsilon}V(s)$, with $s=T\sqrt{F/(m\varepsilon)}$ and $V=s,\sqrt{2s^2+4}-s,2$ on intervals split at sqrt(2),4; blind-delay radii are $P+Fb$, $Q+bP/m+Fb^2/(2m)$ | [R13 §§1–2](../notes/finite-horizon-minimax.md); rearrangement and path-strip extremizers; [B44 written review](../reviews/finite-horizon-B44.md) |
| C083 | R12 product and aggregate radius formulas extend to every horizon using C082; aggregate position risk strictly increases exactly when some $F_iT^2/2<m_i\varepsilon_i$ and another is strictly greater. The F,16F example loses both phase coordinates; identical-copy risk products remain extensive at every horizon | R13 §3; product fibres, exact image and minimum-of-sums identity; B44 written review |

| C084 | Two identical constituents with pointwise quadratic shared record-error budget have exactly the one-body centre risks at mass 2m, force bound 2F and precision epsilon/sqrt(2), for full or averaged records, at every horizon; blind-delay extension and saturated factor 2^(1/4) follow | [R14 §§1–2](../notes/shared-record-budget.md); exact projection/synchronous lift and C082; [B45 written review](../reviews/shared-budget-B45.md) |
| C085 | For n identical constituents with fixed pointwise l^r budget, 1<=r<=infinity, effective centre precision is epsilon n^(-1/r), with equal full/aggregate scalar risks; saturated canonical product is n^(1-3/(2r)) times the one-copy product, including invariant copy-count scaling at r=3/2 | R14 §3; norm inequality, synchronous lift, canonical mass and C082; B45 written review |

| C086 | Independent blocks of identical bounded-force constituents, pointwise l^r budgets and known initial phases have exact full/block-record centre risks Q=sum w_j q(T,E_j), P=sum n_j p(T,E_j), E_j=epsilon_j n_j^(-1/r); whole-centre-only records give q(T,bar E), Np(T,bar E). Saturated momentum loss is strict unless all E_j coincide | [R15 §§1–2](../notes/block-apparatus-composition.md); product fibres and exact aggregate lift; [B46 written review](../reviews/block-apparatus-B46.md) |
| C087 | k independent equal blocks of a constituents have saturated H=k a^(1-3/(2r)) H_1, hence k H_1 at r=3/2. Finite-r product block budgets differ from every single unweighted global ball; equal centre risks can occur despite strict set inclusion. Matching fixed global-budget centre risks requires block allowance epsilon k^(-1/r) | R15 §§3–4; copy-count substitution, enclosing radius and explicit strict inclusion; B46 written review |

| C088 | R06's nominal four-record map has $F_\lambda=-\lambda\mathcal A z+O_{C^1}(\lambda^3)$ on a fixed convex receiver neighbourhood, hence a uniform lower Lipschitz bound at fixed sufficiently small positive coupling | [R16 §2](../notes/fixed-coupling-calibration.md); variational equations, compact bounds and matrix margin; [B47 review](../reviews/fixed-calibration-B47.md) |
| C089 | At that fixed coupling, exact nonlinear minimum-residual calibration has uniform initial-state error bounded by $C_\lambda(b+\rho)$ for preparation width b and four final-record errors rho. Accuracy–disturbance and canonical reconstruction-error products close as b,rho tend to zero at fixed apparatus masses, duration and geometry | R16 §§3–4; compact minimization, C088 and R06 disturbance bound; B47 review |

| C090 | At fixed sufficiently small positive coupling and incoming preparation width b, unknown initial probe momenta compensate every shell-state displacement at most b/(4L lambda), preserving all four exact nonlinear records with at least b/2 preparation margin | [R17 §§1–2](../notes/fixed-preparation-ambiguity.md); compact smooth dependence, contraction and shell chart; [B48 written review](../reviews/fixed-preparation-B48.md) |
| C091 | A common-record shell patch projects onto a canonical rectangle of half-widths L_*r and P_*r, r=min(r_0,b/(4LC_0 lambda)); every deterministic estimator has coordinate risks at least these half-widths, reconstruction product at least L_*P_*r^2, and compatible projected area at least 4L_*P_*r^2 | R17 §§2–3; exact shell chart and endpoint triangle inequality; B48 review; fixed product support and four-record access |

| C092 | For an admissible fixed R06 pulse design, unknown initial probe positions have final-momentum derivative lambda squared B plus a uniform order-three remainder; the finite-clock response makes B lower triangular with nonzero diagonal near the selected shell point | [R18 §§1–2](../notes/position-preparation-ambiguity.md); variational equations and pulse integration by parts; [B49 review](../reviews/position-preparation-B49.md) |
| C093 | With four initial and four final probe momenta revealed, a positive unknown initial-position box hides an exact shell square of radius r=min(r_0,lambda b/(4CC_0)); canonical reconstruction product is at least L_*P_*r squared and projected compatible area at least four times that value | R18 §§3–4; contraction with interior margin and R17 shell chart; B49 review; fixed design, small positive coupling and Cartesian preparation support |

| C094 | With known incoming clock data and probe momenta in fixed small boxes, the eight final pointer records uniformly determine receiver state and unknown incoming positions: the scaled record map is C1-close to (-A_c z,q) on a convex domain and has lower Lipschitz constant beta/2 at sufficiently small positive coupling | [R19 §§1–3](../notes/full-pointer-recovery.md); fixed pulse/cutoff margins, uniform clock signal rank, written variational and segment estimates; [B50 review](../reviews/full-pointer-B50.md) |
| C095 | Under C094, minimum-residual recovery gives canonical error product at most 16 L_*P_* max(rho_pi/lambda,rho_q)^2 / beta^2; it closes with final record errors at fixed positive coupling and fixed positive preparation widths | R19 §4; compact fit and triangle inequality, action units without 2 pi factor; B50 review; exact incoming clock/momentum information and joint final access supplied |

| C096 | An admissible fixed four-pulse design has clock-speed signal determinant derivative -partial_v log abs(det A)=10/v_0+O(epsilon)>0; two implicit equations give an exact common-eight-record receiver energy-shell curve with both canonical phase derivatives nonzero when initial clock data are hidden | [R20 §§1–4](../notes/hidden-clock-ambiguity.md); moment determinant, quadratic-energy transversality and preparation margins; [B51 review](../reviews/hidden-clock-B51.md) |
| C097 | On that fixed-domain family, clock offsets of half-width sigma give every deterministic estimator canonical risks at least k_x sigma and k_P sigma and product at least k_x k_P sigma squared, uniformly at sufficiently small positive coupling | R20 §5; common-record endpoints, fixed positive preparation margins; B51 review; action units, no positive-area conclusion |

| C098 | With revealed initial clock position, known zero probe momenta and exact receiver energy, the augmented eight-record/energy map has a uniform local lower Lipschitz bound gamma/2 on a fixed convex neighbourhood of R20's transverse shell point, for all sufficiently small coupling | [R21 §§1–3](../notes/clock-position-local-recovery.md); kernel reduction tau dv=0, fixed-unit derivative margin and segment integration; [B52 review](../reviews/clock-position-B52.md) |
| C099 | On a compact local shell patch times independent fixed apparatus boxes, minimum-residual fitting recovers receiver/probe positions and unknown initial clock momentum with joint error at most 4 delta/gamma and canonical product at most 16 L_*P_* delta squared/gamma squared, delta=max(rho_pi/lambda,rho_q) | R21 §4; compact fit, exact energy and triangle inequality; fixed positive coupling record-error limit closes the product; B52 review |

| C100 | For a sufficiently early fixed R20 pulse design, two distinct fixed clock speeds and revealed offset admit equal-energy distinct receiver states with identical eight scaled zero-coupling pointer records; the limiting energy-speed quadratic form has both signs and the actual pair follows by continuity | [R22 §§1–2](../notes/global-clock-speed-ambiguity.md); derivative-row expansion and normalized shell path; [B53 review](../reviews/global-clock-B53.md) |
| C101 | These common-record pairs persist with full back-reaction for all sufficiently small positive coupling inside fixed preparation margins; both canonical separations stay positive and every deterministic estimator has error product at least c_x c_P d_v squared/16 | R22 §§3–4; uniform implicit continuation, endpoint signs and two-point risks; B53 review; full shell and fixed speed separation |

| C102 | With known initial offset and zero incoming probe momenta, eight final pointer coordinates plus final clock momentum recover receiver state, incoming positions and unknown initial speed globally on a fixed bounded convex domain; the nonlinear leading map has lower Lipschitz constant beta=min(1,alpha/(1+D)), and the exact map at least beta/2 | [R23 §§1–2](../notes/final-clock-momentum-recovery.md); full clock reaction, uniform C1 perturbation and direct global bound; [B54 review](../reviews/final-clock-B54.md) |
| C103 | Under C102, minimum-residual recovery has canonical error product at most 16 L_*P_* max(rho_pi/lambda,rho_q,rho_c) squared/beta squared; it closes with record error at fixed coupling and positive preparation widths, without supplying exact receiver energy | R23 §3; compact fit, clock-record normalization and action units; B54 review |

| C104 | All ten final apparatus coordinates recover receiver state, incoming probe positions and both initial clock coordinates globally on a fixed bounded convex domain at sufficiently small positive coupling, with known zero incoming probe momenta and time T | [R24 §§1–2](../notes/full-clock-phase-recovery.md); explicit clock shear, uniform signal variation and complete C1 remainder; [B55 review](../reviews/full-clock-B55.md) |
| C105 | Under C104, minimum-residual fitting gives canonical error product at most 16 L_*P_* max(rho_pi/lambda,rho_q,rho_s,rho_c) squared/beta squared, closing with record precision at fixed apparatus and preparation without initial clock calibration or exact receiver energy | R24 §3; compact fit, unit conversion and fixed/joint limit conditions; B55 review |

| C106 | With every initial apparatus coordinate unknown in a full positive box, the inverse free shear gives exact compensation of all ten final records for receiver changes of norm at most b/(4 L lambda), with b/2 preparation margin; an exact energy-shell chart gives positive coordinate risks and projected area | [R25 §§1–2](../notes/full-apparatus-preparation-ambiguity.md); compact smooth-flow derivatives, self-mapping contraction, canonical shell chart; [B56 review](../reviews/full-apparatus-B56.md) |
| C107 | Under C106, if lambda<=min(lambda_0,b/(4 L D)), one full apparatus record is compatible with the entire receiver shell; coordinate minimax risks are sqrt(2E/k_x) and sqrt(2mu E), the optimal error product is 2E sqrt(mu/k_x), and projected compatible area is pi times that product | R25 §3; k_x=a-g^2/d>0, exact shell ellipse, endpoint lower bounds and constant estimator attaining both; B56 review; fixed positive width, no known exact apparatus energy |

| C108 | A backward trajectory from zero terminal probe phase, with terminal total energy E+H_0 and scalar amplitude adjustment, gives exact initial receiver energy E and apparatus energy H_0 with O(lambda) apparatus displacement and b/2 preparation margin | [R26 §§1–2](../notes/energy-constrained-apparatus-ambiguity.md); smooth inverse flow, derivative 2E, exact conservation; [B57 review](../reviews/energy-symmetry-B57.md) |
| C109 | Simultaneous receiver/probe sign reversal gives an exact antipodal initial receiver pair with identical full final apparatus records and both initial energies; the canonical risk-product lower bound tends to E sqrt(mu/(a-g squared/d)) as coupling vanishes at fixed positive preparation width | R26 §§3–4; local equation symmetry, zero terminal probes and two-point risk; B57 review; lower-bound limit, not exact minimax or area |

| C110 | With one nonzero calibrated initial probe displacement and exact receiver/apparatus energies, an eleven-coordinate preparation chart and Borsuk–Ulam give distinct initial states with identical ten final apparatus coordinates and positive box margins | [R27 §§1–2](../notes/calibrated-displacement-ambiguity.md); exact energy charts, compact S^10 and continuous record map; [B58 review](../reviews/calibrated-displacement-B58.md) |
| C111 | Under C110, the inverse-shear flow estimate forces receiver separation at least 2r/sqrt(1+4L squared lambda squared) and full-state minimax error at least r/sqrt(1+4L squared lambda squared), in fixed Euclidean component units | R27 §3; ambient convex-domain derivative bounds and parameter projection; B58 review; dimensionless full-state bound, canonical product unresolved |

| C112 | For a fixed smooth pulse design, nonzero q_1 calibration and exact receiver/apparatus energies admit an exact common-ten-record curve with both canonical derivatives bounded away from zero on a fixed weak-coupling rectangle | [R28 §§1–3](../notes/calibrated-canonical-ambiguity.md); scaled compensator constraints, pulse kernel and uniform implicit continuation; [B59 review](../reviews/calibrated-canonical-B59.md) |
| C113 | Under C112, every deterministic estimator has canonical risk product at least delta squared times absolute v_x v_P divided by 4, uniformly for sufficiently weak positive coupling at fixed preparation | R28 §4; exact common-record endpoints and triangle inequality; action units, design/preparation/energy-dependent, no area or minimax equality |

These are checked derivations. C006 is conditional on its stated quantum
measurement premises. For a new result, provide quantifiers, units, path/operator
domain, boundary conditions, dependencies and gap-closing limits in the proof.

## Literature status

C112–C113: [B59](../references/batches/B59.md) audits inherited smooth-flow,
contraction and inverse methods, with coordinator checking Freire pp. 1–3.
The scaled Hamiltonian constraints, fixed pulse-kernel design, exact curve
and canonical bounds are model-derived; novelty unassessed. One sequential
Luna-low worker and coordinator written proof review completed.

C110–C111: [B58](../references/batches/B58.md) directly verifies the established
Borsuk–Ulam theorem in Arora's Princeton Lecture 13, Theorem 1, PDF p. 1.
The constrained chart and quantitative receiver separation are model-derived
consequences. One sequential Luna-low audit and coordinator source/proof review
completed; exact mechanical prior-art matches and novelty remain unassessed.

C108–C109: [B57](../references/batches/B57.md) audits inherited smooth-flow
and implicit/contraction methods, with zero queries or retrievals. The
backward terminal construction, two-energy sign pair and canonical risks are
model-derived. One Luna-low audit and coordinator written review completed;
exact prior-art matches and novelty remain unassessed.

C106–C107: [B56](../references/batches/B56.md) audits inherited B48/B55
contraction, inverse and smooth-flow methods with zero queries or retrievals.
The free-shear compensator and exact whole-shell saturation are model-derived
consequences; novelty is unassessed. One sequential Luna-low worker and
coordinator written proof/coverage review completed; no fresh source-page reading.

C104–C105: [B55](../references/batches/B55.md) is a zero-query inherited-source
audit of B54/B50 inverse and smooth-flow methods. The full clock extension and
canonical precision bound are model-derived; novelty unassessed. One Luna-low
worker and coordinator written review completed, with no fresh passage claim.

C102–C103: [B54](../references/batches/B54.md) rechecks the existing Freire
perturbation precedent in three pages, with zero discovery queries. The
nonlinear leading-map bound, clock calibration and risk closure are derived
consequences. One Luna-low audit and coordinator source/proof review complete;
novelty unassessed.

C100–C101: [B53](../references/batches/B53.md) audits the local/global
identifiability distinction in Quaiser et al. (2011). The shell pair,
positive-coupling continuation and canonical risk bound are model-derived.
One sequential Luna-low worker and coordinator source/proof review completed;
source metadata was corrected and novelty remains unassessed.

C098–C099: [B52](../references/batches/B52.md) identifies the established
small-Lipschitz-perturbation inverse method in Freire's institutional lecture
notes. The energy-speed Schur complement, uniform physical domain and
canonical recovery bound are model-derived. One sequential Luna-low audit
and coordinator source/proof review are complete; novelty is unassessed.

C096–C097: [B51](../references/batches/B51.md) supplies a bounded Sontag
input-output-equivalence precedent and inherits B50 smooth-flow methods.
The pulse determinant, exact shell family and risk product are model-derived;
novelty is unassessed. One sequential Luna-low worker and coordinator source
and written proof reviews are complete.

C094–C095: [B50](../references/batches/B50.md) verifies the standard smooth-ODE
dependence premise in four selected Sideris pages. The uniform block inverse
and canonical error-product bound are model-derived consequences of standard
perturbation and residual estimates. This bounded premise audit leaves novelty
unassessed and supplies no exact apparatus match.

C092–C093: [B49](../references/batches/B49.md) verifies a standard local
observability precedent and inherits smooth-flow/contraction methods from
B47/B48. The clock-response matrix and exact position compensation are derived
consequences. The bounded audit leaves novelty unassessed; coordinator scan
review corrected the article and theorem pagination.

C090–C091: [B48](../references/batches/B48.md) supplies established contraction
and two-point lower-bound precedents. Exact nonlinear apparatus compensation,
energy-shell patch and canonical projected area are derived consequences;
novelty remains unassessed. Coordinator corrected source metadata and coverage
and reviewed the written proof independently of the statistical comparison.

C088–C089: [B47](../references/batches/B47.md) checks a standard smooth-ODE
dependence premise and inherits the Theurel pointer comparison from B37.
Uniform record-map remainder, nonlinear calibration and fixed-coupling product
closure are derived consequences. The bounded assumption audit leaves novelty
unassessed; fresh and inherited coverage are recorded separately.

C086–C087: [B46](../references/batches/B46.md) supplies bounded optimal-recovery
and convex-support context, with no exact mechanical match in two queries
and two selected passages. These are derived consequences of the stated
model; novelty remains unassessed. Coordinator corrected a worker exponent
label and versioned source anchor before acceptance.

C084–C085: [B45](../references/batches/B45.md) supplies bounded optimal-recovery
and convex-norm context. Exact mechanical projection, finite-horizon transfer
and copy-count exponents are derived consequences; no exact match was obtained
in the two-query coverage. Novelty remains unassessed.

C082–C083: [B44](../references/batches/B44.md) retains the established prepared
pair; the finite-horizon law, blind-delay extension and transient composition
are derived consequences. No exact match was obtained in the bounded coverage;
novelty remains unassessed. Coordinator corrected source attribution and timing.

C080–C081: [B43](../references/batches/B43.md) reuses Seeber–Haimovich's
established one-body bounds. Product support addition, canonical composition,
aggregate image equality, strict information loss and radius-closure conclusions
are derived here from explicit hypotheses. Ruan–Chirikjian supplies geometric
context, with no exact minimax match in the bounded coverage. Novelty remains
unassessed; proof acceptance rests on the written argument and coordinator review.

C078–C079: [B42](../references/batches/B42.md) matches C079's prepared
zero-initial-state pair exactly to Seeber–Haimovich Proposition 3.1 and its
upper bound to §4. The blind-delay phase risks are derived consequences.
C078 has a written proof but no direct source match in this bounded batch;
novelty remains unassessed. The review corrects the worker's initial-data
and half-separation statements.

C076–C077: [B41](../references/batches/B41.md) identifies the exact equal-error
finite-difference bound and optimum in Seeber–Haimovich §4. These are established
results. The fixed mechanical experiment, unequal-error delayed phase estimate
and action-product consequences are derived here; novelty is unassessed.

C074–C075: [B40](../references/batches/B40.md) identifies bounded-error
set-membership and classical mixed-area precedents. The clipped-lens area
and joint bound are derived specializations; novelty is unassessed. Proof
acceptance and limited source coverage are separated in the coordinator review.

C072–C073: [B39](../references/batches/B39.md) records the bounded double-integrator
and discrete hybrid reachable-set precedents. Continuous-time composition,
the rectangle counterexample and conditional areas are derived specializations;
novelty is unassessed. [Coordinator review](../reviews/cut-composition-B39.md)
accepts the written proofs separately from the two-query source coverage.

C070–C071: [B38](../references/batches/B38.md) verifies Liberzon's classical
double-integrator and one-switch time-optimal control passage. The fixed-time
lens, information restriction and deterministic minimax proof are derived
specializations, with novelty unassessed. Two other source routes were
unreadable. [Coordinator review](../reviews/causal-information-B38.md) verifies
the self-contained proof separately from this bounded prior-art coverage.

C068–C069: [B37](../references/batches/B37.md) uses zero searches and four
cached primary pages: Theurel pp. 5–7 and Hermann–Krener p. 733. Conserved
pointer records and the observability rank condition are established ingredients.
The autonomous construction, integrated signal map and uniform bounds are
derived consequences, with novelty unassessed. [Coordinator review](../reviews/autonomous-readout-B37.md)
accepts the written proofs under the explicit preparation, record-access and
latency premises. B36's existing source work is preserved and integrated.

C066–C067: [B35](../references/batches/B35.md) covers Katagiri v2 §5 and
Theurel's APS abstract with two queries and two bounded primary readings.
Canonical pointer coupling is established; the support-width and finite-chain
refinement estimates are derived consequences with novelty unassessed.
[Coordinator review](../reviews/classical-readout-B35.md) accepts the written
proofs for scalable impulsive probes. R06/B37 now supplies a finite-mass,
finite-duration delayed reconstruction and selected full-model Theurel readings;
causal new information with restricted precision remains R07.

C064–C065: [B34](../references/batches/B34.md) covers Zwanzig's exact
oscillator-bath reduction and Hermann–Krener's observability framework in
two searches and three primary pages. Chain coefficients, sampled determinant
and scaling are derived specializations; exact prior publication is unassessed.
[Coordinator review](../reviews/three-body-memory-B34.md) accepts the written
proofs separately from the bounded literature coverage.

C062–C063: [B33](../references/batches/B33.md) audits two cached primary
pages with zero searches. Harmonic propagation and bath-memory reduction are
established ingredients; the fixed-energy conditional kernel, reset limit and
action comparison are elementary derived consequences, with novelty unassessed.
[Coordinator review](../reviews/classical-cut-state-B33.md) accepts the written
proofs and corrects the worker's source-page coverage.

C060–C061: [B32](../references/batches/B32.md) verifies the classical
Fenchel–Borsuk input in Milnor (1950). Mechanical inequalities and the smooth
equality construction are derived consequences, with novelty unassessed in
the bounded one-query, two-page audit.

C058–C059: [B31](../references/batches/B31.md) matches the established
relativistic circular-balance and radial-stability framework. The fixed smooth
force-bounded example and conditional speed-floor inequality are derived
consequences; exact prior publication is unassessed in the bounded search.

C056–C057 have the bounded [B30 audit](../references/batches/B30.md):
conformally symplectic scaling has established geometric prior art; the exact
model map and conditional infimum statements are elementary derived consequences.
No exact match was found in the two-source coverage; novelty is unassessed.
[Coordinator review](../reviews/dilation-B30.md) accepts the written proofs.

C054–C055 have the bounded [B29 audit](../references/batches/B29.md):
covariance determinant and affine symplectic invariance are established
rms-emittance machinery; circular formulas and threshold transfer are derived
specializations, with novelty unassessed. Uniform phase is sufficient for the
action equality; matching its first and second moments also suffices.

Proof status above and literature status below are independent. Each accepted
result has a bounded librarian audit; exact source inputs and elementary
consequences are identified separately.

| Claims | Literature classification | Audit |
| --- | --- | --- |
| C052 | Established Boyer orbit classification, with explicit domain and normalization | [B27](../references/batches/B27.md), [B28](../references/batches/B28.md) |
| C053 | Elementary effective-potential consequence; no exact match in two-query follow-up coverage; novelty unassessed | B28 |
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
| C039 | Established normalized checkerboard reconstruction; elementary wavepacket and spectral-limit consequences | [B18](../references/batches/B18.md); Skopenkov–Ustinov Definition 2, Propositions 5–6, direct basis match and coordinator proof |
| C040 | Elementary measurement-protocol consequence of the audited coin, with no novelty claim | B18 bounded addendum checks Born probability and union bound; exact prior-art formulation not separately searched |
| C041 | Standard finite reversible spectral/product-chain consequence of the established Green–Kubo representation | [B20](../references/batches/B20.md); Pavliotis pp. 4–5, coordinator proof; explicit hidden-label specialization |
| C042 | Elementary frame/inverse-operator consequence; exact combined formulation unmatched and not independently searched | B20 bounded algebra/prior-art audit; novelty unassessed, no novelty claim |
| C043–C044 | Elementary bounded-control and Lipschitz-variance specializations; exact combined prior-art match not found in bounded search | [B21](../references/batches/B21.md); two worker searches, one coordinator search and Liberzon framework passage; no novelty claim |
| C045 | Elementary product-chain and response counterexample; exact example publication not established, no novelty claim | [B22](../references/batches/B22.md); saved Luna-low audit and coordinator review |
| C046 | Standard tensorization and derived local-frame consequence | B22; Levin–Peres §12.4, direct continuous-generator proof and clock audit |
| C047 | Elementary finite harmonic propagation and displacement-variance consequence; phase-torus and centre conventions explicit | [B23](../references/batches/B23.md); Ford–Kac–Mazur and Zwanzig source ingredients; bounded audit, no novelty claim |
| C048–C049 | Harmonic-chain spectral ingredients established; normalized limit and fixed-phase speed-support consequences derived | [B24](../references/batches/B24.md); three-page bounded audit, coordinator proof/source review; no novelty claim |
| C050 | Established dichotomic Jepsen-gas covariance and Markov interpretation; explicit gap proof and action/scaling consequences | [B25](../references/batches/B25.md); source pp. 7–8, 17–19 and coordinator proof review |
| C051 | Explicit ordered-preparation consequence; exact ensemble unmatched in two-query search, novelty unassessed | [B26](../references/batches/B26.md); two HTML documents, coordinator proof review |

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

[B23](../reviews/harmonic-receiver-B23.md) supports C047 through one Luna-low
audit and coordinator source/proof review. Eight identities, three network
checks and four bound cases pass. Finite-size and large-receiver limits remain
separate; the friction kernel is distinguished from velocity covariance.

[B22](../reviews/observable-access-B22.md) supports C045–C046: saved Luna-low
audit, coordinator source-image and proof review, six identities, three
rational velocity cases, three product spectra and two frame checks. The
source's clock normalization and printed proof index are explicitly corrected.

[B20](../reviews/susceptibility-B20.md) audited C041–C042 with one Luna-low
worker. Coordinator verified the weighted centered-space inverse, inequality
directions, frame hypothesis, parameter-family limits and Pavliotis p. 5
visually. Eleven identities, five rational bound cases and four weighted-chain
checks pass. Sokal remains a discovery-only route, not a passage attribution.

[B18](../reviews/checkerboard-B18.md) audited C039–C040 with one Luna-medium
worker and a bounded addendum. Coordinator checked source pp. 12, 13, 19,
31 visually; corrected version date, proof-page anchor and kernel scope;
proved the explicit basis map and strong wavepacket limit. Fourteen algebra
identities, fourteen finite path/norm checks and three numerical mode tests pass.

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
