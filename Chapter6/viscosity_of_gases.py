from matplotlib.pylab import *

def mu(T,gas,mu_data):
    T_0=mu_data[gas]['T_0']
    C=mu_data[gas]['C']
    mu = mu_data[gas]['mu_0']
    return mu*( (T-C) / (T+C) )*(T/T_0) ** 1.5

def main():
    gas={}
    infile=open('viscosity_of_gases.dat','r')
    for line in infile:
        if (line[0]=='#'):
            pass
        elif(line=='\n'):
            pass
        else:
            gas_prop = {}
            words=line[17:].split()
            gas_prop['C']=float(words[0])
            gas_prop['T_0'] = float(words[1])
            gas_prop['mu_0'] = float(words[2])
            name=' '.join(line[0:16].split())
            gas[name]=gas_prop

    T= linspace(223,373,100)
    mu_air=mu(T,'air',gas)
    mu_CO2 = mu(T, 'carbon dioxide', gas)
    mu_H = mu(T, 'hydrogen', gas)

    plot(T,mu_air)
    plot(T, mu_CO2)
    plot(T, mu_H)
    xlabel(r'$T(K)$')
    ylabel(r'$\mu (Pa s)$')
    legend(['air','CO2','H'])
    show()

    print("")

if __name__=='__main__':
    main()