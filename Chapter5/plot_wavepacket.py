from matplotlib.pylab import *
from numpy import *

def f(x,t):
    return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

def main():
    t=0
    x=linspace(-4,4,1000)
    y=f(x,t)
    plot(x,y)
    xlabel('x')
    ylabel('f(x,0)')
    show()

if __name__ == '__main__':
    main()