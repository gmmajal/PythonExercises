from matplotlib.pylab import *
from numpy import *

def c(l):
    rho= 1000
    g= 9.81
    s= 7.9e-2
    h= 50
    return sqrt( ((g*l)/(2*pi)) * (1+(s*4*pi**2)/(rho*g*l**2)) * tanh((2*pi*h)/l) )

def main():
    small_l=linspace(0.001,0.1,1000)
    large_l=linspace(1,2000,1000)
    small_c=c(small_l)
    large_c=c(large_l)
    figure()
    plot(small_l,small_c)
    xlabel(r'$\lambda (m)$')
    ylabel(r'c($\lambda$) (m/s)')
    show()
    figure()
    plot(large_l,large_c)
    xlabel(r'$\lambda (m)$')
    ylabel(r'c($\lambda$) (m/s)')
    show()

if __name__=='__main__':
    main()