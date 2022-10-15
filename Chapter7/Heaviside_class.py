from math import pi, sin
import numpy as np

class Heaviside(object):

    def __init__(self, eps=0.0):
        self.eps=eps

    def __call__(self,x):
        eps=self.eps
        if isinstance(x,np.ndarray):
            r = np.zeros(len(x), dtype=float)
            if eps!=0.0:
                condition1= x<-eps
                condition2= np.logical_and(-eps<=x,x<=eps)
                condition3= x>eps
                r[condition1] =  0.0
                r[condition2] =  0.5 + (x[condition2]/(2.0*eps)) + (1.0/(2.0*np.pi))*np.sin((np.pi*x[condition2])/eps)
                r[condition3] = 1.0
                return r
            else:
                r[x >= 0.0] = 1.0
                return r
        else: 
            if eps !=0.0:
                if x<-eps:
                    return 0.0
                elif x>eps:
                    return 1.0
                else:
                    return 0.5+ (x/(2.0*eps)) + (1.0/(2.0*pi))*sin((pi*x)/eps)
            else:
                if x<0.0:
                    return 0.0
                else:
                    return 1.0         



def test_block():
    H=Heaviside()
    print (H(0.1))
    H=Heaviside(eps=0.8)
    print(H(0.1))

    H = Heaviside()
    # original discontinous Heaviside function
    x = np.linspace(-1, 1, 11)
    print (H(x))
    H = Heaviside(eps=0.8) # smoothed Heaviside function
    print (H(x))



if __name__=='__main__':
    test_block()