import  sympy
from math import pi

class Central(object):

    def __init__(self,f,h=1e-9):
        self.f=f
        self.h=h

    def __call__(self,x):
        f=self.f
        h=self.h
        return (f(x+h)-f(x-h))/(2.0*h)

def f(x):
    return 0.25*x**4

def g(x):
    return 2*x**2

def test_Central():
    df = Central(f) # make function-like object df
    # df(x) computes the derivative of f(x) approximately
    x = 2
    print ('df(%g) = %g' % (x, df(x)))
    print ('exact:', x**3)

def table(f,x,h=1e-5):
    xx = sympy.Symbol('xx')
    df_exact= sympy.lambdify([xx],sympy.diff(f))
    ff=sympy.lambdify([xx], f)
    df_num = Central(ff)  # make function-like object df
    print('%-10s %-10s %-15s %-30s'%('x','f\'(x)','f\'(x)_approx','error'))
    print('%s'%'-'*100)
    for x_val in x:
        error=abs(df_num(x_val)-df_exact(x_val))
        print('%-10f %-10f %-15f %-30f'%(x_val,df_exact(x_val),df_num(x_val),error))


def test_block():
    test_Central()
    dg = Central(g)  # make function-like object df
    # df(x) computes the derivative of f(x) approximately
    x = 1
    print('df(%g) = %g' % (x, dg(x)))
    print('exact:', 4*x )

    xx = sympy.Symbol('xx')
    f_expr = 'xx * sin(2 * xx)'
    x=[0, pi/2.0, pi, 1.5*pi, 2*pi]
    table(f_expr,x)

if __name__=='__main__':
    test_block()