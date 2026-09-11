# R20 review: exact phase ambiguity with a hidden clock

C096–C097 are accepted as checked derivations for the pulse design and local
preparation domains in [R20](../notes/hidden-clock-ambiguity.md).

- Smoothness: dividing the integrated momentum force by lambda removes its
  zero before extension to lambda=0. Finite-time smooth dependence includes
  clock derivatives and yields a common parameter-implicit-function domain.
- Offset identity: integration by parts has vanishing endpoint terms and
  gives partial_s A=-AM/v. Thus the compensated receiver follows Mz/v at
  lambda=0 and its energy derivative vanishes exactly.
- Design: four independent Taylor observation rows and the invertible bump
  moment matrix give determinant order 4+0+1+2+3=10. The expansion is analytic
  in r epsilon; the factored remainder can be differentiated in v. Its
  logarithmic derivative yields trace B=10/v_0+O(epsilon)>0.
- Transversality: the symmetric matrix G-normalization of GB has trace B.
  A positive trace supplies a positive quadratic direction. Its positive
  shell subset is open and intersects the complement of both canonical
  velocity-zero hyperplanes. This selects a point with nonzero energy-speed
  derivative and both nonzero canonical phase derivatives.
- Exact shell: solving the scalar energy equation for speed preserves E at
  positive coupling. The resulting phase family has uniformly nonzero x and
  P derivatives on a small fixed interval. Since q=0 and v=v_0 along the
  zero-coupling family, their deviations are O(lambda times offset), preserving
  half of each positive preparation margin for small lambda.
- Risks: common-record endpoints separated in each coordinate give the two
  worst-case lower bounds. Their product has action units. A one-dimensional
  family supports this risk claim without supplying a positive area bound.

All design parameters are chosen before the physical coupling and preparation
limits. The positive product depends on unknown initial clock offset and
restricted records; it is a delayed reconstruction result. Supplied known
observation time T is retained. The chosen nominal receiver point, design and
constants need not apply to every point or every pulse geometry.

[B51](../references/batches/B51.md) records the sequential librarian and
coordinator source review. Sontag's all-input/all-time equivalence is a method
comparison; no such full dynamical symmetry is imported. No numerical or
symbolic verification scripts were created or run.
