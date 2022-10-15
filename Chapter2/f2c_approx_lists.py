F=[i for i in range(0,110,10)]
C=[(5.0*(f-32))/9.0 for f in F]
C_hat=[0.5*(f-30) for f in F]
conversion=[[f, c, c_h] for f,c,c_h in zip(F,C,C_hat)]
for i,j,k in conversion:
    print '%g\t%g\t%g'%(i,j,k)
