# B24 chain-limit source companion

## Result and coverage

The prior-art audit supports the oscillator-chain spectral ingredients, but not
the normalized observable or any universality claim. The only source read was
G. W. Ford, M. Kac and P. Mazur, “Statistical Mechanics of Assemblies of
Coupled Oscillators,” *J. Math. Phys.* **6** (1965), 504–515,
doi:10.1063/1.1704304, cached as `.build/b23/ford-kac-mazur.pdf` (SHA-256
`94af20edeaa11240c70666be1f063d7d65c1f4d6739aeb4e268dacd41b0d27ef`). Printed
pp. 506–508 were reported read (three source pages; correct PDF pages 4–6).
No discovery search was needed. The cached copy came from the USP institutional
course mirror recorded in B23, rather than directly from AIP. The file
`.build/b24/ford-pages.txt` contains full-document extraction, distinct from
the worker's reported reading coverage. No Rubin or DLMF page was read.
Coordinator visually checked printed p. 506 (PDF p. 4), corrected the page
range, source route and dispersion notation below. A metadata recheck against
Michigan returned HTTP 403; B23's verified publication metadata is retained.

## Source-established ingredients

Ford–Kac–Mazur p. 506, equations (12), (14), (17)–(18), gives a finite cyclic
interaction matrix, Fourier eigenvectors, eigenvalues indexed by wave number,
and the nearest-neighbour dispersion
`w_s^2 = omega_bar^2 sin^2(pi s/(2N+1))` (their chain has `2N+1` sites and unit
masses). Their p. 506 equations (19)–(24) then replace finite sums by an
integral in an infinite-chain limit, under a slowly-varying spectral function.
This establishes the general sum-to-integral route and tagged matrix-element
weighting, not the odd-ring fixed-energy preparation used in the draft.

On p. 507, equations (25)–(28), they introduce a high-frequency cutoff and
show a further cutoff limit can produce an exponential tagged momentum
correlation and Markov process. This is a bath/Markov construction, not a claim
about the finite-chain displacement-action observable. On p. 508, equations
(35)–(43), they note translation invariance forces a zero eigenvalue, explain
why the canonical distribution is then improper, and regularize it; they derive
a generalized Langevin equation and a continuum white-noise covariance. These
passages reinforce that centre/zero-mode conventions and order of limits are
substantive assumptions.

## Claim audit of the A11 draft

* The odd-ring frequencies `omega_j = Omega sin(pi j/N)`, `Omega=2 sqrt(k/m)`,
  equal paired site weights, and
  `C_N(t)=Theta/(mN) sum_{j=1}^{N-1} cos(omega_j t)` are **derived**, not
  source-established. They follow directly by diagonalising the stated
  nearest-neighbour Hamiltonian, fixing the centre mode, and assigning each
  real mode energy `Theta`; Ford–Kac–Mazur supplies only the analogous Fourier
  diagonalisation template (p. 506).
* The formula
  `h_N(Delta)=2 Theta/(N Delta) sum (1-cos(omega_j Delta))/omega_j^2` is a
  **derived consequence** of the stated covariance and the definition in §2.
  It is not a literature formula identified in the read pages.
* The tagged continuum density
  `rho(omega)=2 Theta/(pi m sqrt(Omega^2-omega^2))` and the fixed-Delta
  Riemann limit are **derived** from the dispersion and change of variables.
  The density is integrable at `Omega` and finite at zero, as stated.
* The long-window limit `2 Theta/Omega` is **derived**. Splitting at `a>0`,
  scaling `y=omega Delta`, and dominated convergence are valid; the tail is
  `O(Delta^-1)`. The use of
  `integral_0^infty (1-cos y)/y^2 dy = pi/2` is a standard calculus identity,
  not supported by a page read here.
* The reversed limits are **derived**: every fixed finite ring has a finite
  cosine sum, so `h_N(Delta)->0`; taking `N` first gives the positive continuum
  plateau. This is an order-of-limits result for the displayed observable and
  preparation, not Ford–Kac–Mazur’s Markov limit.
* The joint bound is **derived and checks out**. With
  `f(z)=2(1-cos z)/z^2=2 integral_0^1 (1-r) cos(zr) dr`, `|f'|<=1/3`.
  The integrand has Lipschitz constant at most
  `pi Theta Omega Delta^2/3`; the left-sum error and omitted zero term give
  `pi Theta Omega Delta^2/(6N)+Theta Delta/N`. Thus
  `(Omega Delta_N)^2/N -> 0` and `Omega Delta_N -> infinity` imply the
  positive plateau.
* The exact site-zero support maximum
  `(N-1) sqrt(Theta/(mN))` is **derived** by aligning the `(N-1)/2` cosine
  mode phases; every neighbourhood has positive phase measure. Consequently
  a common hard ceiling `c` necessarily gives
  `Theta_N <= m c^2 N/(N-1)^2 = O(N^-1)`. This is necessary only, based on one
  site; it is not a global sufficiency statement.
* The bound
  `h_N <= 4 Theta_N (N^2-1)/(3 N Omega^2 Delta)` follows from
  `1-cos z <= 2` and the exact cosecant-square sum. Together with
  `h_N <= Theta_N Delta`, minimising the two bounds yields
  `sup_Delta h_N <= (2 Theta_N/Omega) sqrt((N^2-1)/(3N))`. The identity and
  the minimax step are **derived**. Under the necessary ceiling scaling this
  tends to zero, so the positive plateau and a common strict speed ceiling are
  different preparation classes.

## Limits and next mechanism

The continuum calculation does not assert an invariant absolute-position law:
the centre mode is fixed before the tagged covariance is considered. Keep
receiver size, observation window, centre-mode removal and mesh refinement as
separate limits. A useful next mechanism is a bounded-velocity nonlinear
reservoir (for example rotors or angle variables with a hard speed constraint)
whose low-frequency tagged spectral weight can be tuned independently of total
energy; test whether its speed ceiling still forces the zero plateau.
