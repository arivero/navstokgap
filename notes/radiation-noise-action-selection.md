# Radiation balance selects a spectral shape, but leaves its action amplitude free

A charged harmonic probe driven by a common cubic electric-noise spectrum has
mean energy approaching K times its frequency in a narrow-resonance limit.
Radiation damping cancels the probe's charge and mass in that limit. The
coefficient K remains the chosen field amplitude: damping also admits the
quiet field, and the effective model has no finite-energy cutoff-free limit
at fixed damping. This is Q02's conditional mechanism test, not a derivation
of quantum structure. Written review is recorded separately in
[the Q02 review](../reviews/radiation-noise-Q02.md).

## 1. Physical premises and observable

Consider a one-dimensional dipole coordinate x with mass m>0, nonzero charge q,
and natural angular frequency w>0, in SI units. Use the stable effective law

$$m\ddot x+m\gamma\dot x+mw^2x=qE(t),\qquad
\gamma=\frac{q^2w^2}{6\pi\epsilon_0mc^3}>0.$$

The damping rate follows cycle-averaged dipole radiation: the Larmor power
q² times mean acceleration squared divided by 6π epsilon_0 c³ equals
m gamma times mean velocity squared on a harmonic orbit. It is an on-resonance,
weak-damping approximation, with gamma/w much smaller than one; it is not a
point-charge radiation-reaction equation valid at arbitrarily high frequency.
For each finite cutoff below, the stable equation defines the tested model.

Supply a centered stationary Gaussian field, independent of probe initial data,
with two-sided angular-frequency spectral density defined by

$$\langle E(t)E(0)\rangle=\int_{\mathbb R}\frac{d\omega}{2\pi}
 S_E(\omega)e^{-i\omega t},\qquad
 S_E(\omega)=\frac{K}{3\pi\epsilon_0c^3}|\omega|^3
 \mathbf1_{|\omega|\le\Lambda},\quad \Lambda>w,\quad K\ge0.$$

K has action units. The cubic shape is a candidate radiation preparation;
stationarity and the oscillator equation do not select it. The common field
uses the same K and cutoff for all probes. A finite laboratory cutoff specifies
a frame; no exact Lorentz invariance is asserted for this regulated model.
The external harmonic potential, Gaussian reservoir and dipole approximation
are supplied physical premises. Gaussian tails do not impose a hard speed bound.

Measure the ensemble mechanical action

$$J(t)=\frac{m}{2w}\langle\dot x(t)^2+w^2x(t)^2\rangle.$$

This is mean oscillator energy divided by angular frequency, not the earlier
long-window displacement observable. For a deterministic undamped orbit it is
(1/2π) times the closed phase-space integral of p dx. No phase or commutator
postulate enters its definition.

## 2. Exact stationary response of the effective model

At fixed positive gamma and finite Lambda, homogeneous solutions decay.
The stationary forced solution has finite position and velocity variance;
finite-second-moment initial transients vanish. Thus J(t) tends to J_* as
physical time tends to infinity. In the underdamped regime the homogeneous
amplitude decays as exp(-gamma t/2); the reservoir determines the limiting
covariance, rather than that covariance being fixed by the damping alone.
Fourier response gives the exact model identity

$$J_* =\frac{q^2}{2mw}\int_{-\Lambda}^{\Lambda}\frac{d\omega}{2\pi}
 \frac{(\omega^2+w^2)S_E(\omega)}
 {(w^2-\omega^2)^2+\gamma^2\omega^2}.
\tag{1}$$

For the supplied spectrum this becomes

$$\frac{J_*}{K}=\frac{\gamma}{\pi w^3}
 \int_0^\Lambda
 \frac{\omega^3(\omega^2+w^2)}
 {(w^2-\omega^2)^2+\gamma^2\omega^2}\,d\omega
\quad(K>0).\tag{2}$$

The prefactor uses q²/(3π epsilon_0 c³)=2m gamma/w². All quantities in
(2) are dimensionless after integration: gamma/w³ has units of time squared.

## 3. The cancellation and its order of limits

Take gamma/w to zero with w, K and finite Lambda>w fixed, after reaching the
stationary state. This can be implemented by reducing q²/m while retaining
the same imposed field. In a neighborhood of omega=w, put u=omega-w.
The numerator in (2) approaches 2w⁵ and its denominator is
w²(4u²+gamma²) to leading order. Since

$$\int_{-\infty}^{\infty}\frac{du}{4u^2+\gamma^2}
 =\frac{\pi}{2\gamma},$$

the resonant contribution to the integral is πw³/gamma. Outside any fixed
neighborhood of w the integral stays bounded as gamma tends to zero; its
prefactor tends to zero. Taking that neighborhood smaller after the damping
limit proves

$$\lim_{\gamma\downarrow0}J_*=K.\tag{3}$$

More generally, for a fixed even field spectrum continuous at w and integrable
on a finite cutoff, the same argument gives

$$J_*\longrightarrow\frac{3\pi\epsilon_0c^3S_E(w)}{w^3}.$$

Consequently requiring the same limiting J_* over a band of oscillator
frequencies requires S_E(w) proportional to w³ on that band. This explains
what the radiation clock contributes beyond mass-only composition: it selects
a spectral *shape conditional on equal actions*, and cancels q and m. It does
not dynamically enforce equal actions or set the common amplitude. The
convergence is pointwise in probe parameters, with resonance strictly inside
the cutoff; no uniformity over all frequencies or arbitrarily small masses is
claimed. Dipole and nonrelativistic validity also require appropriate probe
amplitudes, for example Kw/(mc²) much smaller than one in the resonance limit.

Taking q to zero at finite observation time instead removes forcing and
damping, retaining the initial oscillator energy. Relaxation time diverges
as gamma tends to zero. The stationary-first limit is essential.

## 4. Quiet preparation and ultraviolet countertests

For any fixed cutoff and probe parameters, replacing E by aE replaces K and
J_* by a²K and a²J_*. The deterministic damping and natural frequency do not
change. At K=0 the damped oscillator approaches rest; arbitrarily small
positive K gives arbitrarily small positive stationary action. A nonzero
reservoir spectrum supplies positivity, but no lower bound independent of
preparation. Even a symmetry condition on field covariances that preserves
multiplication by a positive constant cannot fix that constant.

Cutoff removal gives a separate obstruction in this effective model. At large
omega the integrand in (2) is asymptotic to omega. At fixed gamma>0,

$$\frac{J_*}{K}\sim\frac{\gamma\Lambda^2}{2\pi w^3}
 \quad(\Lambda\longrightarrow\infty).\tag{4}$$

Thus stationary energy diverges for K>0. Position variance separately has a
logarithmic ultraviolet divergence; velocity variance supplies the quadratic
energy divergence. Taking weak damping first at every finite cutoff gives
(3), whereas removing the cutoff first diverges. A joint limit needs control
of the ultraviolet tail as well as the narrow resonance; (3) supplies none.
Equation (4) diagnoses failure of extending the viscous approximation and the
cubic preparation together. It is not a no-go theorem for an extended-charge,
causal field-plus-particle model with frequency-dependent response.

## 5. Strategic decision

Radiative response is a useful physical explanation for a conditional
mass/charge cancellation and an energy-frequency relation. This linear,
externally maintained reservoir fails to select a positive universal action:
its amplitude is freely rescalable, its quiet solution is admitted, and its
cutoff-free extension fails. Gaussian classical states persist; the calculation
supplies no quantum measurement or phase structure and no physical energy gap.

Park linear radiation-balance variants. A return requires an explicit dynamical
reservoir/backreaction law that breaks amplitude rescaling and excludes the
quiet state, with a controlled ultraviolet response. The next mechanism test
should ask whether autonomous nonlinear energy transfer can supply that missing
selection, using its zero-field solution and stability as the first countertest.
No prescribed nonzero noise amplitude may stand in for that test.

Source recovery used [B23](../docs/batches/B23/harmonic-receiver-source-companion.md),
Zwanzig's equations (16)–(17), (23), (25)–(30): forcing, friction and reservoir
preparation must be accounted for separately. These supply the reduction
perspective, not the radiation spectrum. The [composition note](composition-universality.md)
§4 supplies the preparation-label comparison. Radiation-specific source coverage
and written proof status are in the review; this note is a completed exploratory
test and has no new accepted claim ID.
