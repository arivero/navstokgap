# Notation and scale roles

Reference map, 2026-10-01. Definitions are local to the linked notes;
matching letters do not imply matching physical quantities. Keep c, ℏ and
dimensional couplings explicit when converting rates or cutoffs to physics.

| Newton quantity | Definition / units | Conceptual role and caution |
| --- | --- | --- |
| τ, partition mesh | Cell duration; time | Time regulator/refinement parameter; different from preparation width or observation horizon |
| F, m, v | Force, mass, horizontal velocity | Physical model parameters; m cancels from some scaled relations but controls the mechanical action at fixed force |
| A=vFτ³/(6m) | Inertial–parabola spatial area | Observable geometric area, not action; (3F/v)A=τΔE |
| ΔE=F²τ²/(2m) | Kinetic-energy gain from rest in the forced direction | Deterministic energy gain, not energy uncertainty |
| τΔE=F²τ³/(2m) | Action | Galileo comparison observable; equals 12Kτ in the constant-force convention |
| Kτ=F²τ³/(24m) | Action; Dirichlet chord-defect functional | Matched-endpoint cell action; cut s spends 3s(1−s)Kτ. The inertial area and chord lens differ by endpoint convention |
| s, J | s=Fτ²/(2m), J=Fτ in the record-cost trilogy | Inertial sag/displacement and impulse; midpoint chord sagitta is Fτ²/(8m), four times smaller. Elsewhere s is a dimensionless cut fraction |
| κ | Action in δΔ≥κ | Supplied mark error/recoil constant. Quantum position probes give κ≥ℏ/2. A Brownian diffusion convention also calls mD κ, with different factors |
| ζ | √detΣ; action for a canonical pair | Covariance-area ceiling/floor parameter; affine Gaussian statistical-speed result gives h*=2ζ. A prior restriction is not automatically posterior closure |
| h, ℏ=h/(2π), h* | Action | Planck phase unit, reduced phase unit, and classical statistical-speed coefficient respectively; equality requires a calibration theorem |
| h_rad, γ | Action and dimensionless matching coefficient | Radiation unit from thermodynamic scaling; conditional SED matching gives h*=γ h_rad. Positivity of the radiation unit does not prove apparatus closure |
| δ, σ; Δ | Position resolution and impulse spread | Apparatus/preparation resources. σ may be a Gaussian pointer width, not a cutoff; δ also denotes other errors in gauge notes |
| L, P; LP | Position/momentum aperture; action product | Bounds on body states used by a protocol; a balanced aspect ratio is extra input, so area alone is insufficient |
| Statistical/Bures angle θ | Dimensionless distance between laws/states | Record distinguishability or information path length, not an action scale. Multiplication by a supplied h* or ℏ enters a speed bound |
| ε | Error probability, action resolution, or small perturbation depending on note | Never substitute one role for another; ε→0 may change preparation and resources |

Newton sources: [insertion action](../notes/newton-insertion-action.md),
[cut measure](../notes/cut-measure-newton.md),
[mark cost](../notes/mark-cost-and-statistical-floor.md),
[path length](../notes/record-distance-path-length.md),
[routes](../notes/newton-indeterminacy-routes.md),
[radiation unit](../notes/necessity-unit-and-indeterminacy.md).

| Gauge quantity | Definition / units | Conceptual role and caution |
| --- | --- | --- |
| a, a0; L | Spatial/temporal lattice spacing and physical box length | UV regulators versus IR volume; limits and anisotropy must be stated |
| t | Heat-kernel plaquette time, dimensionless | Gauge weight parameter, not physical time; in the repository convention t=λD a^(4−D), up to explicitly stated action normalizations |
| λD=ℏ g_cl² | Length^(D−4) | Supplied dimensionful gauge coupling in D dimensions; D=4 gives g² containing ℏ |
| g², β | Dimensionless bare coupling and Wilson coefficient | Wilson convention β=2N/g², hence 6/g² for SU(3); heat-kernel and Wilson actions need explicit matching |
| n, b, a_n=b^n a | Block depth, factor, coarse spacing | RG schedule/regulator labels; a physical scale is held fixed through matching, not by keeping every bare coefficient fixed |
| ξ_lat, ξ_phys=aξ_lat | Correlation length in lattice cells / length | An exponential clustering scale; relation to a physical Hamiltonian gap needs reconstruction and admissible observables |
| δ_lat, Δ_phys | Dimensionless spectral gap / energy | Δ_phys=(ℏc/a)δ_lat when that transfer/Hamiltonian normalization applies. A relaxation clock or a physical inverse length has different units |
| m, m_gap | Mass, energy, or inverse correlation length by local convention | Translate explicitly: energy E, mass E/c², inverse length E/(ℏc). “m>0” alone does not specify units |
| Λ | Inverse length from dimensional transmutation | Dynamically generated scale relative to a calibrated trajectory; existence of Λ does not prove positive spectral weight or m_gap/Λ>0 |
| Strong-coupling target | Region of coupling plus bounds on generated local interactions | Sufficient finish-line criterion for its transfer/Hamiltonian; an effective action must actually arrive there |
| ε_sf, t^α; k_t, p | Chart size / heat-dependent small-field scale; moment order and rarity | Technical control parameters; p is a probability majorant, not momentum |
| u, q=u^−1, r | Source/response or recoupling parameters | Their domains differ: (113)'s u and a weak-recoupling strip are not the physical coupling g² |
| c_C, b_H, a_H | Good polymers, bad supports, dressed activities | Expansion coefficients with specified support norms; activity bounds are not yet the full physical nonlinear integral |
| β_eff, generated vertices | Coefficients after elimination | Effective couplings, often including nonlocal or higher-order interactions. Keeping only one coefficient requires a controlled truncation |
| b0=11N/(48π²) | Dimensionless one-loop coefficient | Perturbative matching input in four dimensions; for SU(3), 11/(16π²); not itself a mass-gap lower bound |

Gauge sources: [series/parallel](../notes/series-parallel-gauge-refinement.md),
[lattice obligations](../notes/mass-gap-obligations-lattice.md),
[target box](../notes/strong-coupling-target-box.md),
[small-field notebook](../notes/su2-midplane-small-field.md),
[4D composition](../notes/four-dimensional-composition.md).

For new explanatory prose use τ for mechanical time, t_hk when gauge heat
time might be confused with it, s_cut versus s_sag for the two s conventions,
and Δ_phys for energy gaps. Retain existing source notation and give its
local definition. In particular, uv-halving-ir-confinement writes t=ℏg²
in passages where g is the classical coupling; the lattice/LLM convention
usually absorbs ℏ into g² and writes t=g². Do not add a second ℏ when
transferring those formulas. Its exponent coefficient γ is called c in the
atlas, where c also denotes the speed of light elsewhere.
No source-wide normalization change is warranted by this
audit. An overall classical action factor rescales the ratio S/ℏ in a path
integral only once that quantum representation and the held ℏ are specified;
classical equations alone can be unchanged by a common factor.
