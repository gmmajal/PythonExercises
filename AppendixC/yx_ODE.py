import numpy
from matplotlib.pyplot import *

def main():
    a=0;b=4
    dx=[1,0.25,0.01]
    eps=1e-3
    ynum=[[],[],[]]
    x=[[],[],[]]
    y_exact=numpy.zeros(1001)
    for i in range(len(dx)):
        n=int((b-a)/dx[i]+1)
        x[i]=numpy.linspace(a,b,n+1)
        ynum[i]=[1+numpy.sqrt(eps)]*(n+1)
        for k in range(1,n+1):
            #The initial value of y is approximately one and thus the value y(0)-1 is very small.
            # If dx is large then dx/(y[0]-1) will be large as well. Leading to an overshoot in the iteration.
            ynum[i][k]=ynum[i][k-1]+dx[i]/(2.0*(ynum[i][k-1]-1))
    x_exact=numpy.linspace(0,4,1001)
    y_exact=1+numpy.sqrt(x_exact+eps)
    plot(x[0], ynum[0],x[1],ynum[1],x[2],ynum[2])
    plot(x_exact,y_exact)
    legend([r'$\Delta x=1$',r'$\Delta x=0.25$',r'$\Delta x=0.01$','exactSolution'])
    xlabel(r'x')
    ylabel(r'y')
    show()
if __name__=='__main__':
    main()