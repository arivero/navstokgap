# B75: result-specific publication audit for the elastic-gas comparison

## Finding

The bounded search found no exact publication match for the complete C050--C051 comparison: an equal-mass one-dimensional hard-point gas with speeds $\pm u$, compared under a marked Poisson preparation and two independently shifted opposite-sign lattices of spacing $2/\rho$, with fixed $m,u,\rho$, energy density and mean tagged collision rate $\rho u$, but respectively $D=u/(2\rho)$ and $D=0$ through bounded periodic displacement.

There is, however, close conceptual prior art. Leibovich and Barkai compare random and equally spaced initial positions at the same density for hard-core Brownian single-file dynamics and obtain different tagged-particle transport coefficients. Cividini and Kundu place the dependence on quenched versus annealed initial configurations in a broader arbitrary-initial-position framework. These sources make “initial correlations affect tagged transport” an established message. The draft's defensible contribution is the elementary Hamiltonian sharpening: velocity-mark correlations change ordinary diffusion into exact periodic cancellation while the kinetic scales and mean collision frequency remain matched. The audit is bounded and supports no claim of novelty or priority.

## Source 1: equal spacing versus random positions

N. Leibovich and E. Barkai, *The Lasting Effect of Initial Conditions on Single File Diffusion*, arXiv:1304.7462v1 (2013), published as *Physical Review E* 88, 032107, DOI 10.1103/PhysRevE.88.032107.

- Primary routes: [arXiv record](https://arxiv.org/abs/1304.7462), [versioned record](https://arxiv.org/abs/1304.7462v1), [PDF](https://arxiv.org/pdf/1304.7462).
- Local retrieval: `.build/b75/leibovich-barkai-1304.7462.pdf`, paired with `.build/b75/leibovich-barkai-1304.7462.md`; SHA-256 `4d14e0249449179f5d979a01371f9f3b1bdb4374625a18a0f7fc16ca7a5a86c9`.
- Reading level and coverage: **passage**, PDF pp. 1--4 and 9--10 (six substantive pages). Text extraction located passages; equations and preparation statements on pp. 1--4 were checked against the selected PDF pages.

Page 1, abstract and Sections I--II, states the comparison between equal particle spacings and a uniform equilibrium distribution, with density held fixed, and announces different mean-square displacements and transport coefficients. Page 2, equation (1), defines the regular preparation $x_n(0)=na$; equation (2) gives
\[
 \langle x_T^2(t)\rangle_{\rm lat}
 =a\sqrt{2D/\pi}\,t^{1/2},\qquad
 \langle x_T^2(t)\rangle_{\rm uni}
 =2\rho^{-1}\sqrt{D/\pi}\,t^{1/2},
\]
and explicitly compares them at $a=\rho^{-1}$. Pages 2--4 use the Jepsen-line/noninteracting-label mapping for identical hard-core Brownian particles. Page 9, Section VII, concludes that the generalized diffusion coefficient and two-time correlations retain preparation dependence at long times; it specifically calls for Hamiltonian one-dimensional tagged-particle examples without stochastic assumptions beyond random preparation. Page 10 restates the identical-particle label-exchange construction in the simulation appendix.

This is a near match to the teaching thesis and to the regular-versus-random comparison. It is not an exact source overlap with C050--C051: the microscopic trajectories are Brownian rather than ballistic $\pm u$ lines; there are no two independently shifted, velocity-marked sublattices; the reported difference is a $\sqrt2$ prefactor rather than positive diffusion versus bounded periodic motion; and no matched tagged collision rate $\rho u$ is formulated.

## Source 2: arbitrary initial configurations

J. Cividini and A. Kundu, *Tagged particle in single-file diffusion with arbitrary initial conditions*, arXiv:1704.04017v1 (2017), *Journal of Statistical Mechanics: Theory and Experiment*, DOI 10.1088/1742-5468/aa75de.

- Primary routes: [arXiv record](https://arxiv.org/abs/1704.04017), [versioned record](https://arxiv.org/abs/1704.04017v1), [PDF](https://arxiv.org/pdf/1704.04017).
- Local retrieval: `.build/b75/cividini-kundu-1704.04017.pdf`, paired with `.build/b75/cividini-kundu-1704.04017.md`; SHA-256 `5012c1cbd2c0514a856173fdd4f9838f899b91a4917708c0c5f41b61dd794c54`.
- Reading level and coverage: **abstract/passage**, PDF pp. 1--2 (two substantive pages). The paper's later formulas and examples were not read under this batch's page budget.

Page 1 states an exact tagged-position distribution for arbitrary initial particle positions and general single-particle propagators. Page 2, Section I, distinguishes uniform annealed initial positions from uniform quenched positions at spacing $\rho_0^{-1}$ and summarizes established differences in mean-square-displacement prefactors and large-deviation functions. It also distinguishes diffusive tagged motion for Hamiltonian individual dynamics from subdiffusion for Brownian particles.

This supplies broad correlation-dependence context, not an exact match. The selected passages do not specify opposite velocity marks tied to two lattice phases, a uniform-phase square-wave tag, matched collision frequency, bounded displacement, or $D=0$. Because only pp. 1--2 were read, B75 does not claim that the paper's full general formalism excludes or subsumes the ordered construction.

## Exact source overlap and model-specific content

The existing B25 source remains the direct literature match for C050's Poisson endpoint: Balakrishnan, Bena and Van den Broeck give the two-speed covariance $u^2e^{-2\rho ut}$ and hence $D=u/(2\rho)$. B75 adds no new reading of that source. The two B75 sources overlap with the broader proposition that tagged transport retains initial-condition dependence and, in Leibovich--Barkai, with a same-density random-versus-regular comparison.

Within the selected B75 passages, the following finished-comparison elements remain model-specific derivations in the repository: the two independent uniform shifts; the assignment of $+u$ and $-u$ to separate spacing-$2/\rho$ lattices; equality of $m,u,\rho$, energy density and mean tagged collision rate across the two preparations; the exact square-wave period $2/(\rho u)$; bounded displacement; and the endpoint contrast $D=u/(2\rho)$ versus $D=0$.

## Discovery and page accounting

Exactly four discovery queries were used on 2026-09-13:

1. `"hard-point gas" "equally spaced" tagged particle velocities`
2. `Jepsen gas lattice initial conditions tagged particle diffusion correlated positions`
3. `"hard point gas" periodic initial condition alternating velocities tagged`
4. `single file diffusion quenched lattice initial condition tagged particle correlations`

Search snippets were discovery leads only. Two primary sources were selected. The substantive-page total was eight: Leibovich--Barkai pp. 1--4 and 9--10 (six), plus Cividini--Kundu pp. 1--2 (two). Metadata/abstract records were checked separately. No citation chaining, additional discovery query, numerical calculation or symbolic script was used.

## Source-to-model and teaching suggestion

Position the draft as a Hamiltonian sharpening of the established preparation-memory lesson. Cite Leibovich--Barkai at the first statement that regular and random preparations can yield different tagged transport, then make the new pedagogical step explicit: positional regularity alone changes a coefficient in their Brownian file, whereas coupling each velocity sign to its own random-phase lattice produces exact square-wave cancellation and drives the ordinary diffusion coefficient all the way to zero without changing the mean collision rate. A compact comparison table should list microscopic propagator, position law, velocity-mark law, tagged clock and long-time displacement; this prevents the broad known lesson from being mistaken for the draft's specific construction.


## Coordinator verification and editorial use

The coordinator rechecked both versioned arXiv metadata records and read
Leibovich–Barkai PDF pp. 1–2 and 9 and Cividini–Kundu pp. 1–2 from the cached
originals. These are within the worker's selected pages. The manuscript uses
only the preparation-dependence prose, not either source's displayed transport
formula. The Cividini–Kundu cached PDF has 13 physical pages and a 2021 typeset
date despite its 2017 v1 arXiv watermark/record; cite the arXiv version and the
stated physical page anchors, not an inferred new scientific revision.

The coordinator separately read the [AJP editorial policy](https://www.aapt.org/Publications/AJP/About/editorial_policy.cfm)
on 2026-09-13. This editorial check is outside the two-paper scientific audit;
no further discovery query was used. The policy requires accessibility,
teaching value and original physical insight; it does not make expository
repackaging sufficient. P05 is an author-review draft, with editorial acceptance
and originality beyond this bounded coverage still unestablished.
