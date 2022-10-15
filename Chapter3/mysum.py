def mysum(lst):
    s=lst[0]
    for i in range(1,len(lst)):
        s+=lst[i]
    return s
print mysum([1,3,5,-5])
print mysum([[1,2],[4,3],[8,1]])
print mysum(['Hello,','World!'])

