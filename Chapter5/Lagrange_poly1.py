from numpy import *

def L_k(x,k,xp,yp):
    prodSum = 1.0
    for i in range(len(xp)):
        if i != k:
            prodSum *= float(x-xp[i])/(xp[k]-xp[i])
    return prodSum

def p_L(x, xp, yp):
        sum = 0.0
        for k in range(len(xp)):
            Lk = L_k(x,k,xp,yp)
            sum += yp[k]*Lk
        return sum

def test_p_L(xp,yp):
    for i in range(len(xp)):
        p=p_L(xp[i],xp,yp)
        assert abs(p-yp[i]) < 1e-6


def main():
    x = linspace(0, pi, 5)
    y = sin(x)
    test_p_L(x,y)
    #value taken between two interpolation points
    x_test = (3 * pi) / 8.0
    p_test = p_L(x_test, x, y)
    error= abs(p_test -sin(x_test))
    print("Error value %f" % error)

if __name__ == '__main__':
    main()

