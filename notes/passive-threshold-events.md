# A passive threshold creates events, but its scale belongs to the receiver

Equal independent thresholds applied to two complementary classical work
outputs trade missed events against double events. A mechanical barrier gives
a physical threshold, but stored preparation energy can reduce the required
signal arbitrarily. Accounting for reset locates that energy in the apparatus;
it does not turn the threshold into a universal action constant.

This Q09 calculation is exploratory and unpromoted. It specifies a deterministic
detector class, not a theorem about all classical detectors or a model of
single-photon experiments. Independent proof and literature review precede
any accepted-ledger promotion.

## 1. Integrated work and an event rule

Use Q08's two output works $W_+,W_-\ge0$, with total incident energy E and

$$W_+=\frac E2(1+z),\qquad W_-=\frac E2(1-z),\qquad -1\le z\le1. \tag{1}$$

Here z is normalized pulse overlap. For ideal coherent paths it is the
relative-phase cosine. Equation (1) and the threshold analysis apply directly
to any overlap value, without taking a monochromatic infinite-energy limit.

An ideal lossless work accumulator starts with zero stored energy and receives
nonnegative input power: $\dot e_i=P_i(t)$, $e_i(0)=0$. At the end of one
gate its record is

$$C_i=\mathbf1_{W_i>\Delta},\qquad \Delta>0. \tag{2}$$

The comparator is a stipulated coarse readout, not an independently derived
measurement law. The strict inequality excludes marginal barrier trajectories.
It counts at most one event per gate; rearming and repeated firing require
additional dynamics. Equation (2) by itself does not model permanent memory.

## 2. The complete event regions

For $E>0$ put $r=\Delta/E$. Then

$$C_+=1\ \Longleftrightarrow\ z>2r-1,\qquad
C_-=1\ \Longleftrightarrow\ z<1-2r. \tag{3}$$

If $\Delta<E<2\Delta$, both thresholds cannot be crossed. There is one event
only for $|z|>2\Delta/E-1$; the remaining central interval has no event.
For $E\le\Delta$ there is no event anywhere. If $E>2\Delta$, every overlap
gives at least one event, but both fire for

$$|z|<1-2\Delta/E. \tag{4}$$

At the tuned value $E=2\Delta$, exactly one fires for every $z\ne0$, while
neither fires at $z=0$. Using a non-strict comparator changes this single
boundary point to two events, rather than solving the tie. Thus equal
deterministic thresholds give no open range of incident energies with both
unit efficiency and exclusive events for all overlaps.

At a balanced splitter with equal input signals and identical receiver states,
exchange symmetry is even more immediate: the two deterministic records are
identical, so they are either both zero or both one. Asymmetric preparations,
random local thresholds or communication between receivers alter this premise.
Their statistics and physical cost would have to be specified separately.

If z is experimentally sampled, counts depend on its sampling law and the
threshold. Neither $W_i/E$ nor the conditional fraction of surviving single
events is automatically a Born probability. Discarding no-click or double-click
gates changes the ensemble; it cannot be hidden in normalization.

## 3. A mechanical threshold and stored readiness energy

Consider a receiver coordinate q, momentum p, mass M and potential

$$H_R=\frac{p^2}{2M}+U(q),\qquad
U(q)=\Delta\left(1-\frac{q^2}{\ell^2}\right)^2,
\quad M,\ell,\Delta>0. \tag{5}$$

The left and right minima have zero energy; the intervening saddle at q=0
has energy $\Delta$. Prepare q at $-\ell$, p=0, and deliver a positive
impulse I. The deposited energy is $W=I^2/(2M)$. The subsequent conservative
motion crosses q=0 precisely when $W>\Delta$. Below threshold it turns on
the left; at equality it approaches the saddle only asymptotically.
Indeed, near q=0 at equality,
$\dot q\simeq\sqrt{4\Delta/(M\ell^2)}|q|$, giving a logarithmically
divergent travel time. A finite readout deadline adds another receiver scale.

This is an exact barrier-crossing event after an impulse. General forcing
cannot be replaced by its total work alone without checking its direction
and timing. The conservative particle can recross later: a persistent record
requires a latch, capture or damping and its own energy accounting. Thus this
example justifies a physical threshold, not a free permanent bit.

Now prepare q at $q_0\in(-\ell,0)$ at rest. It already stores
$e_0=U(q_0)$. A positive impulse crosses if

$$W>\Delta-e_0. \tag{6}$$

As $q_0\uparrow0$, the required signal tends to zero at fixed M, $\ell$
and $\Delta$. The receiver is correspondingly close to an unstable state.
This is stored readiness energy, not creation of energy by a small signal.

For a cycle that captures the particle at the right minimum with zero energy,
restoring this ready state requires net work at least $e_0$, when the reset
apparatus supplies all work and losses are nonnegative. Capture must account
for the released $e_0+W$. If energy is recovered into a separate storage
device, include that device in the cycle: it can reduce external work but
does not remove the energy balance. For full return of every storage degree
of freedom, net supplied energy equals exported work plus dissipation.
No universal reset-energy number follows from (5).

## 4. Action test and strategic consequence

For a narrow-band incident pulse of angular frequency $\omega$, its canonical
wave action is approximately $E/\omega$ (with Q08's finite-pulse qualification).
The detector's corresponding scale is $\Delta/\omega$, or
$(\Delta-e_0)/\omega$ for a preloaded receiver. Changing the frequency,
barrier or readiness changes it. Defining instead a barrier energy times a
crossing time gives another apparatus-dependent quantity, with a divergence
at the separatrix rather than a selected constant.

Retain passive barriers as an explicit mechanism for discrete records. Their
thresholds neither guarantee exclusive efficient events nor select a universal
action. Further threshold tuning is parked. A worthwhile next test is to
specify an independent reliability requirement: can a finite-temperature,
finite-retention receiver keep false events below a prescribed probability
while its signal threshold goes to zero? That asks what measurable stability
cost replaces arbitrary preloading. Any resulting scale must retain its
temperature, lifetime and error dependence rather than be called universal.

Source context: [Q08](mechanical-interference-action.md) supplies the work
split and wave-action convention. One discovery query identified the primary
experimental lead P. Grangier, G. Roger and A. Aspect, *Experimental Evidence
for a Photon Anticorrelation Effect on a Beam Splitter: A New Light on
Single-Photon Interferences*, EPL **1**, 173--179 (1986),
[DOI](https://doi.org/10.1209/0295-5075/1/4/004).
Only discovery metadata was checked; no experimental data or detector model
is imported into this derivation. The ideal comparator and passive barrier
are declared model premises. No numerical or symbolic scripts were used.
