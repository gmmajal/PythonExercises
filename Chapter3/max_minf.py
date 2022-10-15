from math import cos, pi

def maxmin(f,a,b,n=1000):
    h=(b-a)/float(n-1)
    x=[a+(i*h) for i in range(0,n)]
    f_x=[f(xx) for xx in x]
    max_val=max(f_x)
    min_val=min(f_x)
    return max_val,min_val
def test_maxmin():
    f= lambda x: cos(x)
    mx_computed, mn_computed=maxmin(f,-0.5*pi,2.0*pi)
    expected_max=1.0
    expected_min=-1.0
    success_max=abs(expected_max-mx_computed)<1e-5
    success_min=abs(expected_min-mn_computed)<1e-5
    msg_max='The computed max value is %g'%mx_computed
    msg_min='The computed min value is %g'%mn_computed
    assert success_max,msg_max
    assert success_min,msg_min
test_maxmin()
