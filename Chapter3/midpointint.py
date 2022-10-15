from math import cos, sin, pi

def midpointint(f,a,b,n):
    h=(b-a)/float(n)
    summation=0
    for i in range(n):
        x_i=a+((i*h)+(0.5*h))
        summation+=f(x_i)
    return h*summation

c =lambda x:cos(x)
s =lambda x:sin(x)

est1=midpointint(c,0,pi,10)
est2=midpointint(s,0,pi,10)
est3=midpointint(s,0,pi*0.5,10)

exact1=0
exact2=2
exact3=1

error1=abs(exact1-est1)
error2=abs(exact2-est2)
error3=abs(exact3-est3)

print '#### Midpoint rule'
print 'The error in the quadrature estimate for the first integral is %g '% error1
print 'The error in the quadrature estimate for the second integral is %g '% error2
print 'The error in the quadrature estimate for the third integral is %g '% error3
