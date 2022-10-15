def maxmin_list(a):
    max_elem=a[0]
    min_elem=a[0]
    for i in range(1, len(a)):
        if a[i]>max_elem:
            max_elem=a[i]
        elif a[i]<min_elem:
            min_elem=a[i]
    return max_elem,min_elem

x=[1,52,4,0.5,-3,210]
mx,mn=maxmin_list(x)
print mx
print mn
