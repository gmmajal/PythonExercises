'''
In [2]: from convert_temp import *

In [3]: C2F(30)
Out[3]: 86.0

In [4]: F2C(86)
Out[4]: 30.0

In [5]: C2K(50)
Out[5]: 323.15

In [6]: K2C(323.15)
Out[6]: 50.0

In [7]: F2K(86)
Out[7]: 303.15

In [8]: K2F(303.15)
Out[8]: 86.0
'''

def C2F(temp):
    return (9.0*temp)/5.0+32.0
def F2C(temp):
    return ((temp-32)*5.0)/9.0
def C2K(temp):
    return temp+273.15
def K2C(temp):
    return temp-273.15
def K2F(temp):
    return (temp-273.15)*(9.0/5.0)+32.0
def F2K(temp):
    return ((temp-32)*5.0)/9.0 +273.15

def get_input_and_convert():
    try:
        temp=float(sys.argv[1])
        deg=sys.argv[2]
    except IndexError:
        print 'Please supply two command line arguments a temperature and its unit(C, F or K)'
        sys.exit(1)
    except ValueError:
        print 'Please make sure that the first entry is a number and the second entry is either C, F or K. There should be a space between the first and second entry.'
        sys.exit(1)
    if deg!='C' and deg!='F' and deg!='K':
        raise ValueError('The second command line argument can only be C, F or K')
    if  ( temp<-273.15 and deg=='C') or (temp<-459.67 and deg=='F') or (temp<0 and deg=='K') :
        raise ValueError('You have entered an unphysical temperature value. If you have entered a value in Celsius it should be larger or equal -273.15.' \
                'If you have entered a value in Fahrenheit it should be larger or equal -459.67. If you have entered a value in Kelvin it should be larger or equal 0.')
    if deg=='C':
        temp_1=C2F(temp)
        temp_2=C2K(temp)
        deg_1='F'
        deg_2='K'
    elif deg=='F':
        temp_1=F2C(temp)
        temp_2=F2K(temp)
        deg_1='C'
        deg_2='K'
    else:
        temp_1=K2C(temp)
        temp_2=K2F(temp)
        deg_1='C'
        deg_2='F'
    return temp_1,deg_1,temp_2,deg_2


def test_conversion():
    f=100
    c=30
    tol=1e-6
    calc_f1=C2F(F2C(f))
    calc_c=K2C(C2K(c))
    calc_f2=K2F(F2K(f))
    success_1=abs(f-calc_f1)<tol
    success_2=abs(c-calc_c)<tol
    success_3=abs(f-calc_f2)<tol
    success=success_1 and success_2 and success_3
    msg='The expected value of f: %g F but the computed value was %g F. The expected value of c:%g C but the computed value was %g C'%(f,calc_f1,c,calc_c)
    assert success,msg

if __name__=='__main__':
    import sys
    if len(sys.argv)==2 and sys.argv[1]=='verify':
        test_conversion()
    else:
        temp_1,deg_1,temp_2,deg_2=get_input_and_convert()
        print '%g %s %g %s'% (temp_1,deg_1,temp_2,deg_2)
