# Q02 review: the response calculation is sound, with two scope repairs

**Result.** Equations (1)--(4) of
[`radiation-noise-action-selection.md`](../notes/radiation-noise-action-selection.md)
are correct for the stated stable, cutoff, locally viscous oscillator. The weak
damping limit selects the cubic spectral *shape* needed for equal oscillator
actions, and it cancels the probe charge and mass. It does not select the
coefficient \(K\). Two clarifications should accompany the result: the numerical
normalization of \(S_E\) has its electromagnetic mode-counting meaning only when
\(E\) is one Cartesian component of a homogeneous isotropic transverse field;
and the quadratic cutoff divergence belongs to the local viscous approximation,
not to a causal point-charge or extended-charge response. These are scope
repairs, not defects in the displayed calculation.

Task: bounded mathematical and primary-source review for Q02. Date:
2026-09-14. Role: reviewer/librarian. Requested model/effort: Sol, medium;
effective model/effort was not independently reported. Inputs were the Q02 note
and `research/handoffs/Q02.md`; this file is the only output. No ledger promotion
or novelty assessment is made.

## Mathematical review

With the note's Fourier convention, the stable susceptibility is

\[
 \chi(\nu)=\frac{q/m}{w^2-\nu^2-i\gamma\nu}.
\]

Consequently the stationary position and velocity variances give exactly (1).
Using

\[
 \frac{q^2}{3\pi\epsilon _0c^3}=\frac{2m\gamma}{w^2}
\]

and evenness of the spectrum gives (2), including its factor \(1/\pi\).
The dimensions also close: \(K\) is an action and \(J_*/K\) is dimensionless.

For the weak damping limit, set \(\nu=w+u\). The integrand in (2) is

\[
 \frac{2w^3}{4u^2+\gamma^2}+o\!\left(
 \frac{1}{u^2+\gamma^2}\right)
\]

on a shrinking neighborhood of the interior resonance. Its integral is
\(\pi w^3/\gamma+o(1/\gamma)\). On the complement of any fixed neighborhood
of \(w\), the integral is bounded uniformly as \(\gamma\downarrow0\), so its
prefactor makes that contribution vanish. This proves (3) in the stated order:
first the stationary limit, then \(\gamma\downarrow0\), at fixed
\(\Lambda>w\). The same approximate-identity calculation applied directly to
(1) gives

\[
 J_*\longrightarrow
 \frac{q^2S_E(w)}{2mw\gamma}
 =\frac{3\pi\epsilon_0c^3S_E(w)}{w^3}.
\]

Thus the general-spectrum coefficient in section 3 is correct. Continuity at
the two resonances and bounded finite-cutoff support are sufficient; global
integrability is stronger than needed here. The result is pointwise in \(w\)
and requires the resonance to remain away from the cutoff, as the note says.
The stationary-first qualification is essential because the relaxation time is
of order \(1/\gamma\).

At high frequency, the integrand in (2) is \(\nu+O(1/\nu)\). Hence

\[
 \frac{J_*}{K}=\frac{\gamma\Lambda^2}{2\pi w^3}
 +O(\gamma\log\Lambda)
\]

at fixed positive \(\gamma\), which verifies (4). Directly from (1), the
position variance has a \(d\nu/\nu\) tail and the velocity contribution a
\(\nu\,d\nu\) tail. The quiet-field and amplitude-rescaling countertests are
also exact: linearity sends \(S_E\) to \(a^2S_E\) and \(J_*\) to \(a^2J_*\),
while \(a=0\) leaves the damped rest state.

The normalization deserves one explicit bridge. For a homogeneous isotropic
transverse radiation field, if \(u(\nu)d\nu\) is the total field energy density
in a positive angular-frequency interval, isotropy and equal electric/magnetic
energy give

\[
 u(\nu)=\frac{3\epsilon_0}{\pi}S_E(\nu).
\]

The electromagnetic mode density is \(\nu^2/(\pi^2c^3)\). The note's choice
\(S_E(\nu)=K\nu^3/(3\pi\epsilon_0c^3)\) therefore means energy \(K\nu\) per
normal mode. In the weak damping limit the mechanical oscillator energy is
\(wJ_*=Kw\). Without the isotropic transverse-field premise, the displayed
factor is simply a chosen one-component noise normalization; stationarity by
itself does not supply the mode-counting interpretation.

## Oscillator approximation versus radiation dynamics

The note correctly labels \(\gamma=q^2w^2/(6\pi\epsilon_0mc^3)\) as the
on-resonance, cycle-averaged damping rate. Extending the resulting term
\(m\gamma\dot x\) to every driving frequency creates the quadratic divergence
in (4). A point-charge Abraham--Lorentz equation instead has a third-derivative
radiation term. Formally its frequency-domain denominator contains an
\(\omega^6\) radiation term rather than the viscous model's
\(\gamma^2\omega^2\); against a cubic field spectrum this softens the mechanical
energy tail to logarithmic order. That formal comparison is not a replacement
calculation: the point-charge equation has runaway/preacceleration issues and
does not directly define the stable stationary causal model assumed in (1).

A useful return construction is therefore a passive, causal extended-charge
susceptibility with an explicit form factor and a controlled cutoff-removal
limit. It would test which ultraviolet divergence survives a physical response.
It cannot by linear response alone repair action selection: multiplying the
homogeneous random-field boundary data by \(a\) still multiplies every forced
covariance by \(a^2\), and the quiet boundary condition remains available unless
additional reservoir dynamics excludes it.

## Primary-literature comparison and exact coverage

The bounded discovery used two web queries in one browser pass. Two primary
sources were retained; no source was downloaded or archived.

1. Timothy H. Boyer, “Derivation of the Blackbody Radiation Spectrum without
   Quantum Assumptions,” *Physical Review* **182** (1969), 1374--1383,
   DOI [10.1103/PhysRev.182.1374](https://doi.org/10.1103/PhysRev.182.1374),
   [APS full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRev.182.1374/fulltext).
   Reading level: **passage**. Inspected pp. 1374--1376 (abstract and section IV's
   Lorentz-invariant zero-point spectrum) and pp. 1379--1380 (section VII.D's
   damped-oscillator energy and its ultraviolet qualification). The PDF OCR is
   defective for several formulas, so formula identifications were limited to
   those also legible from their surrounding prose. Boyer obtains energy linear
   in frequency per mode, applies the nonrelativistic radiation-damped oscillator
   to recover the corresponding mean oscillator energy, and explicitly reports
   divergent kinetic energy from the zero-point tail while saying the dipole and
   nonrelativistic approximations fail at those high frequencies. This is a close
   precedent for Q02's shape, resonance balance, and cutoff warning.

2. Timothy H. Boyer, “Random electrodynamics: The theory of classical
   electrodynamics with classical electromagnetic zero-point radiation,”
   *Physical Review D* **11** (1975), 790--808,
   DOI [10.1103/PhysRevD.11.790](https://doi.org/10.1103/PhysRevD.11.790),
   [APS abstract](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.790).
   Reading level: **abstract** only; the full article was access-restricted on
   the checked APS route. The abstract defines random electrodynamics by a new
   random homogeneous Maxwell boundary condition, states that its spectrum is
   Lorentz invariant, and states separately that Planck's constant sets the
   spectrum's scale. It also says the zero-scale limit returns Lorentz's electron
   theory. This is direct primary evidence that the classical framework supplies
   the cubic/linear spectral form as a boundary condition while importing its
   action normalization; it does not exhibit dynamics selecting a positive
   coefficient.

The literature and the calculation therefore agree on the useful construction:
a cubic electric spectrum corresponds to constant action \(E/\omega\), and
radiation response transfers that constant to a narrow-band oscillator without
retaining \(q\) or \(m\). They also agree on the objection relevant to Q02:
the zero-point amplitude is supplied (historically as Planck's constant), and
the naive point/dipole oscillator has an ultraviolet problem. This bounded
comparison establishes neither exhaustive coverage nor novelty.

## Verdict and remaining dependency

Accept the note as an exploratory negative mechanism test after adding or
retaining the two scope statements above. No displayed equation needs repair.
The strategic decision is unchanged: park linear radiation-balance variants.
The remaining dependency is an autonomous field-plus-matter law that both
controls the ultraviolet response and breaks amplitude rescaling or excludes
the quiet state. Causal regularization alone addresses only the first part.
