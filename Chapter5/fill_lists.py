from math import *

def f(x):
    return (1.0/sqrt(2*pi))*(exp(-0.5*(x**2)))

def main():
    a=-4
    b= 4
    noOfPnts=41
    dx=(b-a)/(noOfPnts-1)
    xlist=[a+(i*dx) for i in range(noOfPnts)]
    ylist=[f(x) for x in xlist]
    print("")

if __name__ == '__main__':
    main()