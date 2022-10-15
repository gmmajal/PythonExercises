import sys
from math import exp,factorial
from Polynomial import Polynomial

def main():
    x = eval(sys.argv[1])
    N = eval(sys.argv[2])
    for i in range(len(x)):
        xx=x[i]
        for j in range(len(N)):
            coeff=[0]*N[j]
            for k in range(0,N[j]):
                coeff[k]=1/factorial(k)
            p=Polynomial(coeff)
            exact=exp(x[i])
            print('exp(%5f):%10f Taylor-Polynomial(N=%d): %10f'%(x[i],exact, N[j], p(xx)) )
            print('-'*50)
        print('-*-' * 100)

if __name__=='__main__':
    main()