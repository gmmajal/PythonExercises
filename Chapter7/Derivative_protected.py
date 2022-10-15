from math import sin,cos


class Derivative(object):
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)

    def __call__(self, x):
        f, h = self._f, self._h # make short forms
        return (f(x+h) - f(x))/h

    def set_precision(self,h):
        self._h=h

    def get_precision(self):
        return self._h


def f(x):
    return sin(x)*cos(x)


def test_block():
    df=Derivative(f)
    x=0
    expected=1.0
    computed=df(x)
    assert abs(expected-computed)<1e-10, "Assertion failed the computed derivative is not close enough to the actual value"
    df.set_precision(1e-9)
    h=df.get_precision()
    assert abs(h-1e-9)<1e-10, "Assertion failed the returned value of h is not close enough to value set earlier"


if __name__=='__main__':
    test_block()