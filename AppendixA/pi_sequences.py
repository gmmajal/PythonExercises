from matplotlib.pyplot import *
from numpy import *

def a(n):
    sum=0.0
    for k in range(1,n+1):
        sum+=((-1.0)**(k+1))/((2*k)-1)
    return 4*sum

def b(n):
    sum=0.0
    for k in range(1,n+1):
        sum+=k**(-2)
    return sqrt(6.0*sum)

def c(n):
    sum=0.0
    for k in range(1,n+1):
        sum+=k**(-4)
    return (90.0*sum)**(0.25)

def d(n):
    sum=0.0
    for k in range(0,n+1):
        sum+=(-1)**k/((3**k)*(2*k+1))
    return (6.0/sqrt(3))*sum

def e(n):
    sum1 = 0.0
    sum2 = 0.0
    for k in range(0,n+1):
        sum1+=(-1)**k/((5**(2*k+1))*(2*k+1))
        sum2+=(-1)**k/((239**(2*k+1))*(2*k+1))
    return 16*sum1-4*sum2

def main():
    N=100
    aa=zeros(N+1)
    bb = zeros(N + 1)
    cc = zeros(N + 1)
    dd = zeros(N + 1)
    ee = zeros(N + 1)
    for i in range(1,N+1):
        aa[i]=a(i)
        bb[i]=b(i)
        cc[i]=c(i)
    for i in range(0,N+1):
        dd[i]=d(i)
        ee[i]=e(i)
    plot(range(1,N+1),aa[1:])
    plot(range(1, N + 1), bb[1:])
    plot(range(1, N + 1), cc[1:])
    plot(range(1, N + 1), dd[1:])
    plot(range(1, N + 1), ee[1:])
    legend([r'$a_n$',r'$b_n$',r'$c_n$',r'$d_n$',r'$e_n$'])
    ylabel('sequence values')
    xlabel('n')
    show()

if __name__=='__main__':
    main()