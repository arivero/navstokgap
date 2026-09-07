# Programme review: composition, crossover and checkerboard dynamics

Composition is the next main selection test. The crossover inequality and
checkerboard correspondence supply a focused companion calculation; the
two-state generator supplies a useful spectral example. This review adopts
those directions with explicit preparation, composition and operator tests.
It assesses the user's six suggestions on 2026-09-08 against C018–C034.

The calculations below are working derivations for task design. B15 verifies
bounded source leads, rather than completing a per-result literature audit.
They enter the accepted claim ledger after their dedicated derivation and audit.
C033–C034 and B14 are already allocated to the completed return bridge.

## 1. Composition: promote to A08, the next main task

The proposed coefficients are correct for independent constituents, with
$M=m_1+m_2$, reduced mass $\mu=m_1m_2/M$, centre position
$R=(m_1X_1+m_2X_2)/M$, and relative position $r=X_1-X_2$.
If $\operatorname{Var}(\Delta X_i)=\kappa_i\Delta/m_i$, direct covariance
transformation gives

$$\kappa_{\rm cm}=\frac{m_1\kappa_1+m_2\kappa_2}{M},\qquad
\kappa_{\rm rel}=\frac{m_2\kappa_1+m_1\kappa_2}{M},\qquad
\kappa_{\rm cm}+\kappa_{\rm rel}=\kappa_1+\kappa_2.$$

For Gaussian bridges the same calculation uses their common temporal covariance
kernel. For stationary Green–Kubo coefficients use independence of the entire
constituent processes and convergence of their correlation integrals. Bound
particles with correlated noise require the cross-correlation terms.

If all positive masses are admissible, $\kappa(m)\ge0$ depends only on mass,
and the composite coefficient equals $\kappa(M)$, then
$f(m)=m\kappa(m)$ is nonnegative and additive. Nonnegativity makes $f$
monotone: $f(y)-f(x)=f(y-x)\ge0$ for $y>x$. Rational approximation therefore
gives $f(m)=Km$, so $\kappa(m)=K\ge0$. No extra continuity assumption is
needed on this domain. The physical content is mass-only dependence and
closure under the stated independent composition, not Cauchy's equation alone.

Three tests strengthen the proposed note:

- At a common fixed environment $\theta$, the same argument allows
  $\kappa(m,\theta)=K(\theta)$. Mass independence and preparation independence
  are separate obligations. A02 supplies a state-dependent action coefficient;
  calling it a reservoir variable does not classify every admissible coefficient.
- The transformed Gaussian cross covariance is
  $\operatorname{Cov}(\Delta R,\Delta r)=\Delta(\kappa_1-\kappa_2)/M$.
  Independence of centre and relative coordinates is an alternative premise
  forcing equality of the two coefficients in this Gaussian setting.
- Two independent $\pm c$ particles have centre velocities including
  $c(m_1-m_2)/M$ and its negative. Their centre process is generally a
  multi-state process, not another $\pm c$ telegraph process. Closure of the
  coefficient can hold while closure of the full trajectory law fails.

Deliver A08 as a short note with five algebra checks, one Luna-low librarian
audit, and explicit correlated/preparation countertests. Keep $K=0$ in its
domain. Also test whether a universal $K$ can be derived for an interacting
body rather than postulated by extending the free-particle class.

## 2. Crossover: adopt the necessary bound and distinguish observables

C018/C031 immediately imply that realizing a positive coefficient $K$ at
window $\Delta$ requires

$$\Delta\ge\Delta_*:=\frac{K}{mu^2},\qquad
u\Delta_* = \frac{K}{mu}.$$

This is a necessary support/variance constraint, not a sufficiency statement.
In particular an exact nondegenerate Gaussian law still has unbounded support
at every finite window. A finite-speed process can approximate its large-scale
statistics. With the additional identifications $K=\hbar$ and $u=c$, the
two expressions are the reduced Compton time and reduced Compton wavelength.
The inequality supplies no pair-creation process, particle-number observable
or interacting field dynamics. Those require a separate physical construction.

For A01, $K=H_*=mu^2/\lambda$ gives $\Delta_*=1/\lambda$, whereas the
velocity correlation time is $1/(2\lambda)$. Its already established
stationary-increment interpolation is

$$\mathsf h(\Delta)=H_*\left[1-
             \frac{1-e^{-2\lambda\Delta}}{2\lambda\Delta}\right].$$

The conditional midpoint coefficient in A06 is a different observable with
fixed initial and final velocities. At small $\lambda T$, its one-switch
component has a deterministic midpoint; A05's random elastic pair instead
mixes the initial sign. Computing a function $g(\lambda T)$, its monotonicity
and long-window limit is a separate bridge-moment task, not an application of
the stationary formula. A09 records these tests without predicting their answer.

## 3. Checkerboard: prioritize the correspondence, track its added premise

The remembered 1984 journal identifiers are correct. Gaveau, Jacobson, Kac and
Schulman's [PRL abstract](https://doi.org/10.1103/PhysRevLett.53.419)
explicitly distinguishes real Poisson telegraph dynamics from analytic
continuation to Dirac dynamics. Jacobson–Schulman,
[J. Phys. A 17, 375–383](https://doi.org/10.1088/0305-4470/17/2/023), is the
relativistic/nonrelativistic path-integral lead. Exact book-page conventions
and the journal derivations await direct passage reading; B15 records coverage.

For any supplied action $K>0$, $u=c$ and $\lambda=mc^2/K$ give
$D=c^2/(2\lambda)=K/(2m)$. This matches Nelson's diffusion normalization
when $K=\hbar$. The free telegraph equation gives a transparent algebra test:

$$p_{tt}+2\lambda p_t=c^2p_{xx},\qquad p=e^{-\lambda t}\phi
\quad\Longrightarrow\quad
\phi_{tt}-c^2\phi_{xx}-\lambda^2\phi=0.$$

Choosing $\lambda=i\omega$, $\omega=mc^2/K$, yields
$\phi_{tt}-c^2\phi_{xx}+\omega^2\phi=0$. This is the Klein–Gordon form.
The continued corner weight is complex; a Dirac construction retains the
two velocity components and specifies its phase, normalization and initial data.
The continued object supplies amplitudes rather than a positive Poisson law.

Real Kac scaling at fixed $c^2/\lambda=K/m$ gives diffusion. Quantum
nonrelativistic scaling gives Schrödinger propagation after the corresponding
complex continuation and rest-energy phase choice. They share a parameter
scaling but are different limits of different propagators.

Fixing microscopic speed to $c$ excludes speed-cooling in this new class.
Fixing one species' actual finite positive rate and imposing universal $K$
then fixes rates for other masses. Merely requiring every rate to be finite
allows a sequence of models with $K\downarrow0$ and finite
$\lambda_m=mc^2/K$ in every model. It establishes positivity within a chosen
model, not a uniform positive floor across that family. Moreover a speed ceiling
$|V|\le c$ and the two-valued rule $V=\pm c$ are different premises.

## 4. Spectral toy: adopt in G01 with a gap-observability test

C019 already gives

$$H_*\gamma_{\min}\le2m\sigma_v^2\le H_*\gamma_{\max}.$$

For the two-state generator, $\gamma=2\lambda$ and
$H_*\gamma=2mu^2$. The operator $-Q$ is self-adjoint on the finite space
$L^2(\pi)$, with inverse-time spectral gap $2\lambda$. Multiplication by a
chosen action unit $K$ produces an energy operator with gap $2K\lambda$.
If $u=c$ and $K=\hbar$, the parameter match gives $2mc^2$, the separation
between the free Dirac branches at zero momentum. A vacuum-to-particle gap
is a different quantity. The two-state relaxation generator is also different
from the spatial Dirac Hamiltonian and from a Yang–Mills transfer Hamiltonian.

The product inequality by itself yields
$\gamma_{\min}\le2m\sigma_v^2/H_*$, an upper bound. To seek a lower gap
bound, test observability of slow modes. For example, append an independent
two-state label with reversal rate $\epsilon$ and let velocity depend only on
the original telegraph sign. The joint finite reversible generator has gap
$\min(2\lambda,2\epsilon)$, while $H_*=mu^2/\lambda$ is unchanged.
The hidden mode closes the full gap without changing this susceptibility.
G01 should derive and audit this test before proposing a transferable estimate.

Use the product relation to extend M03's comparison table after its existing
proof checks and PDF acceptance gates. Appending a correct closing identity
does not complete the rest of that draft's review. WP6 should ask which
observable family controls the slow sector, with estimates uniform in volume
and cutoff; one integrated correlation is insufficient for that task.

## 5. Cut structure: close the chosen constructions, retain the selection test

A03/A05/A06 have completed the selected consistency constructions. Evaluating
cuts on any one path probability space already guarantees restriction
consistency; Markov structure supplies a convenient transition-kernel
description, not a necessary condition. A06's singular conditioning convention
is explicit in its completed note.

C028's estimator is model-specific. For the bounded-speed return paths,
$S_\pi\le mu^2T/2$ implies $2S_\pi/(N-1)\to0$ at fixed $T$ as the node
count grows. Replacing the central target by that estimator would therefore
select the Gaussian class and discard the finite-speed model. Move the main
priority to composition/selection while retaining three separately named
objects: a Gaussian cut estimator, a finite-window variance coefficient and a
long-window Green–Kubo plateau.

## 6. Cheap wins: select by the remaining proof obligation

- Make the crossover inequality F01's first small arithmetic certificate after
  A09's mathematical acceptance; retain the earlier quadratic no-gap family as
  its second exercise. Tool installation remains a separate feasibility decision.
- Mark B11 ready to resume. B12–B15 already demonstrate successful worker
  execution after the old authentication failure, so B11 is valuable for its
  geometry rather than as a pipeline test. A08 has higher present leverage.
- Give G01 the two-state product identity and slow-mode countertest. Finish
  M03 through its established review gates instead of changing its status now.
- Keep Plutarch–C032 as a modern analogy in H05's questions, alongside the
  separate historical reception search. C032 proves deterministic drift from
  bounded speed **and independent stationary increments**; adjacent positions
  can differ by $b\Delta$. A hard speed ceiling alone permits curved motion.
  Historical ancestry needs a documented transmission/use chain.

## Revised order and acceptance

1. A08 composition: mass-only coefficient, preparation class, correlations and
   closure; short derivation, five checks, sequential Luna-low prior-art audit.
2. A09 crossover and checkerboard: direct source passages, real/complex
   recurrences, conditioning-specific moments and modelwise positivity.
3. G01 susceptibility/gap product with slow-mode observability, then M03 review.

A07 remains the bounded-force diagnostic; B11 and H05 retain their saved source
tasks. Every new accepted mathematical result receives a separate prior-art
audit. The current checkpoint changes research priorities, not the accepted
theorem set.
