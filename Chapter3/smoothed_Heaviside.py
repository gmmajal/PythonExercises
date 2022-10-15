from math import sin, pi

def H_eps(x,eps=0.01):
    if x<-eps:
        return 0.0
    elif (-eps<=x) and (x<=eps):
        return 0.5+ (x/float(2*eps))+ (1/(2.0*pi))*sin((pi*x)/float(eps))
    else:
        return 1.0
def test_H_eps():
    eps=2;x_1=-3;x_2=-eps;x_3=0;x_4=eps;x_5=3
    expected_val1=0.0
    expected_val2=0.0
    expected_val3=0.5
    expected_val4=1.0
    expected_val5=1.0
    computed_1=H_eps(x_1,eps)
    computed_2=H_eps(x_2,eps)
    computed_3=H_eps(x_3,eps)
    computed_4=H_eps(x_4,eps)
    computed_5=H_eps(x_5,eps)
    success_1=abs(expected_val1-computed_1)<1e-14
    success_2=abs(expected_val2-computed_2)<1e-14
    success_3=abs(expected_val3-computed_3)<1e-14
    success_4=abs(expected_val4-computed_4)<1e-14
    success_5=abs(expected_val5-computed_5)<1e-14
    msg1='The computed value was %g'% computed_1
    msg2='The computed value was %g'% computed_2
    msg3='The computed value was %g'% computed_3
    msg4='The computed value was %g'% computed_4
    msg5='The computed value was %g'% computed_5
    assert success_1,msg1
    assert success_2,msg2
    assert success_3,msg3
    assert success_4,msg4
    assert success_5,msg5
test_H_eps()

