from numpy import *
from matplotlib.pyplot import *

def main():
    dt=0.25
    N=int((6.0/0.25)+1)
    t=linspace(0,6,N)
    u=zeros(N)
    u_exact=0.5+1.5*exp(2.0*t)
    u[0]=2.0
    for k in range(1,N):
        u[k ] = u[k-1] + dt * ((2.0* u[k-1]) - 1)
    plot(t,u)
    plot(t,u_exact)
    ylabel(r'u')
    xlabel(r't')
    legend([r'$u_{num}$',r'$u_{exact}$'])
    show()

if __name__=='__main__':
    main()
