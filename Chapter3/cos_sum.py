from math import cos,pi
def C(x,n):
    c0=1.0
    term=c0
    s=c0
    for j in range(1,n+1):
        term=-term*((x**2)/float((2.0*j)*((2.0*j)-1.0)))
        s+=term
    return s
def print_errors():
    x=[4*pi, 6*pi, 8*pi, 10*pi]
    n=[5, 25, 50, 100, 200]
    print 'x\t%g\t%g\t%g\t%g\t%g'%(n[0],n[1],n[2],n[3],n[4])
    for i in range(len(x)):
        error=[]
        for j in range(len(n)):
            exact=cos(x[i])
            approx=C(x[i],n[j])
            error.append(abs(exact-approx))
        print '%g\t%g\t%g\t%g\t%g\t%g\n'%(x[i],error[0],error[1],error[2],error[3],error[4])
print_errors()
            
