import sys

def read_F():
    try:
        F=float(sys.argv[1])
    except IndexError:
        raise IndexError('Fahrenheit degrees must be provided on the command line')
    except ValueError:
        raise ValueError('Fahreneheit degree can not be a string. User entered %s'%sys.argv[1])
    if F<-459.67:
        raise ValueError('%g F is a non physical value as it is below absolute zero'%F)
    return F


try:
    F=read_F()
except(ValueError,IndexError) as e:
    print e
    sys.exit(1)
C=(5.0*(F-32))/9.0
print '%g F is %g C'%(F,C)
