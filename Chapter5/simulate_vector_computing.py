import numpy as np

def f(x,t):
    return np.cos(np.sin(x))+np.exp(1.0/t)

def main():
    n=2
    xlist=[0,2]
    tlist=[1,1.5]
    x=np.array(xlist)
    t=np.array(tlist)
    y=np.zeros(n)
    for i in range(n):
        y[i]=f(x[i],t[i])
    print("")

if __name__ == '__main__':
    main()