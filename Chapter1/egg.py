from math import pi, log

M=67 # mass of egg (g)
rho=1.038 # density of the egg (g/cm^3)
c=3.7 # specific heat capacity (J/(g*K))
K= 5.4e-3 # thermal conductivity (W/(cm*K))
T_01=4 # original temperature of the egg taken from the fridge (C)
T_02=20 # original temperature of the egg at room temperature
T_W=100 # temperature of boiling water (C)
T_y=70 # target temperature

t1=((M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*(pi**2)*((4*pi/3.0)**(2/3))))*log(0.76*float((T_01-T_W)/(T_y-T_W)))
t2=((M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*(pi**2)*((4*pi/3.0)**(2/3))))*log(0.76*float((T_02-T_W)/(T_y-T_W)))

print 'The time taken to get a hard boiled egg for an initial temperature of %g C is %f s' %(T_01, t1)
print 'The time taken to get a hard boiled egg for an initial temperature of %g C is %f s' %(T_02,t2)

