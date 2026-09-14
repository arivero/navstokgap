# Mechanical interference measures phase without fixing an action unit

An ideal classical string network sends a finite pulse down two paths and
transfers its entire energy into two mechanical absorbers. Their work records
contain an interference cross term. Attenuating the incident displacement
leaves the normalized fringe unchanged while every energy and canonical action
shrinks quadratically. This exploratory Q08 construction tests the physical
phase premise left by Q07; it is not promoted to the claim ledger.

## 1. Wave, junction and receiver premises

Take identical linear strings with mass per length $\mu>0$, tension $T>0$,
transverse displacement $u(x,t)$ and small slopes. Position and displacement
have length units. Define speed $c=\sqrt{T/\mu}$ and mechanical impedance
$Z=\sqrt{\mu T}=\mu c$, with units mass/time. The stipulated continuum model is

$$
L=\int\frac12(\mu u_t^2-Tu_x^2)\,dx,\qquad
\mu u_{tt}=Tu_{xx},\qquad
 e=\frac12(\mu u_t^2+Tu_x^2),\quad j=-Tu_tu_x.
$$

Multiplying the equation by $u_t$ gives $\partial_t e+\partial_x j=0$.
A right-moving displacement $f(t-x/c)$ has $e=\mu(f')^2$ and
$j=Z(f')^2$. Prepare a nonzero smooth compactly supported pulse $f$;
its incident energy is $E=Z\int_{\mathbb R}(f')^2dt>0$. This preparation
supplies energy; no source operates during its subsequent passage.

A lossless four-port junction mixes two input strings into two output strings
with the real matrix

$$
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
S=\begin{pmatrix}0&H\\H&0\end{pmatrix}.
$$

Here $S$ maps incoming to outgoing displacement profiles on four equal-impedance
ports. It is symmetric, $S^2=I$, and orthogonal. This is an ideal mechanical
constraint, not an assertion that an ordinary tied-string knot has this rule.
For an explicit boundary realization orient all four port coordinates outward,
write $u=a(t+x/c)+b(t-x/c)$ and put $P_\pm=(I\pm S)/2$.
Impose $P_-u(0,t)=0$ and $P_+u_x(0,t)=0$. The first fixes the constrained
junction displacement; the second supplies free force balance in its orthogonal
subspace. For pulses initially at rest these equations give $b=Sa$.
Indeed they give $P_-b=-P_-a$ and $P_+b'=P_+a'$; the integration constant
vanishes before arrival. The displacement velocity lies in the plus subspace
and the boundary force in the minus subspace, so their scalar product and
boundary work vanish. Equivalently $\sum_j(a'_j)^2=\sum_j(b'_j)^2$.
An ideal massless linkage enforcing these fixed linear constraints is a model
premise. Finite junction inertia and bandwidth are outside this construction.

At each final output install a viscous receiver with force coefficient $Z$.
At a right endpoint the balance $Tu_x=-Z u_t$ admits a pure outgoing wave
without reflection. Work delivered to the receiver is

$$
Q(t)=\int_{-\infty}^t Z u_t(s)^2\,ds,\qquad \dot Q\ge0.
$$

The dashpot represents a sink with an internal energy record $Q$; field energy
plus these records is conserved after preparation. It is not a finite closed
Hamiltonian model of the bath. A semi-infinite matched string supplies an
alternative conservative energy sink, with $Q$ the energy transported into it.
Neither realization imposes a minimum resolvable work or a discrete event rule.

## 2. Exact two-path energy readout

Use two such junctions. The first splits the input $(f,0)$; the two arms have
positive travel times $\tau_1,\tau_2$; the second mixes their arriving waves.
The unused source port has no incoming wave and is matched. All connections
are reflectionless in the stipulated model. Output displacements are

$$
b_\pm(t)=\frac12[f(t-\tau_1)\pm f(t-\tau_2)].
$$

Integrating the receiver work over the complete pulse gives

$$
Q_\pm=\frac E2\pm\frac Z2
 \int f'(t-\tau_1)f'(t-\tau_2)\,dt,
\qquad Q_++Q_-=E. \tag{1}
$$

For $\delta=\tau_2-\tau_1$, define the normalized derivative autocorrelation

$$
C(\delta)=\frac{\int f'(s)f'(s-\delta)ds}{\int(f')^2ds},
\qquad \frac{Q_\pm}{E}=\frac{1\pm C(\delta)}2. \tag{2}
$$

Cauchy–Schwarz gives $|C|\le1$, so both receiver energies are nonnegative.
At equal delays $C=1$ and all energy reaches the plus output. When the two
derivative supports do not overlap $C=0$ and each receiver takes $E/2$.
These are deterministic energies in a single pulse experiment. Dividing by
$E$ does not turn them into probabilities of exclusive detector clicks.

For the coherent limit choose $f_D(t)=A g(t/D)\cos(\omega t)$ with a fixed
nonzero smooth compactly supported envelope $g$, $\omega>0$, and fixed delay
$\delta$. Let $D\to\infty$ at fixed $A,\omega,\delta$. The leading derivative
is $-A\omega g(t/D)\sin(\omega t)$; the envelope derivative contributes
lower order terms to the integrals divided by $D$. Setting $t=Dr$, translation
of the envelope tends to the identity, while integration by parts makes the
oscillatory double-frequency term vanish. Thus

$$
C_D(\delta)\longrightarrow\cos(\omega\delta),\qquad
Q_+/E\longrightarrow\cos^2(\omega\delta/2),\quad
Q_-/E\longrightarrow\sin^2(\omega\delta/2). \tag{3}
$$

This is a long coherent pulse limit, with energy growing with $D$ at fixed
amplitude, not an exact sinusoidal formula for an arbitrary finite pulse.
Equations (1)–(2) already give the finite-energy result. Scaling $A$ with $D$
to hold the energy fixed leaves the normalized correlation unchanged.

## 3. Which mechanical action could the phase measure?

A carrier delay produces the unwrapped relative phase $\phi=\omega\delta$;
the two energy records measure its cosine. They determine neither its sign
nor its winding without additional phase scans or timing information.
Complex phasors may abbreviate the real sine/cosine solution; no quantum
probability postulate enters (1).

To expose the action normalization, take the right-moving monochromatic wave
$u=A\cos(\omega t-kx)$, $k=\omega/c$, and one wavelength
$\ell=2\pi c/\omega$. This is a periodic carrier calculation, also applicable
to an exact carrier plateau of a sufficiently long pulse while the cell stays
inside that plateau. With momentum density $p=\mu u_t$, its cell energy is

$$
E_\ell=\int_0^\ell e\,dx
 =\frac12\mu A^2\omega^2\ell=\pi Z A^2\omega.
$$

Over one temporal cycle
the canonical loop integral and action variable are

$$
J_\ell=\int_0^{2\pi/\omega}\!dt\int_0^\ell p u_t\,dx
 =\frac{2\pi E_\ell}{\omega},\qquad
I_\ell=\frac{J_\ell}{2\pi}=\frac{E_\ell}{\omega}=\pi Z A^2. \tag{4}
$$

Spatial integration over a complete wavelength makes $\int p u_tdx=E_\ell$
constant at every time. The signed canonical accumulation over a delay is
$W_\ell(\delta)=E_\ell\delta$, hence

$$
\phi=\frac{W_\ell(\delta)}{I_\ell}. \tag{5}
$$

This supplies an explicit action-to-phase conversion, with a preparation-
and impedance-dependent coefficient. Choosing a cell of $n$ wavelengths
multiplies both $W$ and $I$ by $n$ without altering the phase.
Moreover the spacetime Lagrangian action of this pure traveling wave is zero:
$\mu u_t^2=Tu_x^2$ pointwise. Equation (5) uses a canonical integral, not
$\int Ldt$. A claim that the receiver measures $\exp(iS/K)$ must specify
its action functional and boundary convention; equal action units do not
justify identifying these quantities.

## 4. Decisive attenuation and apparatus tests

At fixed strings, junctions, delays and receivers replace $f$ by $\epsilon f$
with $0<\epsilon\le1$. Linearity preserves all travel times and the normalized
correlation exactly, including for finite pulses. Equations (1) and (4) give

$$
E\mapsto\epsilon^2E,\qquad Q_\pm\mapsto\epsilon^2Q_\pm,
\qquad I_\ell\mapsto\epsilon^2I_\ell,
\qquad \phi\mapsto\phi. \tag{6}
$$

Every positive amplitude retains a defined normalized fringe; its absolute
work vanishes in the zero-amplitude limit. No measurable signal is asserted
at the zero endpoint. A fixed receiver resolution would end practical
visibility earlier and would supply an apparatus energy threshold.

A second family rescales $\mu,T,Z$ together by $\eta>0$, including receiver
impedances. The speed and displacement equations stay fixed, whereas energies
and action integrals acquire $\eta$. A calibrated force or mass standard
would distinguish this family. It demonstrates the same common normalization
freedom as Q06 in an apparatus that now performs interference and absorbs work.
Changing frequency at fixed delay changes the phase; at fixed cell energy it
also changes $I_\ell=E_\ell/\omega$. Neither a cosine fringe nor a square-law
energy record fixes that ratio universally.

## 5. Consequence and next decision

Within this model, coherent path composition and mechanical energy readout
are compatible with arbitrarily small positive classical action. This
closes Q07's proposed linear-wave receiver test. The result is a physical
countermodel to selecting an action unit from interference alone, not a
reconstruction of quantum detection. The admitted field has infinitely many
modes and its receivers record divisible energy.

Park further linear splitter and impedance variants. The sharper next test
is whether localized event readout excludes this alternative: construct a
passive receiver with stored energy and a threshold, account for its reset
work, and test whether exclusive events and their energy scale survive changes
in receiver preparation. A threshold could sharpen event formation while
still supplying its own scale; the calculation must decide that distinction.
Compare this with the gap track before dispatch: the string model already
specifies real physical dynamics, but its nondispersive relation
$\omega=c|k|$ admits low frequencies as wavelength grows and supplies no
positive infinite-volume frequency gap. Another linear mode calculation
would not resolve the missing physical quantum Hamiltonian of G04.

Written consistency checks: variation and local energy balance in section 1;
zero junction work by orthogonal boundary subspaces; receiver work and the
sum/difference cancellation in (1); Cauchy–Schwarz and the envelope limit;
spatial and temporal integrations in (4); distinct canonical and Lagrangian
actions; exact attenuation and common-parameter rescaling. No computational
numerical or symbolic verification was used.

Source context is the [B18 companion](../docs/batches/B18/checkerboard-recurrence-source-companion.md)
and [checkerboard comparison](checkerboard-dynamics.md): their norm/probability
construction motivates the comparison but does not supply the string junction
or receiver model. [Q07](spin-action-patching.md) isolates the phase premise;
[Q06](reciprocal-coupling-normalization.md) isolates reciprocal calibration.
This note gives its own elementary derivation and coordinator consistency
review. Independent proof review and bounded literature comparison remain
required before ledger promotion; no novelty claim is made.
