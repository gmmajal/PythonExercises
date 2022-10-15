from math import sqrt,sin, cos, pi

def pathlength(x,y):
    tot_len=0
    for i in range(1,len(x)):
        tmp=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
        tot_len+=tmp
    return tot_len

for k in range(2,11):
    n=2**k
    x=[0.5*cos((2*pi*i)/float(n)) for i in range (n+1)]
    y=[0.5*sin((2*pi*i)/float(n)) for i in range (n+1)]
    pi_est=pathlength(x,y)
    error=abs(pi-pi_est)
    print 'For k=%g, n=%g, the error in the computed value of pi is %g'%(k,n,error)


