v_0=10
g=9.81
t_0=0
t_n=(2.0*v_0)/g
n=13
h=(t_n-t_0)/float(n)
# part(a)
t=[t_0+(i*h) for i in range(n+1)]
y=[v_0*tt-(0.5*g*tt**2) for tt in t]
ty1=[t,y] 

for i in range (len(t)):
    print '%.2f\t%.2f'%(ty1[0][i], ty1[1][i])

#part(b)
print
ty2=[[tt,yy] for tt, yy in zip(t,y)]
for i, j in ty2:
    print '%.2f\t%.2f'%(i,j)

