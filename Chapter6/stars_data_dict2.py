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
        star_prop={}
        star_prop['distance']=eval(words[i])[1]
        star_prop['apparent brightness'] = eval(words[i])[2]
        star_prop['luminosity'] = eval(words[i])[3]
        stars[eval(words[i])[0]]=star_prop
    print ("")

if __name__=='__main__':
    main()