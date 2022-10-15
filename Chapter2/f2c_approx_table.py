print '-----------'
F=0
dF=10
while F<=100:
    C=((F-32)*5.0)/9.0
    C_hat=(F-30)/2
    F=F+dF
    print F,C,C_hat
print '-----------'
