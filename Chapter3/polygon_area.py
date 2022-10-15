def polygon_area(x,y):
    n=len(x)
    sum_x=x[n-1]*y[0]
    sum_y=y[n-1]*x[0]
    for i in range(n-1):
        sum_x+=x[i]*y[i+1]
        sum_y+=y[i]*x[i+1]
    return 0.5*abs(sum_x-sum_y)
def test_polygonarea():
    # coordinates for triangle
    x_tri=[3,3,1]
    y_tri=[1,0,0]
    expected_tri=1.0
    computed_tri=polygon_area(x_tri,y_tri)
    success_tri=abs(expected_tri-computed_tri)<1e-14
    msg_tri='The computed triangle area is %g'% computed_tri
    assert success_tri, msg_tri
    #coordinates for quadrilateral
    x_quad=[0,3,3,0]
    y_quad=[1,1,0,0]
    expected_quad=3.0
    computed_quad=polygon_area(x_quad,y_quad)
    success_quad=abs(expected_quad-computed_quad)<1e-14
    msg_quad='The computed quadrilateral area is %g'% computed_quad
    assert success_quad,msg_quad
test_polygonarea()
   
