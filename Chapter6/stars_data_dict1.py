
def main():
    infile=open('stars.txt','r')
    infile.readline()
    stars={}
    words=[]
    for line in infile:
        if line[0]!=']':
            words.append(line[:-2])
    infile.close()
    for i in range(len(words)):
        stars[eval(words[i])[0]]=eval(words[i])[3]
    print ("")

if __name__=='__main__':
    main()