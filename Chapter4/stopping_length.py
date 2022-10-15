import sys

v0=float(sys.argv[1])
v0=(v0*1000)/(3600)
mu=0.3
g=9.81
d=0.5*(v0**2)/(mu*g)
print d

