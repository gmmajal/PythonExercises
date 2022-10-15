# I need to get back to this later
from math import *
import sys
from scitools.StringFunction import StringFunction

def midpoint_integration(f,a,b,n=100):
    h=(b-a)/float(n)
    I=0
    for i in range(n):
        I+=f(a+i*h+0.5*h)
    return h*I


def test_midpoint_Integration():
    #formula is -cos(x) with a=0 and b=pi*0.5
    expected_res=1
    f_formula=sys.argv[1]
    a=eval(sys.argv[2])
    b=eval(sys.argv[3])
    if len(sys.argv)<=5:
        n=int(sys.argv[4])
    else:
        n=200
    f=StringFunction(f_formula)
    computed_res=midpoint_integration(f,a,b,n)
    success=abs(expected_res-computed_res)<1e-6
    msg='The expected result was %g but the computed result was %g'%(expected_res,computed_res)

    assert success,msg

test_midpoint_Integration()
