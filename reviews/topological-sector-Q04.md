# Q04 review: topology fixes an energy floor, not an action scale

**Finding.** The central Q04 construction is mathematically sound as an
exploratory countertest.  In the stated normalization, every smooth
finite-energy field with degree \(Q\) obeys
\(H\ge 4\pi\rho |Q|\), and the displayed degree-minus-one family realizes
equality for every \(R>0\).  Its half-energy radius is \(R\), so the smooth
same-sector sequence \(R\downarrow0\) retains energy \(4\pi\rho\), while the
explicitly defined radius-crossing action
\(E_R(R/c)=4\pi\rho R/c\) tends to zero.  Fixed topology therefore supplies a
sector energy floor but does not, by itself, supply the length or duration
needed for a positive action floor.  This conclusion should remain
exploratory: it tests one specified energy-time observable and one classical
Lorentzian field model, not every action-valued functional or a quantum phase
constant.

Status: proof review and bounded literature comparison only; no ledger
promotion or novelty finding.  Requested worker: Sol, medium effort.  Date:
2026-09-14.  Inputs were
`notes/topological-sector-action-selection.md`,
`research/handoffs/Q04.md`, and `research/ACTION_FIELD_TARGET.md`.  This review
is the only output.

## Mathematical proof review

1. **Units and normalization are consistent.**  With dimensionless \(n\),
   \([\rho]=\mathrm{energy}\), and \([c]=L/T\), both terms in (1) have
   dimensions \(L^{-2}\), so the spacetime integral has action units.  The
   stated momentum density \(\pi=\rho\partial_tn/c^2\) and Hamiltonian (2)
   follow.  The argument also correctly observes that \(\rho\) and \(c\)
   alone form no action: \(\rho/c\) still needs a length.

2. **The degree bound has the right coefficient and sign independence.**
   Since \(a,b\perp n\), \(|n\times b|=|b|\), and
   \(a\cdot(n\times b)=-n\cdot(a\times b)=-q\).  Thus the two displayed
   squares give \(|a|^2+|b|^2\ge2|q|\) after choosing the sign, and integration
   gives
   \(E\ge(\rho/2)2|\int q|=4\pi\rho|Q|\).  Adding nonnegative kinetic energy
   yields the same bound for \(H\).

3. **The explicit family and its radius calculation check directly.**  The
   stated densities integrate to
   \(Q=(4\pi)^{-1}2\pi(-4R^2)(2R^2)^{-1}=-1\) and
   \(E=(\rho/2)2\pi(8R^2)(2R^2)^{-1}=4\pi\rho\).
   Integrating only to radius \(r\) gives (6), hence \(E_R(R)=E/2\).  Equality
   in the first-order square makes these fields critical under compactly
   supported smooth variations (which preserve degree), so calling them
   static solutions is justified.  The concentration statement is also
   correct: the energy density is an approximate identity of total mass
   \(4\pi\rho\); pointwise convergence away from the origin does not imply
   strong \(H^1\) convergence.

4. **The contraction answers the stated action question.**  A static solution
   on \([0,R/c]\) has \(S=-E R/c\), yielding (7).  More generally, in two
   spatial dimensions the simultaneous scaling
   \(n_\lambda(t,x)=n(t/\lambda,x/\lambda)\) contributes \(\lambda^3\) from
   the measure and \(\lambda^{-2}\) from either derivative term, so
   \(S[n_\lambda]=\lambda S[n]\); degree is unchanged.  The field equation is
   correspondingly scale covariant.  The comparison varies the history's
   duration together with its size.  It therefore rules out a topology-only
   lower bound for this intrinsic crossing-time prescription, while a fixed
   externally supplied \(T\) defines a different question.

5. **The gap qualifications are adequate, with one useful strengthening.**
   Linearization about the vacuum gives the massless dispersion
   \(\omega=c|k|\), and the normalized dilation packets have Rayleigh quotient
   tending to zero.  Those packets lie in the degree-zero vacuum sector, so
   they do not alone establish a within-\(|Q|=1\) fluctuation statement.  The
   note separately supplies such a statement: translations of a degree-one
   minimizer are an exact moduli family, and \(\partial_i n_R\in L^2\) are
   zero directions of the static Hessian.  This excludes a strictly positive
   unquotiented static Hessian gap.  It does not determine the spectrum after
   quotienting collective coordinates, as the note correctly says.

## Corrections and scope objections

- In section 3, “the same static sector has \(|S|=ET\ge4\pi\rho T\)” should be
  read, or edited, as “the same **static configurations**, each held for
  \(T\), have ...”.  The Lorentzian functional is kinetic minus potential;
  topology does not imply \(|S|\ge4\pi\rho T\) for arbitrary time-dependent
  histories in the sector.  This wording issue does not affect the shrinking
  static counterfamily.

- The radius-crossing time \(R/c\) is a transparent model prescription, not a
  period, relaxation time, or consequence of the static solution.  The proof
  establishes that topology cannot prevent this natural action candidate from
  vanishing.  It does not prove that every operational definition of action
  must use that time window.  A claim of universal action selection would
  still need a physical rule that selects a duration and survives the
  contraction.

- The literature checked below supplies a *time-independent* O(3) model and
  its static solutions.  It does not supply the Lorentzian kinetic term, the
  propagation speed \(c\), the crossing-time interpretation, or the
  low-frequency wave comparison.  Those are project model choices and written
  derivations.  In particular, the historical ferromagnet motivation should
  not be treated as evidence for this second-order Lorentzian dynamics.

- Conservation of degree is conditional on smooth evolution and preservation
  of the boundary extension.  A singularity or boundary flux leaves that
  admissible class.  The note states this condition and does not claim that its
  static contraction is a dynamical collapse, which is the correct physical
  scope.

## Bounded primary-source comparison

Coverage stopped at two search queries, one primary research source, and six
PDF pages.  Queries were (1) “Belavin Polyakov metastable states
two-dimensional isotropic ferromagnets PDF 1975 energy 4 pi scale arbitrary”
and (2) “site:arxiv.org hep-th/9402137 O(3) sigma model instanton scale size
energy bound”.  The CERN route to the 1975 Belavin--Polyakov paper returned an
anti-bot page, so only its metadata was used as a discovery lead and no passage
claim is attributed to it.

Primary passage read: M. S. Ody and L. H. Ryder, “Time-Independent Solutions
to the Two-Dimensional Non-Linear O(3) Sigma Model and Surfaces of Constant
Mean Curvature,” arXiv:hep-th/9402137, [record and PDF](https://arxiv.org/abs/hep-th/9402137),
PDF pp. 2--7 (six pages), especially printed pp. 4--7, equations
(2.1)--(2.26).  Reading level: passage; formula transcription was checked in
the PDF.

| Source passage | Exact established match | Project interpretation beyond the source |
| --- | --- | --- |
| pp. 4--5, (2.1)--(2.16) | Unit-vector field, static Euler--Lagrange equation, finite-energy constant boundary, compactification \(S^2\to S^2\), integer degree, and the \(1/(4\pi)\) charge-density normalization | Embedding the static functional in the Lorentzian action (1), assigning \(\rho\) and \(c\), and treating smooth time evolution as the physical dynamics |
| p. 6, (2.17)--(2.23) | Duality equations, analytic/anti-analytic BP solutions, and \(E_{\rm tot}=4\pi|Q|\) in the source's unit normalization | Multiplication by project stiffness \(\rho\); the square-completion proof as written in Q04; the action-over-time conclusion |
| pp. 6--7, (2.24)--(2.26) | Each soliton carries an arbitrary scale factor \(\rho_n\); total charge is independent of centers and scale factors; a one-soliton can be rescaled to canonical form | Identifying the displayed project's \(R\) as a half-energy radius, taking \(R\downarrow0\), and concluding that the crossing-time action tends to zero |

This is an exact literature match for the static topological energy/scale
ingredients, not for the action-selection conclusion.  No exhaustive coverage
or novelty inference follows from the bounded comparison.

## Source-to-model suggestion and decision

Ody--Ryder's pp. 6--7 isolate the decisive modulus: charge and static energy are
independent of the soliton scale factor.  A useful next model should therefore
be tested by asking whether an added conservative term *lifts that modulus*
and whether its coefficient merely imports the missing scale.  Concretely, for
the proposed three-dimensional quadratic-plus-quartic unit-vector model,
write the rescaled static energy as \(E(R)=aR+b/R\), identify the kinetic
normalization that gives a physical time, and calculate the resulting
size-mode action.  The minimum at \(R=\sqrt{b/a}\) would show size selection,
but any positive action assembled from \(a\), \(b\), and the kinetic coefficient
must still be traced to those dimensional inputs and tested against the vacuum
spectrum.

The review therefore supports Q04's decision: retain fixed topology as a
conservative zero-energy exclusion mechanism, and park topology alone as an
action selector.  The argument is suitable as an exploratory construction
after the fixed-duration wording is tightened; it is not yet a candidate for
accepted-ledger promotion.
