"""Exact checkerboard identities and finite-mode tests; proofs in the note."""
from pathlib import Path
import itertools
import json
import numpy as np
import sympy as s


def main():
    r, eps, omega, lam, p, c, m, K = s.symbols(
        "r eps omega lam p c m K", positive=True)
    I, X, Z = s.eye(2), s.Matrix([[0, 1], [1, 0]]), s.diag(1, -1)
    W = s.Matrix([[0, 1], [-s.I, 0]])
    C = (I-s.I*r*X)/s.sqrt(1+r*r)
    B = s.Matrix([[1, r], [-r, 1]])/s.sqrt(1+r*r)
    P = (1-lam*eps)*I+lam*eps*X
    H = c*p*Z+m*c*c*X
    continued = (1+s.I*r)*I-s.I*r*X
    plus, minus = s.Matrix([1, 1]), s.Matrix([1, -1])
    residuals = {
        "unitary_coin": C.H*C-I,
        "unitary_basis": W.H*W-I,
        "source_coin_basis": W*B*W.H-C,
        "source_shift_basis": W*Z*W.H+Z,
        "probability_column_sum": s.ones(1, 2)*P-s.ones(1, 2),
        "probability_generator": P.diff(eps).subs(eps, 0)-lam*(X-I),
        "coherent_generator": C.subs(r, omega*eps).diff(eps).subs(eps, 0)+s.I*omega*X,
        "dirac_square": H*H-(c*c*p*p+m*m*c**4)*I,
        "continued_symmetric_norm": (continued.H*continued-I)*plus,
        "continued_antisymmetric_norm": (continued.H*continued-(1+4*r*r)*I)*minus,
        "flip_probability": s.conjugate(C[0, 1])*C[0, 1]-r*r/(1+r*r),
        "measured_rate_limit": s.limit(omega**2*eps/(1+omega**2*eps**2), eps, 0),
        "nonrelativistic_dispersion": s.limit(s.sqrt(m*m*c**4+p*p*c*c)-m*c*c, c, s.oo)-p*p/(2*m),
        "heat_coefficient": c*c/(2*m*c*c/K)-K/(2*m),
    }
    for name, residual in residuals.items():
        values = list(residual) if isinstance(residual, s.MatrixBase) else [residual]
        assert all(s.simplify(v) == 0 for v in values), name

    # Direct corner enumeration versus successive coin-and-shift operations.
    # Start after a compulsory right step, matching the source normalization.
    rv = s.Rational(1, 2)
    coin = C.subs(r, rv)
    paths_checked = 0
    for n in range(1, 8):
        expected = {}
        for tail in itertools.product((1, -1), repeat=n-1):
            directions = (1,)+tail
            turns = sum(a != b for a, b in zip(directions, directions[1:]))
            key = (sum(directions), directions[-1])
            amplitude = (-s.I*rv)**turns/(1+rv*rv)**s.Rational(n-1, 2)
            expected[key] = expected.get(key, 0)+amplitude
        state = {(1, 1): s.Integer(1)}
        for _ in range(n-1):
            nxt = {}
            for (x, direction), amplitude in state.items():
                for newdir in (1, -1):
                    key = (x+newdir, newdir)
                    factor = coin[0 if newdir == 1 else 1, 0 if direction == 1 else 1]
                    nxt[key] = nxt.get(key, 0)+factor*amplitude
            state = nxt
        assert state.keys() == expected.keys()
        assert all(s.simplify(state[key]-expected[key]) == 0 for key in state)
        assert s.simplify(sum(s.conjugate(a)*a for a in state.values())) == 1
        paths_checked += 2

    Xn, Zn = np.array(X, dtype=complex), np.array(Z, dtype=complex)
    mode_tests = []
    for pv in (0., .7, 3.):
        # Dimensionless m=c=K=T=1; fixed momenta, varying mesh.
        hn = pv*Zn+Xn
        energy = np.sqrt(1+pv*pv)
        target = np.cos(energy)*np.eye(2)-1j*np.sin(energy)*hn/energy
        errors = []
        for N in (32, 64, 128, 256):
            dt = 1/N
            shift = np.diag(np.exp(-1j*pv*dt*np.array([1, -1])))
            step = shift @ ((np.eye(2)-1j*dt*Xn)/np.sqrt(1+dt*dt))
            errors.append(float(np.linalg.norm(np.linalg.matrix_power(step, N)-target)))
        assert all(b < a for a, b in zip(errors, errors[1:]))
        assert errors[-1] < .02
        mode_tests.append({"momentum": pv, "N": [32, 64, 128, 256], "errors": errors})
    report = {"scope": "Finite checks support, rather than certify, the written strong-limit proof",
              "algebra_checks": {name: "passed" for name in residuals},
              "path_and_norm_checks": paths_checked, "mode_tests": mode_tests}
    target = Path(__file__).resolve().parents[1]/"out"/"checkerboard-checks.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
