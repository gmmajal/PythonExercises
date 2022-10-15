from matplotlib.pylab import *
from numpy import *


def main():
    x=array([])
    y=array([])
    infile = open('xy.dat', 'r')
    for line in infile:
        words=line.split()
        x=append(x,float(words[0]))
        y=append(y,float(words[1]))
    infile.close()
    plot(x,y)
    show()
    print("")

if __name__ == '__main__':
    main()