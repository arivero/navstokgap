# What a necessity argument for $h>0$ must supply: a unit and an indeterminacy

**Result, 2026-09-27.** A positive universal floor on recorded comparisons
in Newton's Galileo comparison needs two separable ingredients. **(U)** a
universal action unit, and **(I)** an indeterminacy of the record's
back-action, since the floors of the [Planck paper](planck-gap-paper.md)
(Theorems 5--6) bound *spreads* of disturbances, and a definite, later
recoverable kick has zero spread. The two have opposite status.

- **(U) follows from classical radiation thermodynamics** (Theorem U).
  Kirchhoff's universality, Wien's scaling law, finite equilibrium energy
  density and low-frequency equipartition force the equilibrium spectrum
  to contain a universal constant $\beta$ with units of kelvin-seconds.
  With Boltzmann's constant it gives an action $h=k_B\beta$, independent of
  every material constant. Its value is already in Wien's displacement
  constant $b$: $h=y_*k_Bb/c$, with $y_*$ a pure number fixed by the
  spectral shape. No premise about the body, its mass or a commutator
  enters.
- **(I) is impossible classically** (Theorem I). Any model with Liouville
  dynamics of body and pointers, product preparations obeying a prior
  density ceiling, and Bayesian conditioning on pointer readings admits
  records whose body posterior has arbitrarily small area. A premise that
  yields (I) must deny one of these three. Quantum kinematics denies the
  third; a universal unrecordable background (stochastic electrodynamics)
  denies the second; an epistemic restriction in Spekkens's sense imposes
  the ceiling directly. Newton's printed optics denies none, which is
  paper §8's $\neg$M3 as an instance.

So the necessity question becomes sharper than before. The existence of
a universal action unit is forced by nineteenth-century physics that
never mentions the body. What remains open is which of three explicit
classical structures a physically justified premise must give up for that
unit to act as a floor on records.

The candidate list and both theorems were proposed by a Fable reviewer at
the user's request (report in the session scratchpad, 2026-09-27), after
three external models (DeepSeek, Mimosa, Muse Spark 1.1) converged on the
Stoney unit $k_e/c$, which the
[dimensional note](action-unit-dimensional-selection.md) already holds.
The ingredients are classical and the theorems elementary; no novelty is
claimed for either. Their use here is to replace the obstruction map of
[action-scale-obstructions](action-scale-obstructions.md) by one statement
of what is missing.

## 1. Two ingredients

The floor of the Planck paper, Theorem 6, is

$$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)
\ge\hbar\arcsin(1-2\epsilon),$$

with $\Delta$ a spread of an undetermined disturbance. Its proof uses
Mandelstam--Tamm in the Bures angle and the Weyl relations, that is,
$\hbar>0$ in two roles.

- **(U), the unit.** By Theorem A of the
  [dimensional note](action-unit-dimensional-selection.md), a floor shared
  by all masses and preparations is a pure number times a product of the
  model's fixed constants with action units. Classical mechanics, gravity
  and electrodynamics hold exactly one mass-independent such product,
  $k_e/c=e^2/(4\pi\epsilon_0c)=\alpha\hbar$.
- **(I), the indeterminacy.** The floor bounds spreads. A record whose
  kick is definite and later recoverable contributes nothing, whatever the
  size of the kick. For example, a charged probe passing a charged body at
  speed $u<c$ and impact parameter $b$ delivers the transverse impulse
  $2n_1n_2k_e/(bu)$, so charge atomicity gives
  $|\Delta p|\,b\ge2k_e/c=2\alpha\hbar$: a universal, mass-independent
  floor on the *magnitude* of a record's kick. The kick is determined by
  the reading, so its spread is zero. The right unit gives the wrong kind
  of quantity.

## 2. Theorem U: the unit from radiation thermodynamics

Let $u(\nu,T)\,d\nu$ be the equilibrium energy density of electromagnetic
radiation between frequencies $\nu$ and $\nu+d\nu$ at absolute temperature
$T$. Assume:

- **(K)** $u$ is the same for every material enclosure (Kirchhoff 1859,
  from the second law: two cavities at one temperature with different
  spectra would drive an engine through a colour filter);
- **(W)** $u(\nu,T)=\nu^3f(\nu/T)$ (Wien 1893, from adiabatic compression
  of a reflecting cavity and the second law
  ([Wien 1893, reprint](https://doi.org/10.1007/978-3-663-13885-3_12),
  metadata));
- **(S)** $\int_0^\infty u\,d\nu<\infty$ for every $T>0$ (Stefan's measured
  law; Boltzmann's $T^4$ theorem from Maxwell's radiation pressure);
- **(R)** $u(\nu,T)\to(8\pi\nu^2/c^3)\,k_BT$ as $\nu/T\to0$ (equipartition of
  the low-frequency modes, the regime Rayleigh and Jeans describe).

**Theorem U.** Under (K), (W), (S), (R) there is a constant $\beta>0$ with
units of kelvin-seconds, independent of every material constant, such
that $f(\nu/T)=(8\pi k_B/c^3)(T/\nu)\,\varphi(\beta\nu/T)$ with $\varphi$ a
function of one dimensionless variable, $\varphi(0)=1$. Hence
$h:=k_B\beta$ is a universal action, and

$$\sigma'=\frac{8\pi k_B^4}{h^3c^3}\int_0^\infty y^2\varphi(y)\,dy,
\qquad h=\frac{y_*k_Bb}{c},$$

where $\sigma'$ is the Stefan constant of the energy density, $b$ is
Wien's displacement constant ($\lambda_{\max}T=b$ for the peak of the
spectrum per unit wavelength), and $y_*$ is the pure number at which that
peak sits.

*Proof.* By (W), $u$ depends on $\nu$ and $T$ through $\nu^3$ and the
ratio $\nu/T$, whose units are $1/({\rm s\cdot K})$. By (K) the only
constants $u$ may contain are universal ones, and (R) displays two, $c$
and $k_B$. From $c$, $k_B$ and $\nu/T$ no dimensionless combination
exists, because $c$ contains a length and $k_B$ an energy, and neither
appears in $\nu/T$. If $u$ contained no further constant, $f$ would be a
pure power, and (R) would fix it to $f=(8\pi k_B/c^3)(T/\nu)$, whose
frequency integral diverges, contradicting (S). So $u$ contains a further
universal constant. By (W) it can enter only through a dimensionless
multiple of $\nu/T$, so it has units of kelvin-seconds; call it $\beta$.
Then $f$ has the displayed form, (R) gives $\varphi(0)=1$, and
substituting $y=\beta\nu/T$ in the integral gives $\sigma'$. The peak
of $u_\lambda=u\,c/\lambda^2$ lies at a fixed value $y_*$ of
$\beta c/(\lambda T)$, so $\lambda_{\max}T=\beta c/y_*$, which is the
expression for $h=k_B\beta$. $\square$

With the spectral shape of Planck 1900
([Ann. Phys. 306, 69](https://doi.org/10.1002/andp.19003060105),
metadata), $\varphi(y)=y/(e^y-1)$, the integral is $\pi^4/15$, $y_*\approx4.965$,
and $h$ is Planck's constant. The theorem needs no shape: any finite
spectrum obeying (K), (W), (R) contains a universal action, fixed up to a
pure number by the measured $b$, $c$ and $k_B$. Planck formed his natural
units from exactly this constant in 1899--1900, before the quantum
hypothesis; the theorem states why a constant had to be there.

Two remarks keep the statement honest. First, $k_B$ converts
kelvins to energy, and its value needs atomism (the gas constant divided by
Avogadro's number); the universal constant of (K)--(W) alone is $\beta$.
Second, with $h$ and $k_e/c$ both available, Theorem A of the dimensional
note no longer fixes a unique unit: any universal floor is
$h\,G(\alpha)$ with $\alpha=k_e/(hc/2\pi)$ dimensionless. Uniqueness of the
unit requires that the floor not depend on the charge, which holds for
records made with neutral probes.

**Bridge to the Opticks.** Newton's *Opticks* holds, per colour, an
interval of fits $\Lambda$ and a corpuscle whose $\Lambda p$ is invariant
under refraction (paper §§7--8), but no universality across colours: on
his ordering of corpuscle sizes, $\Lambda p$ decreases toward the violet
with no least colour. Theorem U supplies exactly the missing cross-colour
constant. Reading $h$ as a per-corpuscle impulse, $p=h/\lambda$, needs
more: Einstein's fluctuation argument applied to an exponential spectral
tail, which is the quantization of the field. So the unit enters honestly
through (K)--(R), and quanta enter through the tail.

## 3. Theorem I: no classical ceiling on posteriors

**Theorem I.** Consider a classical model with (i) Liouville (Hamiltonian)
dynamics of the body and its pointers, (ii) product preparations, each
factor with a prior phase-space density at most $1/X$, and (iii) records
formed by Bayesian conditioning on a pointer coordinate read to finite
precision. Then for every $X>0$ and $\eta>0$ there is a protocol whose
body posterior satisfies $\Delta q\,\Delta p<\eta$, with $\Delta$ the width
of the support.

*Proof.* Let the body prior be uniform on $[0,a]\times[0,X/a]$ and the
first pointer $(y,p_y)$ uniform on $[0,\epsilon]\times[0,X/\epsilon]$;
both have density $1/X$. The impulsive coupling with Hamiltonian
$g\,q\,p_y$ acting for unit time maps $y\mapsto y+gq$ and
$p\mapsto p-gp_y$, leaving $q$ and $p_y$ unchanged, and preserves the joint
density by Liouville. Reading $y$ to precision $\epsilon'$ confines $q$ to
width $(\epsilon+\epsilon')/g$. A second pointer $(z,p_z)$, uniform on
$[0,\epsilon_2]\times[0,X/\epsilon_2]$ and coupled by $g_2\,p_y\,p_z$, maps
$z\mapsto z+g_2p_y$ and kicks only $y$, which is already read. Reading $z$
to precision $\epsilon_2'$ confines $p_y$ to width
$(\epsilon_2+\epsilon_2')/g_2$. The body's momentum is $p-gp_y$, so its
posterior width is at most $X/a+g(\epsilon_2+\epsilon_2')/g_2$, and

$$\Delta q\,\Delta p\le\frac{X(\epsilon+\epsilon')}{ag}
+\frac{(\epsilon+\epsilon')(\epsilon_2+\epsilon_2')}{g_2},$$

which is below $\eta$ for $g_2$ large and $a$ large, or $\epsilon$,
$\epsilon'$ small. The prior ceiling only widens the unread conjugates
$p_y$ and $p_z$. $\square$

The second pointer reads the first pointer's kick; this is paper §8's
countermodel (two position records recover the momentum) in mechanical
form, and each classical entry of the obstruction map is a corner of it.
The recoverable-delayed-record results C068--C069 are the corner
$a\to\infty$, $\epsilon'\to0$.

**What (I) must deny.** A premise that yields a universal posterior
ceiling, and with it paper Theorem 6 with the ceiling in place of
$\hbar$, must deny (i), (ii) or (iii).

- *Quantum kinematics* denies (iii): there is no joint phase-space density
  on which to condition, and every read is also a kick.
- *A universal background that no record can fully capture* denies (ii):
  every preparation is correlated with it. Stochastic electrodynamics is
  of this kind; Lorentz invariance fixes the spectrum of a random
  classical background as $\propto\nu^3$ up to one constant with action
  units ([Marshall 1963](https://doi.org/10.1098/rspa.1963.0220);
  [Boyer 1975](https://doi.org/10.1103/PhysRevD.11.790); metadata). The
  ceiling then needs the extra clause that records cannot read the
  background itself, since otherwise Theorem I applies to the enlarged
  system.
- *An epistemic restriction* imposes the ceiling on every state of
  knowledge. Bartlett, Rudolph and Spekkens show that Liouville mechanics
  with such a restriction reproduces Gaussian quantum mechanics
  ([PRA 86, 012103, 2012](https://doi.org/10.1103/PhysRevA.86.012103),
  metadata; [Spekkens 2007](https://doi.org/10.1103/PhysRevA.75.032110)
  for the discrete toy theory). This is the posterior ceiling as a
  principle, with its value free; Theorem U then fixes the value up to a
  number.
- *Newton's printed optics* denies none: its fits are determinate and its
  records conditionable, which is why paper §8 finds that what Newton
  printed entails $\neg$M3.

## 4. Consequence for STATE

STATE item 2 (Newton necessity) gains a sharp statement. The unit is
settled classically by Theorem U. The open task is a physically justified
premise that denies one of (i)--(iii) of Theorem I, of which the three
known routes are quantum kinematics, an unrecordable universal background
and an epistemic restriction. The historical test worth doing next is
the reviewer's second candidate: whether Newton's inflexion experiments
(*Opticks* Book III, Obs. 1--11) give a bending law $\theta b\approx C\Lambda$
per colour. If they do, Newton's own optics denies (iii) for corpuscle
records, per colour, and paper §8 must be reworded to say that $\neg$M3
follows only for inflexion-free records.
