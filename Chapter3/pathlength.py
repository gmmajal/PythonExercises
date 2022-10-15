from math import sqrt
def pathlength(x,y):
    tot_len=0
    for i in range(1,len(x)):
        tmp_sum=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
        tot_len+=tmp_sum
    return tot_len
def test_pathlength():
    x=[0.5,1,1.5]
    y=[0.5,1,1.5]
    expected=sqrt(2)
    computed=pathlength(x,y)
    assert abs(expected-computed)<1e-14
test_pathlength()

