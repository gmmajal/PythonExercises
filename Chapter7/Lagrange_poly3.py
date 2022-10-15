from matplotlib.pylab import *
from numpy import *


class LagrangeInterpolation(object):

    def __init__(self,x,y):
        self.xp=x
        self.yp=y

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


def test_p_L(xp,yp,p_L):

    for i in range(len(xp)):
        p=p_L(xp[i])
        assert abs(p-yp[i]) < 1e-10

def test_block():
    xp = np.linspace(0, np.pi, 5)
    yp = np.sin(xp)
    p_L = LagrangeInterpolation(xp, yp)
    test_p_L(xp, yp,p_L)
    x = 1.2
    print ('p_L( % g)= % g' % (x, p_L(x)))
    print ('sin( % g)= % g' % (x, np.sin(x)))
    p_L.plot()


if __name__=='__main__':
    test_block()