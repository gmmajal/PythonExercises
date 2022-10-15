from matplotlib.pylab import *
from numpy import *

def f(x,theta,g,v0,y0):
    return x*tan(theta)-(g*x**2)/(2*v0**2*cos(theta)*cos(theta))+y0

def main():
    y0=float(sys.argv[1])
    theta=eval(sys.argv[2])
    v0=float(sys.argv[3])
    g=9.81
    x=linspace(0,10,50)
    y=f(x,theta, g, v0, y0)
    plot(x,y)
    show()
    print("")

if __name__ == '__main__':
    main()