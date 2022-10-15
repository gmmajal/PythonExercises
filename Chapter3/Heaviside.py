def H(x):
    if x<0:
        return 0
    else:
        return 1
def test_H():
    x=1e1 #-1e1,-1e-15,0,1e-15,1e1
    computed_val=H(x)
    expected_val=1
    success=abs(computed_val-expected_val)<1e-14
    msg='The computed value was %g'%computed_val
    assert success, msg
test_H()

