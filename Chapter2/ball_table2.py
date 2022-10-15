v_0=10
g=9.81
t_0=0
t_n=(2.0*v_0)/g
n=13
h=(t_n-t_0)/float(n)
t=[t_0+(k*h) for k in range(n+1)]
y=[(v_0*tt)-(0.5*g*tt**2) for tt in t]
for i,j in zip(t,y):
    print '%g\t%g'%(i,j)
