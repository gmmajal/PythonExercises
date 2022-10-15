def poly(x,roots):
    p=1
    for i in range(len(roots)):
        p*=(x-roots[i])
    return p
def test_poly():
    lst=[2,3]
    x=4
    expected=2
    result=poly(x,lst)
    success=result==expected
    msg='The function failed and gave the wrong output %g'% result
    assert success,msg

test_poly()

