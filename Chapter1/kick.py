from math import pi

rho=1.2 # density(kg/m^3)
C_d=0.4 # drag coeffecient
a=0.11  # radius of football (m)
m=0.43 # mass of football (kg)
g=9.81 # acceleration due to gravity (m/s^2)
A=pi*(a**2) # area of the football (m^2)
V1=30*(1000.0/3600.0) # velocity of the football for a soft kick(m/s)
V2=120*(1000.0/3600.0) # velocity of the football for a hard kick (m/s)
F_d1=0.5*C_d*rho*A*(V1**2) # drag force for a soft kick
F_d2=0.5*C_d*rho*A*(V2**2) # drag force for a hard kick
F_g=m*g # gravity force

print 'The gravity force for a football with mass %g kg is %.1f N' %(m,F_g)

print 'The drag force for a football travelling at %g m/s was calculated to be %.1f N' %(V1, F_d1)

print 'The drag force for a football travelling at %g m/s was calculated to be %.1f N' %(V2, F_d2)
