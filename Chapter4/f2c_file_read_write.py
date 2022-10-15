infile=open('Fdeg.dat','r')
infile.readline()
infile.readline()
infile.readline()
F=[]
for line in infile:
    words=line.split()
    F.append(float(words[2]))
infile.close()
C=[]
for i in range(len(F)):
    C.append((5.0*(F[i]-32))/9.0)
outfile=open('FdegCdeg.dat','w')
outfile.write('Temperature Data\n')
outfile.write('----------------\n')
outfile.write('\n')
outfile.write('{:<15} {:15}'.format("Fahrenheit","Celsius"))
outfile.write('\n')
for i in range(len(F)):
    outfile.write("{:<15} {:<15}".format(F[i],C[i]))
    outfile.write('\n')
outfile.close()






