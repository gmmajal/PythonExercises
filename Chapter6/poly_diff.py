
def diff(p):
    dp={}
    for j in p:
        if j==0:
            pass
        else:
            dp[j-1]=j*p[j]
    return dp

def main():
    dict={}
    dict[0]=-3
    dict[3]=2
    dict[5]=-1
    print(dict)
    diff_dict=diff(dict)
    print(diff_dict)

if __name__=='__main__':
    main()