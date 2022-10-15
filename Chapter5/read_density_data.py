from matplotlib.pylab import *
from numpy import *

def main():
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    infile1=open(filename1,'r')
    infile2 = open(filename2, 'r')
    t1=array([])
    d1=array([])
    for line in infile1:
        words=line.split()
        if len(words)==0:
            pass
        elif words[0]=='#':
            pass
        else:
            t1=append(t1,words[0])
            d1=append(d1,words[1])
    infile1.close()
    t2 = array([])
    d2 = array([])
    for line in infile2:
        words = line.split()
        if  len(words) == 0:
            pass
        elif words[0] == '#':
            pass
        else:
            t2 = append(t2, words[0])
            d2 = append(d2, words[1])
    infile2.close()
    figure
    plot(t1,d1)
    xlabel('Temp(C)')
    ylabel('Density(kg/m^3)')
    title('Density of air at different temperatures, at 1 atm pressure')
    show()
    figure
    plot(t2,d2)
    xlabel('Temp(C)')
    ylabel('Density(kg/m^3)')
    title('Density of water at different temperatures, at 1 atm pressure')
    show()
    print("")

if __name__ == '__main__':
    main()


