def L4(x,n=None,epsilon=None,return_n=False):
    if (epsilon is not None) and (n is not None):
        print 'Both epsilon and n can not be given simultaenously by the user '
    elif n is not None:
        s=0
        for i in range(1,n+1):
            s+=(1.0/i)*(x/(1.0+x))**i
        if return_n:
            return s,n
        else:
            return s
    elif epsilon is not None:
        x=float(x)
        i=1
        term=(1.0/i)*(x/(1+x))**i
        s=term
        while abs(term)>epsilon:
            i+=1
            term=(1.0/i)*(x/(1+x))**i
            s+=term
        if return_n:
            return s,i
        else:
            return s
    else:
        print 'Either epsilon or n should be specified by the user'
val=L4(10,n=100)
print'For the first test case the approximation was %g'%(val)
val,terms=L4(10,n=100,return_n=True)
print 'For the second test case the approximation was %g with n=%g'%(val,terms)
val=L4(10,epsilon=1e-8)
print 'For the third test case the approximation was %g'%(val)
val,terms=L4(10,epsilon=1e-8,return_n=True)
print 'For the fourth test case the approximation was %g with n=%g'%(val,terms)
L4(10)
L4(10,n=100,epsilon=1e-8,return_n=True)
