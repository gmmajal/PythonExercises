from matplotlib.pylab import *
from numpy import *

def c_est(f):
    return (f-30)*.5

def c_exact(f):
    return (5./9.)*(f-32)

def main():
    F=linspace(-20,120,50)
    c1=c_est(F)
    c2=c_exact(F)
    plot(F, c1,'r-')
    plot(F, c2,'bo')
    show()
    print("")

if __name__ == '__main__':
    main()
