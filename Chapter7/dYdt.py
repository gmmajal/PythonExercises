from Derivative import Derivative
from Y import Y


def dydt():
    v0=5.0
    y=Y(v0)
    t0=0;t1=0.5*y.v0*y.g;t2=y.v0/y.g
    d=Derivative(y)
    comp_0=d(t0);comp_1=d(t1);comp_2 = d(t2)
    exact_0=y.v0-y.g*t0;exact_1 = y.v0 - y.g * t1;exact_2 = y.v0 - y.g * t2
    err0=abs(exact_0-comp_0);err1=abs(exact_1-comp_1);err2=abs(exact_2-comp_2)
    print("error:%g for t:%g"%(err0,t0))
    print("error:%g for t:%g"%(err1,t1))
    print("error:%g for t:%g"%(err2,t2))

if __name__=='__main__':
    dydt()