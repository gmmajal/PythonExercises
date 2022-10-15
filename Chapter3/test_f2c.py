def C(f):
    return (5.0/9.0)*(f-32)
def F(c):
    return ((9.0/5.0)*c)+32
def test_F_C():
    tol=1e-14
    temp=30
    comp_F_C=abs(temp-F(C(temp)))<tol
    msg_F_C='Computed result for F(C(%g))=%g != %g'%(temp,F(C(temp)),temp)
    comp_C_F=abs(temp-C(F(temp)))<tol
    msg_C_F='Computed result for C(F(%g))=%g != %g'%(temp,C(F(temp)),temp)
    assert comp_F_C, msg_F_C
    assert comp_C_F, msg_C_F

test_F_C()



