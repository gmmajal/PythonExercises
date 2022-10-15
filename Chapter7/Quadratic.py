from numpy import *


class Quadratic(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def value(self, x):
        return self._a*x**2+self._b*x+self._c

    def table(self, n, L, R):
        x=linspace(L,R,n)
        f=self.value(x)
        print('Polynomial:f(x)=%f x^2+ %f x + %f, with %f values taken in the interval [%f %f]'%(self._a,self._b,self._c,n,L, R))
        print('%s'%('-'*100))
        heading1='x'
        heading2='f(x)'
        print('%-10s %-10s'%(heading1, heading2))
        for i in range(len(f)):
            print('%-10f %-10f'%(x[i],f[i] ))
        print('%s' % ('-' * 100))

    def roots(self):
        disc=self._b**2-4*(self._a*self._c)
        pos_root=(-self._b + emath.sqrt(disc))/(2.0*self._a)
        neg_root = (-self._b - emath.sqrt(disc)) / (2.0 * self._a)
        return pos_root,neg_root


def test_value():
    q=Quadratic(1,0,1)
    expected_value=5
    computed_value=q.value(2)
    diff = abs(expected_value - computed_value)
    tol = 1E-14
    assert diff < tol, 'bug in Quadratic.value, diff=%f' % diff


def test_roots():
    q=Quadratic(1,0,1)
    root1,root2=1j,-1j
    pos_root,neg_root=q.roots()
    diff_1 = abs(root1 - pos_root)
    diff_2 = abs(root2 - neg_root)
    tol = 1E-14
    assert diff_1 < tol, 'bug in Quadratic.root, diff=%s' % diff
    assert diff_2 < tol, 'bug in Quadratic.root, diff=%s' % diff


def test_table():
    q=Quadratic(1,0,1)
    q.table(10,1,11)


if __name__=='__main__':
    test_value()
    test_roots()
    test_table()