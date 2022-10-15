import sys

def load():
    infile=open('constants.txt','r')
    constants={}
    infile.readline()
    infile.readline()
    for line in infile:
        words=line.split()
        if(len(words[:-1])==3):
            constName= words[0]+' '+words[1]
            value=words[2]
        else:
            constName= words[0]+' '+words[1]+' '+words[2]
            value=words[3]
        constants[constName]=float(value)
    infile.close()
    return constants
