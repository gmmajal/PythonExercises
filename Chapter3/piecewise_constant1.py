def piecewise(x,data):
     xx=[]
     v=[]
     for i in data:
         xx.append(i[0])
         v.append(i[1])
     for i in range(len(xx)-1):
         if (xx[i]<=x) and (x<xx[i+1]):
             return v[i]
     return v[len(v)-1]
def test_piecewise():
     data=[(0,-1),(1,0),(1.5,4)]
     x1=0;x2=0.5;x3=1;x4=1.3;x5=1.5;x6=1.7
     expected1=-1
     expected2=-1
     expected3=0
     expected4=0
     expected5=4
     expected6=4
     success1=(piecewise(x1,data)==expected1)
     success2=(piecewise(x2,data)==expected2)
     success3=(piecewise(x3,data)==expected3)
     success4=(piecewise(x4,data)==expected4)
     success5=(piecewise(x5,data)==expected5)
     success6=(piecewise(x6,data)==expected6)
     msg1='The computed value is %g'% piecewise(x1,data)
     msg2='The computed value is %g'%piecewise(x2,data)
     msg3='The computed value is %g'%piecewise(x3,data)
     msg4='The computed value is %g'%piecewise(x4,data)
     msg5='The computed value is %g'%piecewise(x5,data)
     msg6='The computed value is %g'%piecewise(x6,data)
     assert success1,msg1
     assert success2,msg2
     assert success3,msg3
     assert success4,msg4
     assert success5,msg5
     assert success6,msg6
test_piecewise()

