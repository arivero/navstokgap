# Newton's record as a parallel move: what forgetting a record leaves

**Result, 2026-09-27 (atlas of halving, open cell 6).** Inserting an
unobserved time into Newton's cell is a series move and closes exactly
([refinement note](refinement-composition-and-limit.md), §2). Inserting a
*record* at that time attaches a new variable, the pointer, to the body;
forgetting it is the Newtonian counterpart of the parallel move of the
[series/parallel note](series-parallel-gauge-refinement.md). For a
position record with Gaussian pointer of width $\sigma$ this move is exact
(Proposition 1): it leaves the body's position distribution unchanged
and convolves its momentum distribution with a Gaussian of variance

$$v=\frac{\hbar^2}{4\sigma^2}.$$

Three consequences fill the Newton row of the
[atlas](halving-atlas.md).

- **Records at one instant combine in parallel:** precisions add,
  $\sigma^{-2}=\sigma_1^{-2}+\sigma_2^{-2}$, and so do the momentum variances, as the
  heat times of parallel faces combine by conductances in the gauge case.
- **Refining with a record at every inserted time converges iff**
  $\sum_j\sigma_j^{-2}<\infty$: the total momentum diffusion is
  $\frac{\hbar^2}4\sum_j\sigma_j^{-2}$, and the same sum measures the information
  gathered about the place. The continuous-measurement limit of Caves
  and Milburn is the case $\sigma_j^{-2}=\kappa\tau_j$ (Corollary 2).
- **Information and disturbance are locked at $\hbar^2/4$ per unit:**
  $\sigma^2v=\hbar^2/4$ for every record and every mesh. For $\hbar=0$ the move is
  the identity for every $\sigma$: records are series-exact, the Newtonian
  counterpart of a theory with no parallel planes, and exactly the joint
  determinacy of the [fifth-postulate note](principia-fifth-postulate.md).

The Gaussian record channel and its continuous limit are standard
([Caves and Milburn 1987](https://doi.org/10.1103/PhysRevA.36.5543),
metadata, cited in the Planck paper); the reading as the parallel move of
the atlas is this note's. For non-Gaussian records the general floor is
Theorem 6 of the [Planck paper](planck-gap-paper.md).

## 1. The record channel

A position record with Gaussian pointer of width $\sigma$ and outcome $y$ has
Kraus operator $M_y$ acting on wavefunctions by multiplication with
$(2\pi\sigma^2)^{-1/4}e^{-(x-y)^2/(4\sigma^2)}$; forgetting the outcome gives the
channel $\rho\mapsto\int M_y\rho M_y^\dagger\,dy$. Write $W(q,p)$ for the Wigner
function of $\rho$.

**Proposition 1.** The forgotten record acts as
$\rho(x,x')\mapsto\rho(x,x')\,e^{-(x-x')^2/(8\sigma^2)}$, that is,

$$W(q,p)\ \mapsto\ \int W(q,p-p')\,\frac{e^{-p'^2/(2v)}}{\sqrt{2\pi v}}\,dp',
\qquad v=\frac{\hbar^2}{4\sigma^2}.$$

The position marginal is unchanged; the momentum marginal is convolved
with a centred Gaussian of variance $v$.

*Proof.* $\int M_y(x)M_y(x')\,dy=(2\pi\sigma^2)^{-1/2}\int
e^{-[(x-y)^2+(x'-y)^2]/(4\sigma^2)}dy=e^{-(x-x')^2/(8\sigma^2)}$. With
$s=x-x'$ and $W(q,p)=(2\pi\hbar)^{-1}\int\rho(q+\frac s2,q-\frac s2)e^{-ips/\hbar}ds$,
multiplication by $e^{-s^2/(8\sigma^2)}$ is convolution in $p$ with the Gaussian
whose characteristic function in $s/\hbar$ is $e^{-s^2/(8\sigma^2)}$, of variance
$v$ with $v/(2\hbar^2)=1/(8\sigma^2)$. The factor equals one on the diagonal
$s=0$, so the position marginal is unchanged. $\square$

The record's error is $\sigma$ and its delivered impulse has spread $\sqrt v$;
their product is $\hbar/2$, the saturated mark cost of the Planck paper's
Theorem 4.

## 2. Composition

**Parallel.** Two forgotten records at one instant multiply the density
matrix by $e^{-s^2/(8\sigma_1^2)}e^{-s^2/(8\sigma_2^2)}=e^{-s^2(\sigma_1^{-2}+\sigma_2^{-2})/8}$: one
record with $\sigma^{-2}=\sigma_1^{-2}+\sigma_2^{-2}$. Precisions add like conductances,
and the momentum variances add. This is the Newtonian counterpart of
two parallel faces at heat time $2t$ combining into one at $t$ (the
series/parallel note, §3).

**Series.** Between records at different times the body evolves freely
or under constant force, an affine symplectic map on $W$; a momentum
convolution at one time becomes a sheared convolution in $(q,p)$ at a
later time. The channels compose exactly, because Gaussian convolutions
and affine symplectic maps form a closed family.

**Corollary 2 (refinement with records).** Put a record of width $\sigma_j$
at each vertex of a partition of $[0,T]$. The forgotten records convolve
the final momentum distribution with a Gaussian of variance
$\frac{\hbar^2}4\sum_j\sigma_j^{-2}$ (the shear adds a position spread of the same
order in $T$ and changes nothing below). The limit of refinement exists
iff $\sum_j\sigma_j^{-2}$ converges. The records' information about the place,
measured by the Fisher information $\sum_j\sigma_j^{-2}$ for a static position,
converges on the same condition. With $\sigma_j^{-2}=\kappa\tau_j$ the sum is $\kappa T$:
individual records become coarse as the mesh shrinks, and the rate
$\kappa$ and the momentum diffusion rate $\hbar^2\kappa/4$ survive the limit. This is
the continuous position measurement of Caves and Milburn.

*Proof.* The multiplicative factors of Proposition 1 at one instant
multiply; free evolution between vertices is an affine symplectic map,
which carries Gaussian convolutions to Gaussian convolutions without
changing the momentum variance of a convolution applied before it. The
momentum variances therefore add. $\square$

## 3. What the Newton row of the atlas now says

- **Series move** (unobserved insertion): exact after one scalar
  counterterm, at every $\hbar$.
- **Parallel move** (forgotten record): a momentum convolution of
  variance $\hbar^2/(4\sigma^2)$. It is the identity for $\hbar=0$, as a gauge
  theory with no transverse planes has no parallel defect.
- **What survives refinement with records:** the information rate $\kappa$
  and the diffusion rate $\hbar^2\kappa/4$, with fixed product per record.
  This is the Newtonian form of the atlas's error budget: summable
  records, like summable parallel defects, give a limit, and the ratio
  that survives is set by the one action constant.

## 4. Consequence for STATE

Atlas cell 6 is filled for Gaussian records: forgetting a record is an
exact parallel move whose defect is proportional to $\hbar^2$, which makes
joint determinacy the statement that Newton's refinement has no
parallel defect. The general, non-Gaussian record is covered by the
Planck paper's Theorem 6 and by Theorem E of the fifth-postulate note.
