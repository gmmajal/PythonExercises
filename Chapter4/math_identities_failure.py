from math import *
def power3_identity(A=-100,B=100,n=1000):
    import random
    success=0
    tol=1e-6
    for i in range(1,n):
        a=random.uniform(A,B)
        b=random.uniform(A,B)
        comp=(a*b)**3
        exp=a**3*b**3
        if abs(comp-exp)<tol:
            success+=1
    failure=n-success
    failure_frac=failure/float(n)
    print 'The fraction of failures is %g'%failure_frac

def equal(expr1,expr2,A=-100,B=100,n=500):
    import random
    success=0
    tol=1e-6
    for i in range(1,n):
        a=random.uniform(A,B)
        b=random.uniform(A,B)
        try:
            comp=eval(expr1)
            act=eval(expr2)
        except ValueError:
            print 'Please make sure that the value of a and b are within the domain of the function being evaluated.'
        except TypeError:
            print 'Please make sure that the function arguments A, B and n are numbers'
        if abs(comp-act)<tol:
            success+=1
    failure=n-success
    failure_frac=failure/float(n)
    print 'The fraction of failures is %g\n'%failure_frac

print 'Power3_identity function output\n'
power3_identity()
print 'equal function output for (a*b)**3==a**3*b**3\n'
equal('(a*b)**3','a**3*b**3')
print 'equal function output for e(a+b)==e(a)*e(b)\n'
equal("exp(a+b)","exp(a)*exp(b)")
print 'equal function output for ln(a**b)==b*ln(a)\n'
equal("log(a**b)","b*log(a)",1,50,1000)


