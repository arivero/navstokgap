"""Exact finite checks supporting the bounded-acceleration return proofs."""
from pathlib import Path
import json
import sympy as s


def main():
    m,u,a,w,t,d,r,b,F=s.symbols('m u a w t d r b F', positive=True)
    tau=u/a
    T=2*tau+w
    v0=u-a*t
    v1=-a*(t-T+tau)
    total=s.integrate(v0,(t,0,tau))+s.integrate(v1,(t,T-tau,T))
    cost=m/2*(s.integrate(v0**2,(t,0,tau))+s.integrate(v1**2,(t,T-tau,T)))
    pair=s.integrate(s.integrate((t-r)**2,(r,0,d)),(t,0,d))/(2*d)
    phi=t**2*(w-t)**2*(t-w/2)
    residuals={
        'return_displacement':total,
        'start_velocity':v0.subs(t,0)-u,
        'end_velocity':v1.subs(t,T)+u,
        'first_join':v0.subs(t,tau),
        'second_join':v1.subs(t,T-tau),
        'minimum_action':cost-m*u**3/(3*a),
        'excursion':s.integrate(v0,(t,0,tau))-u*u/(2*a),
        'force_normalization':cost.subs(a,F/m)-m*m*u**3/(3*F),
        'small_speed_limit':s.limit(cost,u,0),
        'large_acceleration_limit':s.limit(cost,a,s.oo),
        'pair_variance_constant':pair-d**3/12,
        'idle_bump_zero_mean':s.integrate(phi,(t,0,w)),
        'idle_bump_boundary':phi.subs(t,0)+phi.subs(t,w),
    }
    for name,val in residuals.items():
        assert s.simplify(val)==0,(name,val)
    bump_cost=s.integrate(phi**2,(t,0,w))*m*b*b/2
    assert bump_cost>0
    assert s.limit(bump_cost,b,0)==0
    # m=u=a=1; exact integrals split at the two ramp/wait joins.
    cases=0
    for Tv in (s.Rational(2),s.Rational(3),s.Rational(5)):
        for n in (1,2,3,7):
            nodes=[Tv*s.Rational(i,n) for i in range(n+1)]
            chords=0
            for left,right in zip(nodes,nodes[1:]):
                cuts=sorted(set([left,right]+[z for z in (s.Integer(1),Tv-1) if left<z<right]))
                disp=0
                for lo,hi in zip(cuts,cuts[1:]):
                    mid=(lo+hi)/2
                    v=1-t if mid<1 else (0 if mid<Tv-1 else -(t-Tv+1))
                    disp+=s.integrate(v,(t,lo,hi))
                chords+=disp**2/(2*(right-left))
            error=s.Rational(1,3)-chords
            bound=sum((q-p)**3 for p,q in zip(nodes,nodes[1:]))/24
            assert 0<=error<=bound
            if Tv==2:
                assert error==bound
            cases+=1
    report={'identities':{k:'passed' for k in residuals},
            'positive_excess_checks':2,'rational_partition_cases':cases,
            'scope':'Finite checks; general optimality and convergence proved in the note'}
    target=Path(__file__).resolve().parents[1]/'out'/'bounded-acceleration-checks.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
