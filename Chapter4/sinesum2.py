def S(t,n,T):
    from math import pi, sin
    total=0.0;
    for i in range(1,n+1):
        total+=(1.0/(2*i-1))*sin((2*(2*i-1)*pi*t)/float(T))
    return (4.0/pi)*total
def f(t,T):
    if t>0 and t<=0.5*T:
        return 1
    elif t==0.5*T:
        return 0;
    else:
        return -1
def table(n_values,alpha_values,T):
    t=[a*T for a in alpha_values]
    for i in range(len(t)):
        print'#### The value of t=%g'%t[i]
        func=f(t[i],T)
        for j in range(len(n_values)):
            approx=S(t[i],n_values[j],T)
            error= func-approx
            print'For n=%g, the error=%.4f '%(n_values[j],error)
def read_input():
    try:
        T=float(sys.argv[1])
        n=eval(sys.argv[2])
        alpha= eval(sys.argv[3])
    except IndexError:
        raise IndexError('In this program three command line arguments are expected. A number T. A list of numbers denoting the n_values.'\
        'Finally, a list of numbers denoting the alpha_values')
    except ValueError:
        raise ValueError('Please make sure you are entering numbers and not strings.')
    if not( isinstance(n,list) and isinstance(alpha,list)):
        raise TypeError('Please make sure that you entered a list of numbers as the second and third command line argument.')
    for i in range(len(n)):
        if not(isinstance(n[i],int) or isinstance(n[i],float)):
            raise TypeError('Please make sure that all entries in your list are numbers.')
    for i in range(len(alpha)):
        if not(isinstance(alpha[i],int) or isinstance(alpha[i],float)):
            raise TypeError('Please make sure that all entries in your list are numbers.')
            
    return T,n, alpha


if __name__=='__main__':
    import sys
    T, n_values, alpha_values=read_input()
    table(n_values,alpha_values,T)
    
