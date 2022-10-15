from matplotlib.pylab import *
import numpy as np

def f(v_0,g,t):
    return v_0*t-(0.5*g*t**2)

def main():
    a=0
    v_0 = 10.0
    g = 9.81
    b=(2.*v_0)/g
    t=np.linspace(0,b,20)
    y=f(v_0,g,t)
    plot(t, y)
    show()
    print("")

if __name__ == '__main__':
    main()