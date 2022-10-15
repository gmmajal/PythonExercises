import numpy as np

def main():
    a=0
    b=3
    dx=0.1
    n=int(1+(b-a)/dx)
    w=np.linspace(0,3,n)
    print(w[:])
    print(w[:-2])
    print(w[::5])
    print(w[2:-2:6])
    print("")

if __name__ == '__main__':
    main()