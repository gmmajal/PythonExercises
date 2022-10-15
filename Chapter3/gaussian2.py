from math import exp,pi, sqrt

def gauss(x,m=0,s=1):
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

m=10;s=1
x=[i for i in range(m-5*s,m+5*s+1)]
print'x\t\tf(x)'
for i in range(len(x)):
    f_x=gauss(x[i],m,s)
    print 'x=%.6f\t f(x)=%.6f'%(x[i],f_x)

