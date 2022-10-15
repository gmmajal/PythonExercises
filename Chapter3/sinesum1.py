from math import sin, pi
def S(t,n,T):
    summation=0.0
    for i in range(1,n+1):
       summation+=(1.0/float(2*i-1))*sin((2*(2*i-1)*pi*t)/float(T))
    return (4.0/pi)*summation
def f(t,T):
    if t>0 and t<T*0.5:
        return 1
    elif t==T*0.5:
        return 0
    else:
        return -1
T=2*pi
n=[1,3,5,10,30,100]
alpha=[0.01,0.25,0.49]
t=[a*T for a in alpha]

for i in range(len(t)):
    print '####The value of t=%g'%t[i]
    func=f(t[i],T)
    for j in range(len(n)):
        series_approx=S(t[i],n[j],T)
        error=func-series_approx
        print 'For n=%g, error=%.6f'%(n[j],error)


        

