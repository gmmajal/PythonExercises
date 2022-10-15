from matplotlib.pylab import *
import numpy as np

def f(v_0,g,t):
    return v_0*t-(0.5*g*t**2)

def h(g,v_0):
    return (2.*v_0)/g

def main():
    vlist=sys.argv[1:]
    for i in range(len (vlist)):
        vlist[i]=float(vlist[i])
    v_0=np.array(vlist)
    a=0
    g = 9.81
    b=h(g,v_0)
    t=np.linspace(0,b,20)
    y = f(v_0, g, t)
    ymax=y.max()
    ymin=y.min()
    plot(t, y)

    axis([t.min(), t.max(), ymin - 0.05, ymax + 3])
    show()
    print("")


if __name__ == '__main__':
    main()