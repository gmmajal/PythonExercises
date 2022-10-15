from math import cos, sin, pi

def trapezint1(f,a,b):
    return 0.5*(b-a)*(f(a)+f(b))
def trapezint2(f,a,b):
    mid=0.5*(b-a)
    return 0.5*(((mid-a)*(f(mid)+f(a)))+((b-mid)*(f(b)+f(mid))))
def trapezint(f,a,b,n):
    h=(b-a)/float(n)
    summation=0
    for i in range(n):
        x_i=a+(i*h)
        x_ipl1=a+((i+1)*h)
        summation+=f(x_i)+f(x_ipl1)
    return 0.5*h*summation
s=lambda x: sin(x)
c=lambda x: cos(x)



#est1=trapezint1(c,0,pi)
#est2=trapezint1(s,0,pi)
#est3=trapezint1(s,0,0.5*pi)

#est1=trapezint2(c,0,pi)
#est2=trapezint2(s,0,pi)
#est3=trapezint2(s,0,0.5*pi)

est1=trapezint(c,0,pi,2)
est2=trapezint(s,0,pi,406)
est3=trapezint(s,0,0.5*pi,144)

exact1=0
exact2=2
exact3=1

error1=abs(exact1-est1)
error2=abs(exact2-est2)
error3=abs(exact3-est3)

print'##### Trapezoidal rule'
print 'The error in the quadrature estimate for the first integral is %g' % error1
print 'The error in the quadrature estimate for the second integral is %g' % error2
print 'The error in the quadrature estimate for the third integral is %g' % error3

def test_trapezint():
    c=lambda x:cos(x)
    f=lambda x:x
    tol=1e-14
    expected1=0
    expected2=1.5
    result1=trapezint(c,0,2*pi,3)
    result2=trapezint(f,1,2,3)
    success1=abs(result1-expected1)<tol
    success2=abs(result2-expected2)<tol
    msg1='The output of the trapezoidal method is %g but the expected output was %g'%(result1,expected1)
    msg2='The output of the trapezoidal method is %g but the expect output was %g'%(result2,expected2)
    assert success1,msg1
    assert success2,msg2
test_trapezint()

