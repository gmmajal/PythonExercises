A=1000 #intial amount of money
p=5 #interest rate
n=3 #number of years
growth=A*(1+(p/100.0))**n

print 'An inital amount of %f euros has grown to %f after %f years with a %f percent interest rate'%(A,growth,n,p)
