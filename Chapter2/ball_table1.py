v_0=10 # intial velocity
g=9.81 #acceleration due to gravity
t_0=0
t_n=(2.0*v_0)/g
n=13

# part(a)
h=(t_n-t_0)/float(n)
print 't\t y'
for i in range(n+1):
    t=t_0+(i*h)
    y_t=v_0*t-(0.5*g*t**2)
    print '%g \t %g'%(t,y_t)

# part(b)
print
i=0
t2=t_0
print 't\t y'
while t2<t_n:
    t2=t_0+(i*h)
    y_t2=v_0*t2-(0.5*g*t2**2)
    i=i+1
    print '%g \t %g'%(t2,y_t2)


    
