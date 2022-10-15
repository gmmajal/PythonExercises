def evalcmlarg(text):
    return eval(text)


if __name__=='__main__':
    from  sinesum2 import * 
    from math import pi
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--n','--list of n values',type=evalcmlarg, default=[1,3,5,10,50,100],help='n',metavar='n')
    parser.add_argument('--alpha','--list of alpha values', type=evalcmlarg, default=[0.01,0.25,0.49],help='alpha',metavar='alpha')
    parser.add_argument('--T','--length of the interval',type=float, default=2*pi,help='T',metavar='T')
   
    args=parser.parse_args()
    table(args.n,args.alpha,args.T)
