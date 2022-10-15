from math import *
#note that in python e-9 is the same as exp(-9) and not 1e-9

class Backward(object):
    def __init__(self, f, h=1e-9):
        self.f = f
        self.h = h

    def __call__(self, x):
        h = self.h
        f = self.f
        return (f(x) - f(x-h))/h  # finite difference

def test_block():
    dsin = Backward(sin)
    e = abs(dsin(0) - cos(0))
    print('error:', e)
    dexp = Backward(exp, h=1e-7)
    e = abs(dexp(0) - exp(0))
    print ('error:', e)

if __name__=='__main__':
    test_block()