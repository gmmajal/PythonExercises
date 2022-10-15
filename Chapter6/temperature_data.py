from matplotlib.pyplot import *
import numpy as np


def readHtm():
    dict={}
    infile = open('./city_temp/citylistWorld.htm', 'r')
    for i in range(1,261):
        infile.readline()
    for line in infile:
        if 'mso-list' in line:
            key= line.split('</b>')[0].split('<b>')[1].strip(' ( ')
        if 'href="ftp' in line:
            value= line.split('>')[1].strip('</a')
            dict[key]=value
    return dict

def readTxtFile(dictionary,cityname):
    filename=dictionary[cityname]
    dict={}

    mnth=np.array([])
    year=np.array([])
    date=np.array([])
    temp=np.array([])

    infile=open('./city_temp/'+filename,'r')
    for line in infile:
        col1=line[1:3].strip(' ')
        col2=line[15:18].strip(' ')
        col3=line[29:34].strip(' ')
        col4=line[42:].strip(' ').strip('\n')
        mnth=np.append(mnth,col1)
        date=np.append(date,col2)
        year=np.append(year,col3)
        temp=np.append(temp,col4)

    #remove time values and temp values when there is no recorded data available
    idx=np.where(temp=='-99')
    for i in idx:
        mnth=  np.delete(mnth,i)
        date = np.delete(date, i)
        year = np.delete(year, i)
        temp = np.delete(temp, i)

    dict['city']=cityname
    dict['month']=mnth.astype(int)
    dict['date']=date.astype(int)
    dict['year'] = year.astype(int)
    dict['temperature'] = temp.astype(float)
    return dict

def plot_temp(d):
    temp_val1=readTxtFile(d,'Sydney')
    temp_val2 = readTxtFile(d, 'Stockholm')
    plot(temp_val1['year'],temp_val1['temperature'],'r.')
    plot(temp_val2['year'], temp_val2['temperature'], 'b.')
    xlabel('Year')
    ylabel(r'$Temp(^\circ F)$')
    legend(['Sydney','Stockholm'])

    show()

if __name__=='__main__':
    d=readHtm()
    tempValues_Tirana=readTxtFile(d,'Tirana')
    plot_temp(d)