from matplotlib.pylab import *
from numpy import *

def L_k(x,k,xp,yp):
    prodSum = 1.0
    for i in range(len(xp)):
        if i != k:
            prodSum *= float(x-xp[i])/(xp[k]-xp[i])
    return prodSum

def p_L(x, xp, yp):
        sum = 0.0
        for k in range(len(xp)):
            Lk = L_k(x,k,xp,yp)
            sum += yp[k]*Lk
        return sum

def test_p_L(xp,yp):
    for i in range(len(xp)):
        p=p_L(xp[i],xp,yp)
        assert abs(p-yp[i]) < 1e-6

def graph(f, n, xmin, xmax, resolution=1001):
    xp=linspace(xmin,xmax,n)
    yp=f(xp)
    p=zeros(len(xp))
    for i in range(len(xp)):
        p[i]=p_L(xp[i], xp, yp)
    plot(xp, yp, 'b-')
    plot(xp[0:resolution],p[0:resolution],'ro')
    xlabel('x-coordinate')
    ylabel('y-coordinate')
    legend(['y=f(x)','Interpolated (Lagrangian) points'])
    show()

def test_block():
    n=5
    xmin=0
    xmax=pi
    x = linspace(xmin, xmax, n)
    y = sin(x)
    graph(sin,n,xmin,xmax,5)
    test_p_L(x, y)


if __name__ == '__main__':
    test_block()
