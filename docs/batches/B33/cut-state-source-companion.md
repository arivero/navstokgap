# B33 cut-state source companion

## Coverage

This is a bounded R03 audit requested at Luna-low effort. No web searches were
performed. Two primary pages were read from the cached B23 originals:
Ford–Kac–Mazur, printed p. 505 (PDF p. 3), equations (2)–(7), **passage**;
and Zwanzig, printed p. 219 (PDF p. 5), equations (20)–(24), **passage**.

## What the sources establish

Ford–Kac–Mazur writes coupled oscillator dynamics with matrix cosine/sine
propagators and canonical initial data, then obtains stationary Gaussian pair
correlations. Finite chains have quasiperiodic correlation functions; their
large-chain route to Markov behavior depends on the specified spectral limit.
This supports using a full phase-space propagator and separating finite
conservative dynamics from a reservoir limit.

Zwanzig derives an exact reduced generalized Langevin equation for a particle
coupled to harmonic bath modes. On printed p. 219 the friction coefficient is a
cosine sum over bath frequencies and couplings, and the noise covariance obeys
the fluctuation–dissipation relation. The memory kernel belongs to the reduced
equation and must not be identified automatically with a tagged position
covariance or with the note's action observable.

## Relation to `notes/classical-cut-state.md`

The note's fixed-energy conditional kernel, nonsemigroup mean, reset terminal
`L^2` limit, phase-state restoration and `J=E/omega` normalization are derived
consequences of its explicitly stated two-body Hamiltonian and uniform phase
preparation. The sources are established ingredients only. They do not prove
the reset formulas, a positive action lower bound, preparation independence,
or universality. The note should retain the distinction between an observational
cut (which records a joint path marginal) and a reset (which reapplies `L`), and
should state that the kernel is a stationary conditional kernel rather than a
Markov transition kernel on position alone.

The next bounded construction is a three-body spring system: retain tagged
position and momentum while eliminating one receiver mode, then identify the
memory/interface term and its units. This decides whether tagged momentum alone
closes the cut or whether finite history is required.


Coordinator source correction: the p. 505 image ends during the stationarity
argument; pair-correlation equations (8)–(9) and the finite-chain
quasiperiodicity statement are outside this two-page reading. Those broader
background statements use the earlier B23 companion, not new B33 passage
coverage. The p. 505 matrix propagator and p. 219 memory equation were
visually verified. No additional primary page was read.
