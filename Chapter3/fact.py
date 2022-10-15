def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        prod=1
        for i in range(1,n+1):
            prod*=i
        return prod
def test_fact():
    # Check an arbitrary test case
    n=4
    expected=4*3*2*1
    computed=fact(n)
    assert computed==expected
    # Check the special case
    assert fact(0)==1
    assert fact(1)==1
test_fact()

