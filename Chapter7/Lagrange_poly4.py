import numpy
from matplotlib.pylab import *


def myfunction(x):
    return exp(-x/2.0)*sin(x)


class LagrangeInterpolation(object):

    def __init__(self, arg1, arg2, arg3=None):

        if isinstance(arg1, numpy.ndarray) and isinstance(arg2, numpy.ndarray):
            self.xp = arg1
            self.yp = arg2
        elif callable(arg1) and isinstance(arg2, (list,tuple)) and isinstance(arg3, int):
            f = arg1
            x = arg2
            n = arg3
            self.xp = linspace(x[0],x[-1],n)
            self.yp = f(self.xp)

    def L_k(self,x, k, xp, yp):
        prodSum = 1.0
        for i in range(len(xp)):
            if i != k:
                prodSum *= float(x - xp[i]) / (xp[k] - xp[i])
        return prodSum

    def p_L(self,x, xp, yp):
        sum = 0.0
        for k in range(len(xp)):
            Lk = self.L_k(x, k, xp, yp)
            sum += yp[k] * Lk
        return sum

    def __call__(self, x):
        xp=self.xp
        yp=self.yp
        return self.p_L(x,xp,yp)

    def plot(self):
        xp=self.xp
        yp = self.yp
        p = zeros(len(xp))
        for i in range(len(xp)):
            p[i] = self.p_L(xp[i], xp, yp)
        plot(xp, yp, 'b-')
        plot(xp, p, 'ro')
        xlabel('x-coordinate')
        ylabel('y-coordinate')
        legend(['y=f(x)', 'Interpolated (Lagrangian) points'])
        show()


def test_p_L(arg1,arg2,arg3,arg4=None):
    if isinstance(arg2, numpy.ndarray) and isinstance(arg3, numpy.ndarray):
        xp=arg2;yp=arg3;p_L=arg1
        for i in range(len(xp)):
            p = p_L(xp[i])
            assert abs(p - yp[i]) < 1e-10
    elif callable(arg1) and isinstance(arg2, (list,tuple)) and isinstance(arg3, int):
        xp = linspace(arg1[0],arg1[-1],arg4);yp = arg2(xp);p_L = arg1
        for i in range(len(xp)):
            p = p_L(xp[i])
            assert abs(p - yp[i]) < 1e-10

def test_block():
    p_L = LagrangeInterpolation(myfunction, [0, pi], 11)
    test_p_L(p_L, myfunction,[0, pi], 11)
    x = pi*0.5
    print('p_L( % g)= % g' % (x, p_L(x)))
    print('exp(-%g/2.0)*sin(%g)= % g' % (x,x, myfunction(x)))
    p_L.plot()

    xp = np.linspace(0, np.pi, 5)
    yp = np.sin(xp)
    p_L1 = LagrangeInterpolation(xp, yp)
    test_p_L(p_L1,xp, yp)
    x = 1.2
    print('p_L1( % g)= % g' % (x, p_L1(x)))
    print('sin( % g)= % g' % (x, np.sin(x)))
    p_L1.plot()


if __name__=='__main__':
    test_block()