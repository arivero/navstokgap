"""Exact checks for the composition, crossover and gap-product calculations.

Supports A08/A09/G01 as described in notes/composition-crossover-gap-checks.md.
All checks are symbolic residuals; the general statements are proved in the note.
"""
from pathlib import Path
import json
import sympy as sp

R = sp.Rational


def plateau(Q, pi, v, mass):
    """H_* = 2 m <v, (-Q)^{-1} v>_pi on mean-zero functions (C019)."""
    n = len(v)
    f = sp.symbols(f"f0:{n}")
    eqs = list(-sp.Matrix(Q)*sp.Matrix(f) - sp.Matrix(v))
    eqs.append(sum(pi[i]*f[i] for i in range(n)))
    sol = sp.solve(eqs, f, dict=True)[0]
    return sp.simplify(2*mass*sum(pi[i]*v[i]*sol[f[i]] for i in range(n)))


def reversible_chain(pi, sym, vel):
    """Generator Q_ij = S_ij pi_j for symmetric S; velocities centred under pi."""
    k = len(pi)
    Q = [[sp.Integer(0)]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i != j:
                Q[i][j] = sp.Integer(sym[i][j])*pi[j]
        Q[i][i] = -sum(Q[i][j] for j in range(k) if j != i)
    mean = sum(p*v for p, v in zip(pi, vel))
    return Q, [sp.Integer(v)-mean for v in vel]


def product_chain(Q1, Q2):
    idx = [(i, j) for i in range(len(Q1)) for j in range(len(Q2))]
    Q = [[sp.Integer(0)]*len(idx) for _ in idx]
    for a, (i, j) in enumerate(idx):
        for b, (p, q) in enumerate(idx):
            if j == q and i != p:
                Q[a][b] += Q1[i][p]
            if i == p and j != q:
                Q[a][b] += Q2[j][q]
        Q[a][a] = Q1[i][i] + Q2[j][j]
    return Q, idx


def main():
    checks = {}

    def record(name, residual):
        assert sp.simplify(residual) == 0, (name, residual)
        checks[name] = "passed"

    m1, m2, m3, m, u, lam, eps, T, Delta, s, nu, Mb, ma, mb = sp.symbols(
        "m1 m2 m3 m u lambda epsilon T Delta s nu M_b m_a m_b", positive=True)
    k1, k2, k3, c, hbar, p, kappa, x, omega = sp.symbols(
        "kappa1 kappa2 kappa3 c hbar p kappa x omega", positive=True)
    t = sp.symbols("t", real=True)

    # --- 1. composition inside the A01 class -------------------------------
    pi1 = [R(1, 2), R(1, 3), R(1, 6)]
    pi2 = [R(1, 4), R(1, 4), R(1, 2)]
    Q1, v1 = reversible_chain(pi1, [[0, 1, 2], [1, 0, 3], [2, 3, 0]], [3, -1, 2])
    Q2, v2 = reversible_chain(pi2, [[0, 2, 1], [2, 0, 1], [1, 1, 0]], [-2, 1, 1])
    for Q, pi in ((Q1, pi1), (Q2, pi2)):
        assert all(pi[i]*Q[i][j] == pi[j]*Q[j][i] for i in range(3) for j in range(3))
    H1, H2 = plateau(Q1, pi1, v1, m1), plateau(Q2, pi2, v2, m2)
    Qp, idx = product_chain(Q1, Q2)
    pip = [pi1[i]*pi2[j] for (i, j) in idx]
    M = m1 + m2
    vcm = [(m1*v1[i] + m2*v2[j])/M for (i, j) in idx]
    vrel = [v1[i] - v2[j] for (i, j) in idx]
    Hcm = plateau(Qp, pip, vcm, M)
    Hrel = plateau(Qp, pip, vrel, m1*m2/M)
    record("composition_centre_mass_weighted_mean", Hcm - (m1*H1 + m2*H2)/M)
    record("composition_relative_complementary_weights", Hrel - (m2*H1 + m1*H2)/M)
    record("composition_sum_rule", Hcm + Hrel - H1 - H2)

    states = [(m1*a + m2*b)*u/M for a in (1, -1) for b in (1, -1)]
    targets = [u, -u, u*(m1 - m2)/M, -u*(m1 - m2)/M]
    assert all(any(sp.simplify(st - tg) == 0 for st in states) for tg in targets)
    checks["composite_centre_velocity_states"] = "passed"

    ms, ks = [m1, m2, m3], [k1, k2, k3]

    def coeff(cv):
        w = [ci**2/mi for ci, mi in zip(cv, ms)]
        return sp.simplify(sum(wi*ki for wi, ki in zip(w, ks))/sum(w))

    jac = [coeff([1, -1, 0]),
           coeff([-m1/(m1 + m2), -m2/(m1 + m2), 1]),
           coeff([m1/(m1 + m2 + m3), m2/(m1 + m2 + m3), m3/(m1 + m2 + m3)])]
    record("jacobi_centre_mass_weighted", jac[2] - (m1*k1 + m2*k2 + m3*k3)/(m1 + m2 + m3))
    record("jacobi_sum_rule", sum(jac) - (k1 + k2 + k3))
    record("jacobi_common_kappa_preserved",
           sum(sp.simplify(cc.subs({k1: s, k2: s, k3: s}) - s) for cc in jac))
    covRr = (m1/M)*(k1*Delta/m1) - (m2/M)*(k2*Delta/m2)
    record("cross_covariance_centre_relative", covRr - Delta*(k1 - k2)/M)

    kap1, kap2, kap3 = sp.symbols("kap1 kap2 kap3")
    sol = sp.solve([sp.Eq(3*kap3, kap1 + 2*kap2), sp.Eq(3*kap3, 3*kap1)], [kap2, kap3])
    record("additive_function_split_step", sol[kap2] - kap1)

    def bath(mm):
        return (mm + Mb)*s**2/nu

    record("bath_composition_violation",
           bath(ma + mb) - (ma*bath(ma) + mb*bath(mb))/(ma + mb)
           - 2*ma*mb*s**2/(nu*(ma + mb)))

    # --- 2. crossover window and conditioned midpoint -----------------------
    Dstar = kappa/(m*u**2)
    record("crossover_window_equality", (kappa*Delta/m - u**2*Delta**2).subs(Delta, Dstar))
    below = (kappa*Delta/m - u**2*Delta**2).subs(Delta, Dstar/2)
    assert sp.simplify(below - kappa**2/(4*m**2*u**2)) == 0 and below.is_positive
    checks["crossover_window_violation_below"] = "passed"

    f = 1 - (1 - sp.exp(-2*x))/(2*x)
    record("telegraph_bound_series", sp.series(x - f, x, 0, 3).removeO() - 2*x**2/3)
    assert all(float((x - f).subs(x, val)) >= 0 for val in [R(1, 100), R(1, 10), R(1, 2), 1, 2, 5, 20])
    checks["telegraph_bound_grid"] = "passed"

    a, b = sp.symbols("a b", nonnegative=True)
    half = T/2
    Y_hi, Y_lo = u*(2*a - half), u*(half - 2*b)
    dens = 1/half**2

    def E1(fhi, flo):
        hi = sp.integrate(sp.integrate(fhi*dens, (b, half - a, half)), (a, 0, half))
        lo = sp.integrate(sp.integrate(flo*dens, (b, 0, half - a)), (a, 0, half))
        return sp.simplify(hi + lo)

    EY1 = E1(Y_hi, Y_lo)
    EY21 = E1(Y_hi**2, Y_lo**2)
    Edev1 = E1((Y_hi - u*half)**2, (Y_lo - u*half)**2)
    record("bridge_k1_mean", EY1 - u*T/6)
    record("bridge_k1_second_moment", EY21 - u**2*T**2/12)
    record("bridge_k1_deviation", Edev1 - u**2*T**2/6)

    z = sp.symbols("z", positive=True)
    I0 = 1 + z**2/4 + z**4/64
    w0, w1 = 1/I0, (z/2)**2/I0
    EY = w0*u*half + w1*EY1
    EY2 = w0*(u*half)**2 + w1*EY21
    VarY = sp.series(sp.expand(EY2 - EY**2), z, 0, 4).removeO()
    kmid = sp.simplify(4*m*VarY/T)
    record("bridge_leading_cubic_onset", kmid.subs(z, lam*T) - (m*u**2/lam)*(lam*T)**3/6)
    record("bridge_second_moment_limit", sp.limit(2*m*EY2/T, z, 0) - m*u**2*T/2)

    # --- 3. gap product and slow modes -------------------------------------
    for name, (Q, pi, v, mass) in {"chain1": (Q1, pi1, v1, m1), "chain2": (Q2, pi2, v2, m2)}.items():
        eig = [complex(e).real for e in (-sp.Matrix(Q)).eigenvals()]
        gmin = min(e for e in eig if e > 1e-9)
        gmax = max(eig)
        H = float(plateau(Q, pi, v, mass).subs(mass, 1))
        sig2 = float(sum(pi[i]*v[i]**2 for i in range(3)))
        assert H*gmin <= 2*sig2 + 1e-9 and 2*sig2 <= H*gmax + 1e-9, (name, H*gmin, 2*sig2, H*gmax)
        checks[f"gap_product_bounds_{name}"] = "passed"
    Q2s = [[-lam, lam], [lam, -lam]]
    record("gap_two_state_equality", plateau(Q2s, [R(1, 2)]*2, [u, -u], m)*2*lam - 2*m*u**2)

    labels = [(sg, lb) for sg in (0, 1) for lb in (0, 1)]
    Qs = [[sp.Integer(0)]*4 for _ in range(4)]
    for i, (sg, lb) in enumerate(labels):
        for j, (sg2, lb2) in enumerate(labels):
            if sg != sg2 and lb == lb2:
                Qs[i][j] = lam
            if sg == sg2 and lb != lb2:
                Qs[i][j] = eps
        Qs[i][i] = -(lam + eps)
    Hslow = plateau(Qs, [R(1, 4)]*4, [u*(-1)**sg for (sg, lb) in labels], m)
    record("slow_mode_plateau_unchanged", Hslow - m*u**2/lam)
    eig = {sp.simplify(e) for e in (-sp.Matrix(Qs)).eigenvals()}
    assert all(any(sp.simplify(e - tg) == 0 for e in eig) for tg in (0, 2*eps, 2*lam, 2*lam + 2*eps))
    checks["slow_mode_gap_min_2eps_2lam"] = "passed"

    record("dirac_branch_gap", 2*sp.sqrt(p**2*c**2 + m**2*c**4).subs(p, 0) - 2*m*c**2)
    record("generator_gap_energy_units", hbar*2*(m*c**2/hbar) - 2*m*c**2)

    # --- 4. analytic continuation of the telegraph equation ------------------
    psi = sp.Function("psi")(x, t)
    U = sp.exp(-sp.I*omega*t)*psi
    tele = sp.diff(U, t, 2) + 2*sp.I*omega*sp.diff(U, t) - c**2*sp.diff(U, x, 2)
    kg = sp.diff(psi, t, 2) + omega**2*psi - c**2*sp.diff(psi, x, 2)
    record("continuation_phase_route", tele - sp.exp(-sp.I*omega*t)*kg)
    phi = sp.Function("phi")(x, t)
    P = sp.exp(-lam*t)*phi
    tele_r = sp.diff(P, t, 2) + 2*lam*sp.diff(P, t) - c**2*sp.diff(P, x, 2)
    record("continuation_real_route",
           tele_r - sp.exp(-lam*t)*(sp.diff(phi, t, 2) - c**2*sp.diff(phi, x, 2) - lam**2*phi))

    report = {"scope": "Finite algebra and fixed-chain instances; general proofs in notes/composition-crossover-gap-checks.md",
              "checks": checks}
    output = Path(__file__).resolve().parents[1]/"out"/"six-direction-checks.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
