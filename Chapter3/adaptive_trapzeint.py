from math import sqrt,cos,sin, pi, floor

'''For this excercise the appropriate use of the floor function is quite crucial as well as the choice of eps. The adaptive scheme breaks down for a tolerance below 1e-13.'''

def trapezint(f,a,b,n):
    h=(b-a)/float(floor(n))
    summation=0.
    for i in range(int(floor(n))):
        x_i=a+(i*h)
        x_ipl1=a+((i+1)*h)
        summation+=f(x_i)+f(x_ipl1)
    return 0.5*h*summation

def adaptive_trapezint(f,a,b,eps=1e-5):
    stp_size=1e-1
    delta=(b-a)/10
    fprimeprime=[]
    for i in range(11):
        x=a+(i*delta)
        fprimeprime.append(abs((f(x+stp_size)-(2.0*f(x))+f(x-stp_size))/(stp_size**2))) # finite diff scheme f''(x) approx f(x+h)-2f(x)+f(x-h)/(h^2)
    maximum=max(fprimeprime)
    h=sqrt((12.0*eps)/((b-a)*maximum))
    n=(b-a)/float(h)
    est=trapezint(f,a,b,n)
    return est,n

c=lambda x:cos(x)
s=lambda x:sin(x)

(est1,n1)=adaptive_trapezint(c,0,pi)
(est2,n2)=adaptive_trapezint(s,0,pi)
(est3,n3)=adaptive_trapezint(s,0,pi*0.5)

exact1=0
exact2=2
exact3=1

error1=abs(exact1-est1)
error2=abs(exact2-est2)
error3=abs(exact3-est3)

print 'The exact error for the first integral using the adaptive trapezoidal rule is %g and the number of intervals n was estimated to be %g'%(error1,floor(n1))
print 'The exact error for the second integral using the adaptive trapezoidal rule is %g and the number of intervals n was estimated to be %g'%(error2,floor(n2))
print 'The exact error for the third integral using the adaptive trapezoidal rule is %g and the number of intervals n was estimated to be %g'%(error3, floor(n3))

