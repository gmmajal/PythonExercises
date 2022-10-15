from matplotlib.pylab import *
from numpy import *

def mu(T):
    A=2.414e-5
    B=247.8
    C=140
    return A*10**(B/(T-C))

def main():
   T=linspace(0,100,101)
   K= T+ 273.15
   visc=mu(K)
   plot(T,visc)
   xlabel('temperature(C)')
   ylabel('viscosity (Pa s)')

   axis([T[0],max(T),min(visc)-0.0001,max(visc)+0.0001])
   show()


if __name__=='__main__':
    main()