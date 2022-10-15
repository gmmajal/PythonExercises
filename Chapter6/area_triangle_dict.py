from math import*

def triangle_area(dic):
    x1=dic[1][0]
    x2=dic[2][0]
    x3=dic[3][0]
    y1 = dic[1][1]
    y2 = dic[2][1]
    y3 = dic[3][1]
    return 0.5*abs((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1))

def test_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    tri={}
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    tri[1]=v1
    tri[2]=v2
    tri[3]=v3

    expected = 1
    computed = triangle_area(tri)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' % \
    (computed, expected)
    assert success, msg

if __name__=='__main__':
    test_triangle_area()