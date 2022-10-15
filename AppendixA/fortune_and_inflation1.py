from numpy import *

def main():
    x0 = 100 # initial amount
    p = 5.0 # interest rate
    N = 20 # number of months
    F= 10000# fortune
    q=2#percentage value to be used in the formulation
    I=1.4# inflation percentage

    x = zeros(N+1)
    c = zeros(N+1)
    # Compute solution
    x0=F
    c0= (p*q)/(10**4)*F
    c[0] = c0
    x[0] = x0
    n=0
    x_prev = x[0]
    c_prev = c[0]
    while n+1 <= N :
        x_n=x_prev+(p/(100.0))*x_prev - c_prev
        c_n = c_prev + (I / 100.0) * c_prev
        x[n+1] = x_n
        c[n+1] = c_n
        x_prev=x_n
        c_prev=c_n
        n += 1
    print (x)
    print (c)



if __name__=='__main__':
    main()