from cmath import sqrt as csqrt
from math import sqrt as rsqrt

#note this code assumes that both a and b will not be zero or close to zero, simultaneously

def roots(a,b,c):
    sgn=b**2-(4.0*a*c)
    if sgn<0.0:
        r1=(-b-csqrt(sgn))/(2.0*a)
        r2=(-b+csqrt(sgn))/(2.0*a)
        return r1,r2
    else:
        r1=(-b-rsqrt(sgn))/(2.0*a)
        r2=(-b+rsqrt(sgn))/(2.0*a)
        return r1, r2
def test_roots_float():
    a=1
    b=0
    c=0
    r1,r2=roots(a,b,c)
    check_instance_r1=isinstance(r1,float)
    check_instance_r2=isinstance(r2,float)
    msg_r1='The root r1 %g is not a float'%(r1)
    msg_r2='The root r2 %g is not a float'%(r2)
    assert check_instance_r1,msg_r1
    assert check_instance_r2,msg_r2

def test_roots_complex():
    a=6
    b=0.5
    c=7
    r1,r2=roots(a,b,c)
    check_instance_r1=isinstance(r1,complex)
    check_instance_r2=isinstance(r2,complex)
    msg_r1='The root r1 {r1:f} is not complex' .format(r1=r1)
    msg_r2='The root r2 {r2:f} is not complex' .format(r2=r2)
    assert check_instance_r1, msg_r1
    assert check_instance_r2, msg_r2

test_roots_float()
test_roots_complex()



