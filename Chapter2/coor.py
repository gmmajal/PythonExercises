a=2
b=3
n=5
h=(b-a)/float(n)
lst1=[]
# part (a)
for i in range(n+1):
    x_i=a+(i*h)
    lst1.append(x_i)
for elem in lst1:
    print elem

# part(b)
lst2=[a+(i*h) for i in range(n+1)]
print 
for elem in lst2:
    print elem
    
