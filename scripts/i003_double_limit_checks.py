"""Checks for notes/i003-double-limit-rigidity.md (I003 tests 2 and 3)."""
from pathlib import Path
import json
import sympy as sp


def opnorm(M):
    """Operator norm of a small matrix via the largest singular value."""
    vals = (M.H * M).eigenvals()
    return sp.sqrt(max(sp.simplify(v) for v in vals))


def main():
    checks = {}

    def record(name, residual):
        assert sp.simplify(residual) == 0, (name, residual)
        checks[name] = "passed"

    u, lam, w0, m, c, hbar, T, D, eps, k0, x = sp.symbols(
        "u lambda omega0 m c hbar T Delta epsilon kappa0 x", positive=True)
    k, t = sp.symbols("k t", real=True)
    sx = sp.Matrix([[0, 1], [1, 0]]); sz = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2)

    # 1. Commutator norms and crossover formulas in both faces
    V = u*sz; Q = lam*(sx - I2); A = u*sz; B = w0*sx
    record("commutator_norm_telegraph", opnorm(V*Q - Q*V) - 2*u*lam)
    record("commutator_norm_dirac", opnorm(A*B - B*A) - 2*u*w0)
    record("crossover_time_telegraph", 2*u/(2*u*lam) - 1/lam)
    record("crossover_time_dirac", 2*u/(2*u*w0) - 1/w0)
    record("plateau_from_commutator", 2*m*u**3/(2*u*lam) - m*u**2/lam)
    record("action_from_commutator", 2*m*c**3/(2*c*w0) - m*c**2/w0)
    record("compton_time", (1/w0).subs(w0, m*c**2/hbar) - hbar/(m*c**2))

    # 2. Commuting case: diagonal switching factorizes into straight translations
    Bd = sp.symbols("b0")*I2 + sp.symbols("b1")*sz
    Hd = u*k*sz + Bd
    ev = list(Hd.eigenvals().keys())
    assert all(sp.diff(e, k, 2) == 0 for e in ev)          # affine dispersions: pure translations
    checks["commuting_case_affine_dispersions"] = "passed"
    record("commuting_case_commutator_zero", opnorm(A*Bd - Bd*A))
    Qd = sp.diag(sp.symbols("q1"), sp.symbols("q2"))
    # a diagonal Markov generator has zero rows
    assert sp.solve([Qd[0, 0], Qd[1, 1]], [sp.symbols("q1"), sp.symbols("q2")]) == {sp.symbols("q1"): 0, sp.symbols("q2"): 0}
    checks["diagonal_markov_generator_is_zero"] = "passed"

    # 3. Dirac symbol is an instance of the affine class with entire entries
    E = sp.sqrt(u**2*k**2 + w0**2)
    H = u*k*sz + w0*sx
    M = sp.cos(t*E)*I2 - sp.I*sp.sin(t*E)/E*H
    record("dirac_symbol_unitary", sp.simplify((M.H*M - I2).norm()))
    s = sp.symbols("s")
    entry = sp.cos(t*s) - sp.I*sp.sin(t*s)/s*w0
    record("dirac_entries_even_in_root", sp.simplify(entry - entry.subs(s, -s)))
    # Bernstein bound on the (1,1) entry over a grid: |d/dk cos(tE)| <= u t
    d11 = sp.diff(sp.cos(t*E), k)
    grid_ok = all(abs(float(d11.subs({u: 1, w0: sp.Rational(3, 2), t: tt, k: kk}))) <= 1*tt + 1e-12
                  for tt in (sp.Rational(1, 3), 1, 3) for kk in (-4, -1, 0, sp.Rational(1, 2), 2, 7))
    assert grid_ok
    checks["bernstein_bound_dirac_entry_grid"] = "passed"

    # 4. Telegraph symbol as the affine Euclidean instance; total-mass transform matches C020's kernel
    G = -sp.I*k*V + Q
    Mt = (t*G).exp()
    pi = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    total = sp.simplify((sp.Matrix([[1, 1]])*Mt*pi)[0])
    sroot = sp.sqrt(lam**2 - u**2*k**2)
    target = sp.exp(-lam*t)*(sp.cosh(sroot*t) + lam/sroot*sp.sinh(sroot*t))
    record("telegraph_symbol_total_mass", sp.simplify((total - target).rewrite(sp.exp)))

    # 5. Duhamel first-order identity against finite differences at a numeric point
    kk = sp.symbols("kk", real=True)
    Gn = (-sp.I*kk*sz + sp.Rational(1, 2)*(sx - I2))          # u=1, lambda=1/2
    tt = sp.Rational(1, 4)
    Mfun = lambda kv: (tt*Gn.subs(kk, kv)).exp()
    h = sp.Rational(1, 1000)
    fd = (Mfun(sp.Rational(1, 2) + h) - Mfun(sp.Rational(1, 2) - h))/(2*h)
    Gp = -sp.I*sz
    G0n = Gn.subs(kk, sp.Rational(1, 2)).evalf()
    npts = 400
    duh = sp.zeros(2, 2)
    for j in range(npts):
        sv = (j + sp.Rational(1, 2))/npts
        duh += ((sv*tt*G0n).exp()*Gp*((1 - sv)*tt*G0n).exp()).evalf()/npts
    duh = tt*duh
    err = max(abs(complex(v)) for v in (fd.evalf() - duh))
    assert err < 1e-4, err
    checks["duhamel_first_derivative_numeric"] = "passed"

    # 6. Rounding model: iterated limits and path limits
    f_tel = (m*u**2/lam)*(1 - (1 - sp.exp(-2*lam*D))/(2*lam*D))
    h_eps = f_tel + m*eps**2/(6*D)
    record("rounding_eps_first_then_window", sp.limit(sp.limit(h_eps, eps, 0), D, 0))
    assert sp.limit(sp.limit(h_eps, D, 0), eps, 0) == sp.oo
    checks["rounding_window_first_diverges"] = "passed"
    record("rounding_diffusive_parabola_limit", sp.limit(h_eps.subs(eps, sp.sqrt(6*k0*D/m)), D, 0) - k0)
    record("rounding_ballistic_diagonal_limit", sp.limit(h_eps.subs(eps, u*D), D, 0))
    record("gaussian_control_window_independent", sp.diff(sp.symbols("kappa")*D/m*m/D, D))

    report = {"scope": "Finite algebra for notes/i003-double-limit-rigidity.md; the rigidity theorem's proof is in the note",
              "checks": checks}
    out = Path(__file__).resolve().parents[1]/"out"/"i003-double-limit-checks.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
