"""Finite identities for the supplied polygon proposals and centre limit."""
from pathlib import Path
import json
import sympy as sp


def main():
    m,F,v,R,t,w,tau = sp.symbols("m F v R t w tau",positive=True)
    x,y = v*sp.sin(w*t)/w, R*(1-sp.cos(w*t))
    area_rate = (x*sp.diff(y,t)-(y-R)*sp.diff(x,t))/2
    lens = F*v*tau**3/(12*m)
    xp,yp = v*t,F*t**2/(2*m)
    n,A,hb = sp.symbols("n A hb",positive=True)
    energy=-A/n**2
    period=2*sp.pi*hb/sp.diff(energy,n)
    checks={
        "central_x_equation": sp.diff(x,t,2)+w**2*x,
        "central_y_equation": sp.diff(y,t,2)-w**2*(R-y),
        "constant_sector_rate": sp.trigsimp(area_rate-R*v/2),
        "parabolic_finite_part": sp.integrate((xp*sp.diff(yp,t)-yp*sp.diff(xp,t))/2,(t,0,tau))-lens,
        "tangent_arc_area": sp.integrate(yp*v,(t,0,tau))-2*lens,
        "triangle_decomposition": (F*v*tau**3/(4*m)-lens)-2*lens,
        "receding_chord_limit": sp.limit(F*v/(2*m*w**2)*(tau-sp.sin(w*tau)/w),w,0)-lens,
        "endpoint_correction_limit": sp.limit(F/(2*m*w**2)*(v*sp.sin(w*tau)/w-v*tau),w,0)+lens,
        "action_normalization": F*lens/(2*v)-F**2*tau**3/(24*m),
        "work_normalization": 6*F*lens/v-tau*(F*tau)**2/(2*m),
        "adjacent_level_ratio": (energy.subs(n,n+1)-energy)*period/(2*sp.pi*hb)-n*(2*n+1)/(2*(n+1)**2),
        "cell_counterexample": ((n+sp.Rational(1,2))*hb)*(2*sp.pi/n)-2*sp.pi*hb*(1+1/(2*n)),
    }
    for name,residual in checks.items():
        if sp.simplify(residual)!=0:
            raise AssertionError(f"{name}: {residual}")
    report={"scope":"Exact identities; limit interpretation and premise audit are in the note",
            "checks":{k:"passed" for k in checks}}
    target=Path(__file__).resolve().parents[1]/"out"/"receding-centre-checks.json"
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
