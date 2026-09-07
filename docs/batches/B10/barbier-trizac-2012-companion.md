# Field Induced Stationary State for an Accelerated Tracer in a Bath

> Source: https://arxiv.org/abs/1203.6759 (PDF downloaded from https://arxiv.org/pdf/1203.6759)
> Metadata: Matthieu Barbier and Emmanuel Trizac, arXiv:1203.6759v3, 24 August 2012; J. Stat. Phys. 149 (2012), DOI 10.1007/s10955-012-0591-x
> Local original: `.build/b10/barbier_trizac_2012_field_induced.pdf`
> SHA-256: `58ada65f10326235a5b7951cdd64bc3e4ca2f88270acc47aced6360f465b0603`
> Extraction: `pdftotext -layout`; p. 19 equations were checked against a rendered page image.
> Rights: arXiv open preprint; retained in the build directory for this bounded audit.

## Source digest

The paper studies a Boltzmann–Lorentz tracer in a bath with a collision kernel
whose exponent `nu` selects Maxwell particles at `nu=0`. Its appendix defines
the stationary velocity autocovariance and diffusion coefficient. For
`nu=0`, direct moment evolution gives an exponential covariance
`Gamma(t)=Gamma(0) exp[-(1-a)t]` and the integrated Green–Kubo coefficient
`D=Gamma(0)/(1-a)`.

## Selected reading

- Abstract (p. 1): metadata and model scope.
- p. 19, Appendix Eqs. (89)–(98): covariance representation, normalization,
  Maxwell-kernel exponential decay and integrated covariance.
- Coordinator visually rechecked p. 19 and recalculated the PDF hash.
  Equations (87)–(88) on p. 18 remain outside this reading.

This is an exact structural match to B10's lag-integrated covariance after
restoring the collision rate `nu`; it does not prove B10's nonstationary
preparation-time relaxation, which uses a separate second-moment equation.

## Formula transcription and limits

The source's dimensionless rate is one and its `a` is the tracer coefficient.
The appendix allows an arbitrary bath for the Maxwell kernel, but its main
model also includes acceleration and may use velocity-dependent kernels. B10
uses only the field-free, constant-rate specialization.

## Extraction defects

No material extraction defect on the selected page. The source's page 19 is a
continuation of the appendix and was visually checked.
