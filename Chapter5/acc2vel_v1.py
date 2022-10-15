from matplotlib.pylab import *
from numpy import *

def f(dt,a,k):
    if k==0:
        return 0.0
    else:
        return dt*((0.5*a[0])+(0.5*a[k])+sum(a[1:k]))

def main():
    dt=float(sys.argv[1])
    k= int(sys.argv[2])
    infile=open('acc.dat','r')
    a=array([])
    t=linspace(0,k,k)*dt
    for line in infile:
        words=line.split();
        a=append(a,float(words[0]))
    infile.close()
    plot(t,a[0:k],'ro-')
    xlabel('Time(s)')
    ylabel('Acceleration(m/s2)')
    show()
    index=int(k / 2.0)
    v_k=f(dt,a,index)
    print("v_k:%f for k:%d"%(v_k,index))

if __name__ == '__main__':
    main()