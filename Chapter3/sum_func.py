def sum_1k(M):
    k=1
    s=0.0
    while k<=M:
        s+=1.0/k
        k+=1
    return s
def test_sum_1k():
    tol=1e-14
    reference= 1.0+0.5+(1.0/3)
    result= sum_1k(3)
    success= abs(result-reference)<tol
    msg='sum_1k(3)=%g !=%g'%(result,reference)
    assert success, msg

test_sum_1k()

