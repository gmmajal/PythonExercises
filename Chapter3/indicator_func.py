def H(x):
    if x<0:
        return 0
    else:
        return 1
def indicator_direct(x,L,R):
    if (L<=x) and (x<=R):
        return 1
    else:
        return 0
def indicator_Heaviside(x,L,R):
    return H(x-L)*H(R-x)
def test_indicator():
    L=1;R=3;x1=0.5;x2=L;x3=(L+R)*0.5;x4=R;x5=5
    expected_1=0
    expected_2=1
    expected_3=1
    expected_4=1
    expected_5=0
    if indicator_direct(x1,L,R)==indicator_Heaviside(x1,L,R):
        success1=abs(expected_1-indicator_direct(x1,L,R))<1e-14
    else:
        print 'The direct indicator function yields %g whereas the Heaviside based indicator function yields %g'%(indicator_direct(x1,L,R),indicator_Heaviside(x1,L,R))
    if indicator_direct(x2,L,R)==indicator_Heaviside(x2,L,R):
        success2=abs(expected_2-indicator_direct(x2,L,R))<1e-14
    else:
        print 'The direct indicator function yields %g whereas the Heaviside based indicator function yields %g'%(indicator_direct(x2,L,R),indicator_Heaviside(x2,L,R))
    if indicator_direct(x3,L,R)==indicator_Heaviside(x3,L,R):
        success3=abs(expected_3-indicator_direct(x3,L,R))<1e-14
    else:
        print 'The direct indicator function yields %g whereas the Heaviside based indicator function yields %g'%(indicator_direct(x3,L,R),indicator_Heaviside(x3,L,R))
    if indicator_direct(x4,L,R)==indicator_Heaviside(x4,L,R):
        success4=abs(expected_4-indicator_direct(x4,L,R))<1e-14
    else:
        print 'The direct indicator function yields %g whereas the Heaviside based indicator function yields %g'%(indicator_direct(x4,L,R),indicator_Heaviside(x4,L,R))
    if indicator_direct(x5,L,R)==indicator_Heaviside(x5,L,R):
        success5=abs(expected_5-indicator_direct(x5,L,R))<1e-14
    else:
        print 'The direct indicator function yields %g whereas the Heaviside based indicator function yields %g'%(indicator_direct(x5,L,R),indicator_Heaviside(x5,L,R))

    msg_1='The computed value is %g'%indicator_direct(x1,L,R)
    msg_2='The computed value is %g'%indicator_direct(x2,L,R)
    msg_3='The computed value is %g'%indicator_direct(x3,L,R)
    msg_4='The computed value is %g'%indicator_direct(x4,L,R)
    msg_5='The computed value is %g'%indicator_direct(x5,L,R)

    assert success1,msg1
    assert success2,msg2
    assert success3,msg3
    assert success4,msg4
    assert success5,msg5
test_indicator()
