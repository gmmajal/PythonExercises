m_e=9.1094e-31 #electron mass
e=1.6022e-19   #elementary charge
e_0=8.8542e-12 #electrical permittivity
h=6.6261e-34 # constant
# part (a)
n=20
i=1
while i<=n:
    E_n=(-(m_e*e**4)/(8.0*(e_0**2)*h**2))*(1.0/(i**2))
    print 'The energy level for an electron in a Hydrogen atom E_n at n=%g is %g'%(i,E_n)
    i=i+1

# part (b)

print '\nTable for dE\n'
i=1;f=1;n=5
while i<=n:
    while f<=n:
        dE=(-(m_e*e**4)/(8.0*(e**2)*h**2))*(1.0/(i**2)-1.0/(f**2))
        print '%g' % dE,
        f=f+1
    print
    f=1
    i=i+1

