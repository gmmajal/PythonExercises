from numpy import *
from matplotlib.pyplot import *

def main():
    x0 = 100 # initial amount
    p = 5 # interest rate
    N = 4 # number of years

    x = zeros(N+1)

    # Compute solution
    x[0] = x0
    n=0
    x_prev = x[0]
    while n+1 <= N :
        x_n=x_prev+(p/100.0)*x_prev
        x[n+1] = x_n
        x_prev=x_n
        n += 1
    print (x)
    plot(range(N+1), x, 'ro')
    xlabel('years')
    ylabel('amount')
    show()


if __name__=='__main__':
    main()