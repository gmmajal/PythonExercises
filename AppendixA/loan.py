from numpy import *

def main():
    x0 = 100 # initial amount
    p = 5.0 # interest rate
    N = 20 # number of months

    x = zeros(N+1)
    y = zeros(N+1)
    # Compute solution
    x[0] = x0
    n=0
    x_prev = x[0]
    while n+1 <= N :
        y[n+1]= (p/(12.0*100.0))*x_prev+ x0/N
        x_n=x_prev+(p/(12.0*100.0))*x_prev-y[n+1]
        x[n+1] = x_n
        x_prev=x_n
        n += 1
    print (x)
    print (y[1:])



if __name__=='__main__':
    main()