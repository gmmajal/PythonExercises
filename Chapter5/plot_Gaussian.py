from matplotlib.pylab import *
import numpy as np

def f(x):
    return (1.0 / np.sqrt(2 * np.pi)) * (np.exp(-0.5 * (x * x)))

def main():
    noOfPnts=41
    x= np.linspace(-4,4,noOfPnts)
    y=f(x)
    plot(x,y)
    show()
    print ("")

if __name__ == '__main__':
    main()