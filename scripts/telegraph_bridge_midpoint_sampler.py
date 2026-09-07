"""Exact sampler of the C033 velocity-resolved telegraph return bridge.

Samples the odd switch count from w_k = (z/2)^{2k} / [(k!)^2 I_0(z)], z = lambda T,
then independent uniform simplexes of positive and negative durations, and
evaluates the midpoint Y = X_{T/2}. Prints the variance coefficient
4 m Var(Y)/T relative to H_* = m u^2/lambda, its leading law z^3/6, the
second-moment coefficient 2 m E[Y^2]/T and the midpoint atom mass.
Optional diagnostic; it is outside `make check`. Requires numpy.
"""
import argparse
import math
import numpy as np


def bessel_i0(z, terms=80):
    return sum((z/2)**(2*k)/math.factorial(k)**2 for k in range(terms))


def sample(lam, T, n, rng, m=1.0, u=1.0, kmax=60):
    z = lam*T
    ks = np.arange(kmax)
    w = np.array([(z/2)**(2*k)/math.factorial(k)**2 for k in ks])/bessel_i0(z)
    w /= w.sum()
    K = rng.choice(ks, size=n, p=w)
    Y = np.empty(n)
    for i, k in enumerate(K):
        pos = rng.dirichlet(np.ones(k + 1))*T/2
        neg = rng.dirichlet(np.ones(k + 1))*T/2
        d = np.empty(2*k + 2)
        d[0::2], d[1::2] = pos, neg
        v = u*(-1.0)**np.arange(2*k + 2)
        ends = np.cumsum(d)
        occupation = np.clip(np.minimum(ends, T/2) - (ends - d), 0, None)
        Y[i] = np.sum(v*occupation)
    return 4*m*Y.var()/T, 2*m*(Y**2).mean()/T, np.isclose(Y, u*T/2).mean()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=200000)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    print("   z   kappa_mid/H*     z^3/6   2mE[Y^2]/T    atom   1/I0(z)")
    for z in [0.25, 0.5, 1, 2, 4, 8, 16, 32]:
        kv, km, atom = sample(1.0, z, args.n, rng)
        print(f"{z:5.2f}   {kv:9.5f}   {z**3/6:9.5f}   {km:8.4f}   {atom:.4f}   {1/bessel_i0(z):.4f}")


if __name__ == "__main__":
    main()
