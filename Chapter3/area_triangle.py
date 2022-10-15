def triangle_area(vertices):
    v1=vertices[0]
    v2=vertices[1]
    v3=vertices[2]
    return 0.5*abs(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1])
def test_triangle_area(): 
    """ Verify the area of a triangle with vertex coordinates (0,0), (1,0), and (0,2). """
    v1 = (0,0); v2 = (1,0); v3 = (0,2) 
    vertices = [v1, v2, v3] 
    expected = 1 
    computed = triangle_area(vertices) 
    tol = 1E-14 
    success = abs(expected - computed) < tol 
    msg = 'computed area=%g != %g (expected)' % \
            (computed, expected) 
    assert success, msg
test_triangle_area()
