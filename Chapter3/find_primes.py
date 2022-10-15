from math import floor,sqrt
def SieveOfEratosthenes(n):
    lst=[i for i in range(2,n+1)]
    for i in range (int(floor(sqrt(n)))):
        j=lst[i]
        multiple=0
        while j<=n:
            if (lst[i]**2)+(multiple*lst[i]) in lst:
                lst.remove((lst[i]**2)+(multiple*lst[i]))
            multiple+=1
            j=(lst[i]**2)+(multiple*lst[i])
    return lst

prime_lst1=SieveOfEratosthenes(100)
for i in range (len(prime_lst1)):
    print '%g'%prime_lst1[i]


            

