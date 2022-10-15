from math import exp, sin, pi

def h(t):
    return exp(-a*t)*sin(pi*t)

a=10
print h(0)
print h(1)
