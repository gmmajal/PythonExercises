import sys


try:
    t=float(sys.argv[1])
    v0=float(sys.argv[2])
except IndexError:
        t=float(raw_input('t=?'))
        v0=float(raw_input('v0=?'))
        

g=9.81
y=v0*t-0.5*g*t**2
print y

