from math import *
import numpy as np
def f(x):
    return (1.0 / sqrt(2 * pi)) * (exp(-0.5 * (x ** 2)))

def main():
    a = -4
    b = 4
    noOfPnts = 41
    dx = (b - a) / (noOfPnts - 1)
    x= np.zeros(noOfPnts)
    y= np.zeros(noOfPnts)
    for i in range(noOfPnts):
        x[i]=a+ (i*dx)
        y[i]=f(x[i])
    print ("")

if __name__ == '__main__':
    main()