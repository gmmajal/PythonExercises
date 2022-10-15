import numpy as np
import matplotlib.pyplot as plt

def f(u,t):
    return u*0.1

def Heun(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n + 1)
    u = np.zeros(n + 1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        u_star = u[k] + dt*f(u[k],t[k])
        u[k+1] = u[k] + 0.5*dt*f(u[k],t[k])+ 0.5*dt*f(u_star,t[k])
        t[k+1] = t[k] +dt
    return u,t

def saveToFile(t,u):
    infile = open('tu_Heun.dat','w')
    for i in range(0,len(u)):
        infile.write(str(t[i])+" "+str(u[i])+"\n")
    infile.close()

def solveAndGraphODE():
    u, t = Heun(f, U0=0.2, T=20, n=10)
    saveToFile(t,u)
    u_exact = 0.2*np.exp(0.1*t)
    plt.plot(t, u,'r-.')
    plt.plot(t,u_exact,'b--')
    plt.legend(['numerical','exact'])
    plt.xlabel('t')
    plt.ylabel('u')
    plt.show()


if __name__=='__main__':
    solveAndGraphODE()
