
def main():
    infile=open('human_evolution.txt','r')
    infile.readline()
    infile.readline()
    infile.readline()
    human={}
    for line in infile:
        if(line[0]=='-' or line=='\n' or line[0]=='S'):
            pass
        else:
            human_prop={}
            species='homo '+line[3:21].strip()
            human_prop['when']=line[21:37].strip()
            human_prop['height']=line[37:50].strip()
            human_prop['mass'] = line[50:62].strip()
            human_prop['volume'] = line[62:].strip()
            human[species]=human_prop
    # more info on String formatter https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
    print("%-22s %-16s %-13s %-12s %-25s" %('Species','Lived when','Adult','Adult','Brain volume'))
    print("%-22s %-16s %-13s %-12s %-25s" % ('', '(mill. yrs)','height (m)','mass (kg)','(cm**3)'))
    print("%s"% '-'*85)
    for h in human:
        print("%-22s %-16s %-13s %-12s %-25s" %(h.replace('homo','H.'), human[h]['when'],human[h]['height'],human[h]['mass'],human[h]['volume']))
    print("%s" % '-' * 85)
    print("\nSource: http://en.wikipedia.org/wiki/Human_evolution")

if __name__=='__main__':
    main()

