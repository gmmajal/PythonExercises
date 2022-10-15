import random

def main():
    N=10
    hcount=0
    for i in range(100):
        r=random.random()
        if r<=0.5:
            print('Heads')
            hcount+=1
        else:
            print('Tails')

    print ('Total occurence of heads was:%d'%hcount)

if __name__=='__main__':
    main()