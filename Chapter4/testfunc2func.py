def halve(x):
    return x/2
def test_halve():
    assert halve(5.0)==2.5 #Real number division
    assert halve(5)==2     #Integer division
def add(x,y):
    return x+y
def test_add():
    #Test integers
    assert add(1,2)==3

    #Test floating-point numbers with rounding error
    tol=1E-14
    a=0.1; b=0.2
    computed= add(a,b)
    expected=0.3
    assert abs(expected-computed)<tol

    #Test lists
    assert add([1,4],[4,7])==[1,4,4,7]

    #Test strings
    assert add('Hello, ','World!')=='Hello, World!'
def equal(a,b):
    if a==b:
        return True, a
    else:
        my_str=''
        if len(a)==len(b):
            for i in range(len(a)):
                my_str+=a[i]
                if a[i]!=b[i]:
                    my_str+='|'+b[i]
            return False, my_str
        elif len(a)>len(b):
            for i in range(len(a)):
                if  i<len(b):
                    if a[i]==b[i]:
                        my_str+=a[i]
                    else:
                        my_str+=a[i]+'|'+b[i]
                else:
                    my_str+=a[i]+'|*'
            return False, my_str
        else:
            for i in range(len(b)):
                if i<len(a):
                    if a[i]==b[i]:
                        my_str+=a[i] 
                    else:
                        my_str+=a[i]+'|'+b[i]
                else:
                    my_str+='*|'+b[i]
            return False,my_str
def test_equal():
    assert equal('abc','abc')==(True,'abc')
    assert equal('abc','aBc')==(False,'ab|Bc')
    assert equal('abc','aBcd')==(False,'ab|Bc*|d')
    assert equal('Hello, World!', 'hello world')==(False,'H|hello,|  |wW|oo|rr|ll|dd|*!|*')
test_halve()
test_add()
test_equal()
