# Complete final apparatus records replace the initial clock calibration

All ten final apparatus coordinates determine the receiver state, initial
probe positions and both initial clock coordinates uniformly on a bounded
receiver domain and fixed small apparatus boxes. Initial probe momenta remain
known at zero. This removes both initial clock calibration premises from R23,
including offset, without using exact receiver energy.

R24, 2026-09-12. Retain [R23](final-clock-momentum-recovery.md)'s fixed
Hamiltonian, finite masses, pulse geometry, exact model calibration and known
observation time T. The unknown initial data are w=(z,q,s,v); the physical
clock momentum is M_c v. Their domain is a compact convex product Z times
Q times C, where C is a small rectangle about (s_0,v_0), v>0. Choose common
strict pulse and cutoff margins and a uniform inverse bound for A_(s,v).
The full receiver energy ball is contained in Z. Source coverage is in
[B55](../references/batches/B55.md).

## 1. The full clock record gives an explicit leading inverse

Use fixed receiver/probe units, clock length unit S_* and speed unit V_*;
write theta=T V_*/S_*. Express the following physical record vector in those
units, with its clock momentum block divided by M_c:

$$\mathcal F_\lambda(w)=
 \left(\frac{\pi(T)}{\lambda},q(T),s(T),\frac{p_s(T)}{M_c}\right).$$

In dimensionless coordinates the leading map and remainder are

$$\mathcal F_\lambda=L+R_\lambda,\qquad
 L(z,q,s,v)=(-A_{s,v}z,q,s+\theta v,v),\qquad
 \|R_\lambda\|_{C^1}\le C\lambda. \tag{1}$$

R23 already includes receiver, pointer and clock-momentum reaction. The new
clock-position block follows from the exact physical equation

$$s(T)=s+vT-\frac{\lambda K}{M_c}\sum_j
 \int_0^T(T-t)f'_j(s(t))x(t)q_j(t)\,dt. \tag{2}$$

The compact smooth-flow and variational bounds apply to both initial clock
coordinates; the correction in (2) is O(lambda) in C1. Final clock and
pointer positions are records at the specified time T; their momenta persist
after the pulse supports have been crossed.

## 2. Uniform global inverse on the whole bounded domain

In fixed dimensionless units choose alpha>0 with ||A_c h||>=alpha||h||,
and let D_s=sup||(partial_s A_c)z||, D_v=sup||(partial_v A_c)z|| on C times Z.
For two initial states put d=||L(w)-L(w')|| in the product sup norm. The
last three blocks give

$$|v-v'|\le d,\qquad |s-s'|\le(1+\theta)d,\qquad
\|q-q'\|\le d.$$

Varying s and v along segments within their rectangle, the first block gives

$$\alpha\|z-z'\|\le
 \left[1+D_s(1+\theta)+D_v\right]d.$$

Consequently, with

$$\beta=\min\left\{\frac1{1+\theta},
 \frac{\alpha}{1+D_s(1+\theta)+D_v}\right\}>0,$$
$$\|L(w)-L(w')\|\ge\beta\|w-w'\|.$$

The initial-data product domain is convex, so the remainder is C lambda
Lipschitz. At sufficiently small positive coupling,

$$\|\mathcal F_\lambda(w)-\mathcal F_\lambda(w')\|
 \ge\frac\beta2\|w-w'\|. \tag{3}$$

This proves global recovery of all ten unknowns. The clock shear is inverted
explicitly at leading order; exact reaction is jointly calibrated. No energy
constraint, local receiver-patch prior or shrinking preparation width enters.
The result applies to any fixed R06 signal design with the stated margins
and inverse bound, including the designs producing R20/R22 ambiguities.

## 3. Record precision and action units

For final pointer momentum/position and clock position/momentum errors bounded
by rho_pi,rho_q,rho_s,rho_c in the declared units set

$$\delta=\max(\rho_\pi/\lambda,\rho_q,\rho_s,\rho_c).$$

Minimum-residual fitting on the compact admitted domain and (3) give

$$\|\widehat w-w\|\le4\delta/\beta,\qquad
\epsilon_x\epsilon_P\le\frac{16L_*P_*}{\beta^2}\delta^2. \tag{4}$$

At fixed positive coupling this action-valued product closes as all record
errors close, with apparatus and positive unknown preparation widths fixed.
Initial clock position and momentum errors are bounded by 4 S_* delta/beta
and 4 M_c V_* delta/beta. A joint limit requires rho_pi/lambda tending to zero
as well as the other three errors. These are sufficient upper bounds.

## 4. What information the sequence has isolated

| Result | Initial information supplied | Final records | Recovery scope |
| --- | --- | --- | --- |
| R19 | Clock phase and probe momenta | Eight probe coordinates | Whole bounded receiver domain |
| R20 | Probe momenta | Eight probe coordinates | Hidden clock permits exact shell ambiguity |
| R21 | Clock position, probe momenta, energy, local patch | Eight probe coordinates | Uniform recovery on that patch |
| R22 | Clock position, probe momenta, energy; full shell | Eight probe coordinates | Distinct-speed exact ambiguity |
| R23 | Clock position and probe momenta | Eight probe coordinates plus clock momentum | Whole bounded receiver domain |
| R24 | Probe momenta | All ten apparatus coordinates at known T | Whole bounded receiver domain |

Thus the physical final clock phase replaces its initial calibration. The
common remaining preparation premise is exact incoming probe momenta. Joint
final record access is also supplied; a second readout apparatus has not been
implemented by adding an output coordinate to the mathematical map.

Next R25: let every initial apparatus coordinate, including probe momenta,
be unknown within a fixed positive box. Retain full final apparatus records
and a receiver energy shell. Test whether the free apparatus flow's invertible
initial-to-final derivative permits exact compensation of receiver changes
with interior preparation margins. This directly targets the remaining
preparation premise rather than adding another clock coordinate.
