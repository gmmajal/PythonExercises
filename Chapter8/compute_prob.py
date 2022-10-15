import random
import numpy

def main():
    i=[1,2,3,6]
    N=[10**ii for ii in i]
    for n in N:
        count=0
        x=range(n)
        y=[random.uniform(0,1) for j in x]
        for yy in y:
            if 0.5<=yy and yy<=0.6:
               count+=1
        print("Computed probability is: %f" %(count/float(n)))

if __name__=='__main__':
    main()