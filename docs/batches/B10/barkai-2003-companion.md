# Stable Equilibrium Based on Levy Statistics: A Linear Boltzmann Equation Approach

> Source: https://arxiv.org/abs/cond-mat/0303255 (PDF downloaded from https://arxiv.org/pdf/cond-mat/0303255)
> Metadata: Eli Barkai, arXiv:cond-mat/0303255v1, 13 March 2003 (manuscript dated 31 October 2018)
> Local original: `.build/b10/mai_2003_stable_equilibrium.pdf`
> SHA-256: `ce8b64449681fade17c59439efbb1f7ce33487ff657639d37fd3681563558b84`
> Extraction: `pdftotext -layout`; equations on p. 4 were checked against a rendered page image.
> Rights: arXiv open preprint; retained in the build directory for this bounded audit.

## Source digest

The source gives a one-dimensional elastic tracer map with a bath velocity, a
uniform collision rate independent of velocities, molecular chaos, and a bath
that is not changed by collisions. It writes the affine coefficients in terms
of the mass ratio and derives the linear Boltzmann equation and Poisson
collision-count expansion. These are an exact prior match to the stochastic
premises of B10 after relabelling tracer and bath masses.

## Selected reading

- Abstract (p. 1): metadata and scope.
- pp. 4–5, Eqs. (3)–(12): elastic coefficients, uniform rate, master equation,
  Poisson collision count and iterated law.
- Coordinator added p. 3, visually verifying the collision map (2), and
  recalculated the PDF hash. Total combined source coverage: pp. 1, 3–5.

The source does not state B10's bounded-support contraction proof or its
physical-time second-moment ODE; those are elementary consequences for the
refreshed iid specialization and are not claimed as source-established.

## Formula transcription and limits

With `epsilon=m_b/M_tracer`, the source has
`V+ = ((1-epsilon)/(1+epsilon)) V- + (2 epsilon/(1+epsilon)) v_b`.
Its `R` is a constant collision rate. The source allows general bath PDFs and
does not impose a speed ceiling; B10 adds bounded iid bath velocities and
restricts `m >= M` to make the tracer coefficient nonnegative.

## Extraction defects

No material extraction defect on the selected pages. The arXiv PDF is version
v1; no later-version comparison was needed.
