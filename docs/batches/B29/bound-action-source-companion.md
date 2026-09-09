# B29 source companion: bounded-orbit action observable

## Result and coverage

The A15 circular-orbit identities are correct under their stated preparation
and canonical-coordinate assumptions. The transport coefficient vanishes at
both short and long windows, and the displayed elementary bounds do not imply
a broad positive plateau. The identity `2 sqrt(det Sigma)=RP` is the usual
two-dimensional rms-emittance normalization for a uniform phase ellipse; it is
not a preparation-independent invariant equal to orbital action.

One bounded discovery route was used (two queries, INSPIRE-first wording),
followed by one primary open-access article and exactly two PDF pages. Search
snippets were not evidence. Primary source: L. Groening, C. Xiao and M.
Chung, “Extension of Busch’s theorem to particle beams,” *Phys. Rev. Accel.
Beams* 21, 014201 (2018), DOI 10.1103/PhysRevAccelBeams.21.014201.
Metadata and abstract are verified on the APS record. PDF internal pp. 1–2
(viewer pages P0–P1) were read. P0 defines the canonical beam coordinates and
states the single-particle canonical angular-momentum invariant (Eqs. 1–4).
P1 defines second moments and projected rms emittance (Eqs. 5–11), and states
preservation of eigenemittances and four-dimensional determinant under
symplectic transformations (Eqs. 10–13). This supports prior-art classification
only; it does not discuss the circular-orbit model or conditional variance.

## Proof audit by result

1. **Uniform circular increment.** With `x=R cos(theta)` and uniform phase,
`E[x(t)x(t+Delta)]=(R^2/2) cos z`, hence the variance increment is
`R^2(1-cos z)` and `h_x=mR^2(1-cos z)/Delta=(ell/gamma)(1-cos z)/z`.
This is an exact written trigonometric derivation. Both limits are zero.
The source's beam-moment definitions (P1, Eqs. 8–9) are consistent with the
covariance convention, but provide no new proof of this orbit calculation.
Literature status: derived consequence; no claim of prior publication.

2. **Position-conditioned variance.** Given `x(t)=x`, the two phase branches
have equal weight for uniform phase and next positions
`x cos z +/- sqrt(R^2-x^2) sin z`; their conditional variance is
`(R^2-x^2) sin^2 z`. Averaging over the phase gives the stated coefficient
`ell sin^2 z/(2 gamma z)`. At endpoints use the continuous zero extension.
Conditioning on `(x,p_x)` leaves a deterministic future, so its variance is
zero. Literature status: elementary derived result; no match in the selected
source. The equal branch weights and the distinction between partial and full
state conditioning must remain explicit.

3. **No broad positive plateau.** Since `1-cos z <= min(z^2/2,2)`, a fixed
fraction condition `h_x >= eta ell` implies
`2 gamma eta <= z <= 2/(gamma eta)`. The ratio of any admissible endpoints is
at most `1/(gamma^2 eta^2)`. Thus no parametrically broad interval exists at
fixed positive fraction in this one-frequency family. This is a valid bound,
not a theorem excluding multiscale models. Literature status: derived
countertest; no source match.

4. **Canonical covariance determinant.** Uniform phase gives diagonal
covariance `(R^2/2,P^2/2)`, so `2 sqrt(det Sigma)=RP=ell`, with action units.
For an affine canonical map `S` in this 2D plane,
`Sigma' = S Sigma S^T` and `det S=1`, proving invariance. The selected primary
source independently defines projected rms emittance as the square root of a
second-moment determinant (P1, Eq. 9) and records preservation of emittance
invariants under symplectic transformations (P1, Eqs. 10–13). Its convention
is emittance `sqrt(det)`, so A15's factor two is an explicitly chosen
orbit-area normalization, not universal accelerator convention. Literature
status: established rms-emittance construction and linear-symplectic
invariance; the equality to this orbit's angular action is a derived specialization
with novelty unassessed.

5. **Nonuniform phase and point phase.** The displayed orbit transfer matrix
is linear with determinant one, so covariance determinant is preserved for any
initial phase law for which it exists. A point-phase law has rank-zero
covariance despite `ell>0`; therefore the equality depends on preparation.
Uniform phase is sufficient, rather than necessary: matching its first and
second moments also suffices. This is a direct counterexample to preparation
independence. The primary source's assumptions (linear/mono-energetic beam,
P1) reinforce the need to state the model domain; it does not license a
nonlinear canonical extension.

6. **C052/C053 transfer.** Under the singular Kepler benchmark, the estimator
inherits `inf ell=k/c`; under a fixed softened core, C053 gives infimum zero.
This transfer is logically immediate because the estimator equals `ell` only
for the uniform-phase circular preparation. It is not an observable universal
bound across preparations or potentials, and does not alter the established
status of C052/C053.

## Source-inspired next test

Use a matched ensemble with a small but nonzero phase spread (and, separately,
radial or energy spread), then derive how `det Sigma` departs from `R^2P^2/4`
while the linear transfer remains symplectic. This tests whether any positive
action estimate survives preparation variation; it must be done by written
covariance algebra, with no numerical verification. Keep projected versus
eigen-emittance conventions separate.

## Reproduction and limits

APS article URL: https://journals.aps.org/prab/pdf/10.1103/PhysRevAccelBeams.21.014201
The coordinator downloaded the publisher PDF through the open APS harvest
endpoint after the journal download returned HTTP 403, and visually verified
page 2, Eqs. (6)–(11). Local ignored path: `.build/b29/Groening2018.pdf`.
SHA-256: `94f928e992c5e0c5a0b7cc69cda45ecd6c1dd9eca986ef27460945cf7f496816`.
The source uses normalized momenta and uncentered moments in its beam convention;
A15 uses physical canonical momenta and centered covariance. Its factor two
and action units follow from the written orbit derivation. Coverage is bounded
to the two pages above; no claim is made about later sections or exhaustive
prior art. Effective-model language is not used.
