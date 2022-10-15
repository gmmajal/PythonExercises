from math import exp,pi,cos,log
def diff(f,x,h=1E-5):
    return (f(x+h)-f(x-h))/(2.0*h)
def test_diff():
    f=lambda x: x**2
    g=lambda x: 5*x**2
    h=1e-2
    tol=1e-14
    expected_f=2
    expected_g=10
    computed_f=diff(f,1,h)
    computed_g=diff(g,1,h)
    success_f=abs(expected_f-computed_f)<tol
    success_g=abs(expected_g-computed_g)<tol
    msg_f='The computed derivative for f(x):x^2=%g'% computed_f
    msg_g='The computed derivative for g(x):5x^2=%g'% computed_g
    assert success_f,msg_f
    assert success_g,msg_g
def application():
    f=lambda x:exp(x)
    g=lambda x:exp(-2*x**2)
    hh=lambda x:cos(x)
    m=lambda x:log(x)
    h=1e-2
    exact_f=1
    exact_g=0
    exact_h=0
    exact_m=1
    computed_f=diff(f,0.0,h)
    computed_g=diff(g,0.0,h)
    computed_h=diff(hh,2.0*pi,h)
    computed_m=diff(m,1.0,h)
    error_f=abs(exact_f-computed_f)
    error_g=abs(exact_g-computed_g)
    error_h=abs(exact_h-computed_h)
    error_m=abs(exact_m-computed_m)
    print 'For f(x)=exp(x) at x=0, the error for the computed derivative is %g' %error_f
    print'For f(x)=exp(-2x^2) at x=0, the error for the computed derivative is %g'%error_g
    print'For f(x)=cos(x) at x=2*pi, the error for the computed derivative is %g'%error_h
    print'For f(x)=ln(x) at x=1 , the error for the computed derivative is %g'%error_m
test_diff()
application()
