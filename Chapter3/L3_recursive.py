from math import log
def L3(x,epsilon=1e-6):
    x=float(x)
    i=1
    term=(1.0/i)*(x/(1.0+x))**i
    s=term
    while abs(term)>epsilon:
        i+=1
        term=(1.0/i)*(x/(1.0+x))**i
        s+=term
    return s

def L3_ci(x,epsilon=1e-4):
    c1=1.0/(1+x)
    tot=c1
    term=c1
    i=1
    while abs(term)>epsilon:
        i+=1
        a=((i-1)/float(i))*(x/float(1+x))
        term=a*term
        tot+=term
    return tot
def test_L3_ci():
    x=10
    old_approx=L3(x)
    new_approx=L3_ci(x)
    abs_error=abs(old_approx-new_approx)
    success=abs_error<1e-6
    msg='The expected result was %g and the computed value was %g'%(old_approx,new_approx)
    assert msg,success
test_L3_ci()
