# B75 review: does the elastic-gas comparison survive publication audit?

## Judgement

Yes, as a focused teaching exposition with a specific model contribution. No novelty claim is justified by this bounded audit.

The broad message that initial preparation and correlations affect tagged transport is established prior art. Leibovich and Barkai directly compare random and equally spaced initial positions at the same density in a hard-core Brownian file and obtain different generalized diffusivities. Cividini and Kundu explicitly organize tagged-particle results by quenched and annealed initial configurations. A draft claiming simply “same hard-core law, different preparation, different transport” would be too broad.

C050--C051 adds a sharper elementary Hamiltonian example within the passages checked: both stationary marked-gas preparations use equal masses and speeds $\pm u$ with the same density, energy density and mean tagged collision rate $\rho u$, but the Poisson tag has $D=u/(2\rho)$ while the shifted-lattice tag has square-wave period $2/(\rho u)$, bounded displacement and $D=0$. The audit found no source stating that complete package. Since four queries and eight pages cannot establish absence from the literature, the correct status is “unmatched in bounded coverage.”

## Claim-to-source review

| Draft statement | Evidence status after B75 | Publication treatment |
| --- | --- | --- |
| Equal-mass hard-point collisions admit the free-line/label-exchange map | Established ingredient in B25/B26 and reiterated by Leibovich--Barkai pp. 2--3, 10 | Cite a standard source; do not advertise as contribution |
| Poisson two-speed tag has covariance $u^2e^{-2\rho ut}$ and $D=u/(2\rho)$ | Direct B25 literature match; repository gives an explicit spatial-gap derivation | Cite Balakrishnan--Bena--Van den Broeck; use the derivation pedagogically |
| Initial conditions/correlations can alter tagged transport | Direct broader overlap with Leibovich--Barkai pp. 1--2, 9 and Cividini--Kundu pp. 1--2 | State as established motivation |
| Two independently shifted, opposite-sign lattices give a stationary square-wave tag of period $2/(\rho u)$ and bounded displacement | Repository derivation; unmatched within B75's selected passages | Present as the concrete construction, with bounded-search wording only if literature status is mentioned |
| The Poisson and ordered preparations match $m,u,\rho$, energy density and mean collision rate but have $D>0$ and $D=0$ | Finished comparison unmatched within B75 | Make this the paper's central proposition and teaching payoff |

The manuscript's phrase “This comparison isolates correlation control” is mathematically supported. For publication, “isolates” should refer to this pair of preparations and its listed matched observables; it should not imply that the literature had not previously demonstrated preparation dependence.

## Consistency checks

The source/model distinctions are material and consistent:

- Leibovich--Barkai holds mean density fixed between a Brownian equilibrium position ensemble and an equally spaced position ensemble. Its coefficient changes by a finite prefactor; its tag remains subdiffusive in both cases.
- C050--C051 uses ballistic free trajectories with fixed speeds and changes the joint position--velocity marking. The ordered endpoint is nonmixing and periodic, so the ordinary diffusion coefficient is zero.
- B75 found no checked passage equating regular positions by themselves with the draft's two independent velocity-marked lattices. The random global phases establish stationarity of the marked configuration, while the Palm tag fixes an origin; publication prose should continue to distinguish configuration/velocity stationarity from stationarity of absolute tagged position.

## Recommended teaching position

Cite Leibovich--Barkai before presenting the model and say that fixed-density regular versus random preparations are already known to change tagged transport in Brownian single-file systems. Then describe C050--C051 as the Hamiltonian limiting contrast: correlations in both gaps and velocity marks preserve the mean collision clock yet turn the tag into an exact square wave. A one-page assumptions-and-outcomes table would make the physical lesson accessible and identify precisely what the construction adds.

## Audit limits

The review relies on the exact four-query list and eight-page accounting in the [companion](../docs/batches/B75/publication-source-companion.md). It selected two primary sources and did not audit their complete proofs or citation networks. Search snippets were not evidence. The conclusion is result-specific bounded coverage, not exhaustive prior art, novelty or priority. No numerical or symbolic verification was performed.


## Coordinator manuscript consistency review

The standalone manuscript `papers/same-collisions-different-transport.tex`
reuses the accepted C050–C051 arguments. Section 3 copies the collision-time
construction and divides C050's mass-normalized response by m to recover
position variance; section 4 gives C051's residual-time integral and folded
periodic variance. No new claim ID is introduced.

Written checks: Poisson stream intensity rho/2 and relative speed 2u give
rate rho u; the velocity covariance decays at twice that reversal rate.
The ordered first residual is uniform on (0,d), whereas complete intervals
are d; its residual mean d/2 is not the reciprocal of the long-run collision
rate. The variance bound is u^2 d^2/3=1/(3 rho^2). Both stationary velocity
laws are distinguished from the pinned absolute tagged position. The ordered
state changes the joint position–velocity law, not only the unmarked spacings.
The infinite gas precedes the long-time limit. The ordered covariance is not
assumed integrable; bounded displacement directly proves D=0.

Claim-to-source map: elastic label exchange and the Poisson endpoint reuse
B25; the explicit ordered proof reuses B26; the introductory comparison with
Brownian preparations uses B75's independently rechecked passages. The single
collision figure is a schematic of label exchange, not simulation data.
The classroom questions ask students to reproduce displayed steps. No
numerical/symbolic verification scripts were created or run.
