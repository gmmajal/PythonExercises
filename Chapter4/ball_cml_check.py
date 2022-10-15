import sys

g=9.81
try:
    t=float(sys.argv[1])
    v0=float(sys.argv[2])
except IndexError:
    t=float(raw_input('t=?'))
    v0=float(raw_input('v0=?'))
max_t_val=(2.0*v0)/g
if t<0 or t>max_t_val:
    print 'The value of t={tt}. It must be between 0 and {ss}'.format(tt=t,ss=max_t_val)
    sys.exit(1)

y=v0*t-0.5*g*t**2
print y
    
