from matplotlib.pylab import *
from numpy import *

def fit(x,y,deg):
    coeff = polyfit(x, y, deg)
    p = poly1d(coeff)
    print (p)  # prints the polynomial expression
    y_fitted = p(x)  # computes the polynomial at the x points
    # use red circles for data points and a blue line for the polynomial
    plot(x, y, 'ro', x, y_fitted, 'b-')
    xlabel('Temp(C)')
    ylabel('Density(kg/m^3)')
    legend(['data', 'fitted polynomial of degree %d' % deg])
    show()

def main():
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    infile1 = open(filename1, 'r')
    infile2 = open(filename2, 'r')
    t1 = array([])
    d1 = array([])
    for line in infile1:
        words = line.split()
        if len(words) == 0:
            pass
        elif words[0] == '#':
            pass
        else:
            t1 = append(t1, float(words[0]))
            d1 = append(d1, float(words[1]))
    infile1.close()
    t2 = array([])
    d2 = array([])
    for line in infile2:
        words = line.split()
        if len(words) == 0:
            pass
        elif words[0] == '#':
            pass
        else:
            t2 = append(t2, float(words[0]))
            d2 = append(d2, float(words[1]))
    infile2.close()
    fit(t1,d1,2)
    fit(t2, d2,2)
    print("")


if __name__ == '__main__':
    main()