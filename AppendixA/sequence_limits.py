from math import sin,pi
from matplotlib.pyplot import *

# part(c)
def D(f, x, N):
    d=[0.0]*(N+1)
    for i in range(N+1):
        h=2**(-i)
        d[i]=(f(x+h)-f(x))/h
        if (x==pi):
            print ('n=%d, f(x+h)-f(x):%.22f, h=%.22f'%(i, f(x+h)-f(x),h))
    return d

def main():
    # part(a)
    N = 100
    for i in range(0,N+1,2):
        a=(7.0+1.0/(i+1))/(3.0-1/(i+1)**2)
        print ("a_n:%f for n=%d"%(a,i))
    print('-'*100)
    # part(b)
    N = 100
    for ii in range(0,N+1):
        d= sin(2**(-ii))/(2**(-ii))
        print ("d_n:%f for n=%d"%(d,ii))
    #part(c)
    N=80
    y=D(sin,0,N)
    figure
    plot(range(N+1),y,'o')
    ylabel(r'$D_n$ values')
    xlabel('n values')
    title(r'$f(x)=sin(x)$ for $x=0$')
    show()
    #part(d)
    y=D(sin,pi,N)
    figure
    plot(range(N + 1), y, 'o')
    ylabel(r'$D_n$ values')
    xlabel('n values')
    title(r'$f(x)=sin(x)$ for $x=\pi$')
    show()
    #part(e)
    # f(x+h)-f(x)-> 0 as h->0, thus for large n D_n->0

if __name__=='__main__':
    main()