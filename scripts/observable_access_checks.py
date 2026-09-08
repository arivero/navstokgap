"""Exact finite checks for G02; general statements are proved in the note."""
import json
from pathlib import Path
import sympy as s


def main():
    lam, eps, u, m, d = s.symbols('lambda epsilon u m delta', positive=True)
    inv = s.diag(1/(2*lam), 1/(2*eps), 1/(2*(lam+eps)))
    frame = s.diag(u*u, u*u*d*d, u*u*d*d)
    v = s.Matrix([u/s.sqrt(2), u*d/s.sqrt(2), 0])
    total = s.trace(inv*frame)
    plateau = (2*m*v.T*inv*v)[0].subs(eps, lam*d*d)
    residuals = {
        'plateau': plateau-m*u*u/lam,
        'total_response': total.subs(eps, lam*d*d)-u*u/lam*(1+d*d/(2*(1+d*d))),
        'response_limit': s.limit(total.subs(eps, lam*d*d), d, 0)-u*u/lam,
        'gap_limit': s.limit(2*lam*d*d, d, 0),
        'frame_limit': s.limit(u*u*d*d, d, 0),
        'readout_gain': 2*u/(s.sqrt(2)*u*d)-s.sqrt(2)/d,
    }
    for key, value in residuals.items():
        assert s.simplify(value) == 0, key
    cases = []
    for dv in [s.Rational(1,4), s.Rational(1,10), s.Rational(1,100)]:
        velocities = [s.simplify((a+dv*b)/s.sqrt(2)) for a in [-1,1] for b in [-1,1]]
        assert len(set(velocities)) == 4
        assert all(x*x < 1 for x in velocities)
        sv = total.subs({u:1, lam:1, eps:dv*dv, d:dv})
        assert 0 < dv*dv/sv <= 2*dv*dv
        cases.append(str(dv))
    # Construct actual N-factor generators, keeping clocks per constituent.
    products = []
    flip = s.Matrix([[-1,1],[1,-1]])
    for n in (2,3,4):
        q = s.zeros(2**n)
        for j in range(n):
            q += s.kronecker_product(*[flip if k == j else s.eye(2) for k in range(n)])
        spectrum = (-q).eigenvals()
        assert spectrum[0] == 1
        assert min(x for x in spectrum if x > 0) == 2
        assert min(x/n for x in spectrum if x > 0) == s.Rational(2,n)
        products.append(n)
    # In the two-factor centered eigenbasis, local readouts miss the mixed mode.
    local_frame = s.diag(1,1,0)
    assert local_frame.rank() == 2
    assert local_frame*s.Matrix([0,0,1]) == s.zeros(3,1)
    report = {'symbolic_identities': list(residuals), 'injective_velocity_cases': cases,
              'product_sizes': products, 'local_frame_checks': 2,
              'scope': 'Six identities, three rational cases, three product spectra, two frame checks'}
    target = Path(__file__).resolve().parents[1]/'out'/'observable-access-checks.json'
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
