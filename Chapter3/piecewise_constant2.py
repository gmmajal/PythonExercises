def indicator_direct(x,L,R):
    if (L<=x) and (x<=R):
        return 1
    else:
        return 0
def piecewise(x,xi,v):
    tot=0
    for i in range(len(v)):
        tot+=v[i]*indicator_direct(x,xi[i],xi[i+1])
    return tot
xx=[0, 1, 1.5,2]
v=[-1,0,4]

x1=0;x2=0.5;x3=1;x4=1.2;x5=1.5;x6=1.7;x7=2
print piecewise(x1,xx,v)
print piecewise(x2,xx,v)
print piecewise(x3,xx,v)
print piecewise(x4,xx,v)
print piecewise(x5,xx,v)
print piecewise(x6,xx,v)
print piecewise(x7,xx,v)
