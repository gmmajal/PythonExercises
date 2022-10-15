from matplotlib.pylab import *
from numpy import *
# from math import factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def S(x,n):
    sum=zeros(len(x))
    for j in range(n+1):
        add(sum,(-1)**j * x**(2*j+1)/factorial(2*j+1),out=sum,casting="unsafe")
    return sum

def main():
    x=linspace(0,4*pi,1000)
    figure
    s1=S(x,1)
    s2=S(x,2)
    s3=S(x,3)
    s6 = S(x, 6)
    s12 = S(x, 12)
    plot(x/pi,sin(x))
    plot(x/pi,s1)
    plot(x/pi, s2)
    plot(x/pi, s3)
    plot(x/pi, s6)
    plot(x/pi, s12)
    legend([r'$sin(x)$','S(x,1)','S(x,2)','S(x,3)','S(x,6)','S(x,12)'])
    axis([0,4,-1.1,1.1])
    show()

if __name__=='__main__':
    main()