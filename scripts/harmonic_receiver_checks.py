"""Exact A10 modal, receiver and finite-window checks."""
import json
from pathlib import Path
import sympy as s


def main():
    m, mr, k, E, w, T, t = s.symbols('m mr k E omega T t', positive=True)
    phi = s.symbols('phi', real=True)
    mu = m*mr/(m+mr)
    q = s.sqrt(2*E)/w*s.cos(w*t+phi)
    p = s.diff(q,t)
    avg = lambda x: s.integrate(s.expand_trig(x), (phi,0,2*s.pi))/(2*s.pi)
    cov = s.simplify(avg(p*p.subs(t,0)))
    variance = s.simplify(avg((q.subs(t,T)-q.subs(t,0))**2))
    integ = s.integrate((T-t)*s.cos(w*t),(t,0,T))
    pair = 2*m*E/k/T*(mr/(m+mr))**2*(1-s.cos(w*T))
    via_mode = m/T*(mr/(m+mr))**2*variance/mu
    residuals = {
        'mode_equation': s.diff(q,t,2)+w*w*q,
        'mode_energy': (p*p+w*w*q*q)/2-E,
        'stationary_covariance': cov-E*s.cos(w*t),
        'phase_displacement': variance-2*E/w**2*(1-s.cos(w*T)),
        'covariance_integral': integ-(1-s.cos(w*T))/w**2,
        'two_body_coefficient': via_mode.subs(w,s.sqrt(k/mu))-pair.subs(w,s.sqrt(k/mu)),
        'short_window_coefficient': s.limit(m*variance/T**2,T,0)-m*E,
        'centre_kinetic_split': m*(mr/(m+mr))**2+mr*(m/(m+mr))**2-mu,
    }
    for name, residual in residuals.items():
        assert s.trigsimp(s.simplify(residual)) == 0, name
    # Explicit equal-mass connected three-body spring chain, unit masses/springs.
    K = s.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
    U = s.Matrix.hstack(s.ones(3,1)/s.sqrt(3),
                       s.Matrix([1,0,-1])/s.sqrt(2),
                       s.Matrix([1,-2,1])/s.sqrt(6))
    assert U.T*U == s.eye(3)
    assert s.simplify(U.T*K*U) == s.diag(0,1,3)
    weights = [s.Rational(1,2),s.Rational(1,6)]  # E_1=E_2=1, tag 1
    B = weights[0]+weights[1]/3
    assert B == s.Rational(5,9)
    # Cosines are in [-1,1], so these exact extremal phase assignments test bound.
    for c1,c2 in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        numerator = 2*(weights[0]*(1-c1)+weights[1]/3*(1-c2))
        assert 0 <= numerator <= 4*B
    report = {'symbolic_identities': list(residuals),
              'three_body_checks': 3, 'cosine_bound_cases': 4,
              'scope': '15 finite checks supporting written general proofs'}
    target = Path(__file__).resolve().parents[1]/'out'/'harmonic-receiver-checks.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
