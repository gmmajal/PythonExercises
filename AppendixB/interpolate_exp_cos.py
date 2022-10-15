from numpy import *

def f(x):
    return exp(-(x)**2)*cos(2*pi*x)

def S(x,y,xx,k):
    numerator= y[k+1]-y[k]
    denominator= x[k+1]-x[k]
    fraction=numerator/denominator
    difference=xx-x[k]
    return y[k]+fraction*difference


def main():
    q=[2,4,8,16]
    xx=-0.45
    for i in range(len(q)):
        x=linspace(-1,1,q[i]+1)
        exact_val=f(xx)
        y=f(x)
        max_value=(max(where(x<xx)))
        idx=max_value[-1]
        x_interp=S(x,y,xx,idx)
        error=abs(exact_val-x_interp)
        print('q=%-2d error=%-12f'%(q[i],error))

if __name__=='__main__':
    main()