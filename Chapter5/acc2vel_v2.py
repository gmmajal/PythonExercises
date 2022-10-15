from matplotlib.pylab import *
from numpy import *

def f(dt,a,v,k):
    for i in range(1,k):
        v[i]=v[i-1]+(0.5*dt*(a[i-1]+a[i]))
    return v

def main():
    dt=float(sys.argv[1])
    k= 101
    infile=open('acc.dat','r')
    a=array([])
    t=linspace(0,10,k)*dt
    for line in infile:
        words=line.split();
        a=append(a,float(words[0]))
    infile.close()
    v1=zeros(k)
    v2=f(dt,a,v1,k)
    figure
    plot(t,v2,'ro-')
    xlabel('Time(s)')
    ylabel('Velocity(m/s)')
    show()
    figure
    plot(t, a, 'bo-')
    xlabel('Time(s)')
    ylabel('Acceleration(m/s2)')
    show()

if __name__ == '__main__':
    main()