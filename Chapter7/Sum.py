from math import factorial,pi,sin


def term(k, x):
    #return (-x)**k
    return ((-1)**(k)*(x)**(2*k+1))/factorial(2*k+1)


class Sum(object):

    def __init__(self,arg1,arg2,arg3):
        self.f=arg1
        self.m=arg2
        self.n=arg3

    def __call__(self, x):
        sum=0.0
        for k in range (self.m,self.n+1):
            sum+=self.f(k,x)
        return sum

    def term(self,k,x):
        return term(k,x)


def test_sineTaylor():
    S = Sum(term, 0, 10)
    x = pi
    print(sin(x))
    print(S(x))
    print(S.term(k=10, x=x))  # (-1)**(10*0.5)*(0.5)**10/(2*10+1)!

def test_block():
    S = Sum(term, 0, 3)
    x = 0.5
    print (S(x))
    print (S.term(k=4, x=x)) # (-0.5)**4


if __name__=='__main__':
    test_block()
    test_sineTaylor()