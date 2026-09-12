# R33 stage 1 review

C122 accepts the conditional-fibre suppression bound and inverse expansion.
It leaves the mechanical coefficient and global risk classification open.

1. The report admits a fixed scalar line C-C_*=alpha L e_y, with three
   exact complementary constraints. Fixed normalization makes epsilon/ lambda
   the correct interval bound. Independent component tolerances are a different
   domain.
2. The exact reference and inverse chart give w_0(s)=s e_y and
   w_lambda(0)=0. R32's uniform inverse image neighbourhood applies to this
   line after choosing a smaller interval. The physical box remains fixed.
3. Bounded mixed derivatives yield partial_s w_lambda=e_y+O(lambda).
   Integration from s=0 preserves the |s| factor; scalar extrema then give
   the conditional risk upper bound. Hidden-y extent persists as lambda
   tends to zero at fixed epsilon.
4. N=lambda Lw+lambda^2 V(w)+... implies the inverse coefficient
   -L^{-1}V(s e_y), with V=partial_lambda^2 N/2. A C^1-in-s Taylor
   remainder anchored at zero yields O(lambda^2 |s|).
5. If both entries of b'(0) are nonzero, continuity and endpoint integration
   give the product lower bound with factor 1/4. This is a conditional theorem,
   not a verified nonvanishing assertion for the mechanics.
6. All radii refer to this compact common-record segment. Their upper bound
   does not upper-bound full-class minimax risk. The source audit and revised
   restart task retain that quantifier.

Written derivation and source review only; no numerical/symbolic scripts.
