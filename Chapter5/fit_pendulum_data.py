from matplotlib.pylab import *
from numpy import *

def fit(x,y,deg):
    coeff = polyfit(x, y, deg)
    p = poly1d(coeff)
    print (p)  # prints the polynomial expression
    y_fitted = p(x)  # computes the polynomial at the x points
    # use red circles for data points and a blue line for the polynomial
    plot(x, y, 'ro', x, y_fitted, 'b-')
    xlabel('Length of rod (m)')
    ylabel('Period of oscillation(s)')
    legend(['data', 'fitted polynomial of degree %d' % deg])
    show()

def main():
    infile = open('pendulum.dat', 'r')
    l = array([])
    t = array([])
    infile.readline()
    for line in infile:
        words = line.split()
        l = append(l, float(words[0]))
        t = append(t, float(words[1]))
    infile.close()
    fit(l, t, 2)
    print("")

if __name__ == '__main__':
    main()