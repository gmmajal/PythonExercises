import sys

from numpy import *
from matplotlib.pyplot import *

def main():

    q=float(sys.argv[1])
    dt=float(sys.argv[2])
    T=float(sys.argv[3])

    if q==1.0:
        T=6.0
    else:
        T = 1.0 / (q - 1) - 0.1

    N=int((T/dt)+1)
    t=linspace(0,T,N)
    u=zeros(N)
    if q == 1.0:
        u_exact=exp(t)
    else:
        # solution applicable for q>1 and t*(1-q)+1>0
        u_exact=(t*(1-q)+1)**(1.0/(1-q))
    u[0]=1.0
    for k in range(1,N):
        u[k] = u[k-1] + dt * ( u[k-1]**q)
    plot(t,u)
    plot(t,u_exact)
    ylabel(r'u')
    xlabel(r't')
    legend([r'$u_{num}$',r'$u_{exact}$'])
    show()

if __name__=='__main__':
    main()