from math import sin, cos,pi
#a)
x = pi/4
val_1 = sin(x)**2+cos(x)**2 # 1_val = math.sin^2(x)+math.cos^2(x)
print val_1 # print 1_VAL

#b)
v0=3 #v0 = 3 m/s
t=1 #t = 1 s
a=2 #a = 2 m/s**2
s = v0*t + 0.5*a*t**2
print s

#c)
a=3.3;b=5.3 #a=3,3 b=5,3
a2=a**2
b2=b**2

eq1_sum=a2+2*a*b+b2 #eq1_sum=a2+2ab+b2
eq2_sum=a2-2*a*b+b2 #eq2_sum=a2-2ab+b2

eq1_pow=(a+b)**2
eq2_pow=(a-b)**2

print 'First equation: %g=%g' %(eq1_sum, eq1_pow) # print 'First equation: %g=%g', %(eq1_sum, eq1_pow)
print 'Second equation: %g=%g' %(eq2_pow, eq2_pow) # print 'Second equation: %h=%h', %(eq2_pow,eq2_pow)
