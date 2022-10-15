infile=open('tempData.txt','r')
infile.readline()
infile.readline()
infile.readline()
datastr=infile.readline()
infile.close()
words=datastr.split()
F=float(words[2])
C=(5.0*(F-32))/9.0
print 'The temperature in Celsius is %f'%C

