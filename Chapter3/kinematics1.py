def kinematics1(i,x,t):
    v=(x[i+1]-x[i-1])/float(t[i+1]-t[i-1])
    t_fd=t[i+1]-t[i]
    t_bd=t[i]-t[i-1]
    x_fd=x[i+1]-x[i]
    x_bd=x[i]-x[i-1]
    t_cent=t[i+1]-t[i-1]
    a=(2.0/t_cent)*( (x_fd/float(t_fd)) - (x_bd/float(t_bd)))
    return v,a
def test_kinematics():
    V=10.0
    t=[0,0.5,1.5,2.2]
    x=[ti*V for ti in t]
    v1,a1=kinematics1(1,x,t)
    expected_v1=10
    success_v=abs(expected_v1-v1)<1e-14
    msg_v='The computed v was %g'% v1
    expected_a1=0
    success_a=abs(expected_a1-a1)<1e-14
    msg_a='The computed a was %g'% a1
    assert success_v, msg_v
    assert success_a,msg_a

test_kinematics()


