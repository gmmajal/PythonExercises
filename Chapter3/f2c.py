def C(f):
    return (5.0/9.0)*(f-32)
def F(c):
    return ((9.0/5.0)*c)+32
cc=10
ff=50
print F(C(ff))
print C(F(cc))
