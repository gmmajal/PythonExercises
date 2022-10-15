from matplotlib.pylab import *
from numpy import *
from scitools.StringFunction import StringFunction
import sys

def main():
    f=StringFunction(sys.argv[1])
    a=float(eval(sys.argv[2]))
    b = float(eval(sys.argv[3]))
    n = int(sys.argv[4])
    x= linspace(a,b,n)
    f.vectorize(globals())
    y=f(x)
    outfile = open('output1.dat', 'w')
    for i in range(len(x)):
        outfile.write(' %10f  %10f\n' % (x[i], y[i]))
    outfile.close()
    x = array([])
    y = array([])
    infile = open('output1.dat', 'r')
    for line in infile:
        words = line.split()
        x = append(x, float(words[0]))
        y = append(y, float(words[1]))
    infile.close()
    plot(x, y)
    axis([0,2*pi,-1.005,1.005])
    show()

if __name__ == '__main__':
    main()