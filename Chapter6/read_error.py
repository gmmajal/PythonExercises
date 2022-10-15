import numpy as np
from matplotlib.pylab import *

def read_errorFile(filename):
    infile = open(filename, 'r')
    epsilon = np.array([])
    exact = np.array([])
    n = np.array([])
    for line in infile:
        if (line[0] == 'x' or line[0] == 'n'):
            pass
        elif(line == '\n'):
            pass
        else:
            words=line.split()
            epsilon=np.append(epsilon,float(words[1].replace(',','')))
            exact = np.append(exact, float(words[4].replace(',','')))
            n = np.append(n, float(words[5].replace('n=','')))
    infile.close()
    return epsilon, exact,n

def main():
    eps,ex,n=read_errorFile("lnsum.txt")
    semilogy(n,eps,'r*')
    semilogy(n, ex, 'bo')
    xlabel('n')
    legend(['epsilon','exact error'])
    show()

if __name__=='__main__':
    main()